# FAQ - Emissão de NFS-e no Portal Nacional

> Audiência: contribuintes, prestadores de serviço, contadores
> Temas: emissão no portal, preenchimento, dados do tomador, CEP, códigos de serviço, relatórios, acesso como procurador
> Sistema: NFS-e Nacional - Portal do Contribuinte, Emissor Web

---

## Dúvida 003: Endereço desatualizado do tomador impede emissão

**Pergunta:** O tomador teve alteração de endereço e o endereço que aparece no emissor nacional é o antigo. Não estamos conseguindo emitir a nota. O que fazer?

**Resposta:**

Para resolver a impossibilidade de emissão da NFS-e devido ao endereço desatualizado do tomador, é necessário compreender como o Sistema Nacional obtém esses dados e quais as vias de atualização disponíveis.

1. Origem dos Dados do Tomador

O emissor nacional utiliza duas fontes principais para preencher automaticamente os dados do tomador ao digitar o CNPJ: Base da Receita Federal (RFB) e Cadastro Nacional Complementar (CNC). Se o tomador alterou o endereço recentemente, o sistema pode estar refletindo a base da RFB que ainda não foi sincronizada.

2. Por que a nota não é emitida?

A dificuldade provavelmente ocorre porque muitos serviços possuem regras de Local de Incidência vinculadas ao endereço do tomador. Se o endereço antigo pertence a um município diferente do novo, o sistema pode estar calculando o imposto para a localidade errada ou bloqueando a nota por inconsistência.

3. O que pode ser feito

Ação pelo Prestador: Verifique a edição manual no momento da Emissão Completa. Se estiver usando rascunho antigo, inicie uma Nova NFS-e do zero para que o sistema realize nova busca na base da RFB.

Ação pelo Tomador: O tomador deve entrar em contato com a Prefeitura do município do novo endereço e solicitar atualização cadastral no CNC. Deve garantir que a alteração já foi formalizada no CNPJ perante a Receita Federal.

**Resumo:** O tomador precisa solicitar que o gestor tributário do seu novo município realize a atualização cadastral no módulo CNC do portal nacional. Uma vez atualizado, os dados corretos serão recuperados ao digitar o CNPJ no emissor.

---

## Dúvida 009: Local de prestação incorreto na consulta pública (Osasco)

**Pergunta:** O local de prestação das notas fiscais emitidas pelo município de Osasco está sendo informado como "Osasco" na consulta pública, mas o correto seria outro local. O município disse que a plataforma nacional tem inconsistências. Como resolver?

**Resposta:**

Para resolver a divergência na informação do local de prestação na consulta pública, é necessário compreender as responsabilidades de transcrição de dados.

1. Responsabilidade pela Transcrição (Emissão Tipo 2)

Muitos municípios operam com sistemas próprios que se integram ao ADN via transcrição (tpEmis = 2). O município é obrigado a transcrever as informações de suas NFS-e locais para o modelo XML da NFS-e Nacional antes de compartilhá-las. O campo xLocPrestacao exibido na consulta pública é a descrição textual do código IBGE informado no campo cLocPrestacao da DPS. Se o portal exibe "Osasco" em vez do local real, o erro geralmente ocorre no mapeamento durante a integração com o ADN.

2. XML vs. Consulta Pública

A Consulta Pública e o DANFSe são representações resumidas e podem apresentar limitações de exibição. O arquivo XML é o documento fiscal com validade jurídica real. O contribuinte deve realizar o download do XML e verificar a tag cLocPrestacao. Se o código IBGE estiver correto no XML, a nota é juridicamente válida.

3. Procedimento de Correção para o Município

O município deve revisar sua integração via API, garantindo que o campo cLocPrestacao esteja sendo enviado com o código IBGE correto da localidade onde o serviço foi efetivamente executado.

**Resumo:** O contribuinte deve validar a informação no XML da nota. Se o código IBGE do local de prestação estiver correto no XML, o documento está fiscalmente hígido. Se estiver errado, a prefeitura deve ajustar a rotina de transcrição e compartilhamento.

