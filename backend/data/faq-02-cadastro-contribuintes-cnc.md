# FAQ - Cadastro Nacional de Contribuintes (CNC)

> Audiência: gestores municipais, fiscais, contribuintes
> Temas: CNC, primeiro acesso, tríade (Município+CNPJ/CPF+IM), inativação, reativação, e-mail, status de emissão
> Sistema: NFS-e Nacional - Painel Administrativo Municipal, Portal do Contribuinte

---

## Dúvida 002: Cadastro duplicado e erro "Indicador Municipal em uso"

**Pergunta:** O contribuinte está tentando fazer o cadastro no site como primeiro acesso. Foi realizado o cadastro no Portal Nacional, porém a fiscal errou e cadastrou duas vezes com indicador municipal diferente, e desabilitou de forma equivocada o cadastro correto. Não tem opção para reativar e, ao tentar novo cadastro, dá mensagem de que o indicador municipal está sendo usado. Como resolver?

**Resposta:**

A mensagem "Não foi possível criar seu usuário" ocorre quando os dados digitados pelo contribuinte não puderam ser validados nas bases federais ou quando não há autorização municipal. O fiscal deve verificar no Painel Municipal se o contribuinte está com o "Status para emissão de NFS-e" definido como "Autorizado" e se a "Data de Autorização de Uso dos Emissores" já é vigente.

No Sistema Nacional, a identificação do contribuinte é baseada em uma tríade única: Código do Município + CNPJ/CPF + Inscrição Municipal (IM). Quando um registro no CNC é alterado para "Inativo", ocorre uma "Exclusão Lógica". O sistema não permite reativar esse registro específico. Se o sistema diz que o IM está em uso, é porque existe outro registro (o "duplicado" com IM diferente) que ainda está com o status "Ativo" vinculado àquele CNPJ.

Passo a passo para a Fiscal: (1) Inativar o registro duplicado/errado no menu "Cadastrar contribuinte local"; (2) Realizar um NOVO cadastro para o registro correto inserindo o CNPJ e o IM correto; (3) Marcar a situação como "Ativo", o status de emissão como "Autorizado" e informar a "Data de Autorização de Uso dos Emissores".

**Resumo:** O sistema não possui botão "reativar" para exclusões lógicas. A fiscal deve inativar todos os registros incorretos e fazer um novo cadastramento individual (ou via upload de .CSV) inserindo novamente o CNPJ com o IM correto e garantindo que o status de emissão seja "Autorizado".

---

## Dúvida 006: E-mail desconhecido no primeiro acesso

**Pergunta:** O contribuinte não está conseguindo gerar o primeiro acesso pois tem um e-mail cadastrado que desconhece. Onde faz essa atualização de e-mail?

**Resposta:**

Os dados de contato no sistema nacional são recuperados de bases oficiais (Receita Federal e CNC).

• Atualização via Município (Recomendado): Como o contribuinte não consegue completar o primeiro acesso, ele deve comparecer presencialmente ao serviço de atendimento da prefeitura. O Gestor Atendente Municipal deve acessar o Painel Administrativo Municipal e realizar a regularização do emitente diretamente no módulo CNC (Cadastro Nacional Complementar), atualizando o e-mail e outras informações complementares.

• Acesso Alternativo via GOV.BR: Caso o representante legal possua uma conta GOV.BR de nível Prata ou Ouro, ele pode tentar o login através do botão "Entrar com gov.br". Para MEI, essa forma de acesso dispensa a necessidade de senha vinculada ao e-mail cadastrado.

• Alteração após o Login: Uma vez que o contribuinte consiga acessar o sistema, ele deve acessar o menu "Configurações" (ícone da engrenagem) e atualizar o campo E-mail nas "Informações Pessoais".

**Resumo:** O contribuinte deve solicitar que a Prefeitura local atualize seu e-mail no módulo CNC do Sistema Nacional. Após essa atualização feita pelo fisco municipal, o novo e-mail será reconhecido para a conclusão do primeiro acesso e criação da senha.

---

## Dúvida 015: Como habilitar contribuinte cadastrado no CNC a emitir notas

**Pergunta:** Prefeitura fez o cadastro de um contribuinte no CNC. Agora quer saber como habilitá-lo a emitir notas.

