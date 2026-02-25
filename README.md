# Chatbot NFS-e - RAG Especializado

Chatbot de autoatendimento para dúvidas sobre Nota Fiscal de Serviços Eletrônica (NFS-e), utilizando RAG (Retrieval-Augmented Generation) com base nos 8 arquivos FAQ do projeto.

## Arquitetura

- **Backend**: Python + FastAPI + LlamaIndex + Anthropic Claude + Qdrant
- **Frontend**: Next.js 15 + TailwindCSS + Vercel AI SDK
- **Base de conhecimento**: 8 arquivos Markdown em `data/` (~105 Q&As)

## Pré-requisitos

- Python 3.11+
- Node.js 18+
- Docker (para Qdrant)
- Chave API Anthropic

## Configuração

### 1. Variáveis de ambiente

**Backend** (`backend/.env`):
```
ANTHROPIC_API_KEY=sua_chave_anthropic
QDRANT_URL=http://localhost:6333
```

**Frontend** (`frontend/.env.local`):
```
BACKEND_URL=http://127.0.0.1:8000
```

### 2. Subir o Qdrant

```bash
docker compose up -d qdrant
```

### 3. Indexar os documentos

```bash
cd chatbot-nfse
pip install -r backend/requirements.txt
python -m backend.ingest
```

### 4. Iniciar o backend

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Iniciar o frontend

```bash
cd frontend
npm install
npm run dev
```

Acesse http://localhost:3000

## Estrutura do Projeto

```
chatbot-nfse/
  backend/
    main.py           # API FastAPI
    rag_engine.py     # Lógica RAG
    ingest.py         # Script de indexação
    requirements.txt
  frontend/
    app/
      page.tsx        # Interface do chat
      api/chat/       # Proxy para o backend
  data/               # FAQs em Markdown
  docker-compose.yml  # Qdrant
```

## Perguntas de teste

- "Como fazer o primeiro acesso ao Portal Nacional?"
- "O que é o erro E0831?"
- "Como funciona a retenção de PIS/COFINS/CSLL após a NT 007?"
- "Como migrar do emissor próprio para o nacional?"
