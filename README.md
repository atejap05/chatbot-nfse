# Chatbot NFS-e - RAG Especializado

Chatbot de autoatendimento para dúvidas sobre Nota Fiscal de Serviços Eletrônica (NFS-e), utilizando RAG (Retrieval-Augmented Generation) com base nos 8 arquivos FAQ do projeto.

## Arquitetura

- **Backend**: Python + FastAPI + LlamaIndex + Anthropic Claude + Qdrant
- **Frontend**: Next.js 16 + TailwindCSS + Vercel AI SDK
- **Base de conhecimento**: 8 arquivos Markdown em `data/` (~105 Q&As)

## Pré-requisitos

- Python 3.11+
- Node.js 20.9+ (LTS; exigido pelo Next.js 16)
- Docker (para Qdrant)
- Chave API Anthropic

## Configuração

Execute os passos abaixo **na raiz do repositório** (`chatbot-nfse/`), salvo indicação em contrário.

### 1. Variáveis de ambiente

**Backend** – crie `backend/.env`:

```
ANTHROPIC_API_KEY=sua_chave_anthropic
QDRANT_URL=http://localhost:6333
```

**Frontend** – crie `frontend/.env.local`:

```
BACKEND_URL=http://127.0.0.1:8000
```

### 2. Ambiente virtual Python (venv)

Crie e ative o venv na raiz do projeto:

```bash
python -m venv .venv
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

Com o venv ativado, instale as dependências do backend:

```bash
pip install -r backend/requirements.txt
```

### 3. Subir o Qdrant

```bash
docker compose up -d qdrant
```

### 4. Indexar os documentos

Com o venv ativado e o Qdrant em execução:

```bash
python -m backend.ingest
```

### 5. Iniciar o backend

Com o venv ativado:

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### 6. Iniciar o frontend

Em outro terminal:

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
