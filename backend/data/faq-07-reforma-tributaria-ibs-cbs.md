# FAQ - Reforma Tributária, IBS e CBS

> Audiência: contribuintes, gestores municipais, contadores
> Temas: Reforma Tributária, IBS, CBS, RTC, MAN, DNA, LC 214/2025, grupos IBSCBS
> Sistema: NFS-e Nacional - Portal do Contribuinte, Painel Administrativo Municipal

---

## Dúvida 012: Advogados conveniados - CNPJ, CPF e emissão de notas na Reforma Tributária

**Pergunta:** O município possui convênio de assistência jurídica. Advogados atendem como pessoa física e emitem RPA. Com a Reforma Tributária, profissionais liberais precisarão de CNPJ? O cadastro fiscal é municipal ou o CNPJ? É possível emitir notas avulsas pelo CPF?

**Resposta:**

1. O "CNPJ para Pessoa Física" e o Cadastro Fiscal

O cadastro mencionado na LC 214/2025 e nas diretrizes do Comitê Gestor do IBS refere-se a identificação fiscal para fins de apuração nacional. O sistema da NFS-e Nacional opera sob a "tríade única": Código do Município + Inscrição Federal (CNPJ ou CPF) + Inscrição Municipal (IM). O "cadastro fiscal" não substitui o municipal; integra a base onde a prefeitura complementa as informações do profissional (CPF ou CNPJ) com a IM local através do CNC.

2. Emissão por CPF vs. CNPJ

Embora haja movimento para que profissionais liberais possuam CNPJ para "facilitar a apuração" de IBS/CBS, o sistema está preparado para emitir notas tanto para CNPJ quanto para CPF. O município possui, no Painel Administrativo, a opção de configurar se "é permitida a emissão de NFS-e por pessoas físicas (CPF)". A tendência da reforma é que o RPA seja substituído pela NFS-e, inclusive na modalidade NFS-e Avulsa (Código 103).

3. Regime de "Profissional Autônomo" (Advogados)

Para advogados como pessoa física (CPF), o sistema prevê o Regime Especial Código 5 – Profissional Autônomo. Quando configurado neste regime, não há destaque de ISSQN na NFS-e (o recolhimento costuma ser por valor fixo anual ou outra forma prevista na lei municipal).

4. Impacto da Reforma (IBS e CBS)

A partir de janeiro de 2026, mesmo que o profissional continue emitindo como CPF (se autorizado), a nota deverá conter os grupos de informações do IBS e da CBS. Para optantes do Simples Nacional, esses grupos só serão obrigatórios em 2027. Para profissionais liberais no regime regular, a obrigatoriedade inicia em 01/01/2026.

**Resumo:** O cadastro fiscal integra o municipal. Emissão por CPF é possível se o município autorizar. Advogados podem usar Regime Especial Profissional Autônomo. Grupos IBS/CBS passam a ser obrigatórios conforme o regime e o cronograma da reforma.

---

## Dúvida 016: Guia de pagamento unificado do ISSQN e retenções na fonte

**Pergunta:** Em que momento os usuários do emissor nacional terão acesso para emissão e pagamento do ISSQN referente às notas emitidas em janeiro/2026? E quanto às retenções em fonte, como a prefeitura irá proceder? Haverá guia de pagamento dentro do Painel Municipal?

**Resposta:**

1. Disponibilidade do Módulo de Apuração Nacional (MAN)

O pagamento do ISSQN no Sistema Nacional é realizado por meio do Documento Nacional de Arrecadação (DNA), gerado através do MAN. Embora a transição para o novo layout (IBS e CBS) esteja confirmada para janeiro de 2026, a funcionalidade de apuração unificada depende da ativação total do módulo MAN. Conforme os guias técnicos de outubro de 2025, o MAN constava como "não disponível nesta versão", com previsão de liberação em produção.

2. Procedimentos para Retenções na Fonte

O Sistema Nacional atua na identificação e validação da obrigatoriedade, enquanto o recolhimento segue as regras parametrizadas pela prefeitura. A prefeitura deve configurar no Painel Municipal quais serviços ou responsáveis estão sujeitos à retenção. Se a regra estiver ativa, o sistema apresentará alerta ou calculará automaticamente o valor a ser retido. O valor retido pelo tomador também deverá ser processado e recolhido através do sistema, vinculando o fato à nota original por meio de Evento de Tributos Recolhidos.

3. Guia de Pagamento no Painel Municipal

O gestor municipal possui aba de parametrização para "Eventos do MAN" e pode visualizar se uma nota possui tributos recolhidos vinculados. O objetivo do DNA é unificar o ponto de emissão da guia, consolidando os valores (emissão própria e retenções) para os entes interessados através do ADN.

**Resumo:** Para as notas de janeiro/2026, a emissão da guia de pagamento unificada ocorrerá através do MAN, que gerará o DNA. O acesso efetivo depende da conclusão da implantação tecnológica do módulo pelo Comitê Gestor.

---

## Dúvida 018: Procedimento para apuração do ISS enquanto o MAN está em teste