**Resposta:**

Para que um contribuinte cadastrado no CNC esteja efetivamente habilitado a emitir notas pelo sistema nacional, a prefeitura deve configurar dois parâmetros fundamentais:

1. Configurar o Status de Emissão (cStatEmiss): No registro do contribuinte dentro do módulo CNC, o campo "Status para emissão de NFS-e" deve ser definido como "1 - Autorizado".

2. Definir a Data de Autorização (dAutEmiss): É obrigatório informar a "Data de Autorização de Uso dos Emissores Públicos". O contribuinte só poderá emitir notas a partir desta data ou a partir da data de início de vigência do convênio municipal, prevalecendo a que for maior. Essa data deve ser igual ou posterior à data da Inscrição Municipal (IM) registrada no CNC.

3. Verificar a Configuração do Convênio: No menu Parametrização > Configuração do Convênio, a opção "O município irá utilizar os Emissores Públicos Nacionais?" deve estar marcada como "Sim". Se o município utiliza a Adoção Faseada, o gestor deve preencher a data inicial de autorização no cadastro individual do prestador dentro do CNC.

4. Próximos Passos para o Contribuinte: O contribuinte deve acessar o Portal de Gestão NFS-e - Contribuinte, realizar o "Primeiro Acesso" para criar sua senha (ou entrar via GOV.BR se for MEI) e configurar e-mail e telefone em "Configurações".

**Resumo:** A prefeitura deve acessar o cadastro do contribuinte em "Contribuintes Locais", definir o status como "Autorizado" e preencher a "Data de Início" na seção de Autorização de Uso dos Emissores Públicos.

---

## Dúvida 027: MEI e CPF - dois cadastros no emissor nacional

**Pergunta:** O contribuinte tem MEI para uma atividade, porém gostaria de emitir notas do seu CPF, pois o MEI não contempla o serviço prestado. É possível ter dois cadastros no emissor nacional, um para o MEI e outro para o CPF?

**Resposta:**

Sim, é possível ter cadastros distintos para o MEI (CNPJ) e para a Pessoa Física (CPF) no sistema nacional. O sistema identifica o contribuinte por uma tríade única: Código do Município + Inscrição Federal (CNPJ ou CPF) + Inscrição Municipal (IM). Como o CNPJ do MEI e o CPF do indivíduo são números de identificação federal diferentes, o sistema os trata como entidades distintas.

Para emitir notas como Pessoa Física (CPF): (1) O município deve ter configurado no Painel Administrativo que "é permitida a emissão de NFS-e por pessoas físicas (CPF)"; (2) O contribuinte deve possuir uma Inscrição Municipal ativa para o seu CPF cadastrada no CNC; (3) Geralmente utiliza-se o Regime Especial de Tributação: Código 5 – Profissional Autônomo.

Para acessar os perfis: Ao entrar via GOV.BR, o sistema vincula o CPF ao CNPJ MEI para a emissão. Para emitir como Pessoa Física, o usuário deve garantir que está logado no perfil do seu CPF. Se o município permitir, ele poderá realizar o "Primeiro Acesso" com os dados do CPF para criar uma senha específica.

**Resumo:** O contribuinte pode manter o MEI para as atividades permitidas e estar cadastrado como autônomo (CPF) no município. Deve ter duas Inscrições Municipais diferentes (uma vinculada ao CNPJ e outra ao CPF) e a prefeitura deve autorizar a emissão para pessoas físicas no portal nacional.

---

## Dúvida 028: Erro "Não foi possível criar seu usuário" no primeiro acesso

**Pergunta:** Contribuintes devidamente cadastrados e autorizados a emitir nota têm se deparado com o erro "NÃO FOI POSSÍVEL CRIAR SEU USUÁRIO - Os dados digitados não puderam ser validados" durante o primeiro acesso. O que pode estar ocasionando e quais medidas adotar?

**Resposta:**

