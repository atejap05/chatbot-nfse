# Integração com o Frontend

## Visão Geral

O backend é consumido pelo frontend Next.js através de um **proxy** em `app/api/chat/route.ts`. O frontend nunca chama o backend diretamente do browser; todas as requisições passam pelo proxy.

## Configuração

### CORS

O backend permite requisições de:

```python
allow_origins=["http://localhost:3000"]
```

Para produção, ajuste em `main.py`:

```python
allow_origins=["https://seu-dominio.com"]
```

### URL do Backend

O frontend configura a URL via variável `BACKEND_URL` (padrão: `http://127.0.0.1:8000`). O proxy usa essa URL para encaminhar as requisições.

## Contrato da API

### POST /api/chat

**Request**

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| messages | array | Sim | Lista de mensagens |
| messages[].role | string | Sim | `"user"` ou `"assistant"` |
| messages[].content | string | Sim | Conteúdo da mensagem |

**Response (sucesso)**

- **Status**: 200
- **Content-Type**: `text/plain; charset=utf-8`
- **Body**: Stream de texto (chunks em UTF-8)

**Erros**

| Status | Detalhe |
|--------|---------|
| 400 | "Nenhuma mensagem enviada" |
| 400 | "Nenhuma mensagem do usuário encontrada" |
| 400 | "Mensagem vazia" |
| 500 | Erro interno (ex: ANTHROPIC_API_KEY ausente, Qdrant indisponível) |

### GET /health

**Response**

```json
{"status": "ok"}
```

Útil para health checks e verificação de disponibilidade.

## Transformação no Proxy

O backend retorna **texto puro**. O proxy do frontend transforma em **Server-Sent Events (SSE)** no formato Data Stream Protocol do Vercel AI SDK:

| Backend envia | Proxy transforma em |
|---------------|---------------------|
| chunk "Para emitir..." | `data: {"type":"text-delta","delta":"Para emitir..."}\n\n` |
| (fim do stream) | `data: {"type":"text-end"}\n\n`, `data: {"type":"finish"}\n\n`, `data: [DONE]\n\n` |

## Diagrama de Integração

```
┌─────────────────┐                    ┌─────────────────┐
│   Browser       │                    │   Next.js        │
│   (useChat)     │  POST /api/chat    │   (Proxy)        │
│                 │ ─────────────────▶ │                  │
└─────────────────┘                    └────────┬────────┘
       ▲                                        │
       │                                        │ fetch(BACKEND_URL/api/chat)
       │  Response (SSE)                        │
       │  Data Stream Protocol                  ▼
       │                                ┌─────────────────┐
       │                                │   FastAPI       │
       │                                │   :8000         │
       │                                │                 │
       │                                │  StreamingResponse
       │                                │  (text/plain)   │
       │                                └────────┬────────┘
       │                                         │
       └─────────────────────────────────────────┘
                Proxy transforma e repassa
```

## Dependências para Funcionamento

Para o backend responder corretamente:

1. **Qdrant** rodando (ex: `docker compose up -d qdrant`)
2. **Collection `nfse_faq`** populada (`python -m backend.ingest`)
3. **ANTHROPIC_API_KEY** configurada no `.env`
4. **CORS** permitindo a origem do frontend

## Teste Manual

```bash
# Health check
curl http://localhost:8000/health

# Chat (stream)
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"O que é o erro E0831?"}]}'
```
