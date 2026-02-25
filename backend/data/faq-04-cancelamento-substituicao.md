# FAQ - Cancelamento e Substituição de NFS-e

> Audiência: contribuintes, gestores municipais, contadores
> Temas: cancelamento, substituição, análise fiscal, cancelamento por ofício, manifestação, evento E0831, evento E0840
> Sistema: NFS-e Nacional - Portal do Contribuinte, Painel Administrativo Municipal, API de Eventos

---

## Dúvida 011: Substituição de nota sem dados do tomador bloqueada

**Pergunta:** Contribuintes estão enfrentando erros ao tentar substituir NFS-e para corrigir a ausência dos dados do tomador. A mensagem é "Não foi possível avançar. Tente em alguns minutos". Como resolver?

**Resposta:**

O problema está geralmente atrelado a travas de Regras de Negócio e à parametrização do município no Painel Administrativo.

1. Impedimento por Ausência de Tomador (Regra E0056)

A Regra E0056 estabelece que uma NFS-e não pode ser substituída se não possuir identificação do tomador. O sistema valida a nota original; se ela foi emitida como "Tomador não informado", o processo de substituição pode ser bloqueado automaticamente pelo ADN.

2. Parametrização Municipal (Configuração de Eventos)

A possibilidade de realizar essa substituição depende de como o município configurou as regras de evento. O gestor municipal deve acessar Parametrização > Eventos > Substituição de NFS-e e verificar o campo: "É permitido substituir uma NFS-e onde os não-emitentes não foram identificados?". Se estiver marcado como "Não", o sistema impedirá qualquer tentativa de substituição de notas geradas originalmente sem os dados do tomador.

3. Alteração de Identificação (Regra E0058)

Alterações de identificação do tomador em substituições podem ser restritas por regras adicionais. Verifique a parametrização municipal.

**Resumo:** O gestor municipal deve acessar Parametrização > Eventos > Substituição de NFS-e e habilitar a opção "É permitido substituir uma NFS-e onde os não-emitentes não foram identificados?". Caso contrário, a alternativa é cancelamento via análise fiscal e emissão de nova nota.

---

## Dúvida 024: Tomador rejeitou a nota mas ela ainda consta como emitida

**Pergunta:** O tomador recebeu uma nota que não reconhece, fez a recusa, mas a nota ainda encontra-se como emitida. Qual procedimento?

**Resposta:**

O Evento de Manifestação de Rejeição realizado pelo tomador é um registro de fato que não altera automaticamente o status da nota de "Emitida" para "Cancelada". A manifestação serve para declarar que o tomador não aceita as informações, servindo como prova da discordância.

1. Responsabilidade pelo Cancelamento

O evento de rejeição dá ciência ao prestador e ao fisco sobre a irregularidade, mas o cancelamento efetivo depende de ação posterior. O prestador deve realizar o cancelamento (ou substituição) através do seu painel, desde que dentro do prazo parametrizado. Se o prestador não cancelar, a ATM pode realizar o Cancelamento por Ofício.

2. Procedimento para a Prefeitura

Acesse o Painel Administrativo Municipal e o menu Consulta NFS-e (ícone da lupa). Pesquise a nota pela chave de acesso ou dados do tomador/prestador. Ao localizar, clique em Visualizar NFS-e para verificar os Eventos Vinculados (constará a Rejeição do Tomador). Se o fisco se convencer de que o serviço não foi prestado, selecione "Cancelar por Ofício" na linha da nota, informando Número do Processo Administrativo e Justificativa.

3. Solicitação de Análise Fiscal

Se o prestador tentar cancelar mas o prazo já expirou, deve gerar evento de Solicitação de Análise Fiscal para Cancelamento. Essa solicitação aparecerá no menu "Pendências" (ícone do hexágono com exclamação). O gestor municipal pode Deferir o pedido, resultando no cancelamento efetivo no ADN.

**Resumo:** A recusa pelo tomador é apenas declaração de discordância. Para a nota deixar de constar como emitida, o prestador deve cancelá-la ou a prefeitura deve realizar o cancelamento por ofício após analisar a manifestação.

---

## Dúvida 035: Nota não integrou o ISS com a prefeitura e não gera guia

**Pergunta:** A nota emitida está correta, porém a nota baixada do ambiente nacional não integrou o ISS com a prefeitura de Pindamonhangaba e não está gerando a guia para pagamento.

**Resposta:**

O motivo é erro no preenchimento dos campos estruturados de tributação por parte do emitente.

1. Seleção de "Não Incidência"

Embora o contribuinte tenha escrito na descrição que o serviço está "Sujeito a retenção na fonte", os campos técnicos foram preenchidos de forma contrária: Tributação do ISSQN como "Não incidência"; Município de Incidência como "Nenhum"; ISSQN Apurado zerado.

