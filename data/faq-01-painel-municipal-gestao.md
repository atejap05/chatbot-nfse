# FAQ - Painel Municipal e Gestão

> Audiência: gestores municipais, administradores tributários
> Temas: Painel Municipal, parametrização, ativação de convênio, adoção faseada, menu Pendências, sincronização ADN, NFS-e Via
> Sistema: NFS-e Nacional - Painel Administrativo Municipal

---

## Dúvida 001: Painel Municipal zerado e notas para cancelamento

**Pergunta:** A página de visão geral do Painel Municipal está zerada. E a página inicial do painel não está mostrando notas para cancelamento. Como resolver?

**Resposta:**

Para que a página de Visão Geral e os gráficos da página inicial do Painel Municipal exibam informações, o município deve estar com a situação "Ativo" no Sistema Nacional. Se essas telas aparecem "zeradas" ou vazias, a causa provável está relacionada à ativação do convênio ou à localização correta das solicitações.

1. Verificação da Ativação do Município

Os "painéis" de acompanhamento gerencial e as estatísticas de emissão só são habilitados para a administração tributária municipal após a conclusão total da parametrização e a efetiva ativação do convênio.

• Assistente de Parametrização: Se, ao entrar no painel, você ainda visualiza o "Assistente de Parametrização", significa que o município ainda está Inativo. É necessário concluir todos os passos obrigatórios (como alíquotas, regras de retenção e cadastro de gestores) e acionar o comando "Concluir Parametrização".

• Data de Expectativa: Mesmo após clicar em concluir, o sistema aguarda a "data de expectativa" informada para a ativação automática. Se essa data for futura, as informações gerenciais permanecerão indisponíveis até que o prazo seja alcançado.

2. Onde Localizar Notas para Cancelamento

Se você busca notas que dependem de autorização da prefeitura para serem canceladas (Solicitações de Análise Fiscal), elas não aparecem diretamente nos gráficos da página inicial, mas sim em um módulo específico:

• Ícone de Pendências: Você deve acessar o ícone identificado por um hexágono com um ponto de exclamação (!) no menu superior.

• Análise de Cancelamentos: Esta funcionalidade exibe a lista de Eventos de Solicitação de Cancelamento por Análise Fiscal emitidos pelos contribuintes. Se a lista estiver vazia, significa que não há pedidos pendentes de deferimento ou indeferimento pelo fisco no momento.

3. Página Inicial "Zerada" (Dashboards)

Se o município já está Ativo, mas os gráficos (NFS-e por dia, por horário, etc.) estão vazios:

• Falta de Dados: Isso ocorre quando ainda não houve emissão de notas fiscais pelos contribuintes locais ou notas com incidência no seu município após a data de ativação.

• Sincronização: O painel reflete as notas emitidas via Emissores Públicos Nacionais ou compartilhadas por Sistemas Próprios via API. Certifique-se de que os documentos foram efetivamente autorizados e integrados ao Ambiente de Dados Nacional (ADN).

**Resumo:** Confirme se o convênio está Ativo e se a data de início de vigência já passou. Para analisar cancelamentos solicitados por contribuintes, clique no ícone "Verificar Pendências" (ícone "!") no menu superior. Se desejar cancelar uma nota de ofício, utilize o menu "Consulta NFS-e" (ícone da lupa).

---

## Dúvida 004: Acesso ao menu Pendências indisponível

**Pergunta:** Estamos sem acesso ao menu "Pendências", funcionalidade indispensável para que os municípios possam analisar e deliberar sobre as solicitações de cancelamento de notas fiscais. Como resolver?

**Resposta:**

Para resolver a indisponibilidade de acesso ao menu "Pendências" no Painel Municipal, especialmente considerando o contexto de transição para o ambiente da Reforma Tributária em janeiro de 2026, seguem as orientações técnicas:

1. Localização do Menu (Ícone Específico)

