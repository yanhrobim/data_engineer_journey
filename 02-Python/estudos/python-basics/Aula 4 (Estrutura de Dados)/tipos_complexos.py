# ================
#       LIST
# ================
# Estrutura de Dados.

# 1. Exemplo List

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
# Muito semelhante a lista, porém a principal diferença é a estrutura sendo chave-valor.

# Exemplo Dict

filme_marvel = {"Nome": "The Amazing Spider Man",
                "Ano": 2012,
                "Marca": "Marvel"
}

# filme_marvel.clear()  # Limpa o dicionário. (Literalmente, tira tudo que há dentro dele)

copy_dict = filme_marvel.copy()     # Mesmo objetivo do método copy() em listas.

nome_get = filme_marvel.get("Bilheteria") # o método get() nos permite pegar o valor de uma chave em um dict. No caso passando ela como parâmetro ao método.
print(nome_get)

key_não_existente = filme_marvel.get("Bilheteria", "NULL")    
# O get() possuí um segundo parâmetro, o 'default', com ele conseguimos dizer ao método o que fazer se caso tal chave não existir ou não conter valor dentro de dicionário.
# No get() acima deste, quando não estabelecemos o parâmetro, ele nos retornaria None como padrão.
# Este parâmetro torna este método rico em manipular dicionários, por abrir bastante portas a normalizar valores faltantes, criar novas chaves, etc.
print(key_não_existente)

dict_view = filme_marvel.items() 
# { O método items() bem complexamente retorna nossas chaves e valores do dicionário em uma forma de visualização, uma forma dinâmica.
# Dinâmica pois não é uma cópia, se mudarmos chave A, o dicionário é modificado da mesma forma. }  Explicação Seguindo a Documentação.
# Basicamente, é retorna nossas chaves e valores, poderiamos por exemplo manipular estes valores com iter(), reversed()
# porém temos uma forma mais fácil de fazer este mesmo tipo de manipulação, sendo o loop for.
# Por isso em um loop for quando utilizamos .items() passamos dois valores, um sendo para a chave(str) e outro para valor(Any), justamente o que é o método retorna. (Possível visualizar isto passando o mouse acima do método)

chaves_dict = filme_marvel.keys()
print(chaves_dict)
# O método keys() de forma complexa tem a mesma explicação do items() (segundo a documentação do Python),
# porém existe a diferença em que ao invés de retornar todos os itens presentes no dicionário, retorna somente as chaves.


filme_marvel.pop("Marca")   # O método pop() tem o objetivo de remover chave-valor de um dicionário.
                            # O método acessa a chave passada como parâmetro e a apaga, limpa, remove do dict. (Semelhante ao método remove() de list, porém mais eficiente por acessar a chave diretamente.)
print(filme_marvel)         # Também possuí o parâmetro 'default'.

filme_marvel.popitem()      # O método popitem() remove a última chave-valor do dict.
print(filme_marvel)

filme_marvel.setdefault("vezes_assistidas", 0) 
# O método setdefault assim como o parâmetro 'default' em outros métodos é muito útilizavel para normalizar valores faltantes ou criar chaves.
# Passamos a chave que queremos "criar" e o valor que iremos ter como padrão quando chave for criada.
# Se chave passada existir, não faz exatamente nada, preserva o que já temos.
# Se não, o método cria a chave e o valor padrão.

print(filme_marvel)

filme_marvel.update({
    "Ano": 2012,
    "Marca": "Marvel"
})   # O método update() é muito semelhante ao método append() de list, porém existe uma diferença que muda tudo.
     # O update() atualiza o dicionário, ou cria aquilo que ainda não existe, com o append() não atualizamos e sim adicionamos mais valores,
     # com o update() se valor existir, é sobrescrevido pelo novo valor.
     # Bem importante ter esta diferença em mente pelo risco de perder dados antigos.

print(filme_marvel)

valores = filme_marvel.values()
print(valores)
# O método values() de forma complexa tem a mesma explicação do items() (segundo a documentação do Python),
# porém existe a diferença em que ao invés de retornar todos os itens presentes no dicionário, retorna somente os valores.