2. Regras de Integração e Arrecadação

O sistema só identifica a localidade de incidência e destaca o imposto quando a operação é marcada como "1 - Operação Tributável". Quando indica "Não Incidência", o sistema é impedido de informar local de incidência ou calcular o imposto. Não há valor a integrar nem guia a gerar.

3. Inconsistência no Local da Prestação

O serviço 07.09.01 (Varrição, coleta e remoção de lixo) exige que o local de incidência seja o local da prestação. Ao selecionar "Não Incidência" para serviço tributável no local da prestação (Pindamonhangaba), o emitente desabilitou o cálculo automático do imposto.

Como Resolver: O contribuinte deve realizar a Substituição da NFS-e. No Passo 3 (Valores), alterar "Tributação do ISSQN" para "1 - Operação Tributável" e "Retenção do ISSQN" para "2 - Retido pelo Tomador". Ao finalizar a substituição, o sistema reconhecerá o ISSQN para Pindamonhangaba e permitirá a geração da guia.

**Resumo:** A nota está com preenchimento técnico incorreto (marcada como não tributável). O prestador deve substituir a nota corrigindo a tributação para "Operação Tributável" com "Retenção pelo Tomador".

---

## Dúvida 063: Endpoint e permissões para Cancelamento por Ofício via API

**Pergunta:** Qual o endpoint e as permissões para envio de Pedidos de Registro de Eventos (Cancelamento por Ofício - código 305101) via API? Estamos recebendo erros E999, 405 e 404.

**Resposta:**

A) Endpoint Oficial de Produção

Para o registro de eventos realizados pelo Município Emissor (MEmis): Método POST; URL de Produção: https://adn.nfse.gov.br/municipios/nfse/{chaveAcesso}/eventos. O erro 404 ocorre quando o recurso ou a chave de acesso não são informados corretamente. O erro 405 indica que o POST está sendo enviado para a raiz /municipios/ ou /NFSe/ sem o complemento /eventos.

B) Perfil do Agente e Restrições de Segurança

O CPF do Agente Tributário (CPFAgTrib) informado no XML deve corresponder a um Gestor Municipal ATIVO. Para eventos de competência do município, a assinatura deve ser feita com o certificado digital do município (e-CNPJ da prefeitura). O campo autor deve refletir o CNPJ do município se estiver usando certificado da prefeitura.

C) Parametrização no Painel Administrativo

O evento 305101 (Cancelamento por Ofício) independe dos prazos e limites de valor do cancelamento automático. O erro E999 pode ocorrer se o município não estiver com status "ATIVO" no Cadastro de Convênio. Verifique se a nota possui "Evento de Bloqueio de NFS-e por Ofício" vigente; se houver bloqueio ativo, o sistema rejeitará o pedido.

**Resumo:** Use POST em https://adn.nfse.gov.br/municipios/nfse/{chaveAcesso}/eventos. Certifique-se de que o município está Ativo e que não há bloqueio vigente na nota. Assine com certificado da prefeitura.

---

## Dúvida 093: Erro E0831 ao cancelar no Portal Nacional nota emitida no portal municipal

**Pergunta:** A NFS-e foi emitida pelo portal municipal. Após identificar valor incorreto, o cancelamento foi realizado no portal municipal. Porém, no Portal Nacional a nota permanece como válida. Ao tentar cancelar pelo ambiente nacional, retorna: "E0831 – O pedido de registro de evento deve ser enviado para o ambiente gerador de NFS-e de acordo com o ambGer indicado na NFS-e referenciada." Como proceder?

**Resposta:**

O erro E0831 e a divergência de status ocorrem devido às regras de governança de dados entre os ambientes geradores.

1. Entendimento do Erro E0831

A regra E0831 estabelece que o pedido de registro de um evento (como cancelamento) deve ser enviado obrigatoriamente para o ambiente que gerou a NFS-e. ambGer = 1: nota gerada por Sistema Próprio do Município. ambGer = 2: nota gerada pela Sefin Nacional. Como a NFS-e foi emitida pelo portal da prefeitura, possui ambGer = 1. O sistema nacional bloqueia qualquer tentativa de cancelamento direto pelo Portal do Contribuinte Nacional.

2. Por que a nota continua "Válida" no Portal Nacional?

A nota permanece como válida no ADN porque, embora o cancelamento tenha sido realizado no sistema municipal, esse evento ainda não foi compartilhado/sincronizado com o ambiente nacional. O município deve realizar a transcrição do evento para o layout padrão nacional e transmiti-lo ao ADN via API.

3. Procedimentos Recomendados

Para o Contribuinte: Não tente cancelar pelo Portal Nacional; o sistema continuará retornando E0831. Acione a Prefeitura informando que o cancelamento local não foi sincronizado com o ADN.