Causas prováveis: (1) Tentativa de Cadastro por MEI via Usuário/Senha - o MEI deve obrigatoriamente utilizar o "ACESSO VIA GOV.BR" (níveis Prata ou Ouro); (2) Município não Ativo ou Emissor Nacional Desabilitado - o município deve ter marcado como "Sim" a opção "O município irá utilizar os Emissores Públicos Nacionais?" na Configuração do Convênio; (3) Falta de Autorização no CNC - o contribuinte precisa estar com o status de emissão como "1 - Autorizado" e a "Data de Autorização de Uso dos Emissores Públicos" já vigente; (4) Inconsistência na Base da Receita Federal - durante o primeiro acesso, o sistema solicita dados como Título de Eleitor ou recibos do IRPF para validar a identidade.

Medidas para solucionar: Orientar os contribuintes MEI a utilizar exclusivamente o botão "Entrar com gov.br". Verificar no Painel Administrativo se o cadastro do contribuinte está como "Habilitado" e se a data de início da autorização já foi atingida. Caso o erro ocorra por falta de Título de Eleitor ou recibos de IRPF, o contribuinte deve comparecer ao atendimento presencial da prefeitura. O Gestor Atendente Municipal pode regularizar o cadastro diretamente no CNC.

**Resumo:** Se o contribuinte não for MEI e o município estiver com o convênio ativo, a falha geralmente é resolvida através da regularização cadastral presencial realizada por um atendente municipal no Painel Administrativo.

---

## Dúvida 042: Inconsistência CPF vs CNPJ no cadastro

**Pergunta:** Foi realizado cadastro utilizando CPF, porém o correto é que a emissão ocorra exclusivamente pelo CNPJ. Mesmo após ajustes no portal municipal, o sistema continua vinculando a emissão ao CPF. Solicitamos a exclusão definitiva do cadastro realizado pelo CPF para realizar novo cadastro correto apenas com o CNPJ.

**Resposta:**

O Sistema Nacional da NFS-e não realiza a "exclusão definitiva" de registros por questões de auditabilidade, mas utiliza o mecanismo de Exclusão Lógica (Inativação).

1. Inativação do Cadastro vinculado ao CPF: O gestor deve acessar o menu CNC > Contribuintes Locais, pesquisar o CPF e selecionar a opção "Inativar" (exclusão lógica). Uma vez inativado, esse registro complementar deixa de existir para fins de validação de emissão.

2. Regularização e Habilitação do CNPJ: O erro "cadastro não encontrado ou não habilitado" ocorre porque o sistema não localizou uma autorização ativa para o CNPJ na data de competência informada. O município deve: incluir o CNPJ no CNC (se exige IM); marcar o campo "Status para emissão de NFS-e" como "1 - Autorizado"; preencher o campo "Data de Início" (Data de Autorização de Uso dos Emissores Públicos) com uma data igual ou anterior à data de competência desejada.

3. Verificação de Permissões: O Gestor Atendente Municipal tem permissão específica para realizar a administração via web do CNC. Verifique também se o município configurou a Adoção Faseada - se a situação padrão estiver como "Não Habilitado", o CNPJ só conseguirá emitir após o gestor habilitá-lo individualmente no CNC.

**Resumo:** O município deve Inativar o CPF no menu "Contribuintes Locais" do CNC e Cadastrar/Habilitar o CNPJ, garantindo que o status seja "Autorizado" e que a "Data de Início da Autorização" contemple a competência desejada.

---

## Dúvida 064: Acessar dados de filial com certificado da matriz

**Pergunta:** O contribuinte entra no Emissor Nacional com o certificado digital do CNPJ da matriz e quer saber como acessar os dados e notas emitidas de uma filial.

**Resposta:**

O Sistema Nacional da NFS-e está orientado para a identificação de cada estabelecimento por meio de uma tríade única: Código do Município + Inscrição Federal (CNPJ ou CPF) + Inscrição Municipal (IM). A matriz e suas filiais são tratadas como entidades distintas para fins de emissão e consulta.

Ao realizar o login, o sistema carrega o perfil correspondente ao CNPJ informado ou selecionado no momento da entrada. Uma vez autenticado, todos os dados cadastrais e a lista de documentos emitidos que aparecem no painel referem-se estritamente ao CNPJ que efetuou o login. Se o contribuinte entrou com o perfil da matriz, ele verá apenas os dados da matriz.

