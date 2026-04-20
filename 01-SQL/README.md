# 🔍 Extração de KPIs de E-commerce - Dataset Olist


## 📌 Introdução ao Projeto
Prática intensiva de **SQL** construindo relatórios mais avançados de negócio utilizando um dataset de E-commerce.

O foco é voltado a um cenário simulando perguntas reais de negócio como: qual foi a receita mensal? Quais clientes geram mais valor? Quais produtos lideram em receita? - Apresentando soluções através do **SQL**, analisando informações como receita, comportamento de cliente, performance de produtos e análise por áreas geográficas.

O Dataset possuí 7 tabelas:
- **Tabela Clientes:** [`olist_customers_dataset.csv`](./data/olist_customers_dataset.csv)

- **Tabela Pedidos:** [`olist_orders_dataset.csv`](./data/olist_orders_dataset.csv)

- **Tabela Informações de Pagamentos:** [`olist_order_payments_dataset.csv`](./data/olist_order_payments_dataset.csv)

- **Tabela Detalhes de Cada Pedido:** [`olist_order_items_dataset.csv`](./data/olist_order_items_dataset.csv)

- **Tabela Avaliação de Cada Pedido:** [`olist_order_reviews_dataset.csv`](./data/olist_order_reviews_dataset.csv)

- **Tabela Produtos:** [`olist_products_dataset.csv`](./data/olist_products_dataset.csv)

- **Tabela Vendedores (Sellers):** [`olist_sellers_dataset.csv`](./data/olist_sellers_dataset.csv)

## 📁 Estrutura do Repositório

```text
.
└── 01-SQL
  ├── data/
  | ├── olist_customers_dataset.csv     # Dados dos clientes.
  | ├── olist_order_items_dataset.csv   # Dados sobre itens e detalhes de cada pedido.
  | ├── olist_order_payments_dataset.csv    # Dados sobre informações de pagamentos de cada pedido.
  | ├── olist_order_reviews_dataset.csv     # Dados sobre a avaliação de cada pedido.
  | ├── olist_orders_dataset.csv        # Dados dos pedidos.
  | ├── olist_products_dataset.csv      # Dados dos produtos.
  | └── olist_sellers_dataset.csv    # Dados dos vendedores.
  |
  ├── estudos/
  | ├── imagens_de_explicação   # Pasta com imagens que explicam conceitos.
  | ├── 01_fundamentos.sql  # Aprendendo Fundamentos da Linguagem SQL.
  | ├── 02_joins.sql    # Práticas para aprender e entender sobre JOINs.
  | └── 03_window_functions.sql  # Exercícios para aprender e entender sobre Window Functions.
  |
  ├── KPIs/
  | ├── report -- Certos Resultados das Consultas (Queries) do Projeto.
  | | ├── cliente_alto_valor_por_estado.csv
  | | ├── crescimento_mensal_ytd.csv    # Clientes de Alto Valor por Estado.
  | | ├── top10_products.csv    # Top 10 produtos em vendas.
  | | ├── total_gasto_cliente_group.csv # RFM simplificado de acordo com o total gasto do cliente.
  | | └── total_receita_gerada_ano.csv  # Receital total gerada a cada ano.
  | └── README.md             #  Perguntas de neǵocio e suas devidas queries de solução, em formato documentação.
  |
  ├── diario_estudos.md        # Registro diário da evolução do projeto
  └── README.md                # Documentação geral do projeto

```

## 📝 Objetivos do Projeto
- Aplicar os fundamentos e ensinamentos aprendidos em **SQL**, com um projeto para prática intensiva.
- Responder perguntas de negócio sobre receita, comportamento do cliente, perfomace de produtos e distribuição geográfica.
- Documentação orientada a um projeto de portfólio no GitHub.
- Aprimorar lógica com boas práticas, conceitos e fundamentos da linguagem.

---

## 🧩 Perguntas de Negócio

