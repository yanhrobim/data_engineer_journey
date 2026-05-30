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

# Meu raciocínio:
# 1. Descobrir o tamanho da lista, resumidamente, quantos valores tem a lista.
# 2. Descobrir o maior valor da lista e menor valor. (max() e min())
# 3. Somar todos os valores que a lista contém.
# 4. Colocar todas as respostas em váriaveis, sendo: tam, maior, menor e soma.
# 5. Exibir no print.

lista: list = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

tam = len(lista)
maior = max(lista)
menor = min(lista)
soma_valores = sum(lista)

print(f"A lista possui {tam} números em que, o maior número é {maior} e o menor número é {menor}. A soma dos valores pares presentes nela é igual a {soma_valores}.") 

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
  
# Meu raciocínio:
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

numero: int = 4
tabuada(4)

# Resposta de Exemplo:
# 4 x 0 = 0
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 4 x 6 = 24
# 4 x 7 = 28
# 4 x 8 = 32
# 4 x 9 = 36
# 4 x 10 = 40

# Questão 3
# Crie uma função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:
# [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
#
# Utilize o return na função e salve a nova lista na variável mult_3.
 
# Meu raciocínio:
# 1. Criar uma função que receba um parâmetro sendo a iterável list.
# 2. Criação de uma lista vázia, sendo a lista que futuramente será populada com os valores múltiplos por 3.
# 3. Individualizar cada elemento da lista.
# 4. Após a individualização, fazer uma condição, sendo: Se número da lista dividido por 3 resultar em resto 0, adicionar este número na lista.
# 5. O retorno da função deve ser a lista.

lista_valores_numericos: list = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def multiplo_3(lista_de_valores_numericos: list[int]):
    lista_multiplo_3 = []
    for numero in lista_de_valores_numericos:
        if numero % 3 == 0:     # Se resultado que for armazenado em numero for maior que zero, executa o bloco.
            lista_multiplo_3.append(numero) # Adicionamos os números que passamos pelo filtro.
    
    return lista_multiplo_3

mult_3 = multiplo_3(lista_valores_numericos)
print(f"Os valores múltiplos por 3 dentre os valores númericos passados na lista são: {mult_3}")

# Questão 4
# Crie uma lista dos quadrados dos números da seguinte lista:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Lembre-se de utilizar as funções lambda e map() para calcular
# o quadrado de cada elemento da lista.
 
lista_quadrados: int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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
 
# Meu raciocínio:
# 1. Receber 5 váriaveis que contém valores númericos, que representa as notas.
# 2. Adicionar as notas em uma lista vázia.
# 3. Dentre as 5 notas, excluir a maior nota e a menor. (max() e min())
# 4. Fazer uma média com as notas que sobraram.
# 5. Retornar a váriavel que possui o valor de média.

nota_1: int = int(input("Digite sua primeira nota: "))
nota_2: int = int(input("Digite sua segunda nota: "))
nota_3: int = int(input("Digite sua terceira nota: "))
nota_4: int = int(input("Digite sua quarta nota: "))
nota_5: int = int(input("Digite sua quinta nota: "))

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

def media_estudante(notas_estudante: list):
    maior_nota = max(notas_estudante)
    menor_nota = min(notas_estudante)
    media = sum(notas_estudante) / len(notas_estudante)

    if media >= 5:
        situacao = "Aprovado(a)"
        print(f"O(a) estudante obteve uma media de {media}, com a sua maior nota de {maior_nota} pontos e a menor nota de {menor_nota} pontos e foi {situacao}!")
    else:
        situacao = "Reprovado(a)"
        print(f"O(a) estudante obteve uma media de {media}, com a sua maior nota de {maior_nota} pontos e a menor nota de {menor_nota} pontos e foi {situacao}!")


lista_notas: list = [3, 5, 4, 4]
media_estudante(lista_notas) 

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
 