Para a Prefeitura: Verificar se o evento de cancelamento foi enviado ao endpoint de recepção de eventos do sistema nacional. Checar se houve rejeição pelo ADN (erro de assinatura ou layout). Se o sistema municipal permitir, retransmitir o evento de cancelamento específico.

**Resumo:** O problema é de integração técnica entre o sistema da prefeitura e o ADN. O cancelamento municipal só aparece no nacional se a prefeitura transmitir o XML do evento de cancelamento ao sistema nacional.

---

## Dúvida 103: Lançamento como tomador, substituição e aceite de notas

**Pergunta:** (1) Lançamento manual não permite lançamento como TOMADOR. (2) Onde fica a opção de substituição de NFS-e para ajuste de alíquota incorreta? (3) Mesmo dando aceite, a nota não é direcionada para a prefeitura de Pindamonhangaba para emissão da guia. Como orientar?

**Resposta:**

1. Lançamento como Tomador (Exportação/Importação)

A emissão de NFS-e pelo tomador está bloqueada na versão atual. A Regra E9996 estabelece que "nesta versão da aplicação, não é permitida a emissão de NFS-e pelo tomador ou intermediário". A funcionalidade está prevista para versão futura do sistema.

2. Opção de Substituição de NFS-e

Para corrigir nota com alíquota incorreta via substituição: Acesse o menu "NFS-e Emitidas" e localize a nota. Clique no ícone de opções (três pontos) na linha da nota e selecione "Substituir". O sistema carregará os dados da nota original para edição. Ao finalizar, será gerada a NFS-e substituta e um Evento de Cancelamento por Substituição será vinculado à nota antiga. A substituição só pode ser realizada pelo emissor do documento.

3. Procedimento de "Aceite" e Integração com Pindamonhangaba

O "Aceite" no Portal Nacional gera um evento de Manifestação de Confirmação do Tomador, vinculado à nota no ADN. O Módulo de Apuração Nacional (MAN) que automatizará a geração de guias ainda não está disponível. Enquanto isso, o recolhimento segue os procedimentos dos sistemas locais. A prefeitura de Pindamonhangaba deve recuperar os documentos via API de distribuição do ADN. Se a nota confirmada não aparece no sistema municipal, a prefeitura deve ser acionada para realizar a importação ou sincronização via Webservice.

**Resumo:** A emissão como tomador está temporariamente desabilitada (Regra E9996). A substituição é feita pelo emissor no menu "NFS-e Emitidas". O "Aceite" é registro nacional, mas a geração da guia depende da sincronização do sistema de Pindamonhangaba com o ADN.

---

## Dúvida 105: Erro E0840 e opções de cancelamento indisponíveis

**Pergunta:** Erro 0840: "O Sistema Nacional NFS-e não pode recepcionar o EVENTO DE CANCELAMENTO DE NFS-e, pois o evento já está vinculado à NFS-e indicada no evento enviado, impedindo sua recepção." O contribuinte precisa cancelar uma nota (serviço não prestado) e não encontra a opção de cancelamento automático nem cancelamento por análise. Como proceder?

**Resposta:**

O erro E0840 ocorre porque o Sistema Nacional identificou que a NFS-e já possui um evento vinculado (solicitação de cancelamento anterior, substituição ou bloqueio) que impede a recepção de um novo pedido de cancelamento.

1. Verifique o Histórico da Nota

Acesse "Consultas > Histórico Nota Fiscal" ou visualize os detalhes da nota em "NFS-e Emitidas". Verifique se já existe um evento como "Solicitação de Análise Fiscal para Cancelamento" com status "aguardando resposta". Se existir, o sistema não exibirá novos botões de cancelamento e retornará E0840 ao tentar enviar novo pedido.

2. Por que as opções de cancelamento sumiram?

Cancelamento Automático: O botão desaparece se a nota ultrapassou o prazo máximo (geralmente 30 a 60 dias) ou o valor limite parametrizado pela prefeitura. Análise Fiscal: Se não visualiza esta opção, a nota pode já estar em processo de análise por solicitação anterior ou a prefeitura configurou "Bloqueio de Ofício" para eventos de cancelamento.

3. Como proceder (Serviço não Prestado)

Se houver solicitação pendente no histórico, aguarde que a ATM municipal defira ou indefira o pedido. Se não houver eventos pendentes e as opções ainda estiverem ocultas, o contribuinte deve procurar a Secretaria de Finanças do município emissor. A prefeitura tem autonomia para realizar o Cancelamento por Ofício pelo Painel Administrativo Municipal, independentemente dos prazos e travas do emissor web, desde que comprovada a não prestação do serviço.

**Resumo:** O erro E0840 indica que o processo de cancelamento já foi iniciado ou bloqueado por outro evento. Consulte o histórico da nota para confirmar se há análise pendente e, se necessário, acione o fisco municipal para cancelamento administrativo.
