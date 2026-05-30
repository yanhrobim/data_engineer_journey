# =============================================================
# HORA DA PRÁTICA - Funções
# =============================================================


# Questão 1
# Escreva um código que lê a lista abaixo e faça:
# lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
#
# - A leitura do tamanho da lista
# - A leitura do maior e menor valor
# - A soma dos valores da lista
#
# Ao final exiba uma mensagem dizendo:
# "A lista possui [tam] números em que o maior número é [maior] e o menor
#  número é [menor]. A soma dos valores pares presentes nela é igual a [soma]"

# Meu racíocinio:
# 1. Descobrir o tamanho da lista, resumidamente, quantos valores tem a lista.
# 2. Descobrir o maior valor da lista e menor valor. (max() e min())
# 3. Somar todos os valores que a lista contém.
# 4. Colocar todas as respostas em váriaveis, sendo: tam, maior, menor e soma.
# 5. Exibir no print.

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

tam = len(lista)
maior = max(lista)
menor = min(lista)
soma_valores = sum(lista)

print(f"A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores pares presentes nela é igual a {soma_valores}.") 

# Resposta:
# A lista possui 17 números em que o maior número é 99 e o menor número é 11. A soma dos valores pares presentes nela é igual a 743.

# Questão 2
# Escreva uma função que gere a tabuada de um número inteiro de 1 a 10,
# de acordo com a escolha da pessoa usuária.
# Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

#
# Tabuada do 7:
# 7 x 0 = 0
# 7 x 1 = 7
# [...]
# 7 x 10 = 70
  
# Meu racíocinio:
# 1. Criar uma função que receba um número como parâmetro, de preferência int.
# 2. O exercício não pede nada relacionado a retorno, ou se iremos precisar da resposta, 
# então apenas fazemos os prints para sinalizar os resultados.


def tabuada(numero: int):
    print(f"{numero} x 0 = {numero * 0}")
    print(f"{numero} x 1 = {numero * 1}")
    print(f"{numero} x 2 = {numero * 2}")
    print(f"{numero} x 3 = {numero * 3}")
    print(f"{numero} x 4 = {numero * 4}")
    print(f"{numero} x 5 = {numero * 5}")
    print(f"{numero} x 6 = {numero * 6}")
    print(f"{numero} x 7 = {numero * 7}")
    print(f"{numero} x 8 = {numero * 8}")
    print(f"{numero} x 9 = {numero * 9}")
    print(f"{numero} x 10 = {numero * 10}")

numero = 4
tabuada(4)

# Questão 3
# Crie uma função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:
# [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
#
# Utilize o return na função e salve a nova lista na variável mult_3.
 
# Meu racíocinio:
# 1. Criar uma função que receba um parâmetro sendo a iterável list.
# 2. Criação de uma lista vázia, sendo a lista que futuramente será populada com os valores múltiplos por 3.
# 3. Individualizar cada elemento da lista.
# 4. Após a individualização, fazer uma condição, sendo: Se número da lista dividido por 3 resultar em resto 0, adicionar este número na lista.
# 5. O retorno da função deve ser a lista.

lista_valores_numericos = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def multiplo_3(lista_de_valores_numericos: list[int]):
    lista_multiplo_3 = []
    for numero in lista_de_valores_numericos:
        if numero % 3 == 0:
            lista_multiplo_3.append(numero)
    
    return lista_multiplo_3

mult_3 = multiplo_3(lista_valores_numericos)
print(mult_3)

# Questão 4
# Crie uma lista dos quadrados dos números da seguinte lista:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Lembre-se de utilizar as funções lambda e map() para calcular
# o quadrado de cada elemento da lista.
 
lista_quadrados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrado_numero = map(lambda numero: numero ** 2, lista_quadrados)  # map() para permitir o lambda lidar com iteráveis.
# Quando queremos fazer algo relacionado a potência em Python utilzamos: '**'.
# Após o operador, precisamos dizer qual o valor númerico que será a potência da váriavel. Na nossa situação sendo ao quadrado (potência 2).

print(list(quadrado_numero))    # list() para vermos o nosso resultado.

# -------------------------------------------------------------
# APLICANDO A PROJETOS
# -------------------------------------------------------------
 
# Questão 5
# Você foi contratado(a) como cientista de dados de uma associação de skate.
# Para analisar as notas recebidas dos(as) skatistas em algumas competições
# ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas.
# Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.
#
# Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior
# e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram.
#
# Retorne a média para apresentar o texto:
# "Nota da manobra: [media]"
 