# Meu raciocínio:
# 1. Individualizar nome por nome e sobrenome, e colocar todos em lower().
# 2. Obter a primeira letra de cada nome e sobrenome e adicionar upper().
# 3. Após estiverem manipulados e corretos, concatenar em formato Nome Sobrenome. (Com map())

# OBS: A medida que fui desenvolvendo a solução, descobri dois métodos para a solução da questão.
# Sendo 1 solução com list comprehension + lambda e map() e outra utilizando função lambda e map() três vezes.


# 1. List Comprehension

nomes: list = ["joão", "MaRia", "JOSÉ"]
sobrenomes: list = ["SILVA", "souza", "Tavares"]


nomes = [nome[:1].upper() + nome[1:].lower() for nome in nomes]
    # Explicando um pouco sobre o código, uma string podemos trata-la com index.
    # Quando fazemos [:1] significa que queremos pegar a primeira letra de uma string, faço isso e entrego ela ao upper() para deixa-la em maiúsculo.
    # Quando fazemos [1:] significa que queremos ter tudo aquilo apartir do index 1. Ou seja, apagamos a primeira letra de cada nome.
    # Como fim, concatenamos as strings manipuladas.

sobrenomes = [sobrenome[:1].upper() + sobrenome[1:].lower() for sobrenome in sobrenomes]

nome_sobrenome = map(lambda nome, sobrenome: nome + " " + sobrenome, nomes, sobrenomes)
print(list(nome_sobrenome))

# 2. Função lambda + map()

nomes: list = ["joão", "MaRia", "JOSÉ"]
sobrenomes: list = ["SILVA", "souza", "Tavares"]

nomes_corretos = map(lambda nome: nome[:1].upper() + nome[1:].lower(), nomes)
    # Explicando um pouco sobre o código, uma string podemos trata-la com index.
    # Quando fazemos [:1] significa que queremos pegar a primeira letra de uma string, faço isso e entrego ela ao upper() para deixa-la em maiúsculo.
    # Quando fazemos [1:] significa que queremos ter tudo aquilo apartir do index 1. Ou seja, apagamos a primeira letra de cada nome.
    # Como fim, concatenamos as strings manipuladas.

sobrenomes_corretos = map(lambda sobrenome: sobrenome[:1].upper() + sobrenome[1:].lower(), sobrenomes)

nome_sobrenome = map(lambda nome, sobrenome: nome + " " + sobrenome, nomes_corretos, sobrenomes_corretos)

print(list(nome_sobrenome))


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

# Meu raciocínio:
# 1. Criar uma função que recebe duas listas de inteiros como parâmetros.
# 2. Regras de négocio:
    # "Regras de Neǵocio": Vitoria = 3.
    # "Regras de Neǵocio": Empate = 1.
    # "Regras de Neǵocio": Vitoria = 0.
    # "Regras de Neǵocio": Se gol marcado for maior que gol sofrido, o time venceu.
    # "Regras de Neǵocio": Se gol marcado for menor que gol sofrido, time perdeu.
    # "Regras de Neǵocio": Se a quantidade de gol sofrido e gol marcado for a mesma, houve empate.

# 3. Descobrir a quantidade total de pontos que o time obteve no campeonato.
    # Criar uma váriavel de pontos para ser populada com dados. Começando o loop com valor = 0, 
    # porém a medida que condições forem atendidas, pontos vão subindo. Caso vitoria + 3, caso empate + 1.
    # Para isso, precisamos comparar cada valor númerico individualmente, porém entre duas listas.

# 4. Para descobrir o aproveitamento em porcetagem:
    # Cada valor númerico dentro da lista, significa uma partida. Ex: index 1 das duas listas, é igual uma partida no campeonato.
    # Para o calculo a lógica é: Quantidade de Pontos do Time Dividido Pela Quantidade Total Que Eles Poderiam Ter Feito. 
    # Formúla em Python: (len(gols_marcados)). Recebemos valor e fazemos: vitoria * resultado de len().
    # Após obtermos um resultado na lógica acima, armazenar em uma váriavel e dividir a quantidade de pontos do time
    # pelo valor obtido.


 
gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

def calculo_pontos(gols_marcados: list[int], gols_sofridos: list[int]):
    pontos = 0

    for marcado, sofrido in zip(gols_marcados, gols_sofridos):
    # Uma leve introdução ao zip(). Basicamente o zip() nos permite trabalhar com dois iteráveis em um único FOR.
    # Bem resumidamente, ele cria um par entre os iteráveis fornecidos, sendo pela sequẽncia no qual estão impostos dentro da estrutura de dados.
    # Se for lista, index 1 com index 1, se for dicionário chave 1 com chave 1. Não precisa necessariamente ser 
    # dois iteráveis iguais, mas a lógica de par é a mesma. Ex: Lista index 1, Dicionário Chave 1.
    # Uma observação, é que ele não possuí um limite de parâmetros, e segue o número de parâmetros que você impôs no For.
        if marcado > sofrido:
            pontos += 3
        if marcado == sofrido:
            pontos += 1

# Não adicionei nada relacionado a derrota, pois isso iria mais poluir a organização do código, a lógica é clara, se for derrota não acontece nada pois é zero da mesma forma.


    maior_pontuacao = 3 * len(gols_marcados)  
    # Aqui o número é 3, pois se queremos descobrir a maior pontuação que o time
    # poderia ter feito, ele teria ganhado todas as partidas.

    aproveitamento = pontos / maior_pontuacao

    print(f"A pontuação do time foi de {pontos} e seu aproveitamento foi de {round(aproveitamento, 2)}%")

calculo_pontos(gols_marcados, gols_sofridos) 
    
 
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

# Meu raciocínio:
# 1. Primeiro, temos que entender que uma função vai complementar a outra no final, então não temos que criar uma função de gastos de hotel, pensando nos gastos de gasolina.
# 2. Regras de Negócio:
    # Regra de Negócio: Cada dia no hotel é igual a 150,00 reais. 
    # Regra de Negócio: O consumo do carro de gasolina é 14 kilometros é igual a 1 litro.
    # Regra de Negócio: O valor da gasolina é 5 reais = 1 litro.
    # Regra de Negócio: Passeio e alimentação é 200 para Salvador, 300 para Fortaleza, e segue a sequência.
    # Regra de Negócio: A distância em kms é: 850 para salvador, 800 para Forteleza e segue a sequência.

# 3. Criar uma função que recebe uma váriavel, e retorna o resultado de 150,00 multiplicado pelos dias que será a viagem.
# 4. Criar uma função para os gastos da gasolina, considerando os kms de cada cidade, o carro faz 14 km = por 1 litro, e 5 reais é um litro.
    # A fórmula para litros é: Quantidade consumo carro DIVIDIDO(/) por Quantidade de km que teremos que percorrer.
    # A fórmula para descobrir os gastos é: valor da gasolina MULTIPLICADO(*) por litros que precisamos.

# 5. Criar uma função para gastos em passeios, considerando o mesmo gasto em todos os dias de cada cidade segundo a lista.
# 6. Todas as funções devem retornar uma váriavel contendo um valor númerico que significa os gastos e no final,
# somar todos os gastos e devolver o print.

def gastos_hotel(quantidade_dias: float):
    
    gastos_com_hotel = 150.00 * quantidade_dias
    return gastos_com_hotel

