# ================
#       LIST
# ================


# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado. (Jornada de Dados)

lista_numeros_1_a_10: list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in lista_numeros_1_a_10:
    numero_ao_quadrado =  numero ** 2
    print(numero_ao_quadrado)


# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby". (Jornada de Dados)

lista_linguagem_programação: list = ["Python", "Java", "C++", "JavaScript"]
index_c = lista_linguagem_programação.index("C++")  
lista_linguagem_programação.pop(index_c)    # Removi 'C++' com pop() e index para a prática, mas certamente o método remove()
                                            # também conseguiria encontrar o item e remove-lo da lista.
lista_linguagem_programação.append("Ruby")
print(lista_linguagem_programação)


# ================
#       DICT
# ================

# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação. (Jornada de Dados)

livros: dict = {"titulo": "A arte da imperfeição", "autor": "Bréne Brown", "ano_de_publicacao": "2020"}

print(f"Nome do livro: {livros['titulo']}")
print(f"Autor do livro: {livros['autor']}")
print(f"Ano de publicação do livro: {livros['ano_de_publicacao']}")


# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário. (Jornada de Dados)
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


# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras. (Jornada de Dados)

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

# 6. Eliminação de Duplicatas (Jornada de Dados)
# Objetivo: Dada uma lista de emails, remover todos os duplicados.

emails: dict = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
for email in emails:    # Fazemos uma iteração sobre a lista, assim indidualizando cada elemento.
    if emails.count(email) > 1:  # O filtro aqui consiste em, contar email (com count) dentro da lista emails, 
                                 # se o count() retornar que tal email possuí maior que valor 1, ele executa bloco do if.
                                    
        emails.remove(email)     # Remove o email que está duplicado.

print(emails)

# 7. Filtragem de Dados (Jornada de Dados)
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades: list = [22, 15, 30, 17, 18]
for idade in idades:
    if idade <= 18:
        idades.remove(idade)

print(idades)

# 8. Análise de Idade por Setor. (Alura)
# O setor de RH da sua empresa te pediu uma ajuda para analisar as idades dos funcionários de 4 setores da empresa. 
# Para isso, ele te forneceu os seguintes dados:

idades_funcionarios: dict = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
                             'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
                             'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
                             'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

# Sabendo que cada setor tem 10 funcionários, construa um código que calcule a média de idade de cada setor, 
# a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.

# Racíocinio:
# 1. Saber a idade média de cada setor em individual.  
# 2. Descobrir a idade média dentre todos os setores, A, B, etc.
# 3. Descobrir quantos funcionários estão acima da idade média que foi obtida anteriormente.

media_cada_setor: dict = {}


for setor, idades in idades_funcionarios.items():       # Iterando as chaves e valores do dict, com .items()
                                                        # Armazenamos cada chave em "setor" e cada valor em "idades".
    media_cada_setor[setor] = sum(idades) / len(idades) 
    # Aqui criamos uma chave no dict vázio, que armazena o nome de cada setor. A cada loop um setor é criado como chave dentro do dict vázio.
    # Criando a nossa chave, o valor é criado após uma seção de cálculos, onde somamos todos os valores obtidos no dict 
    # (no caso uma lista de valores númericos) com sum() e contamos com len() a quantidade de valores que possuí, dividimos a soma pela quantidade e este valor é retornado como valor da chave.


media_geral = (sum(media_cada_setor.values())) / len(media_cada_setor.values()) # Seguindo a mesma lógica com sum() e len().
                                                                                # Aqui somamos todos os valores (todas as idades) e dividimos pela quantidade de valores presentes (quantidade de funcionários).

funcionarios_acima_media: int = 0

for idades in idades_funcionarios.values():
    for idade in idades:    # Iteramos a lista de idades, individualizando cada elemento.
        if idade > media_geral: # Se idade for maior que media geral:
            funcionarios_acima_media += 1  # Com o operador '+=', fazemos que a cada idade que passar no filtro
                                           # será contabilzado +1 na váriavel.

# Respostas em forma dict:

media_geral = {"media_geral": media_geral}   # 38.865
funcionarios_acima_media = {"funcionarios_acima_da_media": funcionarios_acima_media}  # 18