---

## Dúvida 010: E-mails, erro E0008 e CNPJ baixado do tomador

**Pergunta:** Os tomadores e prestadores receberão e-mail quando ocorrer emissão, cancelamento ou substituição? O que é o erro "E000 - A data de emissão do DPS não pode ser posterior à data de processamento"? Quando o CNPJ do tomador está baixado pode ocorrer problema na emissão?

**Resposta:**

1. Envio de e-mails para Tomadores e Prestadores

Os campos de e-mail informados nas configurações são utilizados para a geração do documento e para constar no DANFSe. O ADN envia comunicações de aceite ou rejeição de pedidos de registro de eventos especificamente para o solicitante via API. As fontes não mencionam o envio automático de e-mails de notificação para todos os atores a cada alteração de status. A consulta aos eventos vinculados à chave de acesso é a forma oficial de verificar mudanças.

2. Erro de Data de Emissão do DPS (Regra E0008)

O erro ocorre porque a data e hora de emissão da DPS não pode ser posterior à data do seu processamento (dhProc) pelo Sistema Nacional. Isso geralmente acontece por dessincronização entre o relógio do sistema do contribuinte (Webservice) e o relógio do servidor nacional. O emissor deve garantir que o campo dhEmi utilize o formato UTC correto e que o horário não esteja "no futuro" em relação ao horário oficial do ADN.

3. Emissão para CNPJ de Tomador Baixado

Sim, a situação cadastral do tomador pode impedir a emissão. O Sistema Nacional realiza validações rigorosas contra a base da RFB. A Regra E0190 rejeita a DPS se o CNPJ do tomador não for encontrado no cadastro da RFB. A validade do CNPJ é verificada em relação à data de competência informada na DPS.

**Resumo:** E-mails automáticos para todos os atores não são garantidos; consulte os eventos vinculados. Para E0008, sincronize o relógio e use formato UTC. CNPJ baixado na data de competência impede a emissão.

---

## Dúvida 013: Relatórios de notas emitidas no Emissor Nacional

**Pergunta:** O Emissor Nacional tem alguma funcionalidade que gere relatórios de notas emitidas por contribuinte?

**Resposta:**

O Emissor Nacional não possui ferramenta específica de geração de relatórios em arquivos consolidados (planilhas ou PDFs de listagem), mas oferece o módulo de Consulta de NFS-e Emitidas que cumpre função similar.

O contribuinte pode visualizar a lista de notas geradas e o sistema apresenta um campo totalizador com o quantitativo de registros que atendem aos filtros de busca. O Painel Principal exibe dashboards com informações consolidadas, como as últimas NFS-e emitidas e rascunhos pendentes.

Para a gestão municipal, o Painel Administrativo Municipal oferece estatísticas gerenciais na página inicial (volume de notas por dia da semana e por horário). O download de documentos (XML ou DANFSe) é realizado de forma individual para cada nota listada na consulta.

**Resumo:** Não há exportação consolidada em planilha ou PDF. Use o módulo de Consulta de NFS-e Emitidas para visualizar e filtrar as notas, com download individual de XML e DANFSe.

---

## Dúvida 014: Acesso ao Portal como procurador de pessoa jurídica

**Pergunta:** É possível acessar o Portal como procurador de pessoa jurídica ou somente com o certificado digital do CNPJ?

**Resposta:**

Sim, é possível acessar o portal e realizar ações como procurador, não sendo o acesso restrito apenas ao certificado digital do CNPJ da empresa.

1. Acesso como Procurador (Pessoa Física)

O sistema prevê que o autor de um evento (cancelamento, manifestação) pode ser um procurador. Nos registros de eventos, o campo destinado ao autor permite a informação do CPF do procurador, desde que possua os poderes necessários. Para distribuição e consulta de DF-e, pode-se utilizar certificado digital de Pessoa Física (e-CPF) para acessar dados vinculados ao CPF ou aos CNPJs que representa.

2. Formas de Acesso ao Portal

