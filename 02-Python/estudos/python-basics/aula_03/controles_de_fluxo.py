# ======================
#          IF
# ======================
# Define condições no código, se condição do if for cumprida, roda aquilo que está implementado dentro do bloco do if e ignora o elif/else.
# Se condição de if não for cumprida, verifica condição do elif e assim por diante até encontrar um condição verdadeira e ignora o resto.
# (No caso de haver milhares de if, o código executa aqueles no qual condição é cumprida mesmo que os acima tenham sido executados, mas a estrutura com elif, executa apenas o primeiro verdadeiro).
# Se por ventura não encontrar nenhuma condição cumprida, executa o bloco de else se houver, caso contrário continua com o fluxo normalmente.

idade = 30

if idade >= 12 and idade <= 17:         # Se idade for maior ou igual a 12 e menor ou igual a 17, executa o bloco de código if:
                                        # Se não, continua e ignora o código dentro do bloco.
    print("Você é um adolescente!")
elif idade >= 18 and idade <= 29:
    print("Você é um jovem adulto!")
elif idade >= 30 and idade <= 59:
    print("Você é um adulto!")
else:
    print("Você é um idoso!")

# Na estrutura de if com elif, a primeria condição verdadeira desativa as outras.
# Então, se o primeiro if a condição for cumprida todos os elif e else são ignorados. (Sempre importante ter em mente que condições importantes devem vir primeiro, pois nesta estrutura pode conter condições mortas após a primeira ser cumprida)
# Porém se o primeiro if a condição não for cumprida, o código continua até achar a primeira a ser cumprida, se não achar executa o else.


# ======================
#          FOR
# ======================

# ======================
#         WHILE
# ======================