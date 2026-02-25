# Fluxo de Dados

## Visão Geral

O fluxo de dados no backend envolve: recepção da pergunta, recuperação de contexto, geração da resposta e streaming para o cliente.

## Fluxo de uma Requisição de Chat

```
┌─────────────┐     POST /api/chat      ┌─────────────┐
│  Frontend   │ ──────────────────────▶ │   main.py   │
│  (proxy)    │     { messages }         │   chat()    │
└─────────────┘                         └──────┬──────┘
                                               │
                                               │ 1. Validação
                                               │ 2. Extrai user_query
                                               │ 3. stream_generator(query)
                                               ▼
                                        ┌─────────────┐
                                        │ rag_engine  │
                                        │ stream_gen  │
                                        └──────┬──────┘
                                               │
                    ┌──────────────────────────┼──────────────────────────┐
                    │                          │                          │
                    ▼                          ▼                          ▼
             ┌─────────────┐            ┌─────────────┐            ┌─────────────┐
             │  Embedding  │            │   Qdrant    │            │   Claude    │
             │  (query)    │            │  (busca)    │            │  (geração)  │
             └──────┬──────┘            └──────┬──────┘            └──────┬──────┘
                    │                          │                          │
                    │  vetor da query          │  top-5 chunks            │  prompt
                    └─────────────────────────┼──────────────────────────┘
                                              │
                                              │  context_str + query_str
                                              ▼
                                        ┌─────────────┐
                                        │  Claude     │
                                        │  response_gen
                                        └──────┬──────┘
                                               │
                                               │ chunks de texto
                                               ▼
                                        ┌─────────────┐
                                        │  yield      │
                                        │  (stream)   │
                                        └──────┬──────┘
                                               │
                                               │ StreamingResponse
                                               ▼
                                        ┌─────────────┐
                                        │  Frontend   │
                                        └─────────────┘
```

## Pipeline de Ingestion

```
data/*.md
    │
    ▼  SimpleDirectoryReader
Documents (com file_name, file_path)
    │
    ▼  MarkdownNodeParser
Nodes (chunks por ## Dúvida NNN)
    │
    ▼  Enriquecimento
Nodes + metadata (category, source_file)
    │
    ▼  HuggingFaceEmbedding
Vetores (384 dim)
    │
    ▼  VectorStoreIndex.from_nodes
Qdrant (collection nfse_faq)
```

## Formato dos Dados

### Request (entrada)

```json
{
  "messages": [
    { "role": "user", "content": "Como fazer o primeiro acesso?" }
  ]
}
```

O backend utiliza apenas `user_messages[-1].content` (última mensagem do usuário).

### Response (saída)

- **Content-Type**: `text/plain; charset=utf-8`
- **Body**: Stream de texto puro (chunks concatenados = resposta completa)
- **Headers**: `Cache-Control: no-cache`, `Connection: keep-alive`

Exemplo de chunks:

```
"Para fazer o primeiro acesso, "
"você deve acessar o Portal de Gestão NFS-e..."
```

### Metadados no Qdrant

Cada node indexado possui:

| Campo | Descrição |
|-------|-----------|
| `file_name` | Nome do arquivo (ex: faq-01-painel-municipal-gestao.md) |
| `source_file` | Igual a file_name |
| `category` | Categoria legível (ex: Painel Municipal e Gestão) |

## Streaming

O `response_gen` do LlamaIndex é um gerador síncrono. O `stream_generator` é async e faz:

```python
for text in response.response_gen:
    yield text  # cada chunk vai para o StreamingResponse
```

O frontend (via proxy) recebe esses chunks e os transforma no formato SSE para o useChat.