Usuário e Senha (exige Primeiro Acesso prévio); Certificado Digital (e-CNPJ ou e-CPF habilitado); Acesso via GOV.BR (MEI obrigatório; para demais empresas, em evolução em 2025).

3. Ações de Gestão e Regularização

Caso o procurador não consiga o primeiro acesso digitalmente, pode comparecer ao atendimento presencial da prefeitura. O Gestor Atendente Municipal pode regularizar o cadastro no CNC.

**Resumo:** O portal permite que um procurador atue em nome da pessoa jurídica, utilizando e-CPF ou login/senha, especialmente para assinatura de eventos fiscais.

---

## Dúvida 017: Atualização da base cadastral de CEP no sistema

**Pergunta:** É possível o município atualizar a base cadastral de CEP? Até o ano passado vigorava o CEP único para o município, mas agora há CEP para todas as ruas. Como atualizar essas informações no site da NFS-e?

**Resposta:**

O sistema da NFS-e Nacional não possui funcionalidade para o município "enviar" uma nova base de CEPs diretamente, mas o portal utiliza bases integradas para validação.

1. Integração com Bases Oficiais (Tabela TOM)

O sistema consome informações de bases oficiais (RFB e tabela TOM) para recuperar logradouro, bairro e município quando um CEP é digitado. A atualização dos novos CEPs por rua deve ocorrer primeiramente nos órgãos federais e nos Correios para que, por integração, o sistema da NFS-e passe a reconhecê-los.

2. Atualização dos Dados do Município

O município pode atualizar seu endereço de atendimento presencial (cabeçalho do DANFSe) em Parametrização > Dados do Município. Para contribuintes locais, a ATM pode editar o cadastro individualmente ou via upload de .CSV no CNC.

3. Regra E3313

O sistema verifica se o CEP pertence ao código IBGE do município. Se os novos CEPs ainda não forem reconhecidos, pode haver erro E3313 até a sincronização com a base federal.

**Resumo:** A atualização de CEPs depende das bases federais e dos Correios. O município pode atualizar endereços no CNC. Em caso de CEPs oficializados mas não reconhecidos, registre Solicitação ou Sugestão nos canais do Portal da NFS-e.

---

## Dúvida 019: Campos de Tributação Federal não habilitados para edição

**Pergunta:** Contribuintes não estão conseguindo preencher os campos de Tributação Federal (retenção de INSS e IRPJ). Os campos não estão habilitados para edição. Como resolver?

**Resposta:**

A impossibilidade de editar os campos de Tributação Federal geralmente ocorre devido ao enquadramento tributário do prestador ou ao tipo de emissão selecionada.

1. Enquadramento no Simples Nacional ou MEI

Regra E0676: Não é permitido o preenchimento de tributos federais quando o emitente for MEI na data de competência. Quando o emitente tem tributos apurados pelo Simples Nacional, os campos são travados. Se o cadastro estiver desatualizado e o sistema ainda "enxergar" a empresa como optante, os campos ficarão desabilitados.

2. Emissor Pessoa Física (CPF)

Regra E0675: A prestação de informações de tributos federais é proibida quando o emitente for pessoa física (CPF). Os campos de tributação federal ficam desabilitados permanentemente.

3. Tipo de Emissão (Simplificada vs. Completa)

Emissão Simplificada é destinada exclusivamente a MEIs e não contempla retenções federais detalhadas. Para informar retenções de INSS e IRPJ, o contribuinte deve utilizar a Emissão Completa. Mesmo na emissão completa, os campos só estarão habilitados se o prestador não for MEI, não for CPF e não estiver com regime Simples Nacional ativo.

4. Como resolver

Verifique a modalidade (use Emissão Completa). No Passo 1, confira como o campo "Opção no Simples Nacional" foi recuperado. Se aparecer como "Optante", os campos federais estarão bloqueados. Se a empresa for do Lucro Presumido e o sistema bloquear, pode haver erro na base do CNC; o gestor municipal deve conferir se o regime está corretamente sinalizado como "Não Optante".