def gastos_gasolina(cidade_viagem: str, consumo_carro: float, valor_gasolina: float):
    
    cidades: list = ["Salvador", "Fortaleza", "Natal", "Aracaju"] # Estas são as cidades que podemos viajar.
    
    distancias: list = [850, 800, 300, 550]   # Estas são as distâncias de cada cidade, nessa lista o index 0 é a distância da primeira cidade da lista de cidades, assim por diante.
    
    cidade_user_index = cidades.index(cidade_viagem.strip().replace(" ", ""))    # Aqui descobrimos a posição/index que a cidade escolhida de viagem está na lista.
                                                    # Ex: Salvador retornaria 0.
    cidade_distancia =  list(zip(cidades, distancias))  
    # Tendo em vista, que na lista de cidade cada posição significa uma distância na lista de distância,
    # junto as duas listas com zip, e cada cidade tem sua respectiva distância, seguindo a lógica que expliquei.
    # Ex: (Salvador, 850)

    cidade_viagem = cidade_distancia[cidade_user_index] 
    # Aqui descobrimos qual a cidade que iremos ir dentro da lista passada e também possuímos a distância dela no index 1.
    # Digo index pois a váriavel está assim: ("Cidade", Distância). Está como tupla.

    # Precisamos descobrir o index da cidade em 'cidade_user_index' para encontramos a cidade que desejamos ir dentro da lista de cidades disponíveis.
    # Com o index, sinalizamos a tupla que o zip() devolve, qual o valor que queremos ter para os cálculos.

    quantidade_de_litros = cidade_viagem[1] / consumo_carro # Como eu disse index 1, possuí a distância. Esta divisão retorna a quantidade litros que precisamos para ir até a cidade desejada.
    
    gastos_com_gasolina = valor_gasolina * quantidade_de_litros

    return gastos_com_gasolina  * 2 # Considerando ida e volta.

def gastos_passeio(cidade_viagem: str, quantidade_dias: int):

    cidades: list = ["Salvador", "Fortaleza", "Natal", "Aracaju"]

    lazer_valores: list = [200, 400, 250, 300]

    cidade_user_index = cidades.index(cidade_viagem)

    cidade_valor_lazer =  list(zip(cidades, lazer_valores))

    cidade_viagem = cidade_valor_lazer[cidade_user_index]

    gasto_com_passeios = cidade_viagem[1] * quantidade_dias

    return gasto_com_passeios

def calculo_gastos_com_viagem(cidade_viagem: str, 
                              quantidade_dias: int, 
                              consumo_carro: int, 
                              valor_gasolina: int):    # Simulando um pipeline :)

    gastos_com_hotel = gastos_hotel(quantidade_dias)
    gastos_com_gasolina = gastos_gasolina(cidade_viagem, consumo_carro, valor_gasolina)
    gastos_com_passeio = gastos_passeio(cidade_viagem, quantidade_dias)
    gasto_total = gastos_com_hotel + gastos_com_gasolina + gastos_com_passeio
    print(f"Com base nos gastos definidos, uma viagem de {dias} dias para a cidade de {cidade} saindo de Recife custaria {round(gasto_total, 2)} reais")

cidade = input("Qual a cidade que você deseja ir? Escolha entre: [Salvador, Fortaleza, Natal, Aracaju] ")
dias: int = input("Quantos diárias você pretende ter? ")
consumo_carro: float = input("Quantos Km seu carro corre para gastar 1 litro? ")  # O exercício não pede estas váriaveis, mais adicionei para deixar a função mais aberta outros cenaŕios.
gasolina: float = input("Qual o valor da gasolina? ")  # Mesmo caso da váriavel acima.

calculo_gastos_com_viagem(cidade_viagem=cidade,
                          quantidade_dias=int(dias),
                          consumo_carro=float(consumo_carro),
                          valor_gasolina=float(gasolina))
 
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

# Meu racicínio:
# 1. Criar uma função que recebe uma string, sendo uma frase.
# 2. Utilizar o método split() para separar as palavras da frase e individualizar todas as palavras.
# 3. Adicionar uma condição, com len, onde len(palavra) deve retornar maior que 5.
# 4. Adicionar as palavras que possuem tamanho maior ou igual a 5.

frase =  "Aprender Python aqui na Alura é muito bom"
palavras = frase.split()
lista_palavras = [palavra for palavra in palavras if len(palavra) >= 5]
print(lista_palavras)
