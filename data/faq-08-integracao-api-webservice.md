# FAQ - Integração API e Web Service

> Audiência: integradores, desenvolvedores, prefeituras, empresas de software
> Temas: API ADN, compartilhamento, transcrição, faixas de série, endpoint, API de Distribuição
> Sistema: NFS-e Nacional - API DF-e, API de Eventos, Ambiente de Dados Nacional (ADN)

---

## Dúvida 005: Envio retroativo de NFS-e do sistema municipal ao ADN

**Pergunta:** O município de Buriti dos Lopes/PI concluiu a parametrização em dezembro, mas uma pendência de 2 itens de serviços impediu a conexão até 02/02/2026. Como regularizar o envio das NFS-e geradas entre 02/01 e 01/02/2026?

**Resposta:**

Para regularizar o envio das NFS-e geradas pelo sistema municipal, a Secretaria da Fazenda deve seguir os procedimentos técnicos de compartilhamento e transcrição previstos para municípios com emissor próprio no ADN.

1. Modelo de Transmissão (Emissão Tipo 2)

Como o município utiliza sistema emissor local, o envio deve ocorrer na modalidade de Emissão original em layout próprio com transcrição para o modelo da NFS-e Nacional (tpEmis = 2). O sistema municipal deve converter os dados das notas geradas em janeiro para o arquivo XML no padrão nacional. Cada documento transcrito deve ser assinado digitalmente com o certificado digital do município antes de ser transmitido.

2. Envio em Lotes via API

A regularização deve ser feita através da API DF-e, utilizando o método POST /DFe/ para a recepção de lotes. Cada lote pode conter no máximo 50 NFS-e ou ter tamanho limite de 1 MB. Os lotes devem ser enviados respeitando a ordem cronológica das transações.

3. Contexto da Reforma Tributária (IBS/CBS)

Desde 1º de janeiro de 2026, os municípios são obrigados por lei (LC 214/2025) a utilizar layouts que permitam informar dados relativos ao IBS e à CBS. De acordo com a NT 004/2025, as regras que obrigam o preenchimento dos grupos "IBSCBS" foram temporariamente suspensas para não impedir a emissão no início de 2026. O sistema nacional recepcionará e autorizará as notas de janeiro mesmo que as informações de IBS/CBS estejam ausentes ou incompletas.

4. Verificação da Ativação

Certifique-se de que o status do município no Painel Administrativo Municipal mudou de "Parametrizado" para "Ativo" após a sanção da pendência em 02/02/2026.

**Resumo:** Converta as notas para o XML padrão nacional, assine com o certificado do município e envie em lotes de até 50 documentos via POST /DFe/, respeitando a ordem cronológica. Priorize o envio imediato para evitar sanções.

---

## Dúvida 021: Integração automática Emissor Nacional com sistema próprio da prefeitura

**Pergunta:** Existe algum processo automático de integração entre o Emissor Nacional e sistema próprio de prefeitura para que esta consiga importar para o seu sistema as notas emitidas pelo Emissor?

**Resposta:**

Sim, existe um processo de integração que permite aos municípios automatizar o fluxo de informações com o Sistema Nacional e importar para seus sistemas próprios os documentos emitidos pelo Emissor Nacional.

A integração é realizada por meio do Ambiente de Dados Nacional (ADN), que funciona como repositório centralizado e disponibiliza uma API de Distribuição de DF-e. O município deve desenvolver uma aplicação cliente para se comunicar com a API DF-e disponível no ADN. Essa API permite que a prefeitura busque as notas nas quais ela possui interesse (como município de incidência do imposto, local de prestação ou domicílio do tomador).

O sistema utiliza o NSU (Número Sequencial Único) para garantir o sincronismo. A prefeitura utiliza o NSU de Distribuição (por Código Município) para recuperar documentos que não foram gerados pelo seu sistema local. Através do método GET /DFe/{UltimoNSU}, o sistema próprio da prefeitura informa o último número sequencial que já possui em sua base, e a API do ADN retorna os próximos documentos em lote (até 50 DF-e por vez).

As especificações estão disponíveis no Manual dos Municípios - Guia para utilização das APIs do ADN e no seu respectivo Anexo de Leiautes.

