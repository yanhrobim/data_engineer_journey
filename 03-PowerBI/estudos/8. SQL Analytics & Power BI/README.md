## 🔎 Exercício Analítico

Nesta aula do curso iremos utilizar a linguagem SQL, com o objetivo de criar uma tabela analítica para chegar ao Power BI. 

---

## 💡 Ideia do Exercício

Tive a ideia de fazer este exercício diferente e não só praticar código, e sim minha visão analítica. Muitas outras vezes pratiquei SQL pedindo tarefas para eu realizar, como descobrir KPIs, aplicar métricas, em resumo, era descobrir respostas para perguntas prontas.

Aqui eu fiz diferente. Pedi uma semelhante mensagem de um dia a dia de um engenheiro/analista de dados, não uma pergunta como: "Qual o Top10 Mercados?". A ideia é eu ler a mensagem e ir atrás de respostas, sem pistas, sem que na mensagem tenha um tutorial do que eu tenha que fazer, somente tenha o objetivo e dúvidas de uma empresa.

---

## 💬 A Mensagem (Marina)

```
De: Marina, Diretoria Comercial
Assunto: Entendimento do nosso negócio

Oi, pessoal de dados!

Na próxima semana tenho reunião de planejamento com o board e preciso chegar lá com uma visão clara de como o negócio está indo. Hoje a gente vende para vários mercados, mas sinceramente eu não sei dizer onde estamos bem e onde estamos mal. Tenho a sensação de que algumas regiões dão mais trabalho do que retorno, mas é só uma sensação.

Também queria entender se a gente está dependendo demais de poucas coisas, e se o que estamos fazendo na logística está ajudando ou atrapalhando.

Não preciso de nada muito complexo. Preciso conseguir olhar e responder: “estamos saudáveis? onde devo prestar atenção?”

Consegue pra quinta?

Obrigada!

```

**OBS: Criada somente para a prática por IA.**

---

## 💬 A Resposta (Eu)

Para realmente me aprofundar no exercício, criei uma resposta que seria enviada a Marina.


```
Assunto: Como está o negócio: o que vi e onde olhar

Oi, Marina!

Resumo: No geral estamos saúdaveis, e o frete fica perto da média de 10,58% em todos os mercados, sem uma alta dispersão. Mas é de extrema importância uma atenção nos mercados EU e APAC considerando que eles juntos representam 63,34% do faturamento da empresa, e que se algo acontecer o negócio inteiro sente. 

O que vi:
    • O mercado EU (Europa) e APAC (Ásica Pacífico) juntos representam 63,34% do faturamento total da empresa. O Canada possuí a menor participação, representando 0,49%. (Segundo Query SQL que calcula a participação de cada mercado sobre o faturamento total)
    • Tivemos um custo de 10,58% de frete sobre o faturamento. (Custo total de frete da empresa dividido pelo faturamento total da empresa)
    • A categoria de Tecnologia representa 37,81% do faturamento total da empresa. Enquanto a categoria de Material de Escritório representa 30,29%, mas vendeu 45,265 produtos a mais que Tecnologia. (Query SQL que avalia o desempenho das categorias, com colunas como o faturamento total, quantidade total de produtos vendida.)
    • Os mercados possuem leve dipersão sobre a média de frete (10,58%), chegando no máximo a 1,7 pontos de diferença. O que mais se afasta é o Canadá com 12,27%, mas que não é um mercado de peso dentro do faturamento (0,49%).

Onde olhar:
    1. Forte depedência dos mercados EU e APAC. São mercados que fogem muito do padrão vendido, tendo mais de 1 milhão de diferença de faturamento entre os outros mercados.
    2. Frete do Canada. Apesar de não ser um mercado de peso no faturamento, aquilo que conseguimos com eles, a parte de 12,27% vai para o custo do frete, a medía da empresa sendo 10,58%. Não é um problema nível crítico, mas que pode ser melhorado.

O que não consegui responder:
    • Desempenho da Logística. Para que eu descobrisse se a logística ajuda ou atrapalha, eu precisaria mais de granularidade na tabela de Pedidos, como Dia de Entrega, Prazo, Feedback do Cliente.

O que supus:
    • Na sua mensagem não foi definida nenhuma média para partir do que é seria “estamos bem” ou “estamos mal”, então utilizei a média de empresa como referência.
    • Fiz uma analíse por Mercado, e não por Região. Tive a visão que por mercado teria informações mais claras e mais rápidas de serem transmitidas.
    • Faturamento é valor que foi vendido e que arrecadamos, o frete é o único custo. (Não é diretamente um lucro)
    • Apesar da tabela Pedidos conter colunas com Ano, Mês, Dia, tive a visão que misturar tempo entre as analíses teria a consequência de complexar mais a tabela e dados. Prefiri focar em ver em uma foto única, e por isso motivo não existe a informação se o negócio está crescendo ou caindo.
    • Deduzi que a porcentagem de frete que seria um problema caso ultrapasse 4 pontos de difereça da média. Por este motivo nada ou poucas coisas relacionadas com o custo do frete.

Abraço,
Yan

```

