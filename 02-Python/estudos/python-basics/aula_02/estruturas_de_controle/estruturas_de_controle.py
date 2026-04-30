# # =========================
# #        try-except
# # =========================

try:                # Tente isto:     
    numero_inteiro_1 = int(input("Digite um número inteiro para somar: "))
    numero_inteiro_2 = int(input("Digite o segundo número inteiro para somar: "))
    soma = numero_inteiro_1 + numero_inteiro_2
except ValueError as e:  # Se ocorrer o erro 'ValueError' na execução, faça isso:
    print(f"Ocorreu o erro: {e}. \nParece que você não colocou o tipo de dado correto para a soma de números inteiros!")
    pass
else:                # Se der tudo certo e não ocorrer exeções na execução, faça isso:
    print(f"A soma de {numero_inteiro_1} + {numero_inteiro_2} é: {soma}")
finally:             # Independente se der errado ou certo, faça isso:
    print("____________________________________________________")


# # =========================
# #         TypeError
# # =========================
# Erro para métodos utilizados no tipo de dado errado.
# Tipos de Dados possuem métodos que podem ser executados em outros tipos de dados, ou não (Ex: int() e float()), o TypeError justamente gera um erro e sinaliza quando você utiliza um método não compatível com aquele tipo de dado em específico.

texto_1 = input("Digite duas palavras interessantes :) ")   # Ex: Data Engineer.
try:
    dividir = texto_1 / 2
except TypeError as e:
    print(f"Ocorreu o seguinte erro: {e}")
    print("Ops, parece que você escreveu um metódo para o tipo de dado errado!")
else:
    print(texto_1)

# # ======================
# #        if-else
# # ======================
# if é uma estrutura de controle de fluxo onde toma decisões através de condições.
# Se caso tal condição for True para if, o bloco de código indentado é executado. Caso tal condição for igual a False o bloco de código é ignorado.

idade = int(input("Digite sua idade: "))        # TypeConversion para a resposta não ser outro tipo de dado, caso for: ValueError.
IDADE_MINIMA_USA = 16       
IDADE_MINIMA_BRASIL = 18
IDADE_MINIMA_REINO_UNIDO = 17       # Impondo constantes para definir valores fixos.
                                    # Uma constante é um valor fixo, uma configuração, que não é e não pode ser alterado durante a execução do código/programa.
                                    # Aqui nossas constantes definem os valores fixos onde tal idade pode tirar CNH em seus respectiveis países.
IDADE_MINIMA_IRLANDA = 17
if idade >= IDADE_MINIMA_USA:               # 'Se' idade for maior que o valor fixo da constante 'IDADE_MINIMA_USA', execute isso:
    print("Você pode tirar CNH nos Estados Unidos.")

else:   # 'Se não', execute isso:
    print("Você não poderia tirar CNH nos Estados Unidos.")

if idade >= IDADE_MINIMA_BRASIL:
    print("Você pode tirar CNH no Brasil.")

else:
    print("Você não poderia tirar CNH no Brasil.")

if idade >= IDADE_MINIMA_REINO_UNIDO:
    print("Você pode tirar CNH no Reino Unido.")

else:
    print("Você não poderia tirar CNH no Reino Unido.")

if idade >= IDADE_MINIMA_IRLANDA:
    print("Você pode tirar CNH na Irlanda.")

else:
    print("Você não poderia tirar CNH na Irlanda.")


# # =========================
# #        TypeCheck
# # =========================
# O processo de verificar o tipo de uma váriavel.

numero_ponto_flutuante = float(input("Digite um número de ponto flutuante: "))
if isinstance(numero_ponto_flutuante, float):       # isinstance() pode verificar o tipo de dado de uma váriavel passada. Semelhante a type().
                                                    # Aqui tem o objetivo de verificar se a variável passada como paramêtro tem o tipo de dado float().
    print("A resposta passada é um float()!")
else:
    print("A resposta passada não é um float()!")
    print(f"Na verdade o tipo de {numero_ponto_flutuante} é: {type(numero_ponto_flutuante)}")

# # =========================
# #     TypeConversion
# # =========================
# Também conhecida como Casting, pode referenciar ou mudar o tipo de uma váriavel.
 

numero_int = input("Digite um número inteiro: ")
numero_float = input("Digite um número de ponto flutuante: ")
soma = int(numero_int) + float(numero_float) # Aqui precisamos lembrar que input() retorna str() como padrão.
                                             # Mesmo que ele retorne str(), aplicamos um TypeConversion nas váriaveis automaticamente mudando os tipos delas.
                                             # É importante lembrar que as respostas precisam ser int() e float() mesmo input() retornando string, pois se alguma váriavel conter resposta igual a um texto, o código da erro. (Caso de try-except)
print(soma)

# # Em Python podemos mudar o tipo de uma váriavel para outro, com o TypeConversion, ou também conhecido como 'casting'.
# # Além de mudar, também referenciar antes mesmo de tal valor chegar a ser executado na soma, adicionando o tipo de dado que deve ser armazenado pela váriavel. Ex: numero_float = (float(input("Digite um número de ponto flutuante: ")))