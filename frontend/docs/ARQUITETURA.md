# Arquitetura do Frontend

## Visão Geral

O frontend do Chatbot NFS-e segue uma arquitetura baseada em **Next.js App Router** com separação clara entre:

1. **Camada de apresentação** – componentes React e UI
2. **Camada de API** – rotas de API que atuam como proxy
3. **Integração externa** – comunicação com o backend FastAPI

## Diagrama de Arquitetura

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND (Next.js)                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────────┐     ┌──────────────────────────────────┐  │
│  │   app/page.tsx   │     │      app/api/chat/route.ts        │  │
│  │   (Client)       │────▶│      (Server - Proxy)              │  │
│  │                  │     │                                    │  │
│  │  • useChat       │     │  • Recebe mensagens do useChat     │  │
│  │  • ReactMarkdown │     │  • Formata para backend            │  │
│  │  • UI do chat    │     │  • Transforma stream SSE           │  │
│  └─────────────────┘     └────────────────┬─────────────────┘  │
│            │                               │                      │
│            │  POST /api/chat                │  fetch()            │
│            │  (SSE stream)                  │                      │
│            ◀───────────────────────────────┘                      │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
                                    │
                                    │  POST /api/chat
                                    │  (text/plain stream)
                                    ▼
┌───────────────────────────────────────────────────────────────────┐
│                     BACKEND (FastAPI - :8000)                       │
│  • RAG Engine (LlamaIndex + Claude)                                │
│  • Stream de texto puro                                            │
└───────────────────────────────────────────────────────────────────┘
```

## Componentes Principais

### 1. Página de Chat (`app/page.tsx`)

- **Tipo**: Client Component (`"use client"`)
- **Responsabilidade**: Interface do usuário, gerenciamento de input e exibição de mensagens
- **Estado**: Controlado pelo hook `useChat` do Vercel AI SDK
- **Renderização**: Mensagens do usuário à direita (azul), do assistente à esquerda (branco)

### 2. Rota de API Proxy (`app/api/chat/route.ts`)

- **Tipo**: Server-side Route Handler
- **Responsabilidade**: Intermediar entre o useChat e o backend FastAPI
- **Transformação**: Converte stream de texto puro do backend no formato **Data Stream Protocol** (SSE) esperado pelo Vercel AI SDK

### 3. Layout Raiz (`app/layout.tsx`)

- **Tipo**: Server Component
- **Responsabilidade**: Estrutura HTML, metadados e estilos globais

## Decisões Arquiteturais

| Decisão | Justificativa |
|---------|---------------|
| **Proxy em vez de chamada direta** | Protege a API key do backend; permite transformação de protocolo |
| **useChat do Vercel AI SDK** | Gerencia estado de conversação, streaming e compatibilidade com protocolos |
| **App Router** | Estrutura moderna do Next.js; rotas de API colocalizadas |
| **Client Component para o chat** | Necessário para hooks e interatividade |

## Fluxo de Requisição

1. Usuário digita mensagem e envia (ou clica em sugestão)
2. `sendMessage({ text })` do useChat dispara POST para `/api/chat`
3. Proxy recebe, formata `{ messages: [...] }` e encaminha ao FastAPI
4. FastAPI retorna stream de texto puro
5. Proxy transforma cada chunk em `text-delta` (SSE)
6. useChat consome o stream e atualiza `messages` em tempo real
7. React re-renderiza com o conteúdo incremental
