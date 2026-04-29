# # =========================
# #        try-except
# # =========================

try:                # Tente isto:
    numero_inteiro_1 = int(input("Digite um número inteiro para somar: "))
    numero_inteiro_2 = int(input("Digite o segundo número inteiro para somar: "))       
    soma = numero_inteiro_1 + numero_inteiro_2
except ValueError as e:  # Se ocorrer o erro 'ValueError' na execução, faça isso:
    print(f"Ocorreu o erro: {e}. \nParece que você não colocou o tipo de dado correto para a soma de números inteiros!")
else:                # Se der tudo certo e não ocorrer exeções na execução, faça isso:
    print(f"A soma de {numero_inteiro_1} + {numero_inteiro_2} é: {soma}")
finally:             # Independente se der errado ou certo, faça isso:
    print("____________________________________________________")

