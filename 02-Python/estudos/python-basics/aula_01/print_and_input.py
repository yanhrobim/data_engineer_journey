# ==========================================
#           PRINT E INPUT
# ==========================================

# Em Python, funções são invocada com parênteses.
# Algo já criado anteriormente, que pode ser utilizado para criar funções, classes, ou aquilo que tiver interesse.


# 1. Print()

print("Hello World!!!")     # Print() é o comando utilizado para exibir dados na tela (Terminal).
                            # Transforma aquilo que é passado dentre os () em texto e exibe.

# ==========================================
#           EXEMPLOS COM PRINT()
# ==========================================


print(3)    # Não somente possível exibir somente comentários, mas sim tipos númericos.

print(5 + 5)    # Exibindo uma soma de números.

print("Hello" + " " + "World")    # A soma não é somente limitada a tipos númericos no Print(), e sim também possível entre strings.
                                  # Chamando esta operação de uma forma mais complexa: Concatenar Strings.


# 2. Input()

input("Digite o nome do usuário: ")    # Este comando tem o principal objetivo de capturar dados do usuário.
                                             # Na execução do comando, o programa pausa sua execução na espera, até que o usuário digite algo no console (Terminal) e pressione Enter.
                                             # Os dados inseridos pelo mesmo usuário são retornados como texto (string).
                                             # Semelhante a um sistema de login de um site web, a fim de captar dados do usuário, armazenar, etc.

# ==========================================
#           EXEMPLOS COM INPUT()
# ==========================================


print("__________________________________\n" +input("Qual a nova senha do seu banco? (Não é Golpe) "))
print("__________________________________\n" + input("Certeza que a senha está correta? (Y/N) "))
# Nestes exemplos é mostrado que é possível concatenar respostas do usuário (Input) + exibir dados no Terminal com Print().
# O exemplo teve o objetivo de simular uma quebra de linha no terminal após o usuário responder as perguntas.



