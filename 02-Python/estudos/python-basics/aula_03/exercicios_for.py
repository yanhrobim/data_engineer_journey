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


### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