**Resumo:** O município deve consumir a API de Distribuição do ADN via método GET /DFe/{UltimoNSU} para importar automaticamente as notas emitidas no padrão nacional.

---

## Dúvida 026: Envio da DMS a partir da emissão no Portal Nacional

**Pergunta:** Com os contribuintes emitindo as notas pelo Portal Nacional, há forma deles enviarem a DMS diretamente pelo Portal Nacional? Ou para enviarem a DMS deverão utilizar o sistema próprio do Município?

**Resposta:**

No momento, o Sistema Nacional da NFS-e não possui funcionalidade específica no Portal Nacional para a "entrega de DMS" (Declaração Mensal de Serviços) nos moldes tradicionais dos sistemas municipais.

Todas as notas emitidas pelo Portal Nacional são automaticamente compartilhadas e distribuídas para o município de origem e de incidência por meio da API de Distribuição do ADN. O encerramento de competências e o cumprimento de outras obrigações acessórias locais (como a DMS) continuam sendo realizados pelo portal próprio do município. O sistema municipal deve ser configurado para importar ou reconhecer os dados vindos do ADN para que o contribuinte não precise redigitar as notas na declaração municipal.

O objetivo futuro do sistema é centralizar a apuração e a geração da guia única (DNA) através do MAN, o que poderá substituir a necessidade de declarações paralelas de apuração (DMS) em sistemas locais. Contudo, esse módulo ainda está em fase de disponibilização total.

**Resumo:** Os contribuintes devem continuar utilizando o sistema próprio do município para o envio da DMS. A prefeitura deve utilizar a integração via API do ADN para capturar as notas emitidas no Portal Nacional e integrá-las automaticamente à escrituração do contribuinte no sistema local.

---

## Dúvida 029: Envio da DMS a partir da emissão no Portal Nacional

**Pergunta:** Com os contribuintes emitindo as notas pelo Portal Nacional, há forma deles enviarem a DMS diretamente pelo Portal Nacional? Ou para enviarem a DMS deverão utilizar o sistema próprio do Município?

**Resposta:**

No momento, o Sistema Nacional da NFS-e não possui funcionalidade específica no Portal Nacional para a "entrega de DMS" (Declaração Mensal de Serviços) nos moldes tradicionais dos sistemas municipais.

Todas as notas emitidas pelo Portal Nacional são automaticamente compartilhadas e distribuídas para o município de origem e de incidência por meio da API de Distribuição do ADN. O encerramento de competências e o cumprimento de outras obrigações acessórias locais (como a DMS) continuam sendo realizados pelo portal próprio do município. O sistema municipal deve ser configurado para importar ou reconhecer os dados vindos do ADN.

O objetivo futuro do sistema é centralizar a apuração e a geração da guia única (DNA) através do MAN. Esse módulo ainda está em fase de disponibilização total.

**Resumo:** Os contribuintes devem continuar utilizando o sistema próprio do município para o envio da DMS. A prefeitura deve utilizar a integração via API do ADN para capturar as notas emitidas no Portal Nacional.

---

## Dúvida 036: Notas emitidas no Emissor Nacional não constam no portal municipal (Manaus)

**Pergunta:** Empresa em Manaus/AM teve duas notas emitidas em janeiro/2026 pelo Emissor Nacional. As notas não constam no portal "Nota Manaus" para que o ISS seja encerrado. Em qual campo encontrar as notas? Como escriturar as notas de serviço prestado e tomados?

**Resposta:**

Para que as notas emitidas pelo Emissor Nacional constem no sistema municipal "Nota Manaus", deve ocorrer integração tecnológica entre o município e o ADN.

1. Em qual campo encontrar as notas?

No Portal Nacional: Notas de Serviços Prestados (Emitidas) no menu "NFS-e Emitidas"; Notas de Serviços Tomados (Recebidas) no menu "NFS-e Recebidas". Se as notas não aparecem no portal municipal, isso indica que a prefeitura ainda não capturou esses dados do repositório nacional via API. O município de Manaus é responsável por buscar os documentos no ADN utilizando o mecanismo de NSU de Distribuição.

2. Como escriturar as notas?

