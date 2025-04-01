-- in the last quarter
CREATE VIEW view_relatorio_cadop_demonstracoes_contabeis_ultimo_trimestre AS
SELECT 
    rc.Registro_ANS, 
	rc.CNPJ, 
	rc.Razao_Social,
	TO_NUMBER(REPLACE(dc.vl_saldo_inicial, ',', '.'), '9999999999999.99') AS vl_saldo_inicial,
    TO_NUMBER(REPLACE(dc.vl_saldo_final, ',', '.'), '9999999999999.99') AS vl_saldo_final
FROM relatorio_cadop rc
JOIN demonstracoes_contabeis dc ON TRIM(rc.Registro_ANS) = TRIM(dc.reg_ans) 
WHERE dc.descricao LIKE '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE%' AND 
((dc.dt = '2023-10-01') OR (dc.dt = '2024-10-01'));

SELECT 
	Registro_ANS, 
	CNPJ, 
	Razao_Social, 
	ABS(vl_saldo_final-vl_saldo_inicial) AS deficit 
FROM view_relatorio_cadop_demonstracoes_contabeis_ultimo_trimestre
ORDER BY deficit

-- in the last year
CREATE VIEW view_relatorio_cadop_demonstracoes_contabeis_ultimo_ano AS
SELECT 
    rc.Registro_ANS, 
	rc.CNPJ, 
	rc.Razao_Social,
	TO_NUMBER(REPLACE(dc.vl_saldo_inicial, ',', '.'), '9999999999999.99') AS vl_saldo_inicial,
    TO_NUMBER(REPLACE(dc.vl_saldo_final, ',', '.'), '9999999999999.99') AS vl_saldo_final
FROM relatorio_cadop rc
JOIN demonstracoes_contabeis dc ON TRIM(rc.Registro_ANS) = TRIM(dc.reg_ans) 
WHERE dc.descricao LIKE '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE%' AND 
(dc.dt BETWEEN '2024-01-01' AND '2024-10-01');


SELECT 
	Registro_ANS, 
	CNPJ, 
	Razao_Social, 
	ABS(vl_saldo_final-vl_saldo_inicial) AS deficit 
FROM view_relatorio_cadop_demonstracoes_contabeis_ultimo_ano
ORDER BY deficit
