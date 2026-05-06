# ============================================================================
#   Desafio: Refatorar e Adicionar Tratamento de Erros no Desafio Aula 01
# ============================================================================


try:
    nome_usuario = str(input("Digite seu nome: ")).strip()

    nome_para_verificação = nome_usuario.strip().replace(" ", "")
    print(nome_para_verificação)

    if nome_para_verificação.isalpha():      # Condição que impede que o nome seja algum valor númerico. Ex: 10 
                                             # O comando isalpha() garante que na resposta (string) contenha somente respostas com valores alfabéticos, retornando True para aqueles valores que só possuem letras e False para valores que possuem números, espaços ou caracteres especiais.
                                             # Se o usuário colocar valores númericos como nome, irá ter o retorno de erros.
        pass
    else:
        raise ValueError

    if not nome_para_verificação == "":     # Se a resposta de input não for igual a = "" (nada), retorna erro. 
                                            # Ou seja, se o usuário não colocar nada como resposta, terá erro.
        pass
    else:
        raise print("O valor passado é uma String vázia! Digite um nome!")

            
except ValueError as e:
    print("O tipo do valor passado está incorreto! Escreva um valor tipo String!")

try:
    salario_usuario = input("Digite seu salário: ") # não pode ser negativo. não pode ser vázio. não pode ser string

    if float(salario_usuario) < 0 or float(salario_usuario) == 0:
        raise print("O valor do salário não pode ser negativo ou zero! Tente novamente!")
    else:
        pass

    if not salario_usuario.strip().isdigit():       # isdigit() percorre a resposta do input, e tem o principal objetivo de encontrar SOMENTE valores númericos. Se tiver somente valores númericos ele retorna True, se não, retorna False.
                                                    # Resumidamente, se a condição de ter somente valores númericos NÃO FOR atendida, retorna o raise, e se for, o else.
        raise ValueError
    else:
        pass

except ValueError as e:
    print("Ops! Parece que você inseriu uma resposta diferente de um valor númerico! Digite um valor númerico!")
    print(f"Detalhes do Erro: {e}")

try:
    bonus_usuario = input("Digite seu bônus: ")

    if float(bonus_usuario) < 0 or float(bonus_usuario) == 0:
        print("O valor do bônus não poder ser igual ou menor que 0! Não foi possível fazer o bônus 2024 ;( Tente novamente!")
        
    else:
        pass

    if not bonus_usuario.strip().isdigit():       # isdigit() percorre a resposta do input, e tem o principal objetivo de encontrar SOMENTE valores númericos. Se tiver somente valores númericos ele retorna True, se não, retorna False.
                                                    # Resumidamente, se a condição de ter somente valores númericos NÃO FOR atendida, retorna o raise, e se for, o else.
        raise ValueError
    else:
        pass

except ValueError as e:
    print(f"Você digitou algum valor do tipo errado!")
    print(f"Detalhes do erro: {e}")