A funcionalidade "Verificar Pendências" não fica em uma lista de texto lateral, mas é acessada por um ícone específico no menu superior do Painel Administrativo Municipal, representado por um hexágono com um ponto de exclamação (!). Ao clicar nesse ícone, o sistema deve exibir a lista de Eventos de Solicitação de Análise Fiscal para Cancelamento de NFS-e emitidos pelos contribuintes que aguardam deliberação do fisco.

2. Verificação do Perfil de Acesso

Os perfis Gestor Municipal Principal e Gestor Auditor Municipal possuem permissão total para executar todas as funcionalidades, incluindo a análise de cancelamentos. O perfil Atendente tem acesso limitado apenas à administração do Cadastro Nacional de Contribuintes (CNC) e não à parametrização ou análise fiscal.

3. Instabilidades da Transição RTC (Janeiro/2026)

De acordo com a Nota Técnica 004/2025, os módulos do sistema podem passar por instabilidades temporárias durante o período de adaptação aos novos layouts do IBS e da CBS. Para que os painéis de gestão e a fila de análise fiscal funcionem plenamente, o município deve estar com a situação "Ativo" no sistema.

**Resumo:** Acesse o ícone "!" no menu superior. Verifique se o usuário possui perfil de Gestor Principal ou Auditor. Se o ícone não estiver visível, registre uma Solicitação ou Denúncia através dos canais de atendimento do Portal Nacional da NFS-e ou pelo e-mail atendimento.nfs-e@rfb.gov.br.

---

## Dúvida 008: Migração de emissor próprio para emissor nacional

**Pergunta:** O município quer migrar para o emissor nacional após ter aderido à modalidade de emissor próprio, devido a muitos problemas com a empresa na geração de notas. Como fazer essa mudança?

**Resposta:**

Para que o município realize a migração do sistema de emissor próprio para o Emissor Público Nacional, o Gestor Municipal deve realizar ajustes na Configuração do Convênio e no Cadastro Nacional Complementar (CNC) através do Painel Administrativo Municipal.

A funcionalidade de Adoção Faseada permite que o município controle quais contribuintes devem emitir a NFS-e em cada sistema (próprio ou nacional), facilitando uma migração gradual ou total.

1. Habilitação dos Emissores Públicos Nacionais: Acesse o Painel Administrativo Municipal com certificado digital. Navegue até Parametrização > Configuração do Convênio. No grupo "EMISSORES PÚBLICOS NACIONAIS (WEB, MOBILE, API)", altere a opção para "Sim" na pergunta: "O município irá utilizar os Emissores Públicos Nacionais?". Defina qual será a situação padrão para os contribuintes.

2. Gestão dos Contribuintes: No cadastro de cada contribuinte local no CNC, preencha o campo "Autorização de uso dos Emissores Públicos", informando a data inicial em que o prestador passará a usar o sistema nacional. O sistema nacional não permite que um mesmo contribuinte utilize simultaneamente o emissor próprio e o nacional para uma mesma competência.

3. Compartilhamento de Dados Retroativos: O município permanece obrigado a compartilhar/transcrever para o ADN todas as NFS-e que foram emitidas pelo sistema próprio anterior.

**Resumo:** Configure "Sim" para Emissores Públicos Nacionais na Configuração do Convênio. Gerencie as datas de autorização individualmente no CNC. Descontinue o uso da API de integração com o sistema antigo.

---

## Dúvida 021: Integração automática Emissor Nacional com sistema próprio

**Pergunta:** Existe algum processo automático de integração entre o Emissor Nacional e sistema próprio de prefeitura para que esta consiga importar para o seu sistema as notas emitidas pelo Emissor?

**Resposta:**

Sim, existe um processo de integração que permite aos municípios automatizar o fluxo de informações com o Sistema Nacional e importar para seus sistemas próprios os documentos emitidos pelo Emissor Nacional.

Essa integração é realizada por meio do Ambiente de Dados Nacional (ADN), que funciona como um repositório centralizado e disponibiliza uma API de Distribuição de DF-e (Documentos Fiscais eletrônicos).