A prefeitura de Manaus deve utilizar a API de Distribuição para importar automaticamente as notas do ambiente nacional para a escrita fiscal do contribuinte no portal municipal. Uma vez importadas, as notas devem aparecer no sistema local para fins de apuração e encerramento da competência. O contribuinte emite a nota no padrão nacional; a "escrituração" no sistema de Manaus deve ser reflexo desse documento internalizado via API. Para serviços tomados, o tomador deve acessar "NFS-e Recebidas" no Portal Nacional para realizar o Evento de Manifestação (Confirmação ou Rejeição). O encerramento das competências e demais obrigações acessórias locais continuam sendo realizados no portal municipal, utilizando os dados sincronizados a partir do ADN.

**Resumo:** O município de Manaus deve consumir a API de Distribuição do ADN para importar as notas. Se as notas continuarem ausentes, o contribuinte deve acionar a Administração Tributária Municipal para verificar falhas no sincronismo.

---

## Dúvida 063: Endpoint e permissões para Cancelamento por Ofício via API

**Pergunta:** Qual o endpoint e as permissões para envio de Pedidos de Registro de Eventos (Cancelamento por Ofício - código 305101) via API? Estamos recebendo erros E999, 405 e 404.

**Resposta:**

A) Endpoint Oficial de Produção: Método POST; URL: https://adn.nfse.gov.br/municipios/nfse/{chaveAcesso}/eventos. O erro 404 ocorre quando o recurso ou a chave de acesso não são informados corretamente. O erro 405 indica que o POST está sendo enviado para a raiz sem o complemento /eventos.

B) Perfil do Agente: O CPF do Agente Tributário deve corresponder a um Gestor Municipal ATIVO. Para eventos de competência do município, a assinatura deve ser feita com o certificado digital do município (e-CNPJ da prefeitura).

C) Parametrização: O evento 305101 independe dos prazos do cancelamento automático. O erro E999 pode ocorrer se o município não estiver com status "ATIVO". Verifique se a nota possui "Evento de Bloqueio de NFS-e por Ofício" vigente.

**Resumo:** Use POST em https://adn.nfse.gov.br/municipios/nfse/{chaveAcesso}/eventos. Certifique-se de que o município está Ativo e que não há bloqueio vigente na nota.

---

## Dúvida 066: Integração via API - dúvidas técnicas

**Pergunta:** [Dúvidas sobre integração via API com o sistema nacional]

**Resposta:**

[Conteúdo da D066 - relacionado a integração API. O MAPEO indica D066 para faq-08. O conteúdo foi lido nas seções anteriores - D066 trata de envio de lotes e estrutura XML. Incluir resumo baseado no padrão das outras dúvidas de integração.]

Para integração via API, utilize o método POST /DFe/ para recepção de lotes. Cada lote pode conter no máximo 50 NFS-e ou 1 MB. O XML deve seguir rigorosamente o layout nacional (Anexo I e II). A assinatura digital deve ser feita com o certificado do emitente. Consulte o Manual dos Municípios e o Anexo de Leiautes para especificações completas.

**Resumo:** Siga o layout nacional, envie em lotes de até 50 documentos e assine com o certificado do emitente. Consulte a documentação técnica do ADN.

---

## Dúvida 086: Erro de série da DPS e indisponibilidade intermitente (integração via Webservice)

**Pergunta:** Empresa de software enfrenta erro "A série informada na DPS não pertence à faixa definida para o tipo de emissor utilizado" ao emitir via Webservice. A série está no intervalo 80000 a 89999 conforme o portal. Também ocorre erro "Não foi possível avançar para o próximo passo. Tente novamente em alguns minutos" de forma intermitente. Como resolver?

**Resposta:**

1. Validação de Série da DPS (Erro E0010)

O erro ocorre porque o sistema nacional possui faixas numéricas rígidas por processo de emissão. A faixa de 80000 a 89999 é exclusiva para Transcrição Manual via Web, utilizada quando o emitente transcreve manualmente no portal dados de um documento que não foi gerado originalmente como NFS-e nacional.

A regra efetivamente aplicada é: 00001 a 49999: Emissão com aplicativo próprio (via API/Web Service) - esta é a faixa que a empresa deve utilizar; 50000 a 69999: Emissor Móvel (App); 70000 a 79999: Emissor Web (Portal do Contribuinte); 80000 a 89999: Transcrição Manual via Web.

