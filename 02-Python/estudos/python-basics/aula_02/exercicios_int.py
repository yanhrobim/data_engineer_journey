# ==========================================
#       EXERCICÍCIOS INTEIROS(int)
# ==========================================

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# valor_1 = int(input("Digite um número para soma: "))
# valor_2 = int(input("Digite o segundo número para soma: "))
# print(f"O valor da soma é: {valor_1 + valor_2}")


# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

valor = int(input("Digite um número (Será dividido por 5): "))
resto = valor % 5   # O caractere '%' além de fazer a divisão, nos retorna o resto do cálculo do número inserido dividido por 5.
print(f"O resto da divisão é: {resto}")


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

valor_1 = int(input("Digite um número para a multiplicação: "))
valor_2 = int(input("Digite o segundo número para multiplicação: "))
print(f"O valor da multiplicação é: {valor_1 * valor_2}")   # O caractere '*' faz uma operação de multiplicação.


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

valor_1 = int(input("Digite um número para a divisão (dividendo): "))
valor_2 = int(input("Digite o segundo número para a dividir o primeiro (divisor): "))
inteiro = valor_1 // valor_2
print(f"O valor inteiro da divisão é: {inteiro}")   # O objeto int() possuí o comportamento '//' que executa uma operação de divisão inteira e retorna o quociente. (Caso não conter resto, não sendo uma divisão inteira, resultado é igual a 0)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

valor = int(input("Digite um número para calcularmos o quadrado: "))
quadrado = valor * valor
print(f"O quadrado deste número é: {quadrado}. Operação: {valor} x {valor} = {quadrado}")   
# O valor quadrado de um número é basicamente ele multiplicado por ele mesmo, duas vezes. Tendo isso em vista, a lógica por trás do código é utlizar o caractere de multiplicação (comportamento int) '*'.
# Porém também existe uma outra meneira apresentanda pelo professor: número ** 2.
