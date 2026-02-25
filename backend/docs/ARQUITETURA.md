# Arquitetura do Backend

## Visão Geral

O backend segue uma arquitetura em camadas com separação entre:

1. **API (main.py)** – endpoints HTTP, validação e streaming
2. **RAG Engine (rag_engine.py)** – orquestração do pipeline de recuperação e geração
3. **Ingestion (ingest.py)** – indexação dos documentos no banco vetorial

## Diagrama de Arquitetura

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         BACKEND (FastAPI)                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────┐     ┌─────────────────────────────────────────┐  │
│  │   main.py        │     │           rag_engine.py                   │  │
│  │                  │     │                                           │  │
│  │  POST /api/chat  │────▶│  stream_generator(user_query)             │  │
│  │  GET /health     │     │       │                                   │  │
│  │                  │     │       ├─▶ RetrieverQueryEngine            │  │
│  │  • Validação     │     │       │   • VectorIndexRetriever (top-5)  │  │
│  │  • CORS          │     │       │   • ResponseSynthesizer (stream)  │  │
│  │  • Streaming     │     │       │                                   │  │
│  └─────────────────┘     │       └─▶ yield chunks de texto           │  │
│                           └─────────────────────────────────────────┘  │
│                                            │                            │
│                                            │ consulta                   │
│                                            ▼                            │
│                           ┌─────────────────────────────────────────┐  │
│                           │  Qdrant (vector store)                   │  │
│                           │  Collection: nfse_faq                    │  │
│                           └─────────────────────────────────────────┘  │
│                                            ▲                            │
│                                            │ embeddings                 │
│                           ┌─────────────────────────────────────────┐  │
│                           │  ingest.py (script separado)             │  │
│                           │  • SimpleDirectoryReader                │  │
│                           │  • MarkdownNodeParser                   │  │
│                           │  • HuggingFaceEmbedding                 │  │
│                           │  • VectorStoreIndex.from_nodes           │  │
│                           └─────────────────────────────────────────┘  │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
        │                                              │
        │ POST /api/chat                               │ API Anthropic
        │ (frontend)                                    │ (Claude)
        ▼                                              ▼
┌─────────────────┐                          ┌─────────────────┐
│  Frontend       │                          │  Anthropic      │
│  (Next.js)      │                          │  Claude LLM     │
└─────────────────┘                          └─────────────────┘
```

## Pipeline RAG

```
User Query ──▶ Embedding (HuggingFace) ──▶ Busca vetorial (Qdrant, top-5)
                                                    │
                                                    ▼
                                            Chunks recuperados
                                                    │
                                                    ▼
                                    Prompt (contexto + pergunta) ──▶ Claude
                                                    │
                                                    ▼
                                            Resposta em streaming
                                                    │
                                                    ▼
                                            yield chunks ──▶ Frontend
```

## Componentes Principais

### 1. main.py – Servidor FastAPI

- **Responsabilidade**: Expor endpoints HTTP, validar payload, retornar stream
- **Rota `/api/chat`**: Recebe mensagens, extrai última do usuário, chama `stream_generator`, retorna `StreamingResponse`
- **Rota `/health`**: Verificação de disponibilidade
- **CORS**: Permite `http://localhost:3000` para desenvolvimento

### 2. rag_engine.py – Motor RAG

- **`_get_query_engine()`**: Monta o pipeline LlamaIndex (retriever + synthesizer)
- **`stream_generator(user_query)`**: Async generator que consulta o RAG e emite chunks de texto
- **System prompt**: Instruções do especialista NFS-e (baseado em INSTRUCOES-COPILOT-STUDIO.md)

### 3. ingest.py – Script de Indexação

- **Execução**: Independente do servidor (`python -m backend.ingest`)
- **Responsabilidade**: Carregar Markdowns, parsear, gerar embeddings, persistir no Qdrant
- **Frequência**: Executado manualmente ao adicionar/atualizar documentos

## Decisões Arquiteturais

| Decisão | Justificativa |
|---------|---------------|
| **Ingestion separada** | Indexação é pesada; não deve bloquear o servidor |
| **Qdrant em Docker** | Persistência, escalabilidade, desacoplamento |
| **HuggingFace embeddings** | Gratuito, local, otimizado para português |
| **Streaming** | Melhor UX; resposta aparece progressivamente |
| **Última mensagem apenas** | Simplicidade; histórico pode ser incorporado depois |
