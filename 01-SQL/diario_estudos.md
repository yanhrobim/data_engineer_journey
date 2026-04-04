# 📒 Diário de Estudos - (SQL Básico)

## 📌 Objetivos da Semana

Aprender fundamentos e conceitos da **linguagem SQL** orientados a Engenharia e Análise de Dados, utilizando um Dataset real com um volume significativo de dados.
A fim de, simular um cenário próximo da realidade do cotidiano na área de dados, visando responder perguntas de negócio, praticar consultas, entender os dados e documentar todo o processo.

---

## 📅 Registro Diário

### **Dia 1 (24/03/2026)**

**O que foi estudado:**
* Criação do Database **PostgreSQL** utilizando o Render.
* Configuração da conexão do DBeaver ao Banco de Dados, e utilização da IDE (Ambiente de Desenvolvimento Integrado) como "Cliente" para execução de queries e gerenciamento do banco.
* Criação do Schema e Tabelas do Database (`olist_datasets`).
* Modelagem de tabelas 
    * Definição de **Primary Keys** e **Foreign Keys** entre as tabelas do dataset.
    * Identificação de chaves compostas (Ex: tabela `'olist_order_payments'`).
    * Aplicação de tipagem apropriada aos dados *(VARCHAR, TIMESTAMP, etc)*.

**Aprendizados do dia:**

* Conexão de uma Database IDE **(DBeaver)** e um Banco de Dados **(PostgreSQL)** .
* Criação de Tabelas com **PK** e **FK**.
* A importância de uma análise exploratória nos dados para obter um melhor entendimento, antes de aplicar métricas ou regras de negócio.
* Modelagem antes de carga.

---

### **Dia 2 (25/02/2026)**

**O que foi estudado:**
* Prática de comandos fundamentais. *(SELECT, FROM, WHERE)*
* Queries para a exploração dos dados, entender melhor sobre o volume, comportamento (velocidade, otimização).
* Aplicação de filtros básicos em diferentes cenários.
 


**Aprendizados do dia:**

* Subconjuntos da linguagem e aprofundamento em DQL *(Data Query Language)*.
* Comandos fundamentais da linguagem **SQL**.
* Construção de filtros.
* Uso de operadores em filtros.
    * `>`
    * `<`
    * `AND`

* **SQL** é uma linguagem declarativa, ou seja, eu digo o que eu quero e o banco foca em como obter o resultado, não na forma em que a query foi escrita.
    * O banco possuí um otimizador, que define a estrutura da sua query com o objetivo de deixa-la mais rápida.
* Boas práticas iniciais como a substituição do `SELECT *`, com o objetivo de obter análises mais otimizadas, boa perfomance, e somente colunas necessárias.

**Análises:**
* Quantos pedidos foram entregues: **96,478.** 
    * 96,478 pedidos entregues de 99,441 pedidos realizados.
* Todos os estados onde possuímos clientes:  **Total de 27 estados.**
* Total de Clientes: **99,441.**
    * Período de **2016-09-04** a **2018-10-17.**
* Descobrir quantos pedidos foram pagos com cartão de crédito, parcelando o pagamento em 2 vezes: **12,413.**

---

### Dia 3 (27/03/2026)

**O que foi estudado:**
* Potencializando filtros com operadores mais avançados. *(LIKE, BETWEEN, IN)*
* Aplicando lógica em exercícios/desafios no SQL, para a prática da linguagem.

**Aprendizados do dia:**
* Uso de operadores mais complexos em queries de filtro com WHERE. *(LIKE, BETWEEN, IN)*
* **LIKE** transforma a sua query menos otimizada, principalmente quando utilizamos `%` na busca.
* Pode ser utilizado o uso de Subquery no **IN**.

**Análises:**

* Filtro para obter SOMENTE clientes que moram em cidades que começam com: **"sao"**:
    * Total de Clientes: **20,988.**
    * Total de cidades que começam com São: **224.**
* Pedidos que foram pagos por cartão entre 200 a 400 reais:
    * **11,468** foram pagos por cartão (incluindo débito ou crédito) com valores entre: ***R$ 200 - R$400***.

---

### Dia 4 — 5 (30/03/26) e (31/03/26)

![Explicação JOINs em Imagem](/01-SQL/imagens_de_explicação/join_explanation.png)

**O que foi estudado:**
* JOINs. *(LEFT, INNER, RIGHT e FULL)*
* Primary Key e Foreign Key. (Chaves Primárias e Chaves Estrangeiras)
* Junções entre tabelas diferentes para cruzar dados na análise.
* Tipos de relação. *(1:1, 1:N e N:N)*
* Agrupamento e Filtragem:
    * **GROUP BY**
    * **HAVING**

**Aprendizados do dia:**


* **PK (Primary Key)**: Essa coluna individualiza cada linha da tabela, sem permitir valores duplicados. (Chave Primária)
* **FK (Foreign Key)** : É a chave primária de uma outra tabela, presente em uma tabela diferente, principalmente utilizada para a comunicação/ligação entre tabelas.
* **JOINs**: São principalmente utilizados para cruzar dados de tabelas diferentes que possuem colunas com alguma semelhança.
    * Nem sempre a junção entre colunas de tabelas diferentes ocorre por **PK** e **FK**. Por ventura pode ocorrer em colunas (tabelas diferentes) em que possuem o mesmo tipo e significado. Ex: Tabela A e Tabela B, ambas possuem coluna `Estado`.
* Junções em diferentes tipos de relação.

---

### Dia 6 — 7 (01/04/2026) e (02/04/2026)

![Window Function Explicação em Imagem](/01-SQL/imagens_de_explicação/window_function_explanation.webp)

**O que foi estudado:**
* Window Functions.
* Funções de Ranking. *(ROW_NUMBER( ), RANK( ), DENSE_RANK( ))*
* *LAG( ) e LEAD( )*.
* *NTILE( )*.

**Aprendizados do dia:**

* Window Functions permite fazer cálculos sem agrupar linhas. (Semelhante a um GROUP BY, porém sem juntar as linhas)
* Window Functions Syntax Components:
    * ```sql 
        window_function_name(arg1, arg2, ...) OVER (
        [PARTITION BY partition_expression, ...]
        [ORDER BY sort_expression [ASC | DESC], ...]
        )
        ```

* Rakeando dados e análises de com ranking:

    * **ROW_NUMBER( ):**
        * Sempre irá gerar uma coluna sequencial em formato rank.
        * Não considera empate.
        * Pode utilizar critério implícitos para desempate.

    * **RANK( ):**
        * Valores iguais recebem a mesma posição.
        * Critério de desempate: Se dois valores são o primeiro lugar, o próximo valor recebe terceiro lugar como colocação.

    * **DENSE_RANK( ):**
        * Semelhante ao **RANK( )**. Porém não pula colocações mesmo em caso de empates.

* Comparação de dados anteriores e posteriores com **LAG( )** e **LEAD( )**.
* Divisão do conjunto de dados com **NTILE( )**.

---