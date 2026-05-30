# ===============================
#      BUILT-IN FUNCTIONS
# ===============================
# São funções embutidas e disponibilizadas pelo próprio Python, onde podemos utiliza-las a qualquer momento.

# =======================================
#     EXEMPLOS DE BUILT-IN FUNCTIONS
# =======================================

vendas_anual: dict = { "Janeiro": 1500.00, "Fevereiro": 1230.00, "Março": 1870.00, "Abril": 1450.00,
                       "Maio": 2100.00, "Junho": 1980.00, "Julho": 1760.00, "Agosto": 2240.00,
                       "Setembro": 1690.00, "Outubro": 2500.00,  "Novembro": 2830.00, "Dezembro": 3500.00,
}

#  1. SUM()
# A built-in function sum() recebe um iterável e possui o objetivo de executar uma soma entre os valores númericos.

soma_vendas = sum(vendas_anual.values())

# Resultado: 24650.0
# Aqui a built-in function sum() é utilizada para somar todos os valores do dict, que simula um valor de vendas mensal.


#  2. LEN()
# A built-in function len() faz a contagem de elementos em uma determinada sequência, algo iterável.

qtd_meses = len(vendas_anual.values())  # É importante dizer que não é preciso necessariamente passar listas,
                                        # pode ser tudo aquilo que seja iterável.

# Resposta: 12 (Quantidade de Meses)


media = soma_vendas / qtd_meses


#  3. ROUND()
# A função round() em Python arredonda números decimais (float) para o valor inteiro mais próximo ou para um número específico de casas decimais.

media = round(media, 2)

