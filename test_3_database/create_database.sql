CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
	id_demonstrativo SERIAL PRIMARY KEY,
    dt DATE,
    reg_ans VARCHAR(25),
    cd_conta_contabil INTEGER,
    descricao VARCHAR(250),
    vl_saldo_inicial TEXT,
    vl_saldo_final TEXT
);

CREATE TABLE IF NOT EXISTS relatorio_cadop (
	id_operadora SERIAL PRIMARY KEY,
	Registro_ANS VARCHAR(25),
    CNPJ VARCHAR(25),
    Razao_Social VARCHAR(250),
    Nome_Fantasia VARCHAR(250),
    Modalidade VARCHAR(250),
    Logradouro VARCHAR(250),
    Numero VARCHAR(50),
    Complemento VARCHAR(250),
    Bairro VARCHAR(250),
    Cidade VARCHAR(250),
    UF VARCHAR(5),
    CEP VARCHAR(25),
    DDD VARCHAR(4),
    Telefone VARCHAR(25),
    Fax VARCHAR(25),
    Endereco_eletronico VARCHAR(250),
    Representante VARCHAR(250),
    Cargo_Representante VARCHAR(150),
    Regiao_de_Comercializacao VARCHAR(100),
    Data_Registro_ANS DATE
);