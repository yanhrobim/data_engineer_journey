-- ============================================================================
-- ARQUIVO: 03_window_functions.sql
-- TEMA: Window Functions
-- ============================================================================

--- 01 - Window Function

SELECT 
		oc.customer_unique_id,
		COUNT(oo.order_id) OVER (PARTITION BY oc.customer_unique_id) AS total_pedidos,
		SUM(oi.price) OVER (PARTITION BY oc.customer_unique_id) quanto_gastou_total,
		SUM(oi.freight_value) OVER (PARTITION BY oc.customer_unique_id) total_gasto_frete
FROM olist_customers oc
LEFT JOIN olist_orders oo ON oc.customer_id = oo.customer_id 
INNER JOIN olist_order_items oi ON oo.order_id = oi.order_id


-- 02 - Exercícios

--- 02-1. Faça a classificação dos produtos mais vendidos utilizando RANK(), DENSE_RANK() e ROW_NUMBER().
--- Considere a quantidade total vendida por produto.

SELECT 
		op.product_id,
		SUM(oi.order_item_id * oi.price) AS faturamento,
		ROW_NUMBER() OVER (ORDER BY SUM(oi.order_item_id * oi.price) DESC) AS rank_rn,
		RANK() OVER (ORDER BY SUM(oi.order_item_id * oi.price) DESC) AS rank_rk,
		DENSE_RANK() OVER (ORDER BY SUM(oi.order_item_id * oi.price) DESC) AS rank_dr
FROM olist_products op
INNER JOIN olist_order_items oi  ON op.product_id = oi.product_id
GROUP BY op.product_id


-- Qual função Window Function seria melhor na nossa situação? Neste Dataset é uma pergunta com a resposta de: DEPENDE.
-- Depende de como as regras de negócio iriam aceitar empates, e até mesmo a quantidade de classificação escolhida para decisões de negócio.
-- Até certa classificação não tem empates em nenhuma Window Function (Até o Top 262).

--- 02-2. Liste os vendedores dividindo-os em 3 grupos utilizando NTILE(3).
--- (quantidade de linhas igual ao total de vendedores)

SELECT 
		os.seller_id, 
		os.seller_city, 
		os.seller_state, 
	   	NTILE(3) OVER (ORDER BY os.seller_state DESC) AS group_number
FROM olist_sellers os


--- 02-3. Ordene os custos de frete pagos pelos clientes de acordo com
--- a data do pedido, mostrando também o custo anterior e o custo posterior
--- utilizando LAG() e LEAD().
--- (quantidade de linhas igual ao total de pedidos com frete)