**Resumo:** Verifique se está usando Emissão Completa e se o regime tributário está correto. MEI e CPF não podem preencher tributos federais. Se for Lucro Presumido com bloqueio, verifique o CNC.

---

## Dúvida 020: Erro "CEP do Tomador não está de acordo com o CEP Nacional"

**Pergunta:** MEI vai emitir nota e recebe a mensagem de que o CEP do Tomador não está de acordo com o CEP Nacional. O que seria isso?

**Resposta:**

Essa mensagem indica inconsistência entre o CEP informado para o tomador e a base de dados oficial utilizada pelo Sistema Nacional (integrada à RFB e à Tabela TOM).

1. CEP Inexistente ou Incorreto (Regra E0240)

O sistema valida se o CEP de 8 dígitos existe na base nacional dos Correios e da RFB. O número pode estar errado, conter algarismos trocados ou ser um CEP ainda não oficializado. Verifique erros de digitação ou espaços em branco.

2. Divergência entre CEP e Município (Regra E1309)

O sistema exige que o CEP informado pertença ao município selecionado para o endereço do tomador. Se informar um CEP de outra cidade mas selecionar manualmente outro município, haverá rejeição. Recomenda-se deixar o sistema realizar a busca automática (ícone da lupa ao lado do CEP) em vez de preencher manualmente.

3. Casos de "CEP Único" em transição

Se o município passou de CEP único para CEPs por logradouro, o banco de dados pode estar em sincronização. Utilize o CEP geral do município (se ativo) ou confirme no site dos Correios o CEP exato do logradouro.

**Resumo:** Verifique digitação e use a busca automática pelo CEP. Se a emissão for Simplificada e o serviço não exiger endereço detalhado, o MEI pode optar por não informar o endereço completo do tomador.

---

## Dúvida 023: Cronograma de liberação dos campos IBS e CBS no Emissor

**Pergunta:** Existe previsão oficial de data para liberação do campo IBS/CBS no Emissor Nacional? Enquanto o campo não estiver disponível, haverá penalidade ou irregularidade na emissão das NFS-e sem essa informação?

**Resposta:**

Com base nas Notas Técnicas do Comitê Gestor da NFS-e:

1. Previsão de Liberação

Até dezembro de 2025, as atualizações no Emissor Nacional Web para contemplar os grupos IBS e CBS estavam em desenvolvimento. De acordo com a NT 004/2025, as evoluções de layout serão disponibilizadas ao longo de 2026, com datas a serem divulgadas no Portal da NFS-e. O ambiente com o novo layout da RTC foi programado para operação definitiva a partir de 5 de janeiro de 2026.

2. Penalidades e Irregularidades

Para garantir que a transição não interrompa a atividade econômica, o Comitê Gestor adotou medidas de flexibilização. As regras de negócio que obrigam o preenchimento dos grupos "IBSCBS" foram temporariamente suspensas. O sistema não impedirá a emissão ou recepção de documentos caso esses campos não sejam informados neste momento inicial. Documentos emitidos sem os grupos IBS e CBS serão autorizados e recepcionados pelo ADN, não configurando irregularidade técnica.

3. Obrigatoriedade de Integração

A suspensão da regra de preenchimento não desobriga os municípios de se integrarem à plataforma até 1º de janeiro de 2026. Municípios que não ativarem seus convênios ou não compartilharem documentos no padrão nacional estarão sujeitos à suspensão de transferências voluntárias.

**Resumo:** Enquanto o Emissor Web não for atualizado com a interface para IBS/CBS, os contribuintes podem continuar emitindo normalmente. O sistema aceita documentos sem esses grupos de forma facultativa. Acompanhe as "Últimas Notícias" no Portal Nacional.

---

## Dúvida 025: Emissão com competência anterior à vigência do convênio

**Pergunta:** Contribuinte domiciliado em outro município está emitindo nota para Câmara Municipal de Imbituba, com incidência neste município (11.02, incidência no local), data de competência 01/12/2025. O convênio do município entrou em vigência em 01/01/2026. O contribuinte não consegue emitir. É erro do sistema?

