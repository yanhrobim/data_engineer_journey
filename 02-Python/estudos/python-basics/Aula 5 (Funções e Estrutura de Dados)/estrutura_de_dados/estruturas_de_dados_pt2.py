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
# São uma estrutura de dados imutáveis (Não podem conter alterações, remoções ou modificações após criadas.) para armazenar
# vários itens em uma única variável, sendo frequentemente utilizadas para garantir que os dados não sejam
# modificados.

# 1. Exemplo: Colocando ID aos produtos na lista de listas.
# O ID deve ser a primeira letra do produto + número de 0 a 999.

import random

ids = []

def gerar_numeros():
    numeros = random.randint(0, 999)
    return numeros

for produto in produtos:        # Fiz com a lista de listas 'produtos' com o objetivo para praticar mais com a estrutura.
                                # Porém, o código também poderia ser feito com a lista 'nome_produto' e um range(len()).
    if str(produto[0]).isalpha():
        ids.append((produto[0], produto[0][0] + str(gerar_numeros())))

# ids[2][1] = "F245"  # Exemplo de linha de código que no mostra que os dados armazenados em tupla, não podem ser alterados, atualizados, ou removidos.
# O erro gerado:
# TypeError: 'tuple' object does not support item assignment

# Resposta:
# [('Sorvete', 'S67'), ('Arroz', 'A783'), ('Feijão', 'F279'), ('Leite', 'L194'), ('Pão', 'P533')]


# ===========================
#     LIST COMPREHENSION
# ===========================
# Uma List Comprehension não é uma estrutura de dados necessariamente, e sim uma sintaxe para criar uma lista normal porém seguindo padrões.
# Não deixa de ser uma lista normal, porém é criada seguindo alguns padrões como de loops for, condições if-else. 
# Além disso, List Comprehension é frequentemente utilizada para evitar linhas e linhas de código de um loop for e condições,
# pois pode ser criada em apenas uma linha.

# 1. Exemplo List Comprehesion. (Obter a porcentagem de quanto o valor dos produtos aumentou)

porcentagem_de_aumento = [round(valores[1][0] - valores[1][2] / valores[1][0] / 100 * 100, 2) for valores in produtos]  # Pode ser qualquer passado qualquer objeto iterável.
# Enetendo a lógica por trás, para se obter uma porcentagem entre três valores, você deve ter a formúla: 
# valor inicial - valor final; Após a subtração dividir por 100. Com o resultado, multiplica-lo por cem para obter a porcetagem.
# Tendo isso em vista, com valores[1][0] pego o primeiro valor de todas as listas de valores, e o oposto com valores[1][2] (último valor).
# Aplico a lógica do cálculo e aplico um round() para ter uma visualização em duas casas decimais.

add_porcentagem_caractere = list(map(lambda valor: str(valor) + "%", porcentagem_de_aumento))
# Com este lambda adiciono a porcetagem, mas não é totalmente necessário. Apenas fiz para uma melhor visualização :)


