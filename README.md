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

Atualize o pip:

```powershell
python.exe -m pip install --upgrade pip
```

Com o venv ativado, instale as dependências do backend:

```bash
pip install -r backend/requirements.txt
```

### 3. Subir o Qdrant

#### Opção A: Com Docker (recomendado)

1. Instale o [Docker Desktop para Windows](https://www.docker.com/products/docker-desktop/).
2. Inicie o Docker Desktop e aguarde até estar em execução.
3. Na raiz do projeto, execute:

```bash
docker compose up -d qdrant
```

#### Opção B: Sem Docker (Windows)

Se não quiser usar Docker, rode o Qdrant direto no Windows:

1. Acesse [Qdrant – Releases no GitHub](https://github.com/qdrant/qdrant/releases).
2. Baixe o arquivo **Windows** (ex.: `qdrant-windows-amd64.zip` ou similar).
3. Extraia o ZIP e execute `qdrant.exe` na pasta extraída (por exemplo, pelo PowerShell: `.\qdrant.exe`).
4. O Qdrant sobe em **http://localhost:6333** (API e dashboard em http://localhost:6333/dashboard).

Não é necessário configurar nada além disso para uso local; o backend já aponta para `QDRANT_URL=http://localhost:6333`.

### 4. Indexar os documentos

Com o venv ativado e o Qdrant em execução:

```bash
python -m backend.ingest
```

**Windows:** Se aparecer erro ao carregar `c10.dll` (PyTorch), veja a seção [Problemas comuns](#problemas-comuns) abaixo.

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

## Problemas comuns

### Erro ao indexar no Windows: "Error loading c10.dll" (PyTorch)

O script de indexação usa embeddings locais (HuggingFace/sentence-transformers), que dependem do PyTorch. No Windows às vezes a DLL do PyTorch falha ao carregar. Faça o seguinte:

1. **Instale o Visual C++ Redistributable** (x64), se ainda não tiver:  
   [Baixar VC++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)  
   Instale e reinicie o PC se for a primeira vez.

2. **Reinstale o PyTorch em versão só CPU** (mais estável no Windows). Com o venv ativado:

```powershell
pip uninstall torch -y
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

3. Tente de novo:

```powershell
python -m backend.ingest
```

Se o projeto estiver em uma pasta sincronizada pelo OneDrive, mover o repositório para um caminho local (ex.: `C:\dev\chatbot-nfse`) pode evitar problemas de DLL.

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
