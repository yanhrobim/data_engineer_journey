# 🔎 Prática Intensiva: Análises de Negócio (Olist E-commerce)

<img src="https://img.shields.io/badge/Status-Concluído-green">

## 📝 Objetivo

Prática intensiva de **SQL** construindo relatórios mais avançados de negócio utilizando o dataset da Olist.

O foco é simular um cenário com problemas reais no cotiano de dados, apresentando soluções através do **SQL**, analisando informações como receita, comportamento de cliente, perfomance de produtos e análise por áreas geográficas.

---

## 📊 Relatórios


### 🧩 1. Receita total em um período

- **Qual foi o total de receita da empresa em um ano específico (ex: 2017)?**

```sql
SELECT 
		TO_CHAR(oo.order_purchase_timestamp, 'YYYY') AS ano,
		SUM(oi.price * oi.order_item_id) AS receita_gerada
FROM olist_order_items oi
INNER JOIN olist_orders oo ON oo.order_id = oi.order_id
GROUP BY ano
ORDER BY ano;
```

---

### 🧩 2. Crescimento mensal + YTD

**Faça uma análise de receita mensal ao longo do tempo:**

- **Receita por mês**

```sql
SELECT 
		DATE_TRUNC('month', oo.order_purchase_timestamp) AS mes,
		SUM(oi.price * oi.order_item_id) AS receita_gerada_mes
FROM olist_order_items oi
INNER JOIN olist_orders oo ON oo.order_id = oi.order_id
GROUP BY mes
ORDER BY mes ASC;
```

- **Diferença em relação ao mês anterior**

```sql
SELECT 
		DATE_TRUNC('month', oo.order_purchase_timestamp) AS mes,
		SUM(oi.price * oi.order_item_id) AS receita_gerada_mes,
		LAG(SUM(oi.price * oi.order_item_id)) OVER (ORDER BY DATE_TRUNC('month', oo.order_purchase_timestamp) ASC) AS mes_anterior
FROM olist_order_items oi
INNER JOIN olist_orders oo ON oo.order_id = oi.order_id
GROUP BY mes;
```

- **Percentual de crescimento mensal**

```sql
SELECT 
		DATE_TRUNC('month', oo.order_purchase_timestamp) AS mes,
		SUM(oi.price * oi.order_item_id) AS receita_gerada_mes,
		LAG(SUM(oi.price * oi.order_item_id)) OVER (ORDER BY DATE_TRUNC('month', oo.order_purchase_timestamp) ASC) AS mes_anterior,
	 	ROUND(((SUM(oi.price * oi.order_item_id) - LAG(SUM(oi.price * oi.order_item_id)) OVER (ORDER BY DATE_TRUNC('month', oo.order_purchase_timestamp) ASC))::NUMERIC / SUM(oi.price * oi.order_item_id)) * 100, 2) AS porcentagem_crescimento
FROM olist_order_items oi
INNER JOIN olist_orders oo ON oo.order_id = oi.order_id
GROUP BY mes;
```

- **Receita acumulada no ano (YTD)**

```sql
WITH receita_ano_2016 AS (
	SELECT 
			TO_CHAR(DATE_TRUNC('DAY', oo.order_purchase_timestamp), 'YYYY-MM-DD') AS ano_mes_dia,
			SUM(oi.price * oi.order_item_id) AS receita_gerada_dia		-- Somando todos os preços que foram gerados naquela data.
	FROM olist_order_items oi
	INNER JOIN olist_orders oo ON oi.order_id = oo.order_id
	WHERE EXTRACT(YEAR FROM oo.order_purchase_timestamp) = 2016	-- Especificando o ano dos dados.
	GROUP BY ano_mes_dia
	ORDER BY ano_mes_dia
),
receita_acumulada_ano_2016 AS (
SELECT 
		ano_mes_dia,
		receita_gerada_dia,
		SUM(receita_gerada_dia) OVER (ORDER BY ano_mes_dia) AS receita_acumulada_ano	
		-- Somando de forma sequencial todos os dados da coluna 'receita_gerada_dia'.
	    -- A cada nova linha, é feito uma som com o último valor presente na coluna 'receita_acumulada_ano'.
FROM receita_ano_2016
),
receita_ano_2017 AS (
	SELECT 
			TO_CHAR(DATE_TRUNC('DAY', oo.order_purchase_timestamp), 'YYYY-MM-DD') AS ano_mes_dia,
			SUM(oi.price * oi.order_item_id) AS receita_gerada_dia
	FROM olist_order_items oi
	INNER JOIN olist_orders oo ON oi.order_id = oo.order_id
	WHERE EXTRACT(YEAR FROM oo.order_purchase_timestamp) = 2017
	GROUP BY ano_mes_dia
	ORDER BY ano_mes_dia
),
receita_acumulada_ano_2017 AS (
SELECT 
		ano_mes_dia,
		receita_gerada_dia,
		SUM(receita_gerada_dia) OVER (ORDER BY ano_mes_dia) AS receita_acumulada_ano
FROM receita_ano_2017
),
receita_ano_2018 AS (
	SELECT 
			TO_CHAR(DATE_TRUNC('DAY', oo.order_purchase_timestamp), 'YYYY-MM-DD') AS ano_mes_dia,
			SUM(oi.price * oi.order_item_id) AS receita_gerada_dia
	FROM olist_order_items oi
	INNER JOIN olist_orders oo ON oi.order_id = oo.order_id
	WHERE EXTRACT(YEAR FROM oo.order_purchase_timestamp) = 2018
	GROUP BY ano_mes_dia
	ORDER BY ano_mes_dia
),
receita_acumulada_ano_2018 AS (
SELECT 
		ano_mes_dia,
		receita_gerada_dia,
		SUM(receita_gerada_dia) OVER (ORDER BY ano_mes_dia) AS receita_acumulada_ano
FROM receita_ano_2018
)
SELECT * FROM  receita_acumulada_ano_2016
UNION ALL										
SELECT * FROM receita_acumulada_ano_2017	-- Unindo as queries de forma estruturada (Com UNION ALL), gerando uma organização de zerar o acumulado a cada novo ano.
UNION ALL
SELECT * FROM receita_acumulada_ano_2018;

-- Escolha de estruturar a query com CTEs, visando que a nossa última tabela retornasse a receita acumulada de cada ano, reiniciando a contagem a cada virada de ano.
```

