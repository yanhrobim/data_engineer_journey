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

lista_ex.remove(1.75) # remove() nos permite remover o valor específicado da lista. 
                        # Uma observação enquanto praticava, é que se houver mais de um valor igual ao valor específicado 
                        # ele somente remove o primeiro que acha percorrendo a lista.

lista_ex.pop()      # pop() remove o último valor da lista. O bom deste comando é a perfomace, pois o remove() percorre
                    # a lista inteira para encontrar tal valor, o pop() remove o último valor.
                    # Porém, se adicionarmos o parãmetro de index desse método, ele pode perder esta GRANDE vantagem.

# lista_ex.clear()    # clear() remove todos os itens da lista.


print(f"O index do valor especificado é: {lista_ex.index('Ryan', 0)}") # index() nos permite encontrar o index de um valor específico em uma lista. 
# (Ex: Aqui o método iria devolver o valor de 0, sendo o index do valor "Ryan". O segundo parâmetro é opcional, que signfica por qual index começar.)


print(f"O valor especificado apareceu: {lista_ex.count('Ryan')} na lista")    # O método count() nos permite contar quantas vezes o valor passado como parâmetro aparece na lista.

# lista_ex.sort() # sort() nos permite ordenar os itens dentro da lista. (Parâmetros do método são importantes para a ordenação)

lista_ex.reverse()  # O método reverse() nos permite reverter a sequência da lista, fazendo com que os últimos valores se tornem os primeiros, e os primeiros se tornem os últimos. ("Os últimos serão exaltados")

lista_ex.copy() # copy() nos permite fazer uma cópia da lista que possuimos e seus itens. Importante quando precisamos transformar uma lista, mas não pode ser a original.

print(lista_ex)


# ================
#       DICT
# ================
# Estrutura de Dados.