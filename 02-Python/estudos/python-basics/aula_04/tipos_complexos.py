# ================
#       LIST
# ================
# Estrutura de Dados.

# 1. List

nome: str = "Ryan"
idade: int = 15
altura: float= 1.75

lista_ex: list = []
lista_ex.append(nome)
lista_ex.append(idade)  # Método do objeto list para adicionar itens.
lista_ex.append(altura)


iteravel = [1, 2, 3, 4, 5]

# 2. Métodos do Objeto (list)

lista_ex.append(nome)   # Método do objeto list para adicionar itens. (Aqui, só podemos adicionar 1 item)

iteravel = [1, 2, 3, 4, 5]

lista_ex.extend(iteravel)   # extend() nos permite colocar um item iterável dentro da lista, uma sequência, etc.

lista_ex.insert(3, iteravel)    # insert() nos permite adicionar um item a lista, mas especificando o index em que o valor será adicionado.

lista_ex.remove("Ryan") # remove() nos permite remover o valor específicado da lista. 
                        # Uma observação enquanto praticava, é que se houver mais de um valor igual ao valor específicado 
                        # ele somente remove o primeiro que acha percorrendo a lista.

lista_ex.pop()      # pop() remove o último valor da lista. O bom deste comando é a perfomace, pois o remove() percorre
                    # a lista inteira para encontrar tal valor, o pop() remove o último valor.

# lista_ex.clear()    # clear() remove todos os itens da lista.


# ================
#       DICT
# ================
# Estrutura de Dados.