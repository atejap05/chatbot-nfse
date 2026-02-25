# Fluxo de Dados

## Visão Geral

O fluxo de dados do frontend envolve: estado do chat, envio de mensagens, recebimento do stream e atualização da UI.

## Diagrama de Fluxo

```
┌──────────────┐     sendMessage({ text })      ┌─────────────────┐
│   Usuário    │──────────────────────────────▶│    useChat      │
│   (input)    │                                │    (estado)     │
└──────────────┘                                └────────┬────────┘
       ▲                                                 │
       │                                                 │ POST /api/chat
       │                                                 │ body: { messages }
       │                                                 ▼
       │                                        ┌─────────────────┐
       │                                        │  Proxy Route    │
       │                                        │  (transforma)   │
       │                                        └────────┬────────┘
       │                                                 │
       │                                                 │ fetch(BACKEND_URL)
       │                                                 ▼
       │                                        ┌─────────────────┐
       │                                        │  Backend        │
       │                                        │  FastAPI        │
       │                                        │  (stream texto) │
       │                                        └────────┬────────┘
       │                                                 │
       │                                                 │ ReadableStream
       │                                                 │ (chunks de texto)
       │                                                 ▼
       │                                        ┌─────────────────┐
       │                                        │  Proxy          │
       │                                        │  text → SSE     │
       │                                        │  text-delta     │
       │                                        └────────┬────────┘
       │                                                 │
       │                                                 │ Response (SSE)
       │                                                 ▼
       │                                        ┌─────────────────┐
       │                                        │  useChat        │
       │                                        │  atualiza       │
       │                                        │  messages[]     │
       │                                        └────────┬────────┘
       │                                                 │
       │                                                 │ re-render
       │                                                 ▼
       └─────────────────────────────────────────────────┘
                    UI atualizada (mensagem do assistente)
```

## Estados do useChat

| Estado | Descrição | Comportamento na UI |
|--------|-----------|---------------------|
| `ready` | Pronto para enviar | Input e botão habilitados |
| `submitted` | Requisição enviada | Aguardando resposta |
| `streaming` | Recebendo stream | Indicador "Digitando..."; input desabilitado |
| `error` | Erro na requisição | (tratamento futuro) |

## Estrutura de Mensagens

### Envio (useChat → Proxy)

O useChat envia mensagens no formato UIMessage:

```typescript
// Formato com content (legado)
{ role: "user", content: "Como emitir NFS-e?" }

// Formato com parts (novo)
{ role: "user", parts: [{ type: "text", text: "Como emitir NFS-e?" }] }
```

O proxy normaliza para `{ role, content }` antes de enviar ao backend.

### Recebimento (Backend → useChat)

O backend retorna **texto puro** em chunks. O proxy transforma em SSE:

```
data: {"type":"start","messageId":"msg_xxx"}
data: {"type":"text-start","id":"msg_xxx"}
data: {"type":"text-delta","id":"msg_xxx","delta":"Para emitir"}
data: {"type":"text-delta","id":"msg_xxx","delta":" uma NFS-e..."}
data: {"type":"text-end","id":"msg_xxx"}
data: {"type":"finish"}
data: [DONE]
```

O useChat consome esse stream e monta a mensagem do assistente em `messages`.

## Ciclo de Vida de uma Mensagem

1. **Input**: Usuário digita ou clica em sugestão → `setInput` ou `sendMessage`
2. **Envio**: `sendMessage({ text })` adiciona mensagem do usuário a `messages` e dispara POST
3. **Streaming**: Chunks chegam via SSE → useChat concatena no conteúdo da mensagem do assistente
4. **Finalização**: Evento `finish` → status volta a `ready`
5. **Exibição**: `messages` contém user + assistant; React re-renderiza com `ReactMarkdown` para o assistant
