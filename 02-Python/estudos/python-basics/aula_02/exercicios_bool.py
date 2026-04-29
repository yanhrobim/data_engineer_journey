# ==========================================
#      EXERCICÍCIOS BOOLEANOS(bool)
# ==========================================
# Operadores lógicos, que sempre comparam alguma coisa com outra.

# 1. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

expressao1 = input("Digite a primeira expressão (True ou False): ")
expressao2 = input("Digite a primeira expressão (True ou False): ")
resultado = expressao1 and expressao2
print(f"Resultado: {resultado}")


# 2. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

expressao1 = input("Digite a primeira expressão (True ou False): ")
expressao2 = input("Digite a primeira expressão (True ou False): ")
resultado = expressao1 or expressao2
print(f"Resultado: {resultado}")


# 3. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

expressao1 = input("Digite a expressão (True ou False): ")
resultado = not expressao1
print(f"Resultado: {resultado}")


# 4. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

num1 = int(input("Digite um valor númerico: "))
num2 = int(input("Digite o segundo valor númerico: "))
resultado = num1 == num2
print(f"Os números são iguais? {resultado}")

# 5. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

num1 = int(input("Digite um valor númerico: "))
num2 = int(input("Digite o segundo valor númerico: "))
resultado = num1 != num2
print(f"Os números são diferentes? {resultado}")