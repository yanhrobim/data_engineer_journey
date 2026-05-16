# =======================================================================================================================
#   Integre no projeto anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas
# =======================================================================================================================

try:
    while True:             # Condição verdadeira, "loop infinito".
        try:

            nome_usuario = str(input("Digite seu nome: ")).strip().replace(" ", "")

            if nome_usuario.isalpha():      # Condição que impede que o nome seja algum valor númerico. Ex: 10 
                                                    # O comando isalpha() garante que na resposta (string) contenha somente respostas com valores alfabéticos, retornando True para aqueles valores que só possuem letras e False para valores que possuem números, espaços ou caracteres especiais.
                                                    # Se o usuário colocar valores númericos como nome, irá ter o retorno de erros.
                pass
            else:
                raise ValueError("O valor passado está incorreto! Escreva um valor tipo string! (De preferência um nome)")
            
            if len(nome_usuario) < 3:
                raise ValueError("Nome incorreto! O nome inserido possuí menos de 3 carácteres, nome inválido!")
            

        except ValueError as e:
            print(e)

        else:
            print("Nome verificado e correto!")
            break       # Para quebrar o loop infinito, quando não ocorrer nenhuma exeção no try, o else é rodado com um 'break' que trava o loop.
                        # Lógicamente, se chegar neste else, significa que o valor está correto.

    while True:
        try:
            salario_usuario = input("Digite seu salário: ") # não pode ser negativo. não pode ser vázio. não pode ser string

            if float(salario_usuario) < 0 or float(salario_usuario) == 0:
                raise ValueError("O valor do salário não pode ser negativo ou zero! Tente novamente!")
            else:
                pass

        except ValueError as e:
            print(e)

        else:
            print("Salário verificado e correto!")
            break

    while True:
        try:
            bonus_usuario = input("Digite seu bônus: ")

            if float(bonus_usuario) < 0 or float(bonus_usuario) == 0:
                raise ValueError("O valor do bônus não poder ser igual ou menor que 0! Não foi possível fazer o bônus 2024 ;( Tente novamente!")
                
            else:
                pass


        except ValueError as e:
            print(e)
        
        else:
            print("Bonûs verificado e correto!")
            break

except Exception as e:
    print(f"Ocorreu uma execeção! Detalhes da parte do erro: {e}")
else:
    bonus_2024 = 1000 + float(salario_usuario) * float(bonus_usuario)
    print(f"Olá {nome_usuario}, o seu valor bônus de 2024 é: {bonus_2024}")