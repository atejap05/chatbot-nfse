# FAQ - Tributação ISS e ISSQN

> Audiência: contribuintes, gestores municipais, contadores
> Temas: ISSQN, retenção municipal, local de incidência, alíquota, LC 116/03, regra E0031
> Sistema: NFS-e Nacional - Portal do Contribuinte, Painel Administrativo Municipal

---

## Dúvida 007: ISS retido não está sendo deduzido do valor líquido da nota

**Pergunta:** Prestador emitiu notas para tomador em São José dos Campos/SP, com local da prestação em Aparecida/SP. As notas foram preenchidas com retenção do ISS pelo tomador, mas ao fazer download do XML e PDF o ISS retido não está sendo deduzido do valor líquido. Como resolver?

**Resposta:**

O problema decorre da Regra de Negócio E0031 (Município de Incidência vs. Tomador).

O Sistema Nacional aplica trava de segurança: não pode haver retenção do ISSQN pelo tomador quando o município de incidência do imposto não for o mesmo município de domicílio do tomador. No relato, o tomador está em São José dos Campos e o serviço foi prestado em Aparecida. Se o código de serviço utilizado exige que o imposto seja devido no local da prestação (Aparecida), o sistema identifica que o município de incidência é diferente do município do tomador e rejeita ou ignora a indicação de retenção.

Impacto no Cálculo: O sistema só subtrai o valor do ISSQN do total líquido se o campo tpRetISSQN for validado como retido (valores 2 ou 3). Como a regra E0031 impede a retenção por tomador em município diverso, o sistema desconsidera a retenção informada.

Como Resolver: Confirme se, para o serviço em questão, o ISS é realmente devido em Aparecida. Se o imposto for devido no local do estabelecimento do prestador, altere o município de incidência. Use Emissão Completa. Se o município de incidência for Aparecida e o tomador estiver em São José dos Campos, o prestador deve recolher o imposto diretamente para Aparecida, sem retenção sistêmica pelo tomador, a menos que o tomador possua inscrição ou unidade em Aparecida.

**Resumo:** O ISSQN não está sendo deduzido porque o sistema aplicou a regra E0031, que proíbe retenção quando tomador e incidência estão em municípios diferentes.

---

## Dúvida 035: Nota com ISS incorreto não integra e não gera guia

**Pergunta:** A nota emitida está correta, porém não integrou o ISS com a prefeitura de Pindamonhangaba e não está gerando a guia para pagamento.

**Resposta:**

O motivo é erro no preenchimento dos campos estruturados de tributação. Embora o contribuinte tenha escrito na descrição que o serviço está "Sujeito a retenção na fonte", os campos técnicos foram preenchidos como "Não incidência", "Município de Incidência: Nenhum" e "ISSQN Apurado: zerado".

O sistema só identifica a localidade de incidência e destaca o imposto quando a operação é marcada como "1 - Operação Tributável". Quando indica "Não Incidência", não há valor a integrar nem guia a gerar.

O serviço 07.09.01 (Varrição, coleta e remoção de lixo) exige que o local de incidência seja o local da prestação. Ao selecionar "Não Incidência", o emitente desabilitou o cálculo automático.

Como Resolver: O contribuinte deve realizar a Substituição da NFS-e. No Passo 3 (Valores), alterar "Tributação do ISSQN" para "1 - Operação Tributável" e "Retenção do ISSQN" para "2 - Retido pelo Tomador". Ao finalizar, o sistema reconhecerá o ISSQN para Pindamonhangaba e permitirá a geração da guia.

**Resumo:** A nota está com preenchimento técnico incorreto. O prestador deve substituir a nota corrigindo a tributação para "Operação Tributável" com "Retenção pelo Tomador".

---

## Dúvida 041: ISS sobre guincho, guindastes e içamento (local da execução)

**Pergunta:** A LC 218/2025 regulamenta que o ISS sobre serviços de guincho intramunicipal, guindastes e içamento é devido no local da execução do serviço. Como orientar os contribuintes para o correto preenchimento da NFS-e?

**Resposta:**

Os serviços devem ser classificados nos códigos: 14.14.01 (Guincho intramunicipal) e 14.14.02 (Guindaste e içamento). O Sistema Nacional identifica a localidade de incidência conforme as regras da LC 116/03.

Para que o ISSQN seja corretamente destinado ao município de execução (ex: Pará de Minas), o contribuinte deve usar Emissão Completa e observar: No Passo 2 (Serviço), informar o país e o Município onde o serviço foi efetivamente executado. No Passo 3 (Valores), selecionar corretamente o campo tpRetISSQN: "1 - Não Retido" (prestador recolhe) ou "2 - Retido pelo Tomador" (tomador desconta). Atenção: O sistema rejeitará a retenção se o município de incidência não for o mesmo do tomador (Regra E0031).

