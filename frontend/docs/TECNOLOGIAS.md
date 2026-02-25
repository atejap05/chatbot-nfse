# Tecnologias do Frontend

## Stack Principal

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| **Next.js** | 14.2.18 | Framework React com App Router, SSR e API Routes |
| **React** | ^18.2.0 | Biblioteca de UI |
| **TypeScript** | ^5.0.0 | Tipagem estática |
| **Tailwind CSS** | ^3.4.15 | Estilização utilitária |
| **Vercel AI SDK** | ai ^4.0.0, @ai-sdk/react ^1.0.0 | Chat, streaming e estado de conversação |
| **react-markdown** | ^9.0.0 | Renderização de Markdown nas respostas |

## Dependências de Produção

```json
{
  "@ai-sdk/react": "^1.0.0",   // Hook useChat e integração com AI
  "ai": "^4.0.0",              // Core do Vercel AI SDK
  "next": "14.2.18",
  "react": "^18.2.0",
  "react-dom": "^18.2.0",
  "react-markdown": "^9.0.0"    // Formatação de respostas (listas, negrito, etc.)
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

- **Node.js**: 18+
- **Navegadores**: Chrome, Firefox, Safari, Edge (versões recentes)
- **Next.js**: App Router (não Pages Router)
