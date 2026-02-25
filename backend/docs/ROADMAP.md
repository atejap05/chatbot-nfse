# Roadmap do Backend

## Fase Atual (v0.1.0)

- [x] API FastAPI com rota de chat
- [x] Pipeline RAG com LlamaIndex
- [x] Integração Qdrant + HuggingFace + Anthropic
- [x] Streaming de respostas
- [x] Script de ingestion separado
- [x] System prompt especializado
- [x] Health check

## Melhorias Planejadas

### Curto Prazo

| Item | Descrição | Prioridade |
|------|-----------|------------|
| **Histórico de conversação** | Passar contexto completo para o LLM (últimas N mensagens) | Alta |
| **Citação de fontes** | Retornar metadados dos chunks (source_file, duvida_id) no stream ou em campo separado | Alta |
| **Tratamento de erros** | Respostas estruturadas para Qdrant offline, API key inválida, timeout | Alta |
| **Logging** | Estruturar logs (requisições, latência, erros) | Média |
| **Rate limiting** | Limitar requisições por IP/sessão | Média |

### Médio Prazo

| Item | Descrição | Prioridade |
|------|-----------|------------|
| **Reindexação incremental** | Atualizar apenas documentos alterados no ingest | Média |
| **Múltiplas collections** | Separar por categoria para busca mais precisa | Baixa |
| **Reranking** | Reordenar chunks recuperados antes de enviar ao LLM | Média |
| **Cache de embeddings** | Evitar reembedd de queries repetidas | Baixa |
| **Métricas** | Prometheus/OpenTelemetry para monitoramento | Média |

### Longo Prazo

| Item | Descrição | Prioridade |
|------|-----------|------------|
| **Feedback de qualidade** | Endpoint para registrar avaliação das respostas | Média |
| **A/B testing de prompts** | Testar variações do system prompt | Baixa |
| **Suporte a anexos** | Permitir upload de documentos para contexto adicional | Baixa |
| **API de admin** | Endpoints para trigger de reindexação, status do Qdrant | Baixa |

## Dependências do Ingest

| Item | Descrição |
|------|-----------|
| **Formato dos FAQs** | Markdown com `## Dúvida NNN:` como H2; alterações exigem ajuste no parser |
| **Novos arquivos** | Adicionar em `data/faq-*.md` e em `FAQ_CATEGORIES` no ingest.py |
| **Qdrant** | Deve estar rodando antes de executar o ingest |

## Evolução do RAG

Possíveis melhorias no pipeline:

1. **Hybrid search**: Combinar busca vetorial com BM25 (keywords)
2. **Query expansion**: Reformular a pergunta antes da busca
3. **Parent chunk retrieval**: Incluir chunk pai/filho para mais contexto
4. **Streaming com fontes**: Emitir marcadores no stream indicando qual chunk está sendo usado

## Cronograma Sugerido

| Trimestre | Foco |
|-----------|------|
| Q1 | Histórico de conversação, citação de fontes, tratamento de erros |
| Q2 | Logging, rate limiting, reranking |
| Q3 | Reindexação incremental, métricas |
| Q4 | Feedback de qualidade, API de admin |