• API de Distribuição: O município deve desenvolver uma aplicação cliente para se comunicar com a API DF-e disponível no ADN. Essa API permite que a prefeitura busque as notas nas quais ela possui interesse (como município de incidência do imposto, local de prestação ou domicílio do tomador).

• Mecanismo de NSU: O sistema utiliza o NSU (Número Sequencial Único) para garantir o sincronismo. A prefeitura utiliza o NSU de Distribuição (por Código Município) para recuperar documentos que não foram gerados pelo seu sistema local.

• Método de Integração: Através do método GET /DFe/{UltimoNSU}, o sistema próprio da prefeitura informa o último número sequencial que já possui em sua base, e a API do ADN retorna os próximos documentos em lote (até 50 DF-e por vez).

• Documentação Técnica: As especificações estão disponíveis no Manual dos Municípios - Guia para utilização das APIs do ADN e no seu respectivo Anexo de Leiautes.

**Resumo:** O município deve consumir a API de Distribuição do ADN via método GET /DFe/{UltimoNSU} para importar automaticamente as notas emitidas no padrão nacional.

---

## Dúvida 022: Escrituração manual no módulo Automotivo (NFS-e Via)

**Pergunta:** Alguns prestadores de serviço não realizaram a escrituração das Notas Fiscais de Serviços Tomados no módulo Automotivo. O sistema não permite a realização dessa escrituração de forma manual. Como resolver?

**Resposta:**

O "módulo Automotivo" refere-se à NFS-e Via, um modelo de documento fiscal eletrônico de uso exclusivo para concessionárias de rodovias (serviço código 22.01.01).

Diferente da NFS-e comum, a NFS-e Via possui uma estrutura complexa que exige informações geográficas específicas, como trecho de concessão, praça de pedágio, quilômetro (km) e sentido da via. O sistema foi desenhado para ser altamente transacional e automatizado. Por isso, a geração das notas ocorre obrigatoriamente através da transmissão de arquivos XML via API REST. O portal web não disponibiliza formulários para preenchimento campo a campo.

Os prestadores (concessionárias) devem regularizar a situação através do processo de transmissão em lote: configurar o sistema interno para gerar o arquivo XML no layout específico da NFS-e Via e transmiti-lo ao Ambiente Nacional utilizando o método POST /DFe/. Antes de transmitir, a concessionária deve garantir que o Contrato, Trecho e Praça estão devidamente parametrizados no Portal de Gestão das Concessionárias.

**Resumo:** O sistema não permite a inclusão manual por design. Os prestadores devem realizar a transmissão dos lotes XML via API seguindo o layout da NFS-e Via.

---

## Dúvida 029: Envio da DMS a partir da emissão no Portal Nacional

**Pergunta:** Com os contribuintes emitindo as notas pelo Portal Nacional, há forma deles enviarem a DMS diretamente pelo Portal Nacional? Ou para enviarem a DMS deverão utilizar o sistema próprio do Município?

**Resposta:**

No momento, o Sistema Nacional da NFS-e não possui uma funcionalidade específica no Portal Nacional para a "entrega de DMS" (Declaração Mensal de Serviços) nos moldes tradicionais dos sistemas municipais.

• Sincronização Automática: Todas as notas emitidas pelo Portal Nacional são automaticamente compartilhadas e distribuídas para o município de origem e de incidência por meio da API de Distribuição do ADN.

• Uso do Sistema Municipal: O encerramento de competências e o cumprimento de outras obrigações acessórias locais (como a DMS) continuam sendo realizados pelo portal próprio do município. O sistema municipal deve ser configurado para importar ou reconhecer os dados vindos do ADN para que o contribuinte não precise redigitar as notas na declaração municipal.

• Módulo de Apuração Nacional (MAN): O objetivo futuro do sistema é centralizar a apuração e a geração da guia única (DNA) através do MAN, o que poderá substituir a necessidade de declarações paralelas de apuração (DMS) em sistemas locais. Contudo, esse módulo ainda está em fase de disponibilização total.