Para acessar as informações de uma filial: (1) Verificar se o certificado digital utilizado (da matriz) possui permissão ou se é do tipo que abrange o CNPJ base (os primeiros 8 dígitos); (2) Ao ser solicitada a identificação no login, informar o CNPJ completo da filial desejada; (3) Acessar o menu "NFS-e Emitidas" para consultar os documentos daquela unidade específica.

**Resumo:** O sistema não permite a "troca de filial" dentro de uma mesma sessão se os CNPJs forem diferentes. É necessário realizar o login com a identificação (CNPJ) de cada filial para gerenciar suas respectivas notas e configurações.

---

## Dúvida 098: E-mail alterado na RFB não reflete no CNC

**Pergunta:** O contribuinte já fez a alteração do e-mail na base do CNPJ da Receita Federal, porém o e-mail não foi alterado no sistema da NFS-e.

**Resposta:**

A situação ocorre porque o Cadastro Nacional Complementar (CNC) é uma base de dados mantida pelos municípios que pode sobrepor (priorizar) as informações provenientes das bases federais.

1. Atualização via Gestão Municipal (Recomendado): Como o dado no CNC tem precedência sobre o da Receita Federal para fins do Sistema Nacional, o contribuinte deve solicitar que a Prefeitura de sua localização realize a correção manual. O Gestor Municipal deve acessar o Painel Administrativo, navegar até o módulo CNC > Contribuintes Locais, localizar o CNPJ e editar o campo de e-mail. Ao salvar o registro atualizado no CNC com o status "Autorizado", o sistema passa a utilizar essa informação em detrimento dos dados da Receita Federal.

2. Atualização pelo Contribuinte (Após o Acesso): Se o contribuinte já possui acesso ao sistema (ou consegue entrar via GOV.BR), ele pode atualizar seus dados de contato acessando o menu "Configurações" (ícone da engrenagem) e atualizando o e-mail nas "Informações Pessoais".

O sistema nacional consome dados da RFB, mas permite que o município insira informações complementares no CNC. Uma vez que existe um registro no CNC para aquele CNPJ, o sistema entende que aquela é a informação validada pelo fisco municipal, cessando a busca automática na base da Receita para aquele campo específico.

**Resumo:** O contribuinte deve solicitar à Prefeitura a atualização do e-mail no módulo CNC, pois as informações deste cadastro sobrepõem as da Receita Federal no ecossistema da NFS-e Nacional.

---

## Dúvida 099: Como ativar contribuinte no CNC

**Pergunta:** Prefeitura alega que um determinado contribuinte não está ativo no CNC. Solicita orientação para ativar.

**Resposta:**

Para ativar um contribuinte no Cadastro Nacional Complementar (CNC), a Prefeitura deve realizar o procedimento através do Painel Administrativo Municipal. O sistema identifica o contribuinte por uma tríade única: Código do Município + CNPJ/CPF + Inscrição Municipal (IM).

Procedimento: (1) Acesse o menu CNC > Contribuintes locais; (2) Clique no botão "+ Novo" para realizar uma inclusão individual; (3) Preencha o CPF ou CNPJ e a Inscrição Municipal (IM) do contribuinte; (4) Configurações Obrigatórias: Situação Cadastral como "Ativo"; Status para Emissão de NFS-e (cStatEmiss) como "1 - Autorizado"; Data de Autorização (dAutEmiss) - informar a "Data de Autorização de Uso dos Emissores Públicos". O contribuinte só poderá emitir notas a partir desta data informada. A data deve ser igual ou posterior à data da IM e à data de ativação do convênio do município.

Observações: Se o contribuinte já existia e foi marcado como "Inativo" anteriormente, o registro sofreu exclusão lógica, que é irreversível. Nesses casos, a fiscal deve realizar um NOVO cadastro (Inclusão) inserindo novamente o CNPJ/CPF e a IM. Verifique se o município está com o status "Ativo" no Sistema Nacional. Caso o cadastro tenha sido feito via Upload de Arquivo (.CSV), certifique-se de que o processamento foi concluído com sucesso.

**Resumo:** A Prefeitura deve acessar o módulo CNC > Contribuintes Locais, criar ou editar o registro do contribuinte, definir o status de emissão como "Autorizado" e garantir que a Data de Início da Autorização seja condizente com o período em que o contribuinte deseja operar.
