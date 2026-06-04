# =========================
# Aplicando a projetos
# =========================


# 1. Uma loja possui um banco de dados com informações de vendas.
# Crie uma lista usando list comprehension para filtrar:
# - somente os valores do ano de 2022
# - e que sejam maiores que 6000.
#

vendas = [
    ('2023', 4093), ('2021', 4320), ('2021', 5959),
    ('2022', 8883), ('2023', 9859), ('2022', 5141),
    ('2022', 7688), ('2022', 9544), ('2023', 4794),
    ('2021', 7178), ('2022', 3030), ('2021', 7471),
    ('2022', 4226), ('2022', 8190), ('2021', 9680),
    ('2022', 5616)
]

vendas_2022 = [venda for venda in vendas if venda[0] == "2022" and venda[1] > 6000]
# A lógica desta list comprehension é individualizar cada tupla presente na lista de tuplas, e através do index executar os filtros.
# Entendendo sobre a lista de tuplas, o index[0] são os anos, e index[1] são os valores.
# print(vendas_2022)


# 2. Uma clínica analisa dados de glicemia e deseja rotular os valores:
#
# - Glicose <= 70 → 'Hipoglicemia'
# - Entre 70 e 99 → 'Normal'
# - Entre 100 e 125 → 'Alterada'
# - Maior que 125 → 'Diabetes'
#
# Crie uma lista de tuplas usando list comprehension contendo:
# - o rótulo
# - e o valor da glicemia.

glicemia = [
    129, 82, 60, 97, 101, 65, 62, 167,
    87, 53, 58, 92, 66, 120, 109, 62,
    86, 96, 103, 88, 155, 52, 89, 73
]

rotulo = ["Normal" if dados >= 70 and dados <=99 
                   else "Hipoglicemia" if dados < 70
                   else "Alterada" if dados >=100 and dados <=125
                   else "Diabetes" for dados in glicemia]   
# Para simular um 'elif' dentro de uma list comprehension é preciso que você faça mais de um if-else dentro, após o else, adicionar mais um 1 if (Condição). OBS: No último else, não aplicar.

glicemia_rotulo = list(zip(rotulo, glicemia))   # Método zip() para juntar o rotulo que foi gerado na list comprehension
                                                # com seus respectivos valores.
# print(glicemia_rotulo)

# 3. Um e-commerce possui as seguintes listas:

ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]

preco = [93.0, 102.0, 18.0, 41.0, 122.0,
          14.0, 71.0, 48.0, 14.0, 144.0]
#
# Crie uma lista de tuplas contendo:
# - id
# - quantidade
# - preço
# - valor total (quantidade * preço)
# A primeira tupla deve ser o cabeçalho:
# ('id', 'quantidade', 'preco', 'total')

# Meu raciocínio:
# 1. Objetivo: Juntar todos os valores em uma tupla e criar uma coluna chamada 'total' com o cálculo de quantidade * preco.
# 2. Fazer um list comprehension com zip() para individualizar cada elemento de cada lista.
# 3. Fazer o cálculo da coluna 'total'.
# 4. Inserir com insert() no index 0 os cabeçalhos.

id_quantidade_preco_total = [(iD, quantidade, preco, round(quantidade * preco, 2)) for iD, quantidade, preco in zip(ids, quantidade, preco)]
# A lógica é aplicar um zip para tratar individualizar cada valor de cada lista individualmente, e aplicar o cálculo em quantidade e preco.
# Além disso, aprendi que podemos adicionar valores de colunas desta maneira: (coluna1, coluna2), evitando que no final, o resultado seja somente o cálculo.
id_quantidade_preco_total.insert(0, ('id', 'quantidade', 'preco', 'total')) # insert() nos permite adicionar tal valor especificando o index de nossa preferência.
# print(id_quantidade_preco_total)


# 4. Uma empresa possui uma lista com os estados das filiais:
#
# estados = [
#     'SP', 'ES', 'MG', 'MG', 'SP', 'MG',
#     'ES', 'ES', 'ES', 'SP', 'SP', 'MG',
#     'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP',
#     'MG', 'SP', 'ES', 'SP', 'MG'
# ]
#
# Crie um dicionário usando dict comprehension em que:
# - a chave seja o nome do estado
# - o valor seja a quantidade de vezes que o estado aparece na lista.
#
# Dica:
# Você pode criar uma lista intermediária antes.


# 5. A empresa também possui a seguinte lista:
#
# funcionarios = [
#     ('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6),
#     ('SP', 10), ('MG', 4), ('ES', 9), ('ES', 7),
#     ('ES', 12), ('SP', 7), ('SP', 11), ('MG', 8),
#     ('ES', 8), ('SP', 9), ('RJ', 13), ('MG', 5),
#     ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7),
#     ('ES', 14), ('SP', 10), ('MG', 12)
# ]
#
# Crie:
#
# 1. Um dicionário em que:
#    - as chaves sejam os estados únicos
#    - os valores sejam listas com a quantidade de funcionários
#      referentes a cada estado.
#
# 2. Um dicionário em que:
#    - as chaves sejam os estados
#    - os valores sejam a soma total de funcionários por estado.