**Resumo:** Os contribuintes devem continuar utilizando o sistema próprio do município para o envio da DMS. A prefeitura deve utilizar a integração via API do ADN para capturar as notas emitidas no Portal Nacional e integrá-las automaticamente à escrituração do contribuinte no sistema local.

---

## Dúvida 033: Liberação automática e adoção faseada CNPJ/CPF

**Pergunta:** Assim que for habilitado no portal, automaticamente já fica liberado para os contribuintes se cadastrarem e começar a geração de NFS-e no emissor nacional ou elencamos uma data? Como seria o processo de habilitar apenas CNPJ no emissor nacional e CPF no emissor próprio? No caso se enquadraria na ADOÇÃO FASEADA?

**Resposta:**

A liberação para a geração de notas não ocorre de forma puramente "automática". Ela segue um cronograma de ativação:

• Ativação do Município: Ao concluir a parametrização, o Gestor Municipal Principal define uma "data de expectativa para início de vigência" do convênio. O município só se torna efetivamente "Ativo" ao atingir essa data.

• Autorização do Contribuinte: Mesmo com o município ativo, o contribuinte poderá emitir notas apenas a partir da Data de Autorização de Uso dos Emissores Públicos (dAutEmiss) registrada para ele no módulo CNC.

• Regra da Maior Data: A emissão só é permitida a partir da data de autorização individual OU da data de início de vigência do convênio municipal, prevalecendo a que for maior.

Para habilitar CNPJ no nacional e CPF no próprio (Adoção Faseada): No menu Parametrização > Configuração do Convênio, marque "É permitida a emissão de NFS-e por pessoas físicas (CPF)?" como "Não". Isso impedirá que contribuintes CPF utilizem o emissor nacional, mantendo-os em seu sistema próprio. Gerencie as datas de autorização dos CNPJs individualmente ou por lotes através do CNC.

**Resumo:** A prefeitura deve utilizar a Adoção Faseada, desabilitando a emissão para CPFs na Configuração do Convênio e gerenciando as datas de autorização dos CNPJs individualmente através do CNC.

---

## Dúvida 040: Conflito de cadastro em múltiplos municípios

**Pergunta:** O contribuinte está cadastrado em Vitória/ES além de Niterói/RJ. Vitória incluiu o mesmo CNPJ no CNC. Ele deveria estar cadastrado somente em Niterói conforme comprovante do CNPJ da Receita Federal. Como resolver a dificuldade de emissão?

**Resposta:**

O sistema nacional identifica o contribuinte através de uma tríade única: Código do Município + Inscrição Federal (CNPJ/CPF) + Inscrição Municipal (IM). A inclusão indevida no CNC de Vitória criou um vínculo de "contribuinte local" naquela jurisdição, gerando conflitos de validação no momento da emissão.

Ação Obrigatória de Vitória/ES: O gestor municipal de Vitória deve acessar o Painel Administrativo Municipal, entrar no menu "Contribuintes Locais", localizar o CNPJ e realizar a Exclusão Lógica (inativação) do registro. Ao marcar a situação cadastral no CNC como "0 - Inativo", o registro complementar de Vitória deixa de existir para fins de validação de emissão.

Uma vez que o registro indevido no CNC de Vitória seja inativado, o sistema passará a considerar automaticamente as informações provenientes dos cadastros da Receita Federal (RFB) para este CNPJ. Como o cadastro da RFB indica que a empresa está localizada em Niterói/RJ, o sistema nacional reconhecerá Niterói como o município emissor correto.

**Resumo:** O município que incluiu indevidamente o CNPJ deve inativar o registro em seu Painel Administrativo (menu Contribuintes Locais > Inativar). Isso forçará o sistema a ler o domicílio fiscal correto da Receita Federal.

---

## Dúvida 065: Impossibilidade de editar alíquota e município de incidência do ISSQN

