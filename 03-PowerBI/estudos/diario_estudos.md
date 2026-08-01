# 📒 Diário de Estudos - (Power BI)

## 📌 Objetivos dos Estudos

Aprender fundamentos e conceitos da ferramenta **Power BI**, incluindo Power Query, DAX e modelagem de dados, através do curso da **Data Science Academy**.
Com o objetivo de aprender sobre a ferramenta, consolidar conhecimento e posteriormente aplicá-la em um projeto real de portfólio, unindo Engenharia de Dados e Análise de Dados.

---

## 🛑 Antes de Power BI

### O que é Big Data?

**Big Data** é um conjunto muito grande de dados e mais complexo. São dados que possuem uma maior variedade de tipo, dados que chegam em volumes crescentes com mais velocidade, e que não param de crescer, frequentemente definidos pelos **5Vs (Volume, Velocidade, Variedade, Veracidade e Valor)**. Estes conjuntos de dados são tão volumosos que um software tradicional / computador normal não conseguem entende-los sozinhos. Porém, com um uso de ferramentas especiais conseguimos utiliza-los para descobrirmos tendências, resolução de problemas de negócio.

### O que é Business Intelligence?

**Business Intelligence (BI)** é um conjunto de técnicas e ferramentas utilizadas para transformar os dados em informações úteis visando obter melhores decisões de negócio para a empresa. 

### **O que é Microsoft Power BI?**

**Microsoft Power BI** é uma plataforma da **Microsoft** que permite aos usuários visualizar e analisar dados, criar relatórios e dashboards e compartilhar insights com outros usuários.

No **Power BI** os usuários podem se conectar a diversas fontes de dados, como planilhas, banco de dados, serviços de nuvem e aplicativos, transformando os dados em informações valiosas e úteis.
Com o **Power BI**, podemos importar, limpar, transformar e modelar dados, criar relatórios e visualizações, e em uma versão paga até publicar e compartilhar. Além disso, possui recursos avançados, dashboards interativos, Inteligência Artificial (IA) e automatização de relatórios.

---

## 📝 Registro Por Aula

### | 📚 Aula 01 

#### **Dia 1 — 2 (29/07/26 há 30/07/26)**

**🖋️ Tópicos da Aula:**
- Introdução a ferramenta **Power BI**. (Interface)
- Intrdoução a Relatórios e Dashboards com Laboratório Prático. (Responder Perguntas de Métrica com o **Power BI**)
    - Dados
    - *1. Qual o valor total vendido?*
    - *2. Quantas vendas foram realizadas por categoria de produto?*
    - *3. Quantas vendas foram realizadas por país considerando prioridade de entrega?*
    - *4. Qual foi a média de desconto nas vendas por subcategoria de produto?*
    - *5. Quais países tiveram maior média que 250 (25%) de valor de venda? Demonstre em um mapa.*

**🧠 Aprendizados da aula:**

*Interface Power BI*
- Na interface do Power BI, temos: uma aba de Modelos (modelagem), uma aba de Tabela (visualizar os dados que consumimos) e a aba de Relatórios (onde criamos os dashboards).

*Leve Introdução ao Power Query*
> Obs: anotações do que vi e entendi até agora, pode conter imprecisões, é uma primeira impressão.
- Clicar em "Transformar Dados" redireciona para o Power Query.
- O Power Query possui 6 abas:
  - **Base**: parecido com um banco relacional (ex: PostgreSQL) — consulta a tabela, pega os dados, filtra por coluna, conceitos básicos de SQL.
  - **Transformar**: transformação nos dados — agrupamento, verificação/modificação de tipos, formatação, cálculos estatísticos, scripts de R ou Python.
  - **Adicionar Coluna**: foco em criar novas colunas (ex: Total em vendas), inclui criar coluna, invocar função personalizada, entre outras opções.
  - **Exibição**: filtros de visualização dos dados, opções de nulls, teste de qualidade da coluna, entre outros.
  - **Ferramentas**: "Iniciar Diagnóstico" funciona como um DEBUG — ajuda a entender o dashboard, melhorar performance, encontrar erros.

*Observações/Anotações Próprias*
- Power BI não é uma ferramenta de Ciência de Dados, e sim de Análise de Dados, porém em tarefas específicas dá pra usar Ciência de Dados, com a possibilidade de importar scripts Python ou R na aba Transformar.
- "Relatório" no Power BI equivale a um projeto.
- Os gráficos/dashboards podem ser escolhidos em um menu no lado direito, populá-los é só clicar em quais colunas quero que apareçam.
- Dicas de escolha de gráfico:
  - Pergunta 2 (vendas por categoria, 3 categorias): gráfico de pizza é uma boa opção, mas seria ruim com muitas categorias.
  - Pergunta 3 (vendas por país + prioridade de entrega): gráfico de barra empilhada é bom pra mostrar mais de 2 informações no mesmo gráfico.
- Existe interação entre dashboards: ao clicar em um país no gráfico da pergunta 3, o gráfico da pergunta 1 se atualiza mostrando o total de vendas daquele país, funciona como um filtro.
Dentro dos dashboards conseguimos escolher a métrica que queremos, como soma, média, contagem. Além disso, podemos também aplicar filtros como: **Mostre a região que vendeu mais de 100 mil (Somente exemplo)** .

**Dashboards com a Respostas das Perguntas:** [Dashboards](/03-PowerBI/estudos/1.%20Introdução%20e%20Primeiros%20Passos%20com%20o%20Power%20BI/)

---

### | 📚 Aula 02 

#### **Dia 3 (31/07/26)**

**🖋️ Tópicos da Aula:**
- Introdução a Modelagem de Dados
  - O que é a modelagem de dados?
  - O que é um modelo de dados?
  - Como configurar um modelo de dados no **Power BI**?
  - Quais são as implicações de não criar um modelo de dados corretamente no **Power BI**?
- Relacionamentos
- DAX

**🧠 Aprendizados da aula:**
- A **Modelagem de Dados** é o que você aplica na construção de um **Modelo de Dados**. Simplificando, você aplica técnicas de modelagem de dados para se construir um modelo de dados com o objetivo de visualizar estrutura, visualizar relacionamentos, visualizar organização dos dados.