# Meu racíocinio:
# 1. Receber 5 váriaveis que contém valores númericos, que representa as notas.
# 2. Adicionar as notas em uma lista vázia.
# 3. Dentre as 5 notas, excluir a maior nota e a menor. (max() e min())
# 4. Fazer uma média com as notas que sobraram.
# 5. Retornar a váriavel que possui o valor de média.

nota_1 = int(input("Digite sua primeira nota: "))
nota_2 = int(input("Digite sua segunda nota: "))
nota_3 = int(input("Digite sua terceira nota: "))
nota_4 = int(input("Digite sua quarta nota: "))
nota_5 = int(input("Digite sua quinta nota: "))

def nota_skatista(n1: int, n2: int, n3: int, n4: int, n5: int):
    lista_notas = [n1, n2, n3, n4, n5]
    maior_e_menor_nota = [max(lista_notas), min(lista_notas)]
    lista_notas = [numero for numero in lista_notas if numero not in maior_e_menor_nota]
    media_skatista = sum(lista_notas) / len(lista_notas)

    return round(media_skatista, 2)

nota_final_skatista = nota_skatista(nota_1, nota_2, nota_3, nota_4, nota_5)
print(f"Nota da manobra: {nota_final_skatista}")


# Questão 6
# Para atender a uma demanda de uma instituição de ensino para a análise do
# desempenho de seus(suas) estudantes, você precisa criar uma função que receba
# uma lista de 4 notas e retorne:
# - maior nota
# - menor nota
# - média
# - situação (Aprovado(a) ou Reprovado(a))
#
# Para testar o comportamento da função, os dados podem ser exibidos em um texto:
# "O(a) estudante obteve uma media de [media], com a sua maior nota de [maior]
#  pontos e a menor nota de [menor] pontos e foi [situacao]"
 
 

# Questão 7
# Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada
# estudante concatenando-as para apresentar seus nomes completos na forma "Nome Sobrenome".
#
# As listas são:
# nomes = ["joão", "MaRia", "JOSÉ"]
# sobrenomes = ["SILVA", "souza", "Tavares"]
#
# O texto exibido ao fim deve ser parecido com:
# "Nome completo: Ana Silva"
#
# Dica: Utilize a função map para mapear os nomes e sobrenomes
# e as funções de string para tratar o texto.
 
 

# Questão 8
# Como cientista de dados em um time de futebol, você precisa implementar novas
# formas de coleta de dados sobre o desempenho de jogadores e do time como um todo.
#
# Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas
# de números inteiros, representando os gols marcados e sofridos pelo time em cada
# partida do campeonato.
#
# A função deve retornar a pontuação do time e o aproveitamento em percentual,
# levando em consideração que:
# - Vitória vale 3 pontos
# - Empate vale 1 ponto
# - Derrota vale 0 pontos
#
# Para calcular o aproveitamento: razão entre a pontuação do time
# pela pontuação máxima que ele poderia receber.
#
# Para teste, utilize:
# gols_marcados = [2, 1, 3, 1, 0]
# gols_sofridos = [1, 2, 2, 1, 3]
#
# Provável texto exibido:
# "A pontuação do time foi de [pontos] e seu aproveitamento foi de [aprov]%"
 

 
# Questão 9
# Você recebeu o desafio de criar um código que calcula os gastos de uma viagem
# para uma das quatro cidades partindo de Recife:
# Salvador, Fortaleza, Natal e Aracaju.
#
# - Custo da diária do hotel: R$ 150,00 (todas as cidades)
# - Consumo do carro: 14 km/l
# - Valor da gasolina: R$ 5,00 o litro
# - Gastos com passeios e alimentação por dia: [200, 400, 250, 300] (respectivamente)
# - Distâncias de Recife até cada cidade: [850, 800, 300, 550] km
#
# Crie três funções:
# - gasto_hotel: calcula os gastos com hotel
# - gasto_gasolina: calcula os gastos com gasolina
# - gasto_passeio: calcula os gastos com passeio e alimentação
#
# Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife.
# Considere a viagem de ida e volta de carro.
#
# "Com base nos gastos definidos, uma viagem de [dias] dias para [cidade]
#  saindo de Recife custaria [gastos] reais"
 

 
# Questão 10
# Você iniciou um estágio em uma empresa que trabalha com processamento de
# linguagem natural (NLP). Sua líder requisitou que você criasse um trecho de
# código que recebe uma frase digitada pela pessoa usuária e filtre apenas as
# palavras com tamanho maior ou igual a 5, exibindo-as em uma lista.
#
# Dica: utilize as funções lambda e filter() para filtrar essas palavras.
# Para tratar a frase use replace() para trocar ',' '.' '!' e '?' por espaço.
# https://docs.python.org/pt-br/3/library/functions.html#filter
#
# Use a frase "Aprender Python aqui na Alura é muito bom" para testar o código.
 