**Pergunta:** Estamos enfrentando a impossibilidade de editar os campos "alíquota do ISSQN" e "município de Incidência do ISSQN". O sistema apresenta mensagens como "Não é permitido informar alíquota do ISSQN quando o município de incidência estiver conveniado ao Sistema Nacional NFS-e". Como proceder?

**Resposta:**

A impossibilidade de editar não é um erro técnico, mas uma regra de negócio fundamental. O Sistema Nacional funciona sob a premissa de que o fisco não deve solicitar informações que já possui.

• Alíquota Automática: Se o município de incidência do serviço é conveniado e está "Ativo", a alíquota é recuperada automaticamente da parametrização realizada pela prefeitura no Painel Administrativo Municipal. O sistema bloqueia a edição manual (Regras E0617 e E1300).

• Incidência Automática: O município de incidência é determinado logicamente pelo sistema com base no Código de Tributação Nacional (cTribNac) informado, seguindo as regras da LC 116/03.

Para prestação em município diferente do prestador: O contribuinte deve selecionar "Emissão Completa" e, no Passo 2 (Serviço), informar corretamente o país e o município onde o serviço foi prestado.

Para ajuste de alíquotas: A prefeitura do município de incidência deve acessar o Painel Administrativo Municipal > Parametrização > Lista de Serviços e corrigir o valor da alíquota.

Procedimento de Contingência: Casos excepcionais devem ser tratados via fluxo de Decisão Administrativa/Judicial habilitado pelo município no Painel Municipal.

**Resumo:** Erros de alíquota devem ser corrigidos pela prefeitura no Painel Municipal. Casos excepcionais devem ser tratados via Decisão Administrativa/Judicial.

---

## Dúvida 083: Nota emitida no site nacional não consta no site da prefeitura

**Pergunta:** Contribuinte emitiu uma nota fiscal pelo site nacional e alega que até o momento essa nota não consta no site da prefeitura de Manaus.

**Resposta:**

O problema deve-se à dinâmica de sincronização entre o Ambiente de Dados Nacional (ADN) e os sistemas próprios municipais.

Quando uma nota é emitida com sucesso no Portal Nacional, ela é imediatamente internalizada no ADN, que é o repositório oficial. Se o sistema nacional confirmou a emissão, o documento já possui validade jurídica plena.

Municípios que mantêm sistemas próprios, como Manaus, devem "buscar" as notas emitidas no ambiente nacional para atualizar suas bases locais. O sistema da prefeitura precisa consumir regularmente a API de Distribuição do sistema nacional para recuperar os documentos vinculados ao seu código de município. Se a nota não aparece no site local, é provável que o sistema da prefeitura ainda não tenha processado o lote de distribuição correspondente.

O contribuinte deve acessar a Consulta Pública no Portal Nacional da NFS-e e pesquisar pela chave de acesso da nota. Se a nota for localizada e estiver com o status "Gerada" (Código 100), ela é válida e está devidamente registrada no sistema nacional. Se o prazo para pagamento está próximo e a nota continua ausente no site de Manaus, o contribuinte deve entrar em contato com a Secretaria de Finanças do Município.

**Resumo:** A nota emitida no site nacional já é oficial. O fato de não constar no site da prefeitura indica apenas um atraso na integração técnica (sincronização via API) por parte do município. Se a nota estiver na Consulta Pública Nacional, ela é legítima.

---

## Dúvida 087: Notas não aparecem no emissor nacional (Ginfes/São Bernardo)

**Pergunta:** Contribuinte de São Bernardo do Campo emite notas pelo sistema municipal (Ginfes). Alguns clientes alegam que as notas não estão sendo registradas no emissor nacional e solicitam cancelamento. A Ginfes informou que a disponibilização das notas no ambiente nacional é de responsabilidade da Receita Federal.

**Resposta:**

É necessário distinguir o Emissor Nacional do Ambiente de Dados Nacional (ADN).

Existem duas formas de um município aderir ao sistema: (1) Emissor Nacional - o contribuinte emite diretamente no portal nacional; (2) Sistema Próprio (caso de SBC/Ginfes) - o município mantém seu sistema local, mas fica obrigado a compartilhar os documentos fiscais emitidos com o ADN.

