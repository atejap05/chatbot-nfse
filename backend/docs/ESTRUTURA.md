# Estrutura de Diretórios

## Árvore do Projeto

```
backend/
├── docs/                     # Documentação (este diretório)
│   ├── README.md
│   ├── ARQUITETURA.md
│   ├── TECNOLOGIAS.md
│   ├── ESTRUTURA.md
│   ├── FLUXO-DADOS.md
│   ├── INTEGRACAO-FRONTEND.md
│   └── ROADMAP.md
├── __init__.py               # Marca backend como pacote Python
├── main.py                   # Servidor FastAPI
├── rag_engine.py             # Motor RAG (LlamaIndex)
├── ingest.py                 # Script de indexação
├── requirements.txt          # Dependências Python
└── .env                      # Variáveis de ambiente (não versionado)
```

## Descrição dos Arquivos

### main.py

Servidor FastAPI com:

- **ChatMessage**, **ChatRequest**: Modelos Pydantic para validação
- **health()**: `GET /health` → `{"status": "ok"}`
- **chat()**: `POST /api/chat` → valida mensagens, extrai última do usuário, chama `stream_generator`, retorna `StreamingResponse`
- **CORS**: Middleware para `http://localhost:3000`

### rag_engine.py

Motor RAG com:

- **SYSTEM_PROMPT**: Instruções do especialista NFS-e
- **_get_query_engine()**: Monta VectorStoreIndex, RetrieverQueryEngine, ResponseSynthesizer
- **stream_generator(user_query)**: Async generator que emite chunks de texto
- **get_query_engine()**: Acesso síncrono ao query engine (se necessário)

### ingest.py

Script de indexação com:

- **FAQ_CATEGORIES**: Mapeamento arquivo → categoria legível
- **get_data_path()**: Retorna caminho da pasta `data/`
- **main()**: Carrega docs, parseia com MarkdownNodeParser, enriquece metadados, indexa no Qdrant

### requirements.txt

Lista de dependências com versões mínimas.

## Execução

O backend deve ser executado a partir da **raiz do projeto** para que o pacote `backend` seja resolvido:

```bash
# Da raiz do projeto (chatbot-nfse/)
uvicorn backend.main:app --reload --port 8000
python -m backend.ingest
```

## Dependência da Pasta data/

O `ingest.py` espera a pasta `data/` na raiz do projeto, contendo os arquivos `faq-*.md`:

```
chatbot-nfse/
├── backend/
├── data/           # ← fonte dos documentos
│   ├── faq-01-painel-municipal-gestao.md
│   ├── faq-02-cadastro-contribuintes-cnc.md
│   └── ...
```