**Resposta:**

Não se trata de erro do sistema, mas do cumprimento de regras de negócio e integridade tributária do ADN.

1. Vigência do Convênio e Data de Competência (Regra E1270)

O Sistema Nacional estabelece que a data de competência da prestação deve ser igual ou posterior à data de ativação do convênio do município emissor. O contribuinte está tentando emitir para competência 01/12/2025, quando o convênio de Imbituba ainda não estava vigente (01/01/2026). Mesmo que o município de domicílio do prestador já estivesse conveniado em 2025, o sistema não permite emissão retroativa para municípios de incidência que ainda não haviam "nascido" para o sistema nacional na data do fato gerador.

2. Regra de Integridade

O sistema valida a competência contra a data de início de vigência do município de incidência do imposto. Se o serviço foi prestado em Imbituba em dezembro/2025, mas o convênio de Imbituba só ativou em janeiro/2026, a emissão para aquela competência não é permitida.

**Resumo:** A data de competência deve ser igual ou posterior à data de ativação do convênio do município de incidência. Para competência 01/12/2025, o convênio de Imbituba ainda não estava vigente; a emissão não é permitida.

---

## Dúvida 043: Erro ao emitir como Tomador ou Intermediário

**Pergunta:** Contribuinte não consegue emitir nota. Aparece mensagem relacionada a "Emissão por tomador e intermediário". O que ocorre?

**Resposta:**

A mensagem indica que o contribuinte está tentando emitir selecionando um perfil de emitente (Tomador ou Intermediário) que ainda não está habilitado no sistema nacional.

Na versão atual do Sistema Nacional da NFS-e, a emissão de notas é permitida exclusivamente pelo Prestador de Serviço. Os campos para Tomador e Intermediário constam no layout, mas estão reservados para versão futura.

A Regra de Negócio E9996 rejeita automaticamente qualquer DPS onde o campo tpEmit (Tipo de Emitente) seja preenchido com as opções 2 (Tomador) ou 3 (Intermediário). O erro geralmente ocorre no Passo 1 (Pessoas) da emissão completa, quando o contribuinte responde "Você irá emitir esta NFS-e como?" e seleciona erroneamente uma das opções desabilitadas.

**Resumo:** O contribuinte deve retornar ao início do preenchimento e, na seção "EMITENTE DA NFS-E", marcar a opção "Prestador". Somente com essa opção o sistema permitirá avançar e concluir a emissão.

---

## Dúvida 044: Como reabrir a parametrização no Painel Municipal

**Pergunta:** Prefeitura quer saber como "reabrir" a opção para parametrização das informações no Painel Municipal.

**Resposta:**

O procedimento depende do estágio atual de ativação do convênio.

1. Reabertura antes da Data de Início de Vigência

Se a prefeitura já clicou em "Concluir Parametrização", mas a data de expectativa ainda não chegou, o sistema permite edição total. Ao buscar editar qualquer parâmetro antes da data efetiva de ativação, o sistema retoma automaticamente o status de "pré-ativação". O assistente será aberto novamente com todos os parâmetros cadastrados. Após as edições, o gestor deve clicar novamente em "Concluir Parametrização".

2. Parametrização após a Ativação (Convênio "Ativo")

Uma vez que o convênio atingiu a data de vigência, o assistente passo a passo deixa de existir e é substituído pelo Painel Municipal Principal. Para "reabrir" as opções, o gestor deve acessar o menu no canto superior direito (ícone de barras de ajuste) e selecionar "Parametrização". Qualquer mudança é considerada alteração "controlada", exigindo data de início de vigência, motivo e legislação. O botão de "excluir" é substituído pela funcionalidade de encerrar vigência.

3. Quem pode realizar

Apenas Gestor Municipal Principal, Gestor Auditor Municipal e Gestor Parametrizador Municipal têm permissão.

**Resumo:** Antes da vigência: edite e conclua novamente. Após ativação: acesse o menu Parametrização no canto superior direito; alterações são controladas com vigência.

