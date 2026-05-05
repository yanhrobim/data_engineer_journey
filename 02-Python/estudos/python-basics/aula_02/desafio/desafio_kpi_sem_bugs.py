# ============================================================================
#   Desafio: Refatorar e Adicionar Tratamento de Erros no Desafio Aula 01
# ============================================================================


try:
    nome_usuario = input("Digite seu nome: ").strip()

    if not nome_usuario == "":
        pass
    else:
        raise print("O valor passado é uma String vázia! Digite um nome correto!")
            
except ValueError as e:
    print("O tipo do valor passado está incorreto! Escreva um valor tipo String!")
    print(f"Detalhes do Erro: {e}")


salario_usuario = input("Digite seu salário: ")  # Com o TypeConversion de float(), conseguimos fazer com que o usuário tenha liberdade em escrever tanto um valor númerico inteiro ou um valor númerico com casas decimais.
bonus_usuario = input("Digite seu bônus: ")
try:
    if not float(salario_usuario) < 0 or float(bonus_usuario) < 0:
        if not float(salario_usuario) == 0:
            bonus_2024 = 1000 + float(salario_usuario) * float(bonus_usuario) # Váriavel com o objetivo de realizar os cálculos para descobrir o valor do bônus final, além de priorizar mais organização.

            print(f"Olá {nome_usuario}! O seu valor bônus foi de: {bonus_2024}") 
        else:
            print("O valor de salário está igual a 0. Não foi possível fazer o bônus 2024 ;(")
    else:
        print("O valor do salário ou bônus está com saldo negativo. Não foi possível fazer o bônus 2024 ;(")
except ValueError as e:
    print(f"Você digitou algum valor do tipo errado! \nDetalhes do Erro: {e}")