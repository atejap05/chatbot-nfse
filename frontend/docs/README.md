# Documentação do Frontend - Chatbot NFS-e

Documentação técnica do frontend do Assistente NFS-e, interface de chat para atendimento sobre Nota Fiscal de Serviços Eletrônica.

## Índice

| Documento | Descrição |
|-----------|-----------|
| [ARQUITETURA.md](./ARQUITETURA.md) | Visão geral da arquitetura, componentes e decisões técnicas |
| [TECNOLOGIAS.md](./TECNOLOGIAS.md) | Stack tecnológica, dependências e versões |
| [ESTRUTURA.md](./ESTRUTURA.md) | Estrutura de diretórios e organização do código |
| [FLUXO-DADOS.md](./FLUXO-DADOS.md) | Fluxo de dados entre componentes e estados |
| [INTEGRACAO-BACKEND.md](./INTEGRACAO-BACKEND.md) | Integração com o backend FastAPI, contrato de API e proxy |
| [ROADMAP.md](./ROADMAP.md) | Roadmap de evolução e melhorias planejadas |

## Visão Geral

O frontend é uma aplicação Next.js que fornece a interface de chat para o chatbot RAG especializado em NFS-e. Utiliza o Vercel AI SDK para gerenciamento de estado de conversação e streaming de respostas.

## Início Rápido

```bash
npm install
npm run dev
```

Acesse http://localhost:3000

## Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `BACKEND_URL` | URL do backend FastAPI | `http://127.0.0.1:8000` |

Configure em `.env.local` na raiz do frontend.