---

## Dúvida 051: Erro de compatibilidade do CEP recuperado do CNPJ

**Pergunta:** Ao tentar prosseguir com a emissão, aparece: "A informação do(s) campo(s) CEP recuperada do cadastro CNPJ não possui compatibilidade em tamanho ou formato com a definição especificada para o Sistema Nacional NFS-e." O CEP está corretamente cadastrado em todas as bases. Como resolver?

**Resposta:**

O erro ocorre porque o Sistema Nacional exige que o campo CEP contenha rigorosamente 8 dígitos numéricos, sem hífens, espaços ou caracteres especiais. Quando o sistema recupera a informação da RFB, pode encontrar dado que não segue o padrão técnico (pattern{8}) definido no XSD.

A Administração Tributária Municipal deve intervir utilizando o CNC, que permite sobrepor informações da base RFB.

Procedimento: (1) Acesse o Painel Municipal > CNC > Contribuintes Locais; (2) Localize o CNPJ ou crie registro complementar; (3) No campo CEP, insira manualmente os 8 números, garantindo zeros à esquerda (ex: 01001000) e sem hífen; (4) Salve com Status "1 - Autorizado". O sistema passará a utilizar a informação do CNC em detrimento da RFB.

Mesmo que o CEP pareça correto nas bases, pode estar armazenado com formatação que inclui hífen (ex: 38400-000). O motor de validação rejeita qualquer variação que não seja estritamente 8 números.

**Resumo:** O município deve corrigir o CEP no CNC, inserindo 8 dígitos numéricos sem hífen ou espaços. O CNC sobrepõe os dados da RFB.

---

## Dúvida 059: Retenção ISSQN para CEF, Prefeitura como tomadora e entidades imunes

**Pergunta:** É possível configurar retenção apenas para os itens 15.10 e 19.01 quando o tomador for a CEF? É possível configurar retenção obrigatória quando o tomador for a própria prefeitura? Como tratar entidades imunes e isentas? O que é Manifestação – confirmação tácita? NFS-e rejeitada tem vinculação com cancelamento?

**Resposta:**

1. Retenção Específica para CEF

Sim. O município pode gerenciar regras no Painel Municipal, módulo "Retenções do ISSQN". Crie uma "Nova Retenção", selecione "Retido pelo Tomador", vincule aos subitens 15.10 e 19.01 e inclua o CNPJ da CEF em "Responsáveis Tributários".

2. Retenção Obrigatória para a Prefeitura como Tomadora

Sim. Crie regra de retenção vinculada ao CNPJ da Prefeitura como responsável tributário. Para abranger todos os itens, selecione "Todos os Serviços" ao configurar a regra.

3. Entidades Imunes e Isentas

Imunidades: Os emissores nacionais já estão aptos. No Passo 2 (Serviço), o prestador indica imunidade e seleciona o dispositivo da CF88 correspondente. Isenções municipais: Necessitam parametrização no Painel Municipal no módulo "Benefícios Municipais", tipo "Isenção". O município pode vincular contribuintes específicos via CNC.

4. Manifestação – Confirmação Tácita

É evento gerado automaticamente quando o tomador não se manifesta (confirmando ou rejeitando) dentro do prazo legal. Serve para dar segurança jurídica ao prestador. Está relacionado ao item 6.4 (Manifestação de NFS-e) do Guia do Emissor.

5. Rejeição, Cancelamento e MAN

Rejeição e cancelamento são eventos distintos. A rejeição pode ser motivo para emissão de nova nota. NFS-e cancelada é excluída da apuração e não gera guia. NFS-e rejeitada não anula a nota imediatamente no MAN, a menos que seja seguida de cancelamento ou substituição aceito pelo fisco.

**Resumo:** Retenção para CEF e Prefeitura é configurável no módulo Retenções do ISSQN. Imunidades são informadas pelo prestador; isenções exigem parametrização municipal. Confirmação tácita ocorre por decurso de prazo. Rejeição e cancelamento são eventos distintos.
