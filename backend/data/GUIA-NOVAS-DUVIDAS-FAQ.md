# Guia para Novas Dúvidas e Arquivos FAQ - NFS-e

Este guia orienta como adicionar novas perguntas, criar novos arquivos FAQ e categorizar conteúdo para o chatbot NFS-e no Microsoft Copilot Studio.

---

## 1. Categorias Existentes

As 105 dúvidas originais estão distribuídas em **8 categorias temáticas**. Use-as como referência para classificar novas dúvidas:

| Categoria | Arquivo | Temas principais |
|-----------|---------|------------------|
| Painel Municipal | faq-01 | Parametrização, ativação de convênio, adoção faseada, menu Pendências, sincronização ADN |
| Cadastro CNC | faq-02 | Primeiro acesso, tríade Município+CNPJ/CPF+IM, inativação, reativação, status de emissão |
| Emissão no Portal | faq-03 | Preenchimento, dados do tomador, CEP, códigos de serviço, emissão completa/simplificada, MEI |
| Cancelamento e Substituição | faq-04 | Análise fiscal, cancelamento por ofício, manifestação, substituição |
| Tributação ISS/ISSQN | faq-05 | Retenção municipal, local de incidência, alíquotas, LC 116/03 |
| Tributos Federais | faq-06 | PIS, COFINS, CSLL, IRRF, NT 007, PCC |
| Reforma Tributária | faq-07 | IBS, CBS, RTC, MAN, DNA, LC 214/2025 |
| Integração API | faq-08 | API ADN, compartilhamento, transcrição, faixas de série, XML, erros |

---

## 2. Como Categorizar uma Nova Dúvida

### Passo 1: Identificar o tema principal

- **Qual é o principal problema?** (ex: emissão bloqueada, erro de API, dúvida sobre ISS)
- **Quem é o público?** (contribuinte, gestor municipal, desenvolvedor)
- **Qual sistema está envolvido?** (Portal do Contribuinte, Painel Municipal, API ADN)

### Passo 2: Escolher a categoria

- **Dúvidas que abrangem dois temas** → escolha o mais **específico**
- **Exemplo:** "Erro ao emitir nota por causa de ISS retido" → faq-05 (Tributação ISS), não faq-03 (Emissão)

### Passo 3: Atualizar o mapeamento

Ao adicionar uma nova dúvida, registre o mapeamento em `MAPEO-CATEGORIAS.md`:

```markdown
| D106 | Emissão | faq-03 |
```

---

## 3. Formato Padrão de Cada Q&A

Cada nova entrada deve seguir exatamente este formato:

```markdown
---

## Dúvida NNN: [Título de 5-10 palavras resumindo o problema]

**Pergunta:** Texto original da pergunta (limpo, sem referências a arquivos externos).

**Resposta:**

[Texto da resposta com formatação preservada: listas, subitens, negritos]

**Resumo:** [Frase objetiva com a solução principal em 1-2 linhas]

---
```

### Regras de formatação