---

## 📈 Tabela e Métricas

Para a criação da mensagem e solução de forma analítica das dúvidas da Marina foram feitas mas que somente uma tabela. Além de uma tabela que mostra em dados o desempenho de Mercado/Região, foram feitas mais queries para dar respostas concretas na mensagem.

### 📊 Tabela Desempenho Mercado Regiao

```sql
WITH Desempenho_Mercado_Regiao AS (
SELECT 
		tdc.Mercado,
		tdp.Categoria,
		tdc.Regiao,
		tdc.Pais,
		SUM(tdv.Quantidade_Vendida) AS Quantidade_Produtos_Vendidos,
		ROUND(SUM(tdv.Valor_Venda), 2) AS Faturamento_Total,
		ROUND(SUM(tdv.Custo_Envio), 2) AS Custo_Envio_Total
FROM TB_DSA_CLIENTES AS tdc
LEFT JOIN TB_DSA_VENDAS AS tdv ON tdc.ID_Cliente = tdv.Cliente
INNER JOIN TB_DSA_PRODUTOS tdp ON tdv.Produto = tdp.ID_Produto  
GROUP BY tdc.Regiao, tdp.Categoria)
```

---

### 🟢 Descobrir Faturamento Total Empresa, Custo Total Pago de Frete, Porcentagem do Frete Pago Sobre o Faturamento da Empresa. 

```sql
SELECT 
		SUM(Faturamento_Total) AS Faturamento_Total_Empresa,
		SUM(Custo_Envio_Total) AS Custo_Frete_Total,
		ROUND(SUM(Custo_Envio_Total) * 100 / SUM(Faturamento_Total), 2) AS Porcentagem_Frete_Sobre_Faturamento_Empresa
FROM Desempenho_Mercado_Regiao
```

---

### 🟢 Desempenho Categoria (Quantidade Produtos Vendidos Por Categoria, Faturamento por Categoria, Participação em Porcentagem no Faturamento)	

```sql
SELECT 
		Categoria,
		SUM(Quantidade_Produtos_Vendidos) AS Quantidade_Total_Produtos_Vendidos_Categoria,
		ROUND(SUM(Faturamento_Total), 2) AS Faturamento_Categoria,
		ROUND(SUM(Faturamento_Total) * 100 / SUM(SUM(Faturamento_Total)) OVER(), 2) AS Participacao_No_Faturamento_Total_Da_Empresa
FROM Desempenho_Mercado_Regiao
GROUP BY Categoria
ORDER BY Participacao_No_Faturamento_Total_Da_Empresa DESC
```

---
### 🟢 Faturamento Total Por Regiao.


```sql
SELECT 
		Regiao,
		ROUND(SUM(Faturamento_Total), 2) AS Faturamento_Total 
FROM Desempenho_Mercado_Regiao
GROUP BY Regiao
ORDER BY Faturamento_Total DESC
```

---

### 🟢 Descobrir em Reais a Porcentagem de Frete Paga. (De cada Mercado)


```sql
SELECT 
		Mercado,
		ROUND(SUM(Custo_Envio_Total) / SUM(Faturamento_Total) * 100, 2) AS Porcentagem_Frete_Por_Mercado,
		ROUND(SUM(Custo_Envio_Total) - 0.1058 / SUM(Faturamento_Total), 2) AS Porcentagem_Em_Reais
FROM Desempenho_Mercado_Regiao
GROUP BY Mercado
ORDER BY Porcentagem_Em_Reais DESC
```

---
