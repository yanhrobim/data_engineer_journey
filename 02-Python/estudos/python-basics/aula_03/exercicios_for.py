# ==========================================
#     EXERCICÍCIOS CONTROLES DE FLUXO
# ==========================================

# ======================
#          FOR
# ======================

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada letra aparece nele.

texto = "Três pratos de trigo para três tigres tristes"
lista_t = []

for palavra_t in texto:
   
   if "t" in palavra_t.lower().strip().replace(" ", ""):
    lista_t.append(palavra_t.lower())
    contagem = lista_t.count("t")


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# Meu Raciocínio:
# Precisa ter uma lista de números.
# Pegar o mínimo desta lista de números.
# Pegar o máximo desta lista de números. 
# Organizar em escala 0 a 1, (mínimo ao máximo)
# Fazer estes valores serem representados por 0 o menor valor, 1 o maior valor.

lista_numeros = [10, 100, 1000, 100000]
minimo_lista = min(lista_numeros)
maximo_lista = max(lista_numeros)
order_by_list = [(numero - minimo_lista) / (maximo_lista - minimo_lista) for numero in lista_numeros]


### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.

# Meu Raciocínio:
# Lista com dicionários contendo dados de usuários... (Nome e Email)
# Pegar/Filtrar do dicinário aqueles que possuem um campo vázio (faltando).

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"},
    {"nome": "Mano Yan", "email": ""}
]

usuarios_campo_vazio = [user for user in usuarios if "" in user.values()]       
# Com FOR, iteramos a lista de dicionários, fazendo com que cada dicionário seja um elemento.
# Adiciono uma condição ao bloco de loop, onde somente terá aqueles elementos (dicionários) que possuem o valor de "" em alguma chave.
# O método .values() para manipular dicionários, retorna os valores das chaves dentro do dicionário.


### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# Meu Raciocínio:
# Lista com valores númericos.
# Iterar cada elemento da lista.
# Adicionar condição de somente ter valores pares. (Se um valor númerico dividido por 2 ter o resto 0, ele é par!)
# '%' para adquirir o resto de uma divisão.

lista_de_numeros = [2, 1, 6, 10, 15, 17, 20, 26, 100]
lista_numeros_pares = [numero for numero in lista_de_numeros if numero % 2 == 0]

# OU

lista_numeros_pares = []
for numero in lista_de_numeros:
  if numero % 2 == 0:
    lista_numeros_pares.append(numero)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# Meu Raciocínio:
# Lista de dicionários com vendas, contendo categoria e valor.
# Iterar com FOR sobre a lista, e individualizar cada elemento (dict).
# Extrair cada categoria individualmente.
# Somar todo o valor que envolve aquela categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800},
    {"categoria": "livros", "valor": 300}
]

total_por_categoria = {}    # Dict vázio pensando em futuramente armazenar os valores.

for venda in vendas:        # Individualizando cada elemento.
    categoria = venda['categoria']     # Extraindo categorias, de forma individual.
    valor = venda['valor']              # Extraindo valores, de forma individual.
    if categoria in total_por_categoria:       # Se existir valor de categoria no dicionário vázio:
      total_por_categoria[categoria] += valor  # Some o valor atual com o que ja está armazenado com a categoria.
    else:
      total_por_categoria[categoria] = valor   # Se não existir valor, adicione a categoria e valor.


# Bônus para a prática. Abaixo são exercícios bônus para fins de aprendizado, visando que tive dificuldades no exercício 10.
# Pedi a uma IA para criar exercícios para mim praticar justamente o que mais tive dificuldade.

# Exercício 11. Média Por Aluno
# Dado uma lista de dicionários com nome e nota de alunos, calcule a média de notas por aluno 
# considerando que o mesmo aluno pode aparecer várias vezes.

# Meu Raciocínio:
# Uma lista de dicionários com alunos, contendo dados de nome e nota.
# Individualizar cada elemento da lista de dicionários. (Resumidamente, iterar todos os dicionários)
# Adicionar aluno e nota no dicionário.
# Adicionar caso tiver mais valores, como nota.
# Após todas as notas tiverem armazenadas, fazer a média. (Soma das notas dividido pela quantidade de notas)

notas = [
    {"aluno": "Ana", "nota": 8},
    {"aluno": "Carlos", "nota": 6},
    {"aluno": "Henry", "nota": 8},
    {"aluno": "Ana", "nota": 10},
    {"aluno": "Carlos", "nota": 4},
    {"aluno": "Henry", "nota": 1}
]

media_notas = {}

for aluno in notas:
  nome = aluno['aluno']   # Todos os valores da chave aluno, armazenados nesta váriavel.
  nota = aluno['nota']    # Todos os valores da chave nota, armazenados nesta váriavel.
  if nome in media_notas:
    media_notas[nome]['notas'] += nota
    media_notas[nome]['quantidade_bimestre'] += 1
  else:
    media_notas[nome] = {'notas': nota, 'quantidade_bimestre': 1}

for aluno, dados in media_notas.items():
  media = dados['notas'] / dados['quantidade_bimestre']
  media_notas[aluno] = {"notas" :dados['notas'], "quantidade_bimestre": dados['quantidade_bimestre'], "média": media}

# Resposta:
# {'Ana': {'notas': 18, 'quantidade_bimestre': 2, 'média': 9.0}, 
# 'Carlos': {'notas': 10, 'quantidade_bimestre': 2, 'média': 5.0}, 
# 'Henry': {'notas': 9, 'quantidade_bimestre': 2, 'média': 4.5}}

# Exercício 12. População 
# Dado uma lista de dicionários com país e população de cidades, calcule a população total por país.

# Meu Raciocínio:
# Lista de Dicionários contendo dados de nome do país e população (valor númerico).
# Se objetivo é calcular população total POR país, temos que iterar a lista de dicionários e individualizar todos elementos.
# Adicionar cada país de forma individual a um dicionário, pois trabalharemos com chave e valor, e cada país sera chave. (Lista, não faz sentido aqui)
# Porém, como condição precisamos adicionar caso não ter valor no dicionário, pois se ter, precisa somar os novos dados
# e não sobrescrever os antigos. (Condição if/else)

cidades = [
    {"pais": "Brasil", "populacao": 2000000},
    {"pais": "Argentina", "populacao": 1500000},
    {"pais": "Chile", "populacao": 1000000},
    {"pais": "Brasil", "populacao": 3000000},
    {"pais": "Argentina", "populacao": 500000},
    {"pais": "Chile", "populacao": 500000}
]

populacao_total = {}

for cidade in cidades:
  pais = cidade['pais']
  populacao = cidade['populacao']
  if not pais in populacao_total:
    populacao_total[pais] = populacao     #  '=' este sinal significa que estamos criando uma nova chave (coluna), com um
                                          # um valor definido (váriavel). (Com dict neste contexto)
  else:
    populacao_total[pais] += populacao    # '+=' este sinal significa que estamos adicionando e somando algum valor a uma
                                          # chave que ja deve estar criada, caso não, gera erro. (Além de não sobrescrever os antigos dados)

# Resposta:
# {'Brasil': 5000000, 'Argentina': 2000000, 'Chile': 1500000}