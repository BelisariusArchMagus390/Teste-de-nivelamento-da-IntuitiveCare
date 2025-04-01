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

### Teste 2

### Teste 3
Para o teste 3 foi feito um banco de dados para que pudesse comportar os dados em que seriam trabalhado as queries onde, todas os dados dos arquivos .csv relacionados com os registros contábeis dos trimestres foram mesclados quando importados em uma única tabela de nome demonstracoes_contabeis e para o arquivo de registros cadastrais foi feita uma tabela de nome relatorio_cadop.
O resultado das queries analíticas para as perguntas propostas foram:

1 - Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
<img src="https://imgur.com/a/S1Veo80.PNG" />

2 - Quais as 10 operadoras com maiores despesas nessa categoria no último ano?
<img src="https://imgur.com/a/18nSZnI.PNG" />

### Teste 4

## Requisitos

Para que que todos os testes propostos possam ser executados siga os passos abaixo:
1 - Primeiro clone ou baixe o repositório github
2 - Instale as bibliotecas necessárias executando o comando:

```
pip install -r requirements.txt
```
3 - Para executar o back-end do teste 4 utilize:

```
uvicorn server_api:app --reload
```

4 - Para a execução do front-end do teste 4 utilize:

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