Se o município utiliza o Ginfes (sistema próprio), as notas emitidas por lá só aparecerão no Portal Nacional se o sistema municipal realizar o compartilhamento (transmissão) desses arquivos XML para o ADN. O fato de a nota não constar pode ocorrer por atraso no sincronismo ou erro na transcrição do layout local para o nacional.

Responsabilidade do Município/Ginfes: Transmitir e garantir que as notas emitidas localmente sejam enviadas ao ADN no padrão nacional. Responsabilidade da RFB/ADN: Recepcionar, armazenar e disponibilizar essas informações após o envio bem-sucedido pelo município.

Parecer para os Clientes: A NFS-e emitida pelo sistema autorizado da Prefeitura possui validade jurídica total, independentemente de sua visualização imediata no Portal Nacional. Os clientes podem verificar a veracidade da nota através da Consulta Pública no Portal Nacional (usando a Chave de Acesso). O documento gerado pelo sistema Ginfes é o comprovante oficial da prestação do serviço.

**Resumo:** O problema é de integração técnica (compartilhamento de dados) entre o sistema da prefeitura (Ginfes) e o ADN, e não um erro do emitente. A nota é válida desde sua autorização no município de origem.

---

## Dúvida 095: Parametrização "desfeita" pelo sistema

**Pergunta:** Prefeitura alega que a parametrização foi "desfeita" pelo sistema e solicita que ela seja refeita. Alega inclusive que não é a primeira vez que isso acontece. O que responder?

**Resposta:**

O Sistema Nacional da NFS-e possui regras rígidas de integridade e auditabilidade, o que torna improvável que parametrizações sejam "desfeitas" sem uma ação humana ou motivo técnico específico.

1. Histórico de Alterações: O sistema não permite a exclusão física de parâmetros após a ativação do convênio. Qualquer alteração gera um histórico que registra a data da mudança, o motivo, a legislação e o CPF do gestor responsável. O gestor municipal deve acessar o menu de parametrização e verificar o histórico de cada item para identificar se outro gestor realizou alterações.

2. Retorno ao "Assistente de Parametrização": Se o município já concluiu a parametrização, mas a "Data de Expectativa para Início de Vigência" ainda não chegou, qualquer tentativa de edição faz com que o sistema retome automaticamente o status de "pré-ativação". Nesse estado, o sistema abre novamente o assistente passo a passo. Se o gestor não realizar o comando "Concluir Parametrização" ao final das novas edições, as regras podem não ser consolidadas no ADN.

3. Diferença entre "Ativo" e "Ativo Operacional": Se a data de início da vigência for futura, o município é considerado "Ativo na plataforma" mas não está operacional.

4. Perfis de Gestão e Concorrência: Se múltiplos gestores estiverem operando simultaneamente, um pode estar encerrando vigências que o outro acabou de criar.

Procedimento Recomendado: Confirmar se o município aparece como "Ativo". Clicar no ícone de pendências ("!") para verificar se o sistema indica campos obrigatórios. Acessar cada item parametrizado e verificar o histórico de vigências. Caso precisem refazer algo, seguir todos os passos do assistente e clicar obrigatoriamente em "Concluir Parametrização".

**Resumo:** O sistema mantém o histórico de tudo o que é feito. A prefeitura deve verificar se a parametrização foi efetivamente concluída no assistente ou se as alterações foram sobrepostas por novos registros de vigência feitos pelos próprios gestores locais.

---

## Dúvida 100: Trava de retenção municipal não está funcionando

**Pergunta:** Prefeitura parametrizou quais serviços devem ser retidos pelos tomadores quando da incidência em seu território. Porém a trava não está funcionando - estão emitindo notas em desacordo com a legislação local.

**Resposta:**

O comportamento relatado não é necessariamente um erro de processamento, mas uma característica da fase atual de implementação das regras de retenção.

