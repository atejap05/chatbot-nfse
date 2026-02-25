# Roadmap do Frontend

## Fase Atual (v0.1.0)

- [x] Interface de chat funcional
- [x] Integração com backend via proxy
- [x] Streaming de respostas
- [x] Mensagens sugeridas
- [x] Renderização Markdown
- [x] Layout responsivo básico

## Melhorias Planejadas

### Curto Prazo

| Item | Descrição | Prioridade |
|------|-----------|------------|
| Tratamento de erros | Exibir mensagens de erro ao usuário (backend offline, timeout) | Alta |
| Indicador de status do backend | Badge "Conectado" / "Desconectado" no header | Média |
| Histórico de conversação | Persistência em localStorage ou sessão | Média |
| Acessibilidade | ARIA labels, navegação por teclado, foco em erros | Alta |
| Loading state | Skeleton ou spinner durante carregamento inicial | Baixa |

### Médio Prazo

| Item | Descrição | Prioridade |
|------|-----------|------------|
| Citação de fontes | Exibir FAQ/Dúvida de origem da resposta (quando backend retornar) | Alta |
| Tema escuro | Toggle dark/light mode | Média |
| Exportar conversa | Download da conversa em PDF ou TXT | Baixa |
| Feedback de qualidade | Botões "Útil" / "Não útil" para respostas | Média |
| Componentização | Extrair `ChatMessage`, `ChatInput`, `SuggestedQuestions` | Média |

### Longo Prazo

| Item | Descrição | Prioridade |
|------|-----------|------------|
| PWA | Suporte offline parcial, instalação como app | Baixa |
| Internacionalização | Suporte a múltiplos idiomas (se necessário) | Baixa |
| Analytics | Métricas de uso (perguntas mais frequentes, tempo de resposta) | Média |
| Testes automatizados | Jest + React Testing Library, testes E2E (Playwright) | Alta |

## Dependências de Backend

Algumas melhorias do frontend dependem de evolução do backend:

- **Citação de fontes**: Backend precisa retornar metadados dos chunks recuperados (ex.: `source_file`, `duvida_id`)
- **Feedback de qualidade**: Backend pode expor endpoint para registrar feedback
- **Histórico contextual**: Backend pode aceitar histórico completo para respostas mais contextuais (hoje usa só a última mensagem)

## Cronograma Sugerido

| Trimestre | Foco |
|-----------|------|
| Q1 | Tratamento de erros, acessibilidade, citação de fontes |
| Q2 | Tema escuro, feedback de qualidade, componentização |
| Q3 | Testes automatizados, persistência de histórico |
| Q4 | Analytics, PWA (se relevante) |
