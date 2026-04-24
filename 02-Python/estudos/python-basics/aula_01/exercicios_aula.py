# ==========================================
#           MINI-EXERCICÍCIOS
# ==========================================

# Exercício 1: Crie um programa que o usuário digita o seu nome e retorna o número de caracteres.

print(len(input("Digite o nome do usuário: ")))     # Utilizando o print para exibir aquilo que dentro do () está imposto.
                                                    # Dentro do () está imposto para o comando len (que conta caracteres de uma string), contar aquilo que for respondido ao Input().
                                                    # Se eu responder no Terminal com Yan, o mesmo me retorna 3 na linha abaixo. 


# Exercício 2: Criar um programa onde o usuário digite dois valores numéricos e retorne a soma.

print(int(input("Digite um número para soma: ")) + int(input("Digite o segundo número para soma: ")))
# Utilizei uma tipagem mais complexa para a resolução do mini exercício.
# A tipagem neste contexto transforma o nosso Input() com int(), com que a resposta do usuário seja um valor númerico inteiro, e que caso ao contrário gere até erro.
# O objetivo é que o exercício gere a soma de valores númericos, sem a tipagem as respostas são consideradas strings, sendo uma configuração padrão do comando Input().
# Sem esta tipagem, a resposta em string é retornada desta forma: Primeiro Número: 10 + Segundo Número: 10 = 1010.


# Exercício 03: Refatore o exercício 02 atribuindo variáveis.

valor_1 = int(input("Digite um número para soma: "))
valor_2 = int(input("Digite um segundo número para soma: "))
print(valor_1 + valor_2)

# Uma observação importante é que infelizmente temos algumas portas abertas a bugs neste sistema, um exemplo seria se caso o usuário quisesse passar um número com casas decimais.