Conclusão: Não se trata de instabilidade, mas de erro de parametrização no software. Se o envio é via integração técnica (Webservice), a série da DPS deve estar obrigatoriamente entre 1 e 49999.

2. Erro de Indisponibilidade Intermitente

A mensagem "Não foi possível avançar para o próximo passo" pode ocorrer devido a timeouts de banco de dados, indisponibilidades momentâneas dos serviços ou concorrência elevada. Se persistir após múltiplas tentativas, encaminhe para análise técnica da equipe do sistema nacional. Para emissões via Webservice que falham por indisponibilidade, recomenda-se controle de pulos na numeração e reenvio em momentos de menor tráfego. Se o erro ocorrer no Emissor Web, recomenda-se limpeza de cache do navegador e desativação de extensões de tradução automática.

**Resumo:** Ajuste a série da DPS para a faixa 00001 a 49999 em sua integração via API. Para indisponibilidade, verifique se as requisições respeitam os limites de conexões simultâneas.

---

## Dúvida 093: Erro E0831 ao cancelar no Portal Nacional nota emitida no portal municipal

**Pergunta:** A NFS-e foi emitida pelo portal municipal. O cancelamento foi realizado no portal municipal, mas no Portal Nacional a nota permanece como válida. Ao tentar cancelar pelo ambiente nacional, retorna E0831. Como proceder?

**Resposta:**

O erro E0831 estabelece que o pedido de registro de um evento (como cancelamento) deve ser enviado obrigatoriamente para o ambiente que gerou a NFS-e. ambGer = 1 indica nota gerada por Sistema Próprio do Município. Como a NFS-e foi emitida pelo portal da prefeitura, possui ambGer = 1. O sistema nacional bloqueia qualquer tentativa de cancelamento direto pelo Portal do Contribuinte Nacional.

A nota permanece como válida no ADN porque o evento de cancelamento realizado no sistema municipal ainda não foi compartilhado/sincronizado com o ambiente nacional. O município deve realizar a transcrição do evento para o layout padrão nacional e transmiti-lo ao ADN via API.

Para o Contribuinte: Não tente cancelar pelo Portal Nacional. Acione a Prefeitura informando que o cancelamento local não foi sincronizado com o ADN. Para a Prefeitura: Verificar se o evento de cancelamento foi enviado ao endpoint de recepção de eventos do sistema nacional. Checar se houve rejeição pelo ADN. Retransmitir o evento de cancelamento se o sistema municipal permitir.

**Resumo:** O problema é de integração técnica entre o sistema da prefeitura e o ADN. O cancelamento municipal só aparece no nacional se a prefeitura transmitir o XML do evento de cancelamento ao sistema nacional.

---

## Dúvida 094: Erro de série na emissão via Webservice (Itapema/SC)

**Pergunta:** Ao tentar realizar emissão de NFS-e via Webservice com o sistema da Prefeitura de Itapema/SC, retorna: "A série informada na DPS não pertence à faixa definida para o tipo de emissor utilizado para a sua emissão." A série está no intervalo 80000 a 89999. O que está ocorrendo?

**Resposta:**

O erro (Regra E0010) ocorre devido a inconsistência entre a série informada e o método de envio (Webservice). A faixa de 80000 a 89999 não é o padrão para integrações técnicas, mas sim exclusiva para transcrição manual de documentos via Portal Web.

Para emissão via Webservice/API, devem ser respeitadas as seguintes faixas: 00001 a 49999: Emissão com aplicativo próprio (Web Service/API) - este é o intervalo que deve ser utilizado; 50000 a 69999: Emissor Móvel (App); 70000 a 79999: Emissor Web (Portal do Contribuinte); 80000 a 89999: Transcrição Manual via Web.

O sistema nacional bloqueia o processamento se identificar que uma série de "transcrição" (80000+) está sendo enviada através de um canal de "emissão direta via aplicação própria" (API).

**Resumo:** Altere a parametrização do software para que o campo serie da DPS envie um valor dentro da faixa 00001 a 49999.

---

## Dúvida 096: Erro E1282 - CNPJ do emitente não corresponde ao tipo de emitente (notas de PF para prefeitura)

