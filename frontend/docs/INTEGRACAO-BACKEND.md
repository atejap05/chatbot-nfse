# Integração com o Backend

## Visão Geral

O frontend comunica-se com o backend FastAPI através de um **proxy** em `app/api/chat/route.ts`. O proxy é necessário para:

1. **Proteção**: A API key do Anthropic permanece apenas no backend
2. **Transformação de protocolo**: O backend retorna texto puro; o useChat espera SSE no Data Stream Protocol
3. **CORS**: Evita problemas de origem cruzada em desenvolvimento

## Configuração

### Variável de Ambiente

```env
BACKEND_URL=http://127.0.0.1:8000
```

Arquivo: `frontend/.env.local` (não versionado)

### Backend Esperado

- **URL base**: Configurável via `BACKEND_URL`
- **Endpoint**: `POST /api/chat`
- **Porta padrão**: 8000

## Contrato da API

### Request (Frontend → Proxy → Backend)

**Método**: `POST`  
**URL**: `/api/chat` (proxy) → `{BACKEND_URL}/api/chat` (backend)  
**Headers**: `Content-Type: application/json`

**Body**:

```json
{
  "messages": [
    { "role": "user", "content": "Como fazer o primeiro acesso?" },
    { "role": "assistant", "content": "Para o primeiro acesso..." },
    { "role": "user", "content": "E se for MEI?" }
  ]
}
```

O backend utiliza apenas a **última mensagem do usuário** para a consulta RAG. O histórico é enviado para compatibilidade com o useChat.

### Response (Backend → Proxy → Frontend)

**Backend** retorna:

- **Status**: 200
- **Content-Type**: `text/plain; charset=utf-8`
- **Body**: Stream de texto puro (chunks concatenados formam a resposta completa)

**Proxy** transforma em:

- **Status**: 200
- **Content-Type**: `text/event-stream`
- **Headers**: `x-vercel-ai-ui-message-stream: v1`
- **Body**: SSE no formato Data Stream Protocol

### Erros

| Status | Situação |
|--------|----------|
| 400 | Nenhuma mensagem, nenhuma mensagem do usuário, ou mensagem vazia |
| 500 | Erro ao conectar ao backend ou stream indisponível |

## Transformação de Stream

O backend envia chunks de texto como:

```
"Para emitir uma NFS-e, "
"você deve acessar o Portal Nacional..."
```

O proxy encapsula cada chunk em:

```json
{"type":"text-delta","id":"msg_xxx","delta":"Para emitir uma NFS-e, "}
```

E adiciona eventos de controle: `start`, `text-start`, `text-end`, `finish`, `[DONE]`.

## Diagrama de Integração

```
┌─────────────┐     POST /api/chat      ┌─────────────┐     POST /api/chat     ┌─────────────┐
│   useChat   │ ──────────────────────▶ │   Proxy     │ ────────────────────▶ │   FastAPI   │
│   (client)  │     { messages }        │   (Next.js) │     { messages }      │   (Python)  │
└─────────────┘                         └──────┬──────┘                       └──────┬──────┘
       │                                       │                                      │
       │                                       │         Stream (text/plain)         │
       │                                       │ ◀───────────────────────────────────┘
       │                                       │
       │         Response (text/event-stream)   │  Transformação:
       │         Data Stream Protocol          │  texto → text-delta (SSE)
       │ ◀─────────────────────────────────────┘
       │
       │  useChat parseia e atualiza messages
       ▼
```

## CORS

O backend FastAPI está configurado com CORS para `http://localhost:3000`. Em produção, ajuste `allow_origins` no `main.py` do backend.

## Health Check

O backend expõe `GET /health` para verificação. O frontend não o utiliza atualmente; pode ser usado para:

- Indicador de status "Backend conectado"
- Retry automático em caso de falha
