-- ============================================================================
-- ARQUIVO: 01_fundamentos.sql (Aula 01)
-- TEMA: Comandos Básicos e Filtros (SELECT, WHERE, DISTINCT)
-- ============================================================================

-- 01. COMANDOS BÁSICOS (SELECT, DISTINCT, WHERE)

-- Selecionar todas as linhas do Dataset. 
SELECT * FROM olist_customers oc;

-- Contar o número total de linhas do Dataset.
SELECT COUNT(*) FROM olist_customers oc;
	-- Número Total de Linhas: 99441


-- Listar com DISTINCT para descobrirmos todos os estados (de forma única) onde temos clientes.
SELECT DISTINCT(oc.customer_state)
FROM olist_customers oc;
    -- (RS; SC; DF; MG; RN; SP; GO; AM; PA; PB; PE; AP; ES; TO; MT; RR; PI; PR; CE; BA; AC; RJ; MA; AL; RO; SE; MS)


-- 02. FILTROS (WHERE)

-- Fitro com WHERE para obtermos somente linhas onde 'order_status' tem o valor de 'delivered' (Somente pedidos que foram entregues).   
SELECT * FROM olist_orders oo
WHERE oo.order_status = 'delivered';
    -- Se adicionar COUNT() a query, temos um número total de linhas: 96478.

-- 03. WHERE + OPERADORES (POTENCIALIZANDO UM FILTRO)

-- Fitro para obtermos dados onde pedidos que foram pagos com cartão de crédito e parcelado em duas vezes.
-- Fitragem com WHERE + Uso de AND para adicionar mais um filtro nos dados da tabela.
SELECT oop.order_id, oop.payment_type, oop.payment_installments, oop.payment_value  
FROM olist_order_payments oop
WHERE oop.payment_type = 'credit_card' AND oop.payment_installments = 2;

-- 04. LIKE

--  Filtro para obter SOMENTE clientes que moram em cidades que começam com: "sao". ('sao paulo'; 'sao goncalo'; etc..)
-- LIKE percorre string em busca do valor passado ('sao', no começo), nos dados da coluna 'customer_city'.
SELECT oc.customer_id, oc.customer_city, oc.customer_state
FROM olist_customers oc 
WHERE oc.customer_city LIKE 'sao%';

-- 04-1. LOWER
-- Exemplo com o uso de LOWER (Transforma todos os dados (string) em minúsculo, amplamente usado para encontrar valores que possuem letras maiúsculas em alguma parte da string).
SELECT oc.customer_id, oc.customer_city, oc.customer_state
FROM olist_customers oc 
WHERE LOWER(oc.customer_city) LIKE 'sao%';

-- 04-2. UPPER
-- Exemplo com o uso de UPPER. (Transforma todos os dados (string) em maiúsculo, amplamente usado para encontrar valores que possuem letras minúculas em alguma parte da string).
SELECT oc.customer_id, oc.customer_city, oc.customer_state
FROM olist_customers oc 
WHERE LOWER(oc.customer_city) LIKE 'sao%';

-- Filtro com SIMILAR TO (COMANDO DO POSTGRESQL), tendo objetivo de encontrar pedidos que contém comentários negativos. (Pedidos que contém 'palavras chaves' de reclamações)
-- Percorre os valores da coluna 'review_comment_message' (string), para encontrar os valores passados. 
SELECT *
FROM olist_order_reviews orr
WHERE LOWER(orr.review_comment_message) SIMILAR TO '%não% | %ruim%';

-- 05. IN
SELECT *
FROM olist_customers oc
WHERE oc.customer_state IN ('SP', 'RJ', 'MG');

-- NOT IN 
SELECT *
FROM olist_customers oc
WHERE oc.customer_state NOT IN ('SP', 'RJ', 'MG');

-- 06 BETWEEN

SELECT *
FROM olist_order_payments op
WHERE op.payment_value BETWEEN 1000 AND 2000. 

-- BETWEEN + LIKE, para encontrar pedidos que foram pagos por cartão entre R$ 200 á R$ 400.
SELECT *
FROM olist_order_payments op
WHERE op.payment_type LIKE '%card%' AND op.payment_value BETWEEN 200 AND 400;








