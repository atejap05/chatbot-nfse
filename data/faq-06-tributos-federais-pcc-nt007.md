# FAQ - Tributos Federais, PCC e NT 007

> Audiência: contribuintes, contadores, integradores
> Temas: PIS, COFINS, CSLL, retenção na fonte, vRetCSLL, tpRetPisCofins, Nota Técnica 007
> Sistema: NFS-e Nacional - Portal do Contribuinte, API, layout v1.01

---

## Dúvida 030: Retenção de IRPF para pessoa física prestadora de serviços ao município

**Pergunta:** O contribuinte é pessoa física e presta serviços para o município. Não há obrigatoriedade da retenção? E nos casos com valor superior a R$ 5.000,00, o que fazer, haja vista que o município deve reter o IRPF?

**Resposta:**

O Sistema Nacional possui travas automáticas para emissores Pessoa Física (CPF). A Regra E0675 estabelece que não é permitida a prestação de informações relativas aos tributos federais (como IRRF) quando o emitente for identificado por CPF. Os campos de Tributação Federal ficam desabilitados.

Embora a legislação federal obrigue o município a reter o Imposto de Renda em pagamentos acima de determinados valores, o Padrão Nacional foi desenhado para que a pessoa física não faça o destaque desses tributos diretamente no corpo do documento fiscal. O contribuinte deve emitir a nota pelo valor bruto do serviço, sem o destaque da retenção. No momento do pagamento, a prefeitura (tomadora) deve aplicar as alíquotas da tabela progressiva do IR ou as regras de retenção ampla, efetuando a retenção no seu sistema financeiro/contábil e gerando a guia de recolhimento (DARF).

Alternativa: Se o município possuir norma local que exija o valor retido no XML, pode utilizar o módulo de Parametrização de Decisões Administrativas/Judiciais para cadastrar Decisão vinculando o CPF do contribuinte e o código do serviço.

**Resumo:** Pela regra padrão, o CPF não consegue preencher campos de tributos federais. A retenção do IRPF deve ser calculada e executada pelo município tomador no momento da liquidação financeira do serviço.

---

## Dúvida 031: PIS/COFINS/CSLL duplicados no valor retido

**Pergunta:** O emissor apresentava o campo "Valor Retido CSLL", que foi alterado para "Valor Retido PIS/COFINS/CSLL". Ao informar o valor total correspondente a PIS, COFINS e CSLL nesse campo, o sistema gera duplicidade no valor final, pois PIS e COFINS também são informados em campos próprios. Qual a forma correta de declarar?

**Resposta:**

O layout possui grupo específico para piscofins (PIS e COFINS) e campos individuais para retenções federais: vRetCP (INSS), vRetIRRF (IR) e vRetCSLL (CSLL). O sistema calcula: vTotalRet = (vRetCP + vRetIRRF + vRetCSLL) + vISSQN + (vPis + vCofins).

Se o contribuinte informar o valor acumulado das três contribuições (PCC - 4,65%) no campo que inclui a descrição PIS/COFINS/CSLL e também preencher os campos individuais de PIS e COFINS, o sistema somará os valores novamente, gerando duplicidade.

Forma Correta (conforme layout e Anexo I): O CSLL possui campo próprio de retenção (vRetCSLL). PIS e COFINS são detalhados no grupo piscofins. Os valores não devem ser repetidos em campos que compõem a mesma soma final. Com a NT 007 (vigente desde 09/02/2026), o procedimento correto passou a ser: somar PIS + COFINS + CSLL e informar integralmente no campo vRetCSLL; selecionar tpRetPisCofins = 3 ("PIS/COFINS/CSLL Retidos"); zerar os campos individuais vPis e vCofins.

**Resumo:** Não some os tributos em um único campo e repita em outros. Com a NT 007, some PIS + COFINS + CSLL, informe no vRetCSLL, selecione tipo 3 e mantenha vPis e vCofins zerados.

---

## Dúvida 032: Tributação federal (valor retido CP) não liberada para autônomo

**Pergunta:** Contribuinte autônomo tentou emitir nota e a tributação federal, valor retido CP (INSS), não está liberada. Tentamos pelo Portal Municipal e pelo Portal do Contribuinte, a opção não está liberada. Como resolver?

**Resposta:**

A impossibilidade de editar os campos de Tributação Federal (especificamente o valor retido CP/INSS) para contribuinte autônomo não é erro do sistema, mas trava fundamentada na Regra de Negócio E0675.

O sistema estabelece que não é permitida a prestação de informações relativas aos tributos federais quando o emitente da DPS for identificado por pessoa física (CPF). Como o contribuinte autônomo opera sob CPF (Regime Especial Código 5 – Profissional Autônomo), o sistema desabilita automaticamente todos os campos de retenção federal (INSS, IRRF, CSLL, PIS e COFINS).

O padrão nacional foi desenhado para que, em operações por CPFs, o destaque desses tributos não ocorra dentro do arquivo XML da nota fiscal.

Como resolver: O contribuinte autônomo deve emitir a NFS-e pelo valor bruto do serviço, deixando os campos de tributação federal zerados. O município (ou tomador) deve efetuar o cálculo e a retenção do INSS de forma externa ao sistema da NFS-e, no momento do processamento do pagamento. O valor pode ser informado no campo "Informações Complementares" apenas para fins informativos.

**Resumo:** O campo não será liberado para CPFs devido à regra E0675. O contribuinte deve emitir pelo valor total e a prefeitura deve realizar a retenção do INSS em seu sistema financeiro no momento do pagamento.

---

## Dúvida 037: Campo de retenção PIS/COFINS/CSLL - qual o correto?

**Pergunta:** Ao preencher os dados para emitir a nota, não tem o campo de retenção de PIS/COFINS, apenas o campo "Retenção de PIS/COFINS/CSLL". Preenchendo este campo, o sistema considera retenção total dos tributos? Qual o correto?

**Resposta:**

No Sistema Nacional, as retenções de PIS, COFINS e CSLL possuem campos específicos e o preenchimento deve ser individualizado para evitar duplicidade.

1. Localização dos Campos (Emissão Completa, Passo 3 - Valores, Tributação Federal)

PIS e COFINS: Estão dentro do grupo piscofins. O preenchimento depende da seleção do CST. Ao selecionar CST tributável, o sistema habilita os campos para Alíquota e Valor de PIS e COFINS separadamente. É fundamental marcar "Tipo de retenção do PIS/COFINS" como "1 - Retido" para que os valores sejam subtraídos do valor líquido. CSLL: Possui campo próprio "Valor Retido CSLL" (vRetCSLL).

2. Erro da Retenção Total (Duplicidade)

Se o contribuinte informar o valor total do "pacote" (PIS/COFINS/CSLL - 4,65%) no campo da CSLL e também preencher os campos individuais de PIS e COFINS, o sistema somará os valores novamente, gerando duplicidade.

3. Forma Correta (atualizada pela NT 007)

Desde 09/02/2026, conforme NT 007: Some PIS + COFINS + CSLL e informe o total no campo vRetCSLL ("Valor Relativo às Retenções de Contribuições Sociais"). Selecione tpRetPisCofins = 3 ("PIS/COFINS/CSLL Retidos"). Mantenha os campos individuais vPis e vCofins zerados (exceto se houver débito próprio a declarar).

**Resumo:** Com a NT 007, some PIS + COFINS + CSLL, informe no vRetCSLL, selecione tipo 3 e mantenha vPis e vCofins zerados para evitar duplicidade.

---

## Dúvida 050: PIS/COFINS/CSLL - valor total causa duplicidade no líquido

**Pergunta:** Ao emitir nota, o sistema solicita o valor total de PIS/COFINS/CSLL. Colocando o total dos três tributos, o valor final da nota retém PIS e COFINS em duplicidade. O valor só fecha se for colocado apenas o CSLL. O que está sendo feito de errado?

**Resposta:**

O erro ocorre por confusão entre o rótulo de exibição no portal e a estrutura técnica de cálculo. O sistema calcula: vTotalRet = (vRetCP + vRetIRRF + vRetCSLL) + vISSQN + (vPIS + vCOFINS). Se inserir a soma dos três tributos no campo da CSLL e também preencher os campos específicos de PIS e COFINS, o sistema contará PIS e COFINS duas vezes.

Orientação anterior (pré-NT 007): Declarar o valor de PIS e o de COFINS em seus campos próprios dentro do grupo PIS/COFINS e declarar apenas o valor da CSLL no campo de retenção da CSLL.

Orientação atual (NT 007, vigente desde 09/02/2026): Os valores de PIS + COFINS + CSLL devem ser SOMADOS e informados integralmente no campo vRetCSLL. O campo tpRetPisCofins deve ser preenchido com o código 3 ("PIS/COFINS/CSLL Retidos"). Os campos individuais vPis e vCofins devem ser zerados para fins de retenção.

**Resumo:** Com a NT 007, some PIS + COFINS + CSLL, insira o total no vRetCSLL, selecione tipo 3 e mantenha vPis e vCofins zerados.

---

## Dúvida 092: Retenções federais - PIS e COFINS não considerados como retidos

**Pergunta:** Ao emitir NFS-e para serviço com retenção de tributos federais, o sistema calcula corretamente IRRF e CSLL, mas calcula PIS e COFINS apenas como "Débito de Apuração Própria" e não como tributos retidos na fonte. O valor líquido não reflete todas as retenções. Como corrigir?

**Resposta:**

A situação não se trata de erro de cálculo, mas de mudança na regra de preenchimento e no layout implementada pela Nota Técnica SE/CGNFS-e nº 007 (vigente desde 09/02/2026). A alteração visa adequação às regras da Reforma Tributária (RTC), evitando redução indevida da base de cálculo do IBS e da CBS.

1. Novo Campo de Agregação (vRetCSLL)

Se houver valores de retenções federais de PIS, COFINS e CSLL, eles não devem mais ser informados nos campos individuais de PIS e COFINS para fins de retenção. Os valores de PIS + COFINS + CSLL devem ser SOMADOS e informados integralmente no campo vRetCSLL ("Valor Relativo às Retenções de Contribuições Sociais"). Os campos vPis e vCofins agora são destinados exclusivamente para débitos de apuração própria do prestador.

