# Tecnologias do Backend

## Stack Principal

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| **Python** | 3.11+ | Linguagem base |
| **FastAPI** | >=0.115.0 | Framework web assíncrono |
| **Uvicorn** | >=0.32.0 | Servidor ASGI |
| **LlamaIndex** | core >=0.12.0 | Orquestração RAG |
| **Qdrant** | client >=1.12.0 | Banco vetorial |
| **Anthropic** | via llama-index-llms-anthropic | LLM (Claude) |
| **HuggingFace** | via sentence-transformers | Embeddings |

## Dependências

### Produção

```
fastapi>=0.115.0
uvicorn[standard]>=0.32.0
python-dotenv>=1.0.0

llama-index-core>=0.12.0
llama-index-embeddings-huggingface>=0.3.0
llama-index-llms-anthropic>=0.3.0
llama-index-vector-stores-qdrant>=0.3.0

qdrant-client>=1.12.0
sentence-transformers>=3.0.0
```

### Pacotes LlamaIndex

| Pacote | Função |
|--------|--------|
| `llama-index-core` | VectorStoreIndex, RetrieverQueryEngine, Settings |
| `llama-index-embeddings-huggingface` | HuggingFaceEmbedding |
| `llama-index-llms-anthropic` | Anthropic (Claude) |
| `llama-index-vector-stores-qdrant` | QdrantVectorStore |

## Modelos Utilizados

| Componente | Modelo | Observação |
|------------|--------|------------|
| **LLM** | `claude-3-5-sonnet-20241022` | Alternativa: `claude-sonnet-4-*` |
| **Embeddings** | `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | Local, multilingue, português |

## Qdrant

- **Imagem Docker**: `qdrant/qdrant:latest`
- **Porta**: 6333 (HTTP), 6334 (gRPC)
- **Collection**: `nfse_faq`
- **Dimensão dos vetores**: Definida pelo modelo de embedding (384 para paraphrase-multilingual-MiniLM-L12-v2)

## Variáveis de Ambiente

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `ANTHROPIC_API_KEY` | Chave API Anthropic | `sk-ant-...` |
| `QDRANT_URL` | URL do Qdrant | `http://localhost:6333` |

Arquivo: `backend/.env` (não versionado)