| Elemento | Regra |
|----------|-------|
| `## Dúvida NNN:` | Deve ser **H2** real (##), não texto simples |
| Título | 5–10 palavras, descritivo |
| **Pergunta:** | Sempre presente; texto limpo; sem "Ver arquivo X.pdf" |
| **Resposta:** | Sempre presente; preservar listas, subitens, negritos |
| **Resumo:** | Resumo objetivo da solução (se já existir no texto, manter) |
| `---` | Separador entre cada Q&A (reforça fronteira de chunk no Copilot) |

### O que remover

- Datas de conversação (`quinta-feira, 5 de fevereiro d`)
- Referências a arquivos externos (`Ver o arquivo "Tela 06.jpg"`, `Para responder, veja o arquivo "00 Nota.pdf"`)
- Notas de descarte (`Descarte a dúvida 083`)
- CNPJs/CPFs reais → substituir por genéricos quando não relevantes

---

## 4. Como Adicionar uma Nova Pergunta

### Opção A: Inserir em arquivo existente

1. Localize o arquivo correto pela categoria (ex: `faq-03-emissao-nfse-portal.md`)
2. Use o próximo número sequencial (ex: D106 após D105)
3. Cole o bloco no formato padrão
4. Adicione a linha no `MAPEO-CATEGORIAS.md`, se necessário

### Opção B: Criar novo arquivo FAQ

1. Siga a seção **5. Como Estruturar Novo Arquivo FAQ**
2. Siga a seção **6. Atualizar Configuração do Copilot Studio**

---

## 5. Como Estruturar Novo Arquivo FAQ

### Quando criar um novo arquivo

- Quando surgir um **tema novo** que não se encaixa nas 8 categorias atuais
- Quando um arquivo existente ficar muito grande (> 25–30 Q&As) e o tema permitir subdivisão

### Estrutura do novo arquivo

```markdown
# FAQ - [Nome da Categoria]

> Audiência: [contribuintes / gestores municipais / desenvolvedores]
> Temas: [lista de palavras-chave principais]
> Sistema: NFS-e Nacional - Portal do Contribuinte / Painel Municipal / API ADN

---

## Dúvida NNN: [Título]
...
```

### Regras de metadados

| Campo | Descrição |
|-------|-----------|
| **Audiência** | Quem usa esse conteúdo (contribuintes, gestores municipais, contadores, integradores) |
| **Temas** | Palavras-chave que o orquestrador usa para decidir quando consultar a fonte |
| **Sistema** | Módulo do sistema (Portal, Painel, API) |

### Nomenclatura do arquivo

- Padrão: `faq-NN-[nome-tematico].md`
- Exemplo: `faq-09-compliance-obrigacoes.md`

---

## 6. Atualizar Configuração do Copilot Studio

Ao adicionar um **novo arquivo** FAQ:

1. **Upload:** `Overview > Knowledge > Add Knowledge > Files (Upload)`
2. **Name:** `FAQ - [Tema]`
3. **Description:** texto descritivo específico (ex.: `"Respostas para dúvidas sobre [tema]: [palavras-chave]."`)
4. Aguardar status **Ready** (5–30 min)

> Atualize também a tabela de descrições em `INSTRUCOES-COPILOT-STUDIO.md`.

---

## 7. Checklist para Nova Dúvida

- [ ] Categoria identificada
- [ ] Linha adicionada em `MAPEO-CATEGORIAS.md` (se aplicável)
- [ ] Formato: `## Dúvida NNN:` como H2
- [ ] Labels `**Pergunta:**` e `**Resposta:**` presentes
- [ ] `**Resumo:**` preenchido
- [ ] Separador `---` antes e depois
- [ ] Sem referências a arquivos externos
- [ ] Sem datas de conversação
- [ ] CNPJs/CPFs reais substituídos por genéricos (se aplicável)

---

## 8. Checklist para Novo Arquivo FAQ

- [ ] Nome do arquivo: `faq-NN-[nome-tematico].md`
- [ ] Cabeçalho H1 com nome da categoria
- [ ] Bloco de metadados (Audiência, Temas, Sistema)
- [ ] Primeiro separador `---` após metadados
- [ ] Todas as Q&As no formato padrão
- [ ] Linha adicionada em `MAPEO-CATEGORIAS.md` para cada dúvida
- [ ] Linha adicionada em `INSTRUCOES-COPILOT-STUDIO.md` (Name e Description)

---

## 9. Limites do Copilot Studio

- **Máximo de 5 fontes** diferentes por agente (SharePoint, OneDrive, arquivos, etc.)
- **Máximo de 500 objetos** de conhecimento por agente (arquivos, pastas, etc.)
- **Indexação:** 5–30 minutos após upload
- **Arquivos grandes:** o Dataverse faz chunks; use `---` separadores para reforçar fronteiras entre Q&As

---

## 10. Referências

- [Microsoft Copilot Studio - Unstructured data](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-unstructured-data)
- [Microsoft Copilot Studio - Agent instructions](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-instructions)
- [Instruções de upload no projeto](INSTRUCOES-COPILOT-STUDIO.md)
- [Mapeamento de categorias](MAPEO-CATEGORIAS.md)
