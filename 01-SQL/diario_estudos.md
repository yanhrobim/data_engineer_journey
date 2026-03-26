# 📒 Diário de Estudos - (SQL Básico)

## 📌 Objetivos da Semana

Aprender fundamentos e conceitos da **linguagem SQL** orientados a Engenharia e Análise de Dados, utilizando um Dataset real com um volume significativo de dados.
Afim de, simular um cenário próximo a realidade do cotidiano na área de dados, visando responder perguntas de negócio, praticar consultas, entender os dados e documentar todo o processo.

---

## 📅 Registro Diário

### **Dia 1 (24/03/2026)**

* Criação do Database **PostgreSQL** utilizando o Render.
* Configuração da conexão do DBeaver ao Database, e utilização da IDE (Ambiente de Desenvolvimento Integrado) como "Cliente" para execução de queries e gerenciamento do banco.
* Criação do Schema e Tabelas do Database (`olist_datasets`).
* Modelagem de tabelas 
    * Definição de **Primary Keys** e **Foreign Keys** entre as tabelas do dataset.
    * Identificação de chaves compostas (Ex: tabela `'olist_order_payments'`).
    * Aplicação de tipagem apropriada aos dados (VARCHAR, TIMESTAMP, etc).

**Aprendizados do dia:**

* Conexão de uma Database IDE **(DBeaver)** e um Banco de Dados **(PostgreSQL)** .
* Criação de Tabelas com PK e FK.
* A importância de uma análise expoloratória nos dados para obter um melhor entedimento, antes de aplicar métricas ou regras de negócio.
* Modelagem antes de carga.

---

### **Dia 2 (25/02/2026)**

* Prática de comandos fundamentais. (SELECT, FROM, WHERE)
* Queries para a exploração dos dados, entender melhor sobre o volume, comportamento (velocidade, otimização).
* Aplicagem de filtros básicos em diferentes cenários.
 


**Aprendizados do dia:**

* Subconjuntos da linguagem e aprofundamento em DQL *(Data Query Language)*.
* Comandos fundamentais da linguagem **SQL** (SELECT, FROM, WHERE).
* Construção de filtros.
* Uso de operadores para potencializar filtros.
    * `>`
    * `<`
    * `AND`

* **SQL** é uma linguagem declarativa, onde o banco possuí um otimizador, que define a estrutura da sua query com o objetivo de deixa-la mais rápida.
* Boas práticas iniciais como a substituição do `SELECT *`, com o objetivo de obter análises mais otimizadas, boa perfomace, e somente buscar dados necessários.

**Análises Iniciais:**
* Quantos pedidos foram entregues: **96,478** 
    * 96,478 pedidos entregues de 99,441 pedidos realizado.
* Todos os estados onde possuímos clientes:  **Total de 27 estados.**
* Total de Clientes: **99,441**
    * Período de **2016-09-04** a **2018-10-17**
* Descobrir quantos pedidos foram pagos com cartão de crédito, parcelando o pagamento em 2 vezes: **12,413**