---

##  **👥 Segmentação de Clientes**

### 🧩 3. Receita total por cliente

- **Qual é o valor total que cada cliente já pagou na plataforma?**

```sql
SELECT 
		oc.customer_unique_id AS cliente,
		SUM(oi.price + oi.freight_value) AS valor_total_gasto
		-- Somando preços e fretes de cada pedido feito por cliente.
FROM olist_customers oc 
LEFT JOIN olist_orders oo ON oc.customer_id = oo.customer_id -- LEFT JOIN para unir clientes e seus pedidos.
INNER JOIN olist_order_items oi ON oo.order_id = oi.order_id
-- INNER JOIN para unir pedidos dos clientes e suas informações. (Como Preço, Frete, Produto, etc.)
GROUP BY cliente
```

---

### 🧩 4. Segmentação por valor (RFM simplificado)

- **Separe os clientes em 5 grupos com base no valor total gasto (do maior para o menor).**

```sql
WITH valor_total_gasto_cliente AS (
	SELECT 
		oc.customer_unique_id AS cliente,
		SUM(oi.price + oi.freight_value) AS valor_total_gasto
		-- Somando preços e fretes de cada pedido feito por cliente.
	FROM olist_customers oc 
	LEFT JOIN olist_orders oo ON oc.customer_id = oo.customer_id -- LEFT JOIN para unir clientes e seus pedidos.
	INNER JOIN olist_order_items oi ON oo.order_id = oi.order_id -- INNER JOIN para unir pedidos dos clientes e suas informações. (Como Preço, Frete, Produto, etc.)
	GROUP BY cliente
),
grupo_por_valor_total_gasto AS (
	SELECT 	*,
			NTILE(5) OVER (ORDER BY valor_total_gasto DESC) AS group_number -- Dividindo clientes em grupos pelo valor total que ele gastou na plataforma. 
	FROM valor_total_gasto_cliente
)
SELECT * FROM grupo_por_valor_total_gasto;
```

---

### 🧩 5. Público para marketing

- **Crie um relatório contendo apenas os clientes que pertencem - aos grupos 3, 4 e 5 (clientes de menor valor), para ações de marketing.**

```sql
WITH valor_total_gasto_cliente AS (
	SELECT 
		oc.customer_unique_id AS cliente,
		SUM(oi.price + oi.freight_value) AS valor_total_gasto
		-- Somando preços e fretes de cada pedido feito por cliente.
	FROM olist_customers oc 
	LEFT JOIN olist_orders oo ON oc.customer_id = oo.customer_id -- LEFT JOIN para unir clientes e seus pedidos.
	INNER JOIN olist_order_items oi ON oo.order_id = oi.order_id
	-- INNER JOIN para unir pedidos dos clientes e suas informações. (Como Preço, Frete, Produto, etc.)
	GROUP BY cliente
),
grupos_por_valor_gasto AS (
	SELECT 
			*,
			NTILE(5) OVER (ORDER BY valor_total_gasto DESC) AS group_number
	FROM valor_total_gasto_cliente
),
clientes_menor_valor AS (
	SELECT * 
	FROM grupos_por_valor_gasto
	WHERE group_number > 2 -- Filtragem para apenas trazer clientes que estão nos grupos 3, 4, 5. (Considerados clientes de menor valor)
)
SELECT * FROM clientes_menor_valor;
```

---

## 🛍️ Performance de Produtos

### 🧩 6. Top 10 produtos

- **Identifique os 10 produtos que mais geraram receita na plataforma.**

```sql
SELECT	
		DISTINCT(oi.product_id) AS produto,
		SUM(oi.price * oi.order_item_id) OVER (PARTITION BY oi.product_id) AS produto_receita_gerada
FROM olist_order_items oi
ORDER BY produto_receita_gerada DESC
LIMIT 10;
```

---

## 🌍 Análise Geográfica

### 🧩 7. Clientes de alta receita por localização

- **Quais clientes de um determinado estado (ex: SP) já gastaram mais de 1000 em compras?**

```sql
WITH valor_total_gasto_cliente AS (
SELECT 	DISTINCT
		oc.customer_state AS estado,
		oc.customer_unique_id AS cliente,
		SUM(oi.price + oi.freight_value) OVER (PARTITION BY oc.customer_unique_id) valor_total_gasto
		-- Somando preços e fretes de cada pedido feito por cliente.
FROM olist_customers oc 
LEFT JOIN olist_orders oo ON oc.customer_id = oo.customer_id -- LEFT JOIN para unir clientes e seus pedidos.
INNER JOIN olist_order_items oi ON oo.order_id = oi.order_id -- INNER JOIN para unir pedidos dos clientes e suas informações. (Como Preço, Frete, Produto, etc.)
),
valor_total_mais_1000_por_estado AS (
SELECT *
FROM valor_total_gasto_cliente
WHERE valor_total_gasto > 1000
ORDER BY estado DESC
)
SELECT * FROM valor_total_mais_1000_por_estado
```

---