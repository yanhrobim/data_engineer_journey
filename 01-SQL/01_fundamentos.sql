-- ============================================================================
-- ARQUIVO: 01_fundamentos.sql (Aula 01)
-- TEMA: Comandos Básicos e Filtros (SELECT, WHERE, DISTINCT)
-- ============================================================================

-- 01. COMANDOS BÁSICOS (SELECT, DISTINCT, WHERE)

-- Selecionar todas as linhas do Dataset. 
SELECT * FROM olist_customers oc 

-- Contar o número total de linhas do Dataset.
SELECT COUNT(*) FROM olist_customers oc
	-- Número Total de Linhas: 99441


-- Listar com DISTINCT para descobrirmos todos os estados (de forma única) onde temos clientes.
SELECT DISTINCT(oc.customer_state)
FROM olist_customers oc
    -- (RS; SC; DF; MG; RN; SP; GO; AM; PA; PB; PE; AP; ES; TO; MT; RR; PI; PR; CE; BA; AC; RJ; MA; AL; RO; SE; MS)


-- 02. FILTROS (WHERE)

-- Fitro com WHERE para obtermos somente linhas onde 'order_status' tem o valor de 'delivered' (Somente pedidos que foram entregues).   
SELECT * FROM olist_orders oo
WHERE oo.order_status = 'delivered'
    -- Se adicionar COUNT() a query, temos um número total de linhas: 96478.

-- 03. FILTROS + OPERADORES (POTENCIALIZANDO UM FILTRO)

-- Fitro para obtermos dados onde pedidos que foram pagos com cartão de crédito e parcelado em duas vezes.
-- Fitragem com WHERE + Uso de AND para adicionar mais um filtro nos dados da tabela.
SELECT oop.order_id, oop.payment_type, oop.payment_installments, oop.payment_value  
FROM olist_order_payments oop
WHERE oop.payment_type = 'credit_card' AND oop.payment_installments = 2



