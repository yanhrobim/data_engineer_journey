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


# # =========================
# #         TypeError
# # =========================
# Erro para métodos utilizados no tipo de dado errado.
# Tipos de Dados possuem métodos que podem ser executados em outros tipos de dados, ou não (Ex: int() e float()), o TypeError justamente gera um erro e sinaliza quando você utiliza o método não compatível com aquele tipo de dado em específico.

texto_1 = "Data Engineer"
try:
    dividir = texto_1 / 2
except TypeError as e:
    print(f"Ocorreu o seguinte erro: {e}")
    print("Ops, parece que você escreveu um metódo para o tipo de dado errado!")
else:
    print(texto_1)

