# ================
#       LIST
# ================


# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

lista_numeros_1_a_10: list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in lista_numeros_1_a_10:
    numero_ao_quadrado =  numero ** 2
    print(numero_ao_quadrado)


# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

lista_linguagem_programação: list = ["Python", "Java", "C++", "JavaScript"]
index_c = lista_linguagem_programação.index("C++")  
lista_linguagem_programação.pop(index_c)    # Removi 'C++' com pop() e index para a prática, mas certamente o método remove()
                                            # também conseguiria encontrar o item e remove-lo da lista.
lista_linguagem_programação.append("Ruby")
print(lista_linguagem_programação)


# ================
#       DICT
# ================

# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

livros: dict = {"titulo": "A arte da imperfeição", "autor": "Bréne Brown", "ano_de_publicacao": "2020"}

print(f"Nome do livro: {livros['titulo']}")
print(f"Autor do livro: {livros['autor']}")
print(f"Ano de publicação do livro: {livros['ano_de_publicacao']}")


# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# Iremos precisar de um dict para armazenar o número de ocorrências.
## Neste dict, cada letra deve ser uma chave.
## O valor desta chave é o número de vezes que tal letra está na frase.
# Com um loop for e condição, criamos chaves e adicionamos o valor, a cada vez que letra reaparecer.

frase: str =  "engenharia de dados e sql"

contagem: dict = {}

for letra in frase:
    if letra in contagem:
        contagem[letra] += 1
    else:                       # Esta foi a forma na qual pensei em solucionar o desafio. 
                                # (Através de condições, faço a contagem de letras da string)
        contagem[letra] = 1

#   contagem[letra] = contagem.get(letra, 0) + 1    # Está foi a forma que o professor solucionou na aula.
                                                    # Basicamente, o get() procura dentro do dict cada letra como chave,
                                                    # como paramêtro do método .get() podemos adicionar um valor padrão, caso chave não ter valor ou não estar criada dentro do dict,
                                                    # então dizemos: Procura dentro deste dict tal chave, se não existir, retorna a letra(como chave) e valor igual 0. Se ja existir soma o +1.

print(contagem)


# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista_de_compras: list = ["maçã", "banana", "cereja"]
valores: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(valores[nome_produto] for nome_produto in lista_de_compras) 
# Lista de compras é uma lista onde possuí strings com o nome dos produtos. E valores é um dict, onde tem os nomes como chaves e estas chaves possuem valores númericos (Representando o valor do produto).
# Tendo isto em vista, quando fazemos um for em lista, individualizamos cada elemento, e para conseguirmos
# valores de um dict precisamos necessariamente da chave. 
# Fazendo um FOR pegamos cada elemento da lista (nome dos produtos em string) e damos os
# resultados ao dict em 'valores[nome_produto]', onde o nome no qual o loop está percorrendo significa a chave do dict para obtermos o valor do produto.
# O loop acessa todos os valores dos produtos, através do nome fornecido pela lista e executa um sum() para somar tudo que o loop percorrer.

print("Total da lista de compras:", total)


# ===================================================
#   Exercícios Intermediários e Mais Avançados
# ===================================================

# 6. Eliminação de Duplicatas 
# Objetivo: Dada uma lista de emails, remover todos os duplicados.

emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]