Em um cenário real, um dos papéis de quem trabalha com dados é transformar perguntas de negócio em respostas concretas que apoiam decisões estratégicas. Portanto, o projeto foi estruturado em 4 frentes de análise:

- **Receita:** Como o faturamento evolui ao longo do tempo?
- **Segmentação de Clientes:** Quais são os clientes mais valiosos e/ menos valiosos, e como segmenta-los?
- **Produtos:** Quais produtos concentram a maior parte da receita?
- **Geografia:** Onde se localiza os clientes de maior valor?

Todas as respostas foram obtidas exclusivamente com SQL. As queries completas estão disponíveis em [KPIs](./KPIs/README.md), juntamente sendo possível encontrar certos relatórios com as queries desenvolvidas do projeto em *`report`* .

### 📈 Relatórios de Receita
- **KPI I - Receita Total Por Ano**
    - Permite visualizar o volume total de receita gerada em cada ano, sendo o ponto de partida para qualquer análise financeira ou identificar anos de crescimento ou queda.
- **KPI II - Crescimento Mensal + YTD**
    - Analisa a evolução da receita mês a mês, quebrando em três perspectivas: mensal, oscilação em relação ao mês anterior e acumulado anual (YTD). Identifica se há crescimento, estagnação ou queda ao longo do tempo.

---

### 👥 Segmentação de Clientes
- **KPI III - Receita Total por Cliente**
    - Identifica o quanto cada cliente gastou dentro da plataforma. KPI base para estratégias de retenção, focar em relacionamentos comerciais ou separar clientes de alto/menor valor.
- **KPI IV - Segmentação por valor (RFM simplificado)**
    - Divide os clientes em 5 grupos pelo valor total gasto, baseado na metodologia RFM, segmentando clientes dos mais lucrativos aos menos lucrativos onde cada grupo pode receber uma estratégia de marketing diferente.
- **KPI V - Público para marketing**
    - Extrai diretamente clientes dos grupos 3, 4, 5, entregando clientes de menor valor que podem ser convertidos com ações de reativação ou campanhas de marketing.

---

### 🛍️ Performance de Produtos

- **KPI VI — Top 10 produtos**
    - Um ranking simples com grande impacto, rankeando os 10 produtos que mais geraram receita, informação essencial para decisões de estoque, precificação e marketing, além de indicar onde o negócio concentra sua força de vendas.

---

### 🌍 Análise Geográfica

- **KPI VII - Clientes de alta receita por localização**
    - Filtra clientes acima de R$1.000 gastos por estado, podendo focar em esforços onde os clientes de maior valor estão concentrados ou identificar clientes de alto valor em estados específicos. 

---

## 🛠️ Stack

| Categoria | Ferramentas / Linguagens |
| :--- | :--- |
| **Linguagens de Programação** | SQL |
| **Bancos de Dados** | PostgreSQL |
| **IDEs** | DBeaver |

---

## 📋 Principais Aprendizados
- Escolha correta do **JOIN** para evitar duplicidade nos dados, e entendimento dos tipos de relação entre as tabelas para aplicar métricas corretamente. (1:1; 1:N)
- Identificar cenários onde se é necessário uma **Window Function** ou **GROUP BY**.
- Uso de **CTEs** tanto para organização e estruturação da query, quanto para construir métricas de forma incremental.
- Organização e documentação de um projeto de dados em **SQL** para portfólio.
- Aprofundamento em **Window Function** entendendo melhor partições com **PARTITION BY** e ordenações com **ORDER BY**.

---

## 🚀 Próximos Passos

Como próxima etapa da jornada, o objetivo é **Python aplicado à Engenharia de Dados**, com foco em desenvolver pipelines com etapas de processamento, limpeza de dados e ingestão para visualização. E não só, mas também documentar todo este processo e aplicar os ensinamentos aprendidos em um projeto intensivo para prática.

---

## 👨🏻‍💻 Autor

**👤 Projeto Desenvolvido Por: Yan Robim**

 🌐 [Portfólio/GitHub](https://github.com/yanhrobim)   ✉️ yanrobim@gmail.com





