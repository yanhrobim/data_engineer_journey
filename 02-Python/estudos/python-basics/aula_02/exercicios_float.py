# # ==========================================
# #   EXERCICÍCIOS PONTOS FLUTUANTES(float)
# # ==========================================

# # 1. Escreva um programa que receba dois números flutuantes e realize sua adição.

# valor1 = float(input("Digite um número flutuante (float) para adição: "))
# valor2 = float(input("Digite o segundo número flutuante (float) para adição: "))
# print(f"O resultado da adição entre os números fluantes são: {valor1 + valor2}")


# # 2. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.


# valor1 = float(input("Digite um número flutuante (float) para calcular a média: "))
# valor2 = float(input("Digite o segundo número flutuante (float) para calcular a média: "))
# soma = valor1 + valor2
# media = soma / 2
# print(f"A média dentre os números flutuantes passados é: {media}") # Calcúlo para descobrir a média de valores: soma dos elementos/valores passados | dividido pela quantidade de elemtentos/valores passados.

# # 3. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# valor1 = float(input("Digite a base para o cáculo da potência: "))
# valor2 = float(input("Digite o expoente para o cáculo da potência: "))
# potencia = valor1 ** valor2
# print(f"A potência do valor base {valor1} com o expoente de {valor2} tem o resultado da operação em: {potencia}")
# # Tanto Objetos float() quanto objetos int() possuem o comportamento (operador) '**' que eleva um número a potência de outro.
# # Seguindo esta lógica, elevamos o valor1 a potência do valor2.

# # 4. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# graus_celcius = float(input("Digite uma temperatura em Celcius para ser convertida a Fahrenheit: "))
# temperatura_fahrenheit = graus_celcius * 1. + 32    # Também existe uma formúla alternativa sendo: valor1 * 1,8 + 32.
# print(f"A temperatura de {graus_celcius} Graus Celsius é igual a: {temperatura_fahrenheit} em Fahrenheit!")

# 5. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

import math

raio = float(input("Digite o raio para descobrirmos a área do círculo: "))
area = math.pi * raio ** 2      # Importando o método math que o próprio Python disponibiliza, a fim de importar o número de pi com todas as casas decimais.
                                # Todas as casas decimais com precisão importam, se caso fazermos com apenas com o valor de '3.14', as respostas finais terão irregularidades.
print(f"A área do círculo com raio de {raio} é igual a: {area:.2f}")    # Aplicando o formato de duas casas decimais a resposta que será exibida pelo print. OBS: Não altera a resposta final diretamente, e sim somente a forma que será exibida.



