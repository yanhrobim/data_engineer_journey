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

qtd_meses = len(vendas_anual.values())  # É importante dizer que não é preciso necessariamente passar para o len()
                                # algo que seja iterável.

# Resposta: 12 (Quantidade de Meses)

media = soma_vendas / qtd_meses


#  3. ROUND()
# A função round() em Python arredonda números decimais (float) para o valor inteiro mais próximo ou para um número específico de casas decimais.

media = round(media, 2)


# ==================
#      FUNCÃO
# ==================
# Funções são uma sequência de instruções que criamos em um bloco de código para executar tarefas específicas.
# Além disso, podem ser reutilzidas em diferentes partes do nosso código.

# 1. Função Sem Parâmetros.

def contar_caractere():
    quantidade_caractere = len("palavra")
    print(quantidade_caractere)

contar_caractere()

# 2. Função Com Parâmetros.

def contar_caractere_parâmetro(palavra):
    quantidade_caractere = len(palavra)
    print(quantidade_caractere)

contar_caractere_parâmetro(palavra="engenharia")

# 3. Função Com Retorno.
# Tanto funções com parâmetros ou sem, trabalham com 'escopo de função', onde significa que tuda variável
# que foi criada, desenvolvida dentro da função, após a execução do bloco de código a variável morre.
# Isso pode atrapalhar pois funções sem retorno retornam 'NoneType', e provavelmente você irá precisar do resultado que foi obtido dentro da função.


def contar_caractere_parâmetro_return(palavra):
    quantidade_caractere = len(palavra)

    if quantidade_caractere >= 12:
        situacao = "Palavra Consideravelmente Grande Para o Cotidiano"
    
    else:
        situacao = "Palavra Normal Para o Cotidiano"

    return (quantidade_caractere, situacao)

qtd_caractere, situacao = contar_caractere_parâmetro_return(palavra="paralelepípedo")
print(f"Você digitou uma palavra com {qtd_caractere} caracteres. Ela é uma {situacao}")
