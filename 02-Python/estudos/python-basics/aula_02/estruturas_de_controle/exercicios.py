# # ============================================
# #     EXERCICÍCIOS ESTRUTURAS DE CONTROLE
# # ============================================

# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
# garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

graus_celcius = input("Digite uma temperatura em Celcius para ser convertida a Fahrenheit (float) : ")
try:
    temperatura_fahrenheit = float(graus_celcius) * 1.8 + 32
except ValueError as e:
        print(f"Ops! Parece que o valor informado não é um número de ponto flutuante (float)! Detalhes do Erro: {e}")
        print(f"O valor passado: '{graus_celcius}' Tem o tipo de: {type(graus_celcius)}")
else:
    print(f"A temperatura de {graus_celcius} Graus Celsius é igual a: {temperatura_fahrenheit:.2f} em Fahrenheit!")


#Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.

import string

palavra_user = ""
# Preciso adicionar estes comandos no input(), pois assim que o usuário responder a resposta seja capturada sem espaços e em minúsculo. 
# Caso não tiver estes comandos para a manipulação de string, a resposta do usuário será diferente de todas as maneiras com a váriavel 'palavra_invertida' por conter espaços e ter a possibilidade de conter letras em maiúsculo.
# Sobre a pontuação, é preciso importar um módulo do Python chamado 'string' para importarmos o método 'string.punctuation'. 
# Este método, contém dentro dele todos caracteres espesciais como: '!'; '?'; '+'; '.'; etc.  
# Com translate() e str.maketrans() consigo fazer uma manipulação de string para remover (mais especificada trocar por '' que significa nada) tudo aquilo apontado pelo 'string.punctuation'. 

try:
        if isinstance(palavra_user, str):
                if not palavra_user == "" or palavra_user == " ":  # Filtro, considerando que uma string vázia não é um palíndromo!
                    palavra_user_limpeza = palavra_user.lower().replace(" ", "").strip().translate(str.maketrans('', '', string.punctuation))
                # Caso não tiver estes comandos para a manipulação de string, 
                # a resposta do usuário será diferente de todas as maneiras com a váriavel '
                # palavra_invertida' por conter espaços e ter a possibilidade de conter letras em maiúsculo.

                # Sobre a regra da pontuação, é preciso importar um módulo do Python chamado 'string' para importarmos o método 'string.punctuation'. 
                # Este método, contém dentro dele todos caracteres espesciais como: '!'; '?'; '+'; '.'; etc.  
                # Com translate() e str.maketrans() consigo fazer uma manipulação de string para remover (mais especificada trocar por '' que significa nada) tudo aquilo apontado pelo 'string.punctuation'. 
                
                # Os outros métodos ajudam a formatar a string para a verificação desconsiderar espaços e pontuações. 
                # (.replace() para remover espaços (no meio da string), .strip() para remover espaços inicio e fim, .lower() para transformar toda string em minúsculas)


                    palavra_invertida = palavra_user_limpeza[::-1]
                # [::-1] tem o objetivo de percorrer a string inserida pelo usuário de forma alternativa (de trás para frente).
                # (Imaginando que a string passada é uma lista) Com -1 sinalizamos que em vez de andar um para frente, vamos andar um para trás. Seria por exemplo uma operação de subtração, se temos 7 caracteres na string, começamos pelo 7 e vamos andando para trás 7-1 = 6 -1 = 5, assim por diante. Invés de 1,2,3,5,6,7.
                else:
                      raise ValueError


        else:
             raise ValueError

except ValueError:
        print(f"O valor passado não é uma String! Ou você passou uma String Vázia!")
else: 
    if palavra_invertida == palavra_user_limpeza:
        print("A palavra é um palíndromo!")
    else:
        print("A palavra não é um palindromo!")


# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.

entrada_numerica_1 = input("Digite um valor númerico para a operação de matemática: ")
entrada_numerica_2 = input("Digite o segundo valor númerico para a operação de matemática: ")
operacao = input("Digite a operação mátematica de sua preferência (Multiplicação(*), Divisão(/), Soma(+), Subtração(-) ): ").lower() # Adição do .lower() pois se o usuário escrever tanto SOMA, SomA, Soma, soma, irá ser considerado como resposta e a operação de soma será escolhida.
try:
    if operacao == "soma" or operacao == "+":
        soma = float(entrada_numerica_1) + float(entrada_numerica_2)
        print(f"A soma de {entrada_numerica_1} + {entrada_numerica_2} é igual a: {soma:.2f}")

    if operacao == "multiplicacao" or operacao == "multiplicação" or operacao == "*":
        multiplicacao = float(entrada_numerica_1) * float(entrada_numerica_2)
        print(f"A multiplicação de {entrada_numerica_1} por {entrada_numerica_2} é igual a: {multiplicacao:.1f}")

    if operacao == "divisao" or operacao == "divisão" or operacao == "/":
        divisao = float(entrada_numerica_1) / float(entrada_numerica_2)
        print(f"A divisão de {entrada_numerica_1} dividido por {entrada_numerica_2} é igual a: {divisao:.2f}")

    if operacao == "subtracao" or operacao == "subtração" or operacao == "-":
            subtracao = float(entrada_numerica_1) - float(entrada_numerica_2)
            print(f"A subtracao de {entrada_numerica_1} - {entrada_numerica_2} é igual a: {subtracao:.2f}")
except ValueError as e:
    print(f"O valor passado não é um valor númerico! Detalhes do Erro: {e}")
except ZeroDivisionError as e:
      print("O valor 0 não é aceito para a operação de divisão como divisor!")


# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica
# e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".

numero_user = input("Digite um número para descobrir se é positivo ou negativo: ")

if int(numero_user) > 0:
    print(f"O número {numero_user} é positivo!")
if int(numero_user) < 0:
    print(f"O número {numero_user} é negativo!")
if int(numero_user) == 0:
    print(f"O número {numero_user} é zero!")
if int(numero_user) % 2 == 0:                   # Para descobrir se um número é par ou impar utilizamos o método '%', que em um objeto int() executa uma divisão e retorna o resto.
                                                # A lógica consiste em algo básico, se a divisão do número inserido por 2 ter o resto igual a zero, o número é par pois é uma divisão exata.
                                                # Números impares deixam o resto igual a 1.    
    print(f"O número {numero_user} é par!")       
else:
    print(f"O número {numero_user} é impar!")


# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro.
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.


numeros_usuario = input("Digite uma série de números separados por vírgula (Ex: 1,2,3,4...): ").strip().replace(" ", "")
lista_numeros_usuario = numeros_usuario.split(",")
try:
    lista_numeros_int = []
    for numero in lista_numeros_usuario:       # Individualizando/repartindo cada valor presente na lista. 
                                               # Invés de a String ser: '1,2,3,5...', agora é: '1', '2'... 
                                               # Cada valor separademente do outro, por tanto que 
                                               # quando adicionamos os valores posteriormente na lista vázia 
                                               # são adicionandos um por um.
        lista_numeros_int.append(int(numero))
except ValueError as e:
    print("O valor passado não é um valor númerico!")
else:
    print(f"Lista de números: {lista_numeros_int}")