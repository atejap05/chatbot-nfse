# Documentação do Backend - Chatbot NFS-e

Documentação técnica do backend do Assistente NFS-e, API RAG especializada em Nota Fiscal de Serviços Eletrônica.

## Índice

| Documento | Descrição |
|-----------|-----------|
| [ARQUITETURA.md](./ARQUITETURA.md) | Visão geral da arquitetura, pipeline RAG e componentes |
| [TECNOLOGIAS.md](./TECNOLOGIAS.md) | Stack tecnológica, dependências e versões |
| [ESTRUTURA.md](./ESTRUTURA.md) | Estrutura de diretórios e organização do código |
| [FLUXO-DADOS.md](./FLUXO-DADOS.md) | Fluxo de dados no pipeline RAG e streaming |
| [INTEGRACAO-FRONTEND.md](./INTEGRACAO-FRONTEND.md) | Integração com o frontend, contrato de API e CORS |
| [ROADMAP.md](./ROADMAP.md) | Roadmap de evolução e melhorias planejadas |

## Visão Geral

O backend é uma API FastAPI que implementa um pipeline RAG (Retrieval-Augmented Generation) utilizando:

- **LlamaIndex** para orquestração
- **Qdrant** como banco vetorial
- **HuggingFace** para embeddings (local, gratuito)
- **Anthropic Claude** para geração de respostas
- **Streaming** de texto para o frontend

## Início Rápido

```bash
# 1. Subir Qdrant
docker compose up -d qdrant

# 2. Indexar documentos
python -m backend.ingest

# 3. Iniciar API
uvicorn backend.main:app --reload --port 8000
```

## Variáveis de Ambiente

| Variável | Descrição | Obrigatória |
|----------|-----------|-------------|
| `ANTHROPIC_API_KEY` | Chave API do Anthropic para Claude | Sim |
| `QDRANT_URL` | URL do Qdrant | Não (padrão: http://localhost:6333) |

Configure em `backend/.env`.
