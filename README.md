# Teste de nivelamento da Intuitive Care

## Sumário

* [Testes](#testes)
  * [Teste 1](#teste-1)
  * [Teste 2](#teste-2)
  * [Teste 3](#teste-3)
  * [Teste 4](#teste-4)
* [Requisitos](#requisitos)
* [Testes automatizados](#testes-automatizados)
* [Tecnlogias utilizadas](#tecnlogias-utilizadas)

## Testes

### Teste 1
No Teste 1, para a resolução do que foi proposto foi feito uma classe chamada _**DownloadPDFFile**_, que possui funções que farão a request na url designada, busca de arquivo PDF de nome e tag desejada, o download do mesmo, além de compactação dos arquivos que estiverem na pasta _**downloads_file**_

### Teste 2
No Teste 2, para a resolução do que foi proposto foi feito uma classe de nome _**DataTransformationPDFtoCSV**_, que possui a função que lê um arquivo PDF, encontra as tabelas que estiverem nele e as mescla criando um dataframe, além de funções para conversão em arquivos .csv e excel, renomear colunas, substituir valores de uma determinada coluna e compactação de arquivo

### Teste 3
No Teste 3 foi feito um banco de dados para que pudesse comportar os dados em que seriam trabalhado as queries onde, todas os dados dos arquivos .csv relacionados com os registros contábeis dos trimestres foram mesclados quando importados em uma única tabela de nome _**demonstracoes_contabeis**_ e para o arquivo de registros cadastrais foi feita uma tabela de nome _**relatorio_cadop**_.
O resultado das queries analíticas para as perguntas propostas foram:

1 - Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?

![Resultados do último trimestre](https://i.imgur.com/fByvVYl.png)

2 - Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

![Resultados do último ano](https://i.imgur.com/vxfeLj4.png)

### Teste 4
No Teste 4, para a resolução do que foi proposto foi feito um back-end em python utilizando o FastAPI, que possui uma função que retorna os resultados de uma busca feita no arquivo _**Relatorio_cadop.csv**_, podendo ser buscado através do valor de qualquer coluna e um front-end feito em Vue.js, para conseguir os inputs do usuário e enviar para o servidor.
A coleção de requisoções no postman estão no diretório _**postman_requests**_, no diretório respectivo do Teste 4.

## Requisitos

Para que que todos os testes propostos possam ser executados siga os passos abaixo:

1 - Primeiro clone ou baixe o repositório github

2 - Instale as bibliotecas necessárias executando o comando:

```
pip install -r requirements.txt
```
3 - Para executar o back-end do teste 4 utilize o seguinte comando estando dentro do diretório _**test_4_api**_:

```
uvicorn server_api:app --reload
```

4 - Para a execução do front-end do teste 4 utilize o seguinte comando estando dentro do diretório _**test_4_api/front_server**_::

```
npm run dev
```

Observação: Nos testes 1 e 2, para visualizar a sua resolução execute o arquivo program.py de seu respectivo teste.

## Testes automatizados
Para executar os testes automatizados utilize:

```
pytest testes/
```

## Tecnlogias utilizadas
[![My Skills](https://skillicons.dev/icons?i=git,github,vscode,py,vue,npm,fastapi,mysql)](https://skillicons.dev)
