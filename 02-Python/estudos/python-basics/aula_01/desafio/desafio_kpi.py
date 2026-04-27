# ============================================================
#   Desafio: Cálculo de Bônus com Entrada do Usuário
# ============================================================

nome_usuario = input("Digite seu nome: ")
salario_usuario = float(input("Digite seu salário: "))  # Com a tipagem de float(), conseguimos fazer com que o usuário tenha liberdade em escrever tanto um valor númerico inteiro ou um valor númerico com casas decimais.
bonus_usuario = float(input("Digite seu bônus: "))
bonus_2024 = 1000 + salario_usuario * bonus_usuario   # Váriavel com o objetivo de realizar os cálculos para descobrir o valor do bônus final, além de priorizar mais organização.
print(f"Olá {nome_usuario}! O seu valor bônus foi de: {bonus_2024}")    # Mensagem ao usuário.

