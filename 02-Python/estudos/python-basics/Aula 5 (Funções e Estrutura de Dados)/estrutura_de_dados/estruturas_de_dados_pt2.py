# ======================================
#      ESTRUTURA DE DADOS ANINHADAS
# ======================================

# =========================
#     LISTA DE LISTAS
# =========================
# Possuí o mesmo objetivo de uma lista normal, armazenar uma sequência de elementos.
# Porém a diferença é que os elementos não são somente tipos simples como: strings, int, etc. Uma lista de listas é composta por outras listas armazenadas dentro.

# 1. Transformando uma lista simples em uma lista de listas.
# Objetivo: Colocar produto e preços dentro de uma lista, onde se encontra armazenada dentro de outra lista.
# Ex: produtos: list = [["Kit-Kat", 5.0, 7.0, 9.0]]
historico_precos: list = ["Sorvete", 20.0, 21.0, 25.0, 
                          "Arroz", 18.0, 22.0, 27.0, 
                          "Feijão", 9.0, 11.0, 14.0, 
                          "Leite", 5.0, 6.0, 7.5,
                          "Pão", 8.0, 9.5, 12.0
]   # Simulando um mercado, seus produtos e seus respectivos preços ao longo de um  período. 

nome_produto = []
produto_precos_juntos = []


for i in range(len(historico_precos)):    # Individualizamos cada elemento através do index. 
    # O range() entrega ao loop for não o elemento, e sim um número que significa o index da lista.
    # A cada rodada é entregado o index de um elemento, na nossa lista, o padrão é que a cada 4 elementos, temos o nome do produto.
    if i % 4 == 0:
        nome_produto.append(historico_precos[i])    # Se index for dividido por 4 e retornar 0, adicione ele na lista.

    else:
        produto_precos_juntos.append(historico_precos[i])

produto_precos = []

for preco in range(0, len(produto_precos_juntos), 3):
    produto_precos.append([produto_precos_juntos[preco], produto_precos_juntos[preco+1], produto_precos_juntos[preco+2]])
# O range está começando do index 0, e tem mais um parâmetro chamado 'step' quee está como 3. O step é responsável pela ordem no qual o valor é passado ao loop for.
# Então, a cada rodada, o loop for recebe o index de 3 em 3, o primeiro index é 0, depois 3, depois 6, assim por adiante.
# Quando executamos preco + 1 e preco + 2, estamaos apenas adicionamos a uma lista os valores após o index passado, novamente explicando, de 3 em 3.


# Observação sobre lista de listas.
# Caso queira pegar especifico valor em uma lista de lista:

print(produto_precos[1][0]) # Em termos de hirárquia, primeiro vem o index da lista que desejamos o valor, depois o valor que queremos.

produtos = []

for nome_p, preco_p in zip(nome_produto, produto_precos):
    produtos.append([nome_p, preco_p])
print(produtos)

# Resposta:
# [['Sorvete', [20.0, 21.0, 25.0]], ['Arroz', [18.0, 22.0, 27.0]], ['Feijão', [9.0, 11.0, 14.0]], ['Leite', [5.0, 6.0, 7.5]], ['Pão', [8.0, 9.5, 12.0]]].

# =================
#      TUPLAS
# =================

