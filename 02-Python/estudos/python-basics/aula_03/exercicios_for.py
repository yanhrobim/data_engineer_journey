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
print(contagem)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.