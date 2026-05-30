# ==================
#      FUNCÃO
# ==================
# Funções são uma sequência de instruções que criamos em um bloco de código para executar tarefas específicas.
# Além disso, podem ser reutilzidas em diferentes partes do nosso código.

# 1. Função Sem Parâmetros.

def contar_caractere():
    quantidade_caractere = len("palavra")
    print(quantidade_caractere)

contar_caractere()


# 2. Função Com Parâmetros.

def contar_caractere_parâmetro(palavra):
    quantidade_caractere = len(palavra)
    print(quantidade_caractere)

contar_caractere_parâmetro(palavra="engenharia")


# 3. Função Com Retorno.
# Tanto funções com parâmetros ou sem, trabalham com 'escopo de função', onde significa que tuda variável
# que foi criada, desenvolvida dentro da função, após a execução do bloco de código a variável morre.
# Isso pode atrapalhar pois funções sem retorno retornam 'NoneType', e provavelmente você irá precisar do resultado que foi obtido dentro da função.


def contar_caractere_parâmetro_return(palavra):
    quantidade_caractere = len(palavra)

    if quantidade_caractere >= 12:
        situacao = "Palavra Consideravelmente Grande Para o Cotidiano"
    
    else:
        situacao = "Palavra Normal Para o Cotidiano"

    return (quantidade_caractere, situacao)

qtd_caractere, situacao = contar_caractere_parâmetro_return(palavra="paralelepípedo")
print(f"Você digitou uma palavra com {qtd_caractere} caracteres. Ela é uma {situacao}")


# =======================
#      FUNCÃO LAMBDA
# =======================
# Funções lambdas são funções que não precisam ser nomeadas como as que criamos com def, por isso são chamadas também de funções anônimas.
# Uma função lambda pode ser executada em apenas uma linha de código.

# 1. Exemplo Com Uma Função Normal

numero: int = 11
def par_ou_impar_func(numero):
    divisao = numero % 2
    if divisao == 0:
        print("Par!")
    else:
        print("Impar!")

par_ou_impar_func(numero)


# 2. Com uma função lambda

par_ou_impar = lambda numero: numero % 2    # Basicamente, número é o parâmetro que definimos que a função deve receber.
                                            # Em seguida a o parâmetro que definimos, após ':' definimos a métrica que será
                                            # executada, a lógica, etc.
resultado = par_ou_impar(11)
if resultado == 0:
        print(f"O número {numero} é Par!")
else:
        print(f"O número {numero} é impar!")


# 3. MAP()
# Com o map() conseguimos potencializar o lambda a executar funções em iteráveis, seria individualizar cada elemento como fazemos com um loop FOR.

precos: list = [29.90, 149.99, 89.50, 12.00, 199.90]
aumento =  0.10 # 10%

aumento_valores = map(lambda preco: preco * aumento + preco, precos) # Aqui map permite que pegamos cada valor da lista individualmente, 
                                                                     # para descobrirmos o 10% de cada valor.   

# O map() precisa ser convertido a uma iterável, 
# pois caso não transformamos o resultado com o list() não conseguimos visualizar os valores obtidos.
# Caso contrário, ele nos retorna uma objeto map, mas não as respostas.

print(list(aumento_valores))