**Pergunta:** Como o MAN ainda se encontra em fase de teste, qual o procedimento para a apuração do ISS? Há manual sobre o assunto? Ou a apuração vai continuar em sistema próprio da prefeitura?

**Resposta:**

O Módulo de Apuração Nacional (MAN), responsável pela totalização de notas e geração da guia única (DNA), ainda é indicado nos manuais mais recentes como "não disponível nesta versão".

1. Onde ocorre a apuração atualmente?

Enquanto o MAN não está em operação plena, a apuração e o recolhimento seguem a logística de integração escolhida pelo município. Municípios com Sistema Próprio: a apuração continua no sistema próprio da prefeitura; o sistema municipal gera a guia de recolhimento local com base nas notas emitidas e integradas. Cálculo por Nota no Sistema Nacional: Mesmo sem o MAN, o Sistema Nacional já realiza o cálculo individualizado do ISSQN por nota. O valor (vISSQN) é calculado automaticamente com base na alíquota e deduções parametrizadas no Painel Municipal.

2. Procedimento para a apuração

O município deve obrigatoriamente inserir alíquotas, regras de retenção e benefícios fiscais no sistema nacional. Sem isso, o sistema não consegue validar as DPS. Para benefícios que incidem sobre a totalização de receitas (e não sobre nota isolada), esses poderão ser utilizados quando o MAN estiver disponível; até lá, os ajustes devem ser feitos via sistema municipal ou processos administrativos locais.

3. Manual sobre o assunto

Não existe manual dedicado exclusivamente à operação do MAN, por ele não estar em produção. As informações sobre apuração estão dispersas no Guia do Painel Administrativo Municipal e no Guia do Emissor Público Nacional Web.

**Resumo:** Até que o MAN seja ativado, o controle da arrecadação e a geração de guias consolidadas permanecem vinculados aos procedimentos e sistemas próprios de cada prefeitura. Os cálculos individuais de cada nota já devem respeitar as regras parametrizadas no Painel Municipal.

---

## Dúvida 023: Cronograma de liberação dos campos IBS e CBS no Emissor

**Pergunta:** Existe previsão oficial de data para liberação do campo IBS/CBS no Emissor Nacional? Enquanto o campo não estiver disponível, haverá penalidade ou irregularidade na emissão das NFS-e sem essa informação?

**Resposta:**

1. Previsão de Liberação

Até dezembro de 2025, as atualizações no Emissor Nacional Web para contemplar os grupos IBS e CBS estavam em desenvolvimento. De acordo com a NT 004/2025, as evoluções de layout serão disponibilizadas ao longo de 2026, com datas a serem divulgadas no Portal da NFS-e. O ambiente com o novo layout da RTC foi programado para operação definitiva a partir de 5 de janeiro de 2026.

2. Penalidades e Irregularidades

Para garantir que a transição não interrompa a atividade econômica, o Comitê Gestor adotou medidas de flexibilização. As regras de negócio que obrigam o preenchimento dos grupos "IBSCBS" foram temporariamente suspensas. O sistema não impedirá a emissão ou recepção de documentos caso esses campos não sejam informados neste momento inicial. Documentos emitidos sem os grupos IBS e CBS serão autorizados e recepcionados pelo ADN, não configurando irregularidade técnica.

3. Obrigatoriedade de Integração

A suspensão não desobriga os municípios de se integrarem à plataforma até 1º de janeiro de 2026. Municípios que não ativarem seus convênios ou não compartilharem documentos no padrão nacional estarão sujeitos à suspensão de transferências voluntárias.

**Resumo:** Enquanto o Emissor Web não for atualizado com a interface para IBS/CBS, os contribuintes podem continuar emitindo normalmente. O sistema aceita documentos sem esses grupos de forma facultativa. Acompanhe as "Últimas Notícias" no Portal Nacional.

---

## Dúvida 034: Tratamento fiscal de NFS-e em padrão municipal antigo

**Pergunta:** Qual o tratamento fiscal aplicável às NFS-e emitidas em padrão municipal antigo, quando o fornecedor alega que o município emissor não aderiu ao Portal Nacional? Essas notas podem ser consideradas válidas para créditos de PIS/COFINS? Para dedutibilidade de despesas no IRPJ e CSLL? A Receita Federal considera válidas NFS-e fora do padrão nacional?

**Resposta:**

1. Validade Formal e Integração Obrigatória

A partir de 1º de janeiro de 2026, a integração à plataforma da NFS-e Nacional torna-se obrigatória para todos os municípios e o DF, conforme Art. 62 da LC 214/2025. O padrão e o leiaute da NFS-e são os definidos pelo Comitê Gestor. O município pode manter sistema próprio, mas é obrigado a transcrever os documentos para o leiaute nacional e compartilhá-los com o ADN. Notas que permanecem apenas no "padrão antigo" sem compartilhamento no padrão nacional (tpEmis = 2) estão em desacordo com a obrigatoriedade legal vigente a partir de 2026.

2. Créditos de PIS e COFINS

Para aproveitamento de créditos no regime não cumulativo, a validade do documento fiscal é essencial. Uma NFS-e que não conste no ADN (por falta de adesão ou de compartilhamento) pode ser questionada pela Receita Federal. O novo leiaute padrão é o único preparado para comportar as informações de IBS e CBS necessárias para a apuração correta conforme a Reforma Tributária.

3. IRPJ e CSLL - Dedutibilidade

Para comprovação de despesas dedutíveis, o documento deve ser hábil e idôneo. A LC 214/2025 prevê sanções como suspensão de transferências voluntárias para municípios que não autorizarem a emissão no padrão nacional ou não compartilharem dados com o ADN. O contribuinte tomador deve exigir que o prestador (e seu município) providencie o compartilhamento da nota com o ADN via transcrição para o padrão nacional.

**Resumo:** A partir de 2026, notas emitidas estritamente no padrão municipal antigo, sem registro no ADN, carecem da garantia de integridade nacional, o que compromete sua validade formal perante a Receita Federal para fins de créditos de PIS/COFINS e dedutibilidade de despesas.

---

## Dúvida 084: Teleconsulta para paciente no exterior e Simples Nacional sem sistema híbrido

**Pergunta:** Com a Reforma Tributária, atendimentos por teleconsulta (médicos, psicólogos) terão IBS recolhido para a cidade do paciente. Quando o paciente mora no exterior, onde será recolhido o IBS? Na cidade do prestador? E empresas do Simples Nacional que não optarem pelo sistema híbrido e continuarem pagando pelo DAS: como será informada a separação da IBS para os municípios?

**Resposta:**

1. Teleconsulta para Paciente no Exterior

No contexto da Reforma Tributária, se o paciente (adquirente/destinatário) reside no exterior e o serviço de teleconsulta é prestado de forma remota, a operação geralmente se configura como Exportação de Serviço. Para efeitos de preenchimento no Sistema Nacional, quando o endereço do destinatário é no exterior, o código da localidade de incidência deve ser preenchido com o valor fixo "999999". O contribuinte deve selecionar o modo de prestação "4 - Consumo no Exterior". Em casos de exportação, não há localidade de incidência para o ISSQN e as regras de neutralidade do IBS/CBS visam a desoneração dessas operações.

2. Empresas do Simples Nacional (Não Híbrido)

Para empresas que optarem por permanecer no regime unificado do Simples Nacional (pagando via DAS sem o sistema híbrido de créditos), o preenchimento dos grupos de informações relativos ao IBS e à CBS na NFS-e só será obrigatório a partir de 2027. A separação do IBS para os municípios será realizada com base no campo "Localidade de Incidência do IBS/CBS" (cLocalidadeIncid), que deve identificar o local do consumo/operação. Mesmo que o imposto seja pago de forma unificada no DAS, a NFS-e servirá como instrumento de coleta de dados para que o ADN identifique o destino da parcela do IBS pertencente a cada ente federativo.

**Resumo:** Para pacientes no exterior, utiliza-se o código de localidade "999999". No Simples Nacional, o detalhamento do IBS/CBS na nota só vira obrigação em 2027, e a divisão entre municípios será feita via código da Localidade de Incidência informado na nota.

---

## Dúvida 085: Onde gerar e pagar os tributos após emissão no Emissor Nacional

**Pergunta:** Após a emissão da nota fiscal no Emissor Nacional, os tributos devidos devem ser pagos como? Onde devem ser gerados os documentos de arrecadação?

**Resposta:**

O procedimento depende da fase atual de implementação do sistema:

1. Fase Atual (Transição)

O MAN (Módulo de Apuração Nacional), responsável pela apuração centralizada, ainda não está disponível em sua versão completa para todos os contribuintes. Os contribuintes devem continuar utilizando os sistemas eletrônicos de gestão fazendária de cada prefeitura (sistemas locais) para a apuração do ISSQN e a emissão das guias de recolhimento municipais (como o DAM). O recolhimento deve seguir os prazos e métodos estabelecidos pela legislação vigente em cada município.

2. Fase de Plena Operação (Reforma Tributária / MAN)

Com a implementação total do sistema e a entrada em vigor das regras da RTC, o fluxo será centralizado. Os documentos de arrecadação serão gerados diretamente no Portal Nacional da NFS-e, através do módulo MAN. O sistema gerará o DNA (Documento Nacional de Arrecadação), que consolidará os tributos devidos (ISSQN, e futuramente IBS e CBS) em um único documento unificado.

3. Casos Específicos (NFS-e Via - Pedágios)

Para as concessionárias que emitem a NFS-e Via, a orientação é idêntica: enquanto o MAN não estiver integrado, a sistemática de apuração e os fluxos de arrecadação municipais devem permanecer inalterados.

**Resumo:** Por enquanto, a emissão da nota no Portal Nacional não gera automaticamente a guia de pagamento. Acesse o site da prefeitura local para escriturar a nota (ou importar os dados) e gerar a guia de imposto conforme as regras do seu município.