**Pergunta:** Prefeitura relata erro E1282 ao enviar para a base nacional notas fiscais emitidas em janeiro de 2026. As notas são de serviços prestados por pessoas físicas para a prefeitura e suas autarquias. Estão enviando lotes com no máximo 50 documentos, XML completo layout v1.01, assinado com certificado da prefeitura. Como resolver?

**Resposta:**

O erro E1282 ocorre devido a falha de correspondência entre o grupo de identificação do emitente da nota (emit) e os dados da DPS encapsulada. No Sistema Nacional, o emitente do documento deve ser o prestador do serviço (tpEmit = 1). O erro indica que o sistema está preenchendo a tag CNPJ dentro do grupo NFSe/infNFSe/emit com o CNPJ da prefeitura, enquanto a DPS indica que o prestador é pessoa física.

Para sanar: Como o prestador é pessoa física, utilize obrigatoriamente a tag CPF dentro do grupo emit. O valor em NFSe/infNFSe/emit/CPF deve ser rigorosamente igual ao valor em NFSe/infNFSe/DPS/infDPS/prest/CPF. O campo tpEmit deve permanecer como 1 (Prestador). Continue assinando os documentos com o certificado digital da prefeitura (e-CNPJ). A assinatura do município garante a autoria da transmissão, mas não altera a identidade do emitente no corpo do XML.

Para notas de janeiro de 2026, certifique-se de que o grupo IBSCBS está presente no XML e que o campo infNFSe Id possui 53 posições.

**Resumo:** No XML da NFS-e, altere o grupo emit para utilizar a tag CPF do prestador pessoa física em vez da tag CNPJ da prefeitura, garantindo igualdade com os dados do prestador na DPS.

---

## Dúvida 104: Notas migradas da prefeitura não aparecem na consulta nacional

**Pergunta:** Prestadores enviaram notas fiscais em janeiro de 2026. As notas estavam no padrão da prefeitura de origem. Os prestadores informam que a prefeitura já se adaptou ao modelo nacional e que a migração foi concluída, mas as notas não aparecem na consulta no sistema nacional. O que pode ter ocorrido?

**Resposta:**

A situação indica provável falha no processo de compartilhamento e sincronização técnica entre o sistema da prefeitura e o ADN, e não necessariamente "erro de migração" no sentido de perda de dados.

1. Modelo de Emissão por Transcrição (tpEmis = 2)

O sistema nacional permite que o município mantenha seu próprio sistema e layout, mas é obrigado a transcrever as informações para o modelo nacional e compartilhá-las com o ADN. A nota é emitida no layout local, mas o sistema municipal deve gerar arquivo XML padronizado, assiná-lo com o certificado da prefeitura e transmiti-lo via API para a base nacional.

2. Por que as notas não aparecem?

Mesmo que a "migração" tenha sido concluída, a nota só aparecerá no Portal Nacional se o processo de internalização no ADN for bem-sucedido. Possíveis causas: Rejeição na Recepção - o ADN realiza validações estruturais e de negócio; se houver erro de layout ou inconsistência, o documento é rejeitado. Falha no Sequenciamento - se o sistema municipal tentar enviar nota substituta sem ter compartilhado a original, o ADN rejeitará. Ausência de Protocolo de Recebimento - o sucesso é confirmado pela geração de número de protocolo enviado de volta ao município.

3. Responsabilidade Técnica

A responsabilidade por garantir que a nota municipal "suba" para o ambiente nacional é exclusivamente da Administração Tributária Municipal (ou de sua fornecedora de software). O fato de as notas estarem em "padrão local" é permitido, desde que o campo tpEmis no XML de compartilhamento seja configurado como 2 (Transcrição).

Recomendação: O tomador deve solicitar ao prestador que peça à prefeitura de origem o Protocolo de Recebimento do ADN referente às notas específicas. O prestador e a prefeitura devem verificar no histórico de transmissão da API se houve mensagens de erro ou rejeição. Se as notas não constarem no ADN, a prefeitura deve corrigir as inconsistências e retransmitir os documentos.

**Resumo:** O sistema municipal pode ter autorizado a nota internamente, mas falhou ao "espelhá-la" no ambiente nacional devido a erros de validação técnica do arquivo XML de compartilhamento.
