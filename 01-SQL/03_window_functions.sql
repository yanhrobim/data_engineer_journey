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