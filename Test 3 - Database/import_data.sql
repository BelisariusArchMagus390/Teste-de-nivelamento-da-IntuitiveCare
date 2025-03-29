-- table imports of demonstracoes_contabeis
-- quarters of 2023

COPY demonstracoes_contabeis (dt, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\bart4\Desktop\test_nivelamento_intuitiveCare\Test 3 - Database\data\2023\1T2023.csv'
DELIMITER ';'
CSV HEADER;

COPY demonstracoes_contabeis (dt, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\bart4\Desktop\test_nivelamento_intuitiveCare\Test 3 - Database\data\2023\2t2023.csv'
DELIMITER ';'
CSV HEADER;

COPY demonstracoes_contabeis (dt, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\bart4\Desktop\test_nivelamento_intuitiveCare\Test 3 - Database\data\2023\3T2023.csv'
DELIMITER ';'
CSV HEADER;

COPY demonstracoes_contabeis (dt, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\bart4\Desktop\test_nivelamento_intuitiveCare\Test 3 - Database\data\2023\4T2023.csv'
DELIMITER ';'
CSV HEADER;


-- quarters of 2024

COPY demonstracoes_contabeis (dt, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\bart4\Desktop\test_nivelamento_intuitiveCare\Test 3 - Database\data\2024\1T2024.csv'
DELIMITER ';'
CSV HEADER;

COPY demonstracoes_contabeis (dt, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\bart4\Desktop\test_nivelamento_intuitiveCare\Test 3 - Database\data\2024\2T2024.csv'
DELIMITER ';'
CSV HEADER;

COPY demonstracoes_contabeis (dt, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\bart4\Desktop\test_nivelamento_intuitiveCare\Test 3 - Database\data\2024\3T2024.csv'
DELIMITER ';'
CSV HEADER;

COPY demonstracoes_contabeis (dt, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'C:\Users\bart4\Desktop\test_nivelamento_intuitiveCare\Test 3 - Database\data\2024\4T2024.csv'
DELIMITER ';'
CSV HEADER;


-- table imports of relatorio_cadop
/*
COPY relatorio_cadop (Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS)
FROM 'C:\Users\bart4\Desktop\test_nivelamento_intuitiveCare\Test 3 - Database\data\Relatorio_cadop.csv'
DELIMITER ';'
CSV HEADER;
*/