2. Alteração no Código de Retenção (tpRetPisCofins)

Selecione o código 3: "PIS/COFINS/CSLL Retidos". Este código instrui o motor de cálculo do ADN a considerar o valor total inserido em vRetCSLL como dedução para chegar ao Valor Líquido (vLiq).

3. Procedimento Correto

Zere os campos individuais de PIS e COFINS (se o objetivo for apenas retenção). No campo "Tipo de Retenção PIS/COFINS e CSLL", selecione a opção 3 (PIS/COFINS/CSLL Retidos). No campo vRetCSLL, informe o valor total somado das três contribuições (geralmente 4,65% sobre o valor bruto).

**Resumo:** Zere vPis e vCofins, selecione tipo 3 e informe a soma de PIS + COFINS + CSLL no campo vRetCSLL. Esta mudança é obrigatória desde 09/02/2026.

---

## Dúvida 097: Divergência no valor líquido e na descrição dos impostos retidos

**Pergunta:** Anteriormente fomos orientados a inserir apenas o CSLL no campo para que o valor líquido ficasse correto. Porém agora, se colocamos apenas o CSLL, o valor final não desconta o PIS e COFINS. Se colocamos o valor total (PIS/COFINS/CSLL), o valor líquido fica correto, mas a descrição dos impostos retidos continua incorreta. Como resolver?

**Resposta:**

A situação deve-se à mudança introduzida pela Nota Técnica SE/CGNFS-e nº 007, em vigor desde 09/02/2026. A orientação anterior está desatualizada.

1. Consolidação no campo vRetCSLL

Se houver retenção de PIS, COFINS e CSLL (4,65%), os valores devem ser SOMADOS e informados integralmente em um único campo: o vRetCSLL ("Valor Relativo às Retenções de Contribuições Sociais"). Por isso, ao colocar o valor total, o valor líquido "fecha" corretamente.

2. Seleção do Código de Retenção (tpRetPisCofins)

Selecione a Opção 3: "PIS/COFINS/CSLL Retidos". Este código instrui o motor de cálculo a entender que o valor em vRetCSLL compreende a soma das três contribuições e deve ser deduzido do valor líquido.

3. Zerar os campos individuais de PIS e COFINS

Os campos vPis e vCofins devem ser deixados ZERADOS ou em branco para fins de retenção. Na nova versão do layout, esses campos destinam-se exclusivamente a informar débitos de apuração própria do prestador.

A descrição pode parecer confusa porque o sistema está em fase de transição gradual dos rótulos. Com a obrigatoriedade dos grupos IBS/CBS, o campo que antes era apenas "CSLL" passa a representar a retenção agregada das contribuições sociais.

**Resumo:** Some PIS + COFINS + CSLL, insira o total no vRetCSLL, selecione tipo 3 e mantenha vPis e vCofins zerados.

---

## Dúvida 101: Notas com retenção PCC via webservice com valor líquido incorreto

**Pergunta:** Desde 09/02 as notas fiscais com retenção de PCC (PIS/COFINS/CSLL) estão sendo geradas em desacordo no portal nacional. O ERP gera o XML corretamente, porém no portal as notas saem somente com a retenção do CSLL, e o valor líquido da NF fica incorreto. Como proceder?

**Resposta:**

O problema ocorre devido à mudança estrutural no layout do sistema nacional que entrou em vigor em 09/02/2026. O erro deve-se à forma como o ERP está preenchendo os campos de tributos federais no XML.

1. Diagnóstico do Erro no XML

Os valores de PIS e COFINS foram informados nas tags vPis e vCofins. De acordo com a NT 007, esses campos destinam-se exclusivamente a informar valores de débitos de apuração própria do prestador. Quando informados nesses campos, o sistema não os considera como dedução para o cálculo do valor líquido, tratando-os como imposto a pagar pelo prestador. Por isso apenas o valor na tag vRetCSLL foi retido no portal.

2. Procedimento de Correção (Agregação de Valores)

Some os valores de PIS + COFINS + CSLL. O valor total somado deve ser informado integralmente no campo vRetCSLL. Os campos vPis e vCofins devem ser deixados zerados (caso não haja débito próprio). O campo tpRetPisCofins deve ser preenchido com o código 3 ("PIS/COFINS/CSLL Retidos").

3. Ajuste na Integração

O sistema está enviando os dados no formato antigo. Ajuste a integração para que os valores de PIS e COFINS retidos sejam migrados para dentro do campo vRetCSLL, mantendo os campos originais de PIS/COFINS zerados. Esta mudança é obrigatória para evitar divergências entre o XML emitido e o registro oficial no ADN.

**Resumo:** Ajuste o ERP para informar a soma de PIS + COFINS + CSLL no campo vRetCSLL, com tpRetPisCofins = 3, e zerar vPis e vCofins. Esta mudança é obrigatória desde 09/02/2026.
