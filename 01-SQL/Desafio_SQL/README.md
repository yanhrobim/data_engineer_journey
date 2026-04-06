# 🔎 Prática Intensiva: Análises de Negócio (Olist E-commerce)

<img src="https://img.shields.io/badge/Status-Em%20Andamento-yellow">

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
		SUM(oi.price) AS receita_gerada
FROM olist_order_items oi
INNER JOIN olist_orders oo ON oo.order_id = oi.order_id
GROUP BY ano
ORDER BY ano
```

---

### 🧩 2. Crescimento mensal + YTD

**Faça uma análise de receita mensal ao longo do tempo:**

- **Receita por mês**
```sql
SELECT 
		DATE_TRUNC('month', oo.order_purchase_timestamp) AS mês,
		SUM(oi.price) AS receita_gerada_mês
FROM olist_order_items oi
INNER JOIN olist_orders oo ON oo.order_id = oi.order_id
GROUP BY mês
ORDER BY mês ASC
```

- **Diferença em relação ao mês anterior**

```sql
SELECT 
		DATE_TRUNC('month', oo.order_purchase_timestamp) AS mês,
		SUM(oi.price) AS receita_gerada_mês,
		LAG(SUM(oi.price)) OVER (ORDER BY DATE_TRUNC('month', oo.order_purchase_timestamp) ASC) AS mês_anterior
FROM olist_order_items oi
INNER JOIN olist_orders oo ON oo.order_id = oi.order_id
GROUP BY mês
```

- **Percentual de crescimento mensal**

```sql
SELECT 
		DATE_TRUNC('month', oo.order_purchase_timestamp) AS mês,
		SUM(oi.price) AS receita_gerada_mês,
		LAG(SUM(oi.price)) OVER (ORDER BY DATE_TRUNC('month', oo.order_purchase_timestamp) ASC) AS mês_anterior,
	 	ROUND(((SUM(oi.price) - LAG(SUM(oi.price)) OVER (ORDER BY DATE_TRUNC('month', oo.order_purchase_timestamp) ASC))::NUMERIC / SUM(oi.price)) * 100, 2) AS porcentagem_crescimento
FROM olist_order_items oi
INNER JOIN olist_orders oo ON oo.order_id = oi.order_id
GROUP BY mês
```

- **Receita acumulada no ano (YTD)**

---

##  **👥 Segmentação de Clientes**

### 🧩 3. Receita total por cliente

**Qual é o valor total que cada cliente já pagou na plataforma?**

---

### 🧩 4. Segmentação por valor (RFM simplificado)

- **Separe os clientes em 5 grupos com base no valor total gasto (do maior para o menor).**

---

### 🧩 5. Público para marketing

- **Crie um relatório contendo apenas os clientes que pertencem -- aos grupos 3, 4 e 5 (clientes de menor valor), para ações de marketing.**

---

## 🛍️ Performance de Produtos

### 🧩 6. Top 10 produtos Performance de Produtos

- **Identifique os 10 produtos que mais geraram receita na plataforma.**

## 🌍 Análise Geográfica

### 🧩 7. Clientes de alta receita por localização

- **Quais clientes de um determinado estado (ex: SP) já gastaram mais de 1000 em compras?**
