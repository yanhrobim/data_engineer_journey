-- ============================================================================
-- ARQUIVO: 02_joins.sql
-- TEMA: JOINs (LEFT JOIN, INNER JOIN, RIGHT JOIN...)
-- ============================================================================

-- 01. Exercícios

-- 01-1. Crie um relatório com todos os pedidos realizados em 2017 e seus respectivos clientes.

--- (INNER JOIN)

SELECT 
	oc.customer_id, 
	oo.order_id, 
	TO_CHAR(oo.order_purchase_timestamp, 'YYYY-MM-DD') AS order_purchase_timestamp --- TO_CHAR utilizado como Bônus para visualizarmos a data em formato ANO-MÊS-DIA. 
FROM olist_customers oc
INNER JOIN olist_orders oo ON oc.customer_id = oo.customer_id
WHERE 
	EXTRACT(YEAR FROM oo.order_purchase_timestamp) = 2017
ORDER BY oo.order_purchase_timestamp;


-- 01-2. Crie um relatório que mostra o número de vendedores e clientes de cada cidade que possui vendedores.

--- (LEFT JOIN)

SELECT oc.customer_id, os.seller_id, oc.customer_city
FROM olist_customers oc
LEFT JOIN olist_sellers os ON oc.customer_city = os.seller_city


-- 01-3. Crie um relatório que mostra o número de vendedores e clientes de cada cidade que possui clientes.

--- (RIGHT JOIN)
SELECT os.seller_id, oc.customer_id, oc.customer_city
FROM olist_customers oc
RIGHT JOIN olist_sellers os ON oc.customer_city = os.seller_city

--- OBS: Aqui temos querys "semelhantes", mas que somente mudam a estrutura do SELECT e o tipo de JOIN.
--- Isso acontece pois o tipo de JOIN escolhido altera significadamente o resultado final da análise,
--- sendo assim, percebe-se que os exercícios tem objetivos semelhantes mas de formas diferentes
--- onde a solução de um, deve-se ter coluna X priorizada, na solução de outro coluna Y.
--- No caso de customer_id (Exercício 2) e seller_id (Exercício 3).

-- 01-4. Crie um relatório que mostra o número de vendedores e clientes
-- de cada cidade, incluindo todas as cidades, mesmo aquelas que possuem apenas vendedores, apenas clientes ou ambos.


-- 01-5. Crie um relatório que mostra a quantidade total de produtos vendidos por produto.
-- Mostre apenas produtos cuja quantidade total vendida seja menor que 200.

-- 01-6. Crie um relatório que mostra o total de pedidos por cliente a partir de 01/01/2018.
-- Mostre apenas clientes cujo total de pedidos seja maior que 15.