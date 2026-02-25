# Estrutura de Diretórios

## Árvore do Projeto

```
frontend/
├── app/
│   ├── api/
│   │   └── chat/
│   │       └── route.ts      # Proxy para o backend FastAPI
│   ├── globals.css           # Estilos globais (Tailwind)
│   ├── layout.tsx            # Layout raiz, metadados
│   └── page.tsx              # Página principal do chat
├── docs/                     # Documentação (este diretório)
│   ├── README.md
│   ├── ARQUITETURA.md
│   ├── TECNOLOGIAS.md
│   ├── ESTRUTURA.md
│   ├── FLUXO-DADOS.md
│   ├── INTEGRACAO-BACKEND.md
│   └── ROADMAP.md
├── next-env.d.ts             # Tipos do Next.js
├── next.config.ts            # Configuração do Next.js
├── package.json
├── postcss.config.mjs        # PostCSS (Tailwind)
├── tailwind.config.ts       # Configuração Tailwind
├── tsconfig.json            # Configuração TypeScript
└── .env.local                # Variáveis de ambiente (não versionado)
```

## Descrição dos Arquivos

### `app/page.tsx`

Página principal do chat. Contém:

- Hook `useChat` configurado com `api: "/api/chat"`
- Estado local `input` para o campo de texto
- Lista de `SUGGESTED_QUESTIONS` para perguntas iniciais
- Função `getMessageContent` para compatibilidade com formato `content` ou `parts`
- Layout: header, área de mensagens, formulário de envio

### `app/api/chat/route.ts`

Rota de API que atua como proxy:

- Recebe POST com `{ messages: [...] }`
- Extrai conteúdo de mensagens (suporta `content` e `parts`)
- Encaminha para `BACKEND_URL/api/chat`
- Transforma stream de texto em SSE no formato Data Stream Protocol
- Retorna `Response` com `Content-Type: text/event-stream`

### `app/layout.tsx`

Layout raiz:

- Metadados (title, description)
- Importa `globals.css`
- Estrutura HTML com `lang="pt-BR"`

### `app/globals.css`

- Diretivas Tailwind: `@tailwind base`, `@tailwind components`, `@tailwind utilities`

## Convenções

- **Componentes**: PascalCase
- **Arquivos**: kebab-case ou camelCase conforme padrão Next.js
- **Rotas de API**: `app/api/[recurso]/route.ts`
- **Client Components**: `"use client"` no topo do arquivo