Quando o prestador é domiciliado em município "A" mas executa em Pará de Minas (município "B"): A NFS-e deve indicar Operação Tributável; o local de incidência (cLocIncid) deve ser o código IBGE de Pará de Minas; se houver retenção, os dados do tomador e seu endereço em Pará de Minas devem ser informados.

Para a Prefeitura: Parametrizar a LC 218/2025 no módulo "Legislação para o ISSQN". No módulo "Retenções do ISSQN", vincular os subitens 14.14.01 e 14.14.02 à legislação municipal.

**Resumo:** Instrua o contribuinte a preencher o "Local da Prestação" como o município de execução e marcar "ISS Retido pelo Tomador" se aplicável, garantindo que o município de incidência seja identificado corretamente.

---

## Dúvida 065: Impossibilidade de editar alíquota e município de incidência do ISSQN

**Pergunta:** O sistema não permite editar os campos "alíquota do ISSQN" e "município de incidência do ISSQN". Aparece: "Não é permitido informar alíquota do ISSQN quando o município de incidência estiver conveniado ao Sistema Nacional NFS-e." Como proceder?

**Resposta:**

A impossibilidade de editar não é erro técnico, mas regra de negócio fundamental. O Sistema Nacional funciona sob a premissa de que o fisco não deve solicitar informações que já possui.

Alíquota Automática: Se o município de incidência do serviço é conveniado e está "Ativo", a alíquota é recuperada automaticamente da parametrização realizada pela prefeitura no Painel Administrativo Municipal. O sistema bloqueia a edição manual (Regras E0617 e E1300).

Incidência Automática: O município de incidência é determinado logicamente pelo sistema com base no Código de Tributação Nacional (cTribNac) informado, seguindo as regras da LC 116/03.

Para prestação em município diferente do prestador: O contribuinte deve selecionar "Emissão Completa" e, no Passo 2 (Serviço), informar corretamente o país e o município onde o serviço foi prestado.

Para ajuste de alíquotas: A prefeitura do município de incidência deve acessar o Painel Administrativo Municipal > Parametrização > Lista de Serviços e corrigir o valor da alíquota.

Procedimento de Contingência: Casos excepcionais devem ser tratados via fluxo de Decisão Administrativa/Judicial habilitado pelo município no Painel Municipal.

**Resumo:** Erros de alíquota devem ser corrigidos pela prefeitura no Painel Municipal. Casos excepcionais devem ser tratados via Decisão Administrativa/Judicial.

---

## Dúvida 100: Trava de retenção municipal não está funcionando

**Pergunta:** Prefeitura parametrizou quais serviços devem ser retidos pelos tomadores quando da incidência em seu território. Porém a trava não está funcionando - estão emitindo notas em desacordo com a legislação local.

**Resposta:**

O comportamento relatado não é necessariamente erro de processamento, mas característica da fase atual de implementação das regras de retenção.

1. Natureza Informativa da Regra (Alerta vs. Bloqueio)

As regras de retenção parametrizadas pelo município possuem, neste momento inicial, caráter predominantemente informativo. Quando o contribuinte preenche uma nota cuja regra municipal prevê retenção, o emissor apresenta um ALERTA informando que o Município de incidência indicou que a operação deve ser objeto de retenção. A regra não rejeita a emissão caso o contribuinte ignore o alerta e prossiga sem marcar a retenção.

2. Regra de Negócio E0031

O sistema aplica trava rígida: não pode haver retenção do ISSQN pelo tomador quando o município de incidência não for o mesmo município de domicílio do tomador. Se o serviço for prestado no município mas o tomador estiver em outra cidade, o sistema rejeitará ou ignorará a indicação de retenção.

3. Verificação da Parametrização

A prefeitura deve revisar no módulo Retenções do ISSQN: vinculação de serviços, responsáveis tributários e vigência da regra.

4. Como a Prefeitura deve proceder

Utilizar o ícone de Consulta NFS-e (lupa) no Painel Municipal para filtrar as notas emitidas e identificar aquelas onde o campo tpRetISSQN foi preenchido como "1 - Não Retido" em serviços que deveriam ser retidos. Com base nesses dados, o município pode realizar a cobrança ou ação fiscal.

**Resumo:** O sistema nacional prioriza a emissão, exibindo apenas alerta informativo sobre a retenção municipal. O bloqueio automático não ocorre para evitar conflitos com a LC 116/03. O município deve monitorar via Consulta NFS-e e realizar ação fiscal quando necessário.