1. Natureza Informativa da Regra (Alerta vs. Bloqueio): As regras de retenção parametrizadas pelo município possuem, neste momento inicial, um caráter predominantemente informativo. Quando o contribuinte preenche uma nota cuja regra municipal prevê retenção, o emissor público apresenta um ALERTA informando que o Município de incidência indicou que a operação deve ser objeto de retenção. A regra não é aplicada de modo a rejeitar a emissão da nota caso o contribuinte ignore o alerta e prossiga sem marcar a retenção.

2. Regra de Negócio E0031: O sistema aplica uma trava rígida: não pode haver retenção do ISSQN pelo tomador quando o município de incidência do imposto não for o mesmo município de domicílio do tomador. Se o serviço for prestado no município, mas o tomador estiver localizado em outra cidade, o sistema rejeitará ou ignorará a indicação de retenção.

3. Verificação da Parametrização: A prefeitura deve revisar no módulo Retenções do ISSQN: vinculação de serviços, responsáveis tributários e vigência da regra.

4. Como a Prefeitura deve proceder: Utilizar o ícone de Consulta NFS-e (lupa) no Painel Municipal para filtrar as notas emitidas e identificar aquelas onde o campo tpRetISSQN foi preenchido como "1 - Não Retido" em serviços que deveriam ser retidos. Com base nesses dados, o município pode realizar a cobrança ou ação fiscal.

**Resumo:** O sistema nacional prioriza a emissão, exibindo apenas um alerta informativo sobre a retenção municipal. O bloqueio automático (rejeição da nota) não ocorre para evitar conflitos com a LC 116/03. O município deve monitorar via Consulta NFS-e e realizar ação fiscal quando necessário.

---

## Dúvida 102: Habilitar apenas CNPJ no emissor nacional e CPF no emissor próprio

**Pergunta:** A prefeitura está migrando do emissor próprio para o nacional e gostaria de manter as notas fiscais de CPF ainda sendo geradas por emissor próprio. Deve marcar o campo "É permitida a emissão de NFS-e por pessoas físicas (CPF)?" como "Não"? O gestor não está encontrando esse campo.

**Resposta:**

Sim, a prefeitura deve marcar o campo "É permitida a emissão de NFS-e por pessoas físicas (CPF)?" como "Não". Ao selecionar "Não", o sistema bloqueia o acesso de qualquer contribuinte identificado por CPF aos Emissores Públicos Nacionais (Portal Web, App e API Nacional). Essa configuração permite que o município realize uma migração gradual, autorizando o uso do emissor nacional apenas para CNPJ, enquanto mantém CPF no sistema local.

Localização do campo: O campo relativo à emissão por CPF está inserido no grupo "EMISSORES PÚBLICOS NACIONAIS (WEB, MOBILE, API)". Este campo só ficará disponível para configuração se a pergunta anterior, "O município irá utilizar os Emissores Públicos Nacionais (API, Móvel e Web)?", estiver marcada como "Sim". O campo para CPF deve aparecer logo abaixo da pergunta sobre a situação padrão para contribuintes CNPJ. Se o município marcou que não utilizará os emissores nacionais, o sistema oculta os parâmetros de restrição individual.

Observações: (1) O MEI está obrigado por resolução federal a utilizar o emissor nacional desde janeiro de 2023, independentemente desta configuração municipal. (2) Mesmo que os contribuintes CPF continuem emitindo no sistema próprio, a prefeitura permanece obrigada a compartilhar esses documentos com o ADN, transcrevendo-os para o layout padrão nacional. (3) Para migração mais refinada, a prefeitura pode deixar o parâmetro geral como "Sim" e realizar o bloqueio ou liberação individual de cada contribuinte através do módulo CNC > Contribuintes Locais.

**Resumo:** Marque "Não" no campo de emissão por CPF na Configuração do Convênio. O campo só aparece se "O município irá utilizar os Emissores Públicos Nacionais?" estiver como "Sim". MEI continua obrigado ao emissor nacional.
