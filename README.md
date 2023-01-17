# Intuitive Care
Processo seletivo da empresa IntuitiveCare.

# Instructions
---- Teste 1 - WebScraping ----

Todas as tarefas deste teste devem ser executadas em código nas linguagens Python ou Java

1.1 - Acessar o site: https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude

1.2 - Baixar os Anexos I ao Anexo IV

Untitled (4).png
1.3 - Agrupar os anexos em um mesmo arquivo compactado (ZIP, RAR, ...)

---- Teste 2 Transformação de dados ----- Neste teste o candidato deverá criar um código (em uma das linguagens mencionadas no fim desse e-mail) que execute as tarefas de código abaixo. Tarefas de código:

Todas as tarefas deste teste devem ser executadas em código nas linguagens Python ou Java

Tarefas de código:

Extrair do pdf do anexo I do teste 1 acima os dados da tabela Rol de Procedimentos e Eventos em Saúde (todas as páginas);
Salvar dados em uma tabela estruturada, em csv;
e Zipar o csv num arquivo "Teste_{seu_nome}.zip".- - Com a legenda no rodapé substituir os dados abreviados das colunas OD e AMB para as respectivas descrições.
Untitled (5).png
---- Teste 3 - Banco de dados -----Neste teste o candidato deverá criar scripts .sql (MySQL 8. ou Postgres >10.0) que execute as tarefas de código abaixo.*

Tarefas de Preparação (podem ser feitas manualmente):

Baixar os arquivos dos últimos 2 anos no repositório público: https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/

Baixar csv anexo:

(está em anexo no e-mail)

As tarefas abaixo devem ser executadas em código na linguagem SQL em um banco PostgreSQL ou MySQL

Criar queries para criar tabelas com as colunas necessárias para o arquivo csv.
Queries de load: criar as queries para carregar o conteúdo dos arquivos obtidos nas tarefas de preparação
Atenção ao encoding dos arquivos no momento da importação!
Montar uma query analítica que traga a resposta para as seguintes perguntas:
Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último ano?
---- Teste 4 - API -----Neste teste o candidato deverá criar uma interface web (usando o framework Vue.js) que se comunicará com um servidor em uma das linguagens mencionadas no fim desse email para realizar as tarefas de código abaixo. Tarefas de Preparação:

Todas as tarefas deste teste devem ser realizadas em linguagem Python
Utilizar CSV que esta em anexo:
Tarefas de código:

Criar servidor com rota que realiza uma busca textual na lista de cadastro de operadoras (obtido na tarefa de preparação) e retorne as linhas que mais se assemelham

Criar coleção no Postman para exibir resultado


Serão considerados diferenciais:

Considerações de performance
Considerações de arquitetura
Bom uso de ferramentas de controle de versão
Uso de infra em nuvem
