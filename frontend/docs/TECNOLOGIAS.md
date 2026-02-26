# Tecnologias do Frontend

## Stack Principal

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| **Next.js** | 16.1.6 | Framework React com App Router, Turbopack, SSR e API Routes |
| **React** | 19.2.4 | Biblioteca de UI |
| **TypeScript** | ^5.1.0 | Tipagem estática |
| **Tailwind CSS** | ^3.4.15 | Estilização utilitária |
| **Vercel AI SDK** | ai ^4.0.0, @ai-sdk/react ^1.0.0 | Chat, streaming e estado de conversação |
| **react-markdown** | ^9.0.0 | Renderização de Markdown nas respostas |

## Dependências de Produção

```json
{
  "@ai-sdk/react": "^1.0.0",   // Hook useChat e integração com AI
  "ai": "^4.0.0",              // Core do Vercel AI SDK
  "next": "16.1.6",
  "react": "19.2.4",
  "react-dom": "19.2.4",
  "react-markdown": "^9.0.0"   // Formatação de respostas (listas, negrito, etc.)
}
```

## Dependências de Desenvolvimento

| Pacote | Função |
|--------|--------|
| `@types/node`, `@types/react`, `@types/react-dom` | Tipagens TypeScript |
| `autoprefixer` | Prefixos CSS para compatibilidade |
| `postcss` | Processamento CSS (Tailwind) |
| `eslint`, `eslint-config-next` | Linting |
| `tailwindcss` | Framework CSS |
| `typescript` | Compilador TypeScript |

## Vercel AI SDK

O **Vercel AI SDK** fornece:

- **`useChat`**: Hook que gerencia mensagens, input, status (streaming, ready, error) e envio
- **`sendMessage`**: Função para enviar mensagens programaticamente
- **Data Stream Protocol**: Formato SSE para streaming de texto (`text-delta`, `text-start`, `text-end`, `finish`)

## Tailwind CSS

- Configuração em `tailwind.config.ts`
- Conteúdo escaneado: `./app/**/*`, `./pages/**/*`, `./components/**/*`
- Tema: extensões padrão; paleta Slate para neutros, Blue para ações

## Compatibilidade

- **Node.js**: 20.9+ (LTS; Node 18 não é mais suportado pelo Next.js 16)
- **Navegadores**: Chrome 111+, Edge 111+, Firefox 111+, Safari 16.4+
- **Next.js**: App Router; Turbopack é o bundler padrão em dev e build
