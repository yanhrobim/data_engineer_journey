# ==========================================
#     EXERCICÍCIOS CONTROLES DE FLUXO
# ==========================================

# ======================
#        WHILE
# ======================

### Exercício 1. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

palavra_chave = ''

while palavra_chave != 'sair':
    print("Digite 'sair' para sair do loop...")
    palavra_chave = input("Digite se quer continuar no loop ou sair! ")
    if not palavra_chave == 'sair':
        palavra_chave = input("Digite se quer continuar no loop ou sair! ")

print("Você saiu do loop!")


### Exercício 2. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

numero_user = int(input("Digite um número de 1 a 10: "))

while numero_user < 1 or numero_user > 10:
    print("Você digitou um número que não corresponde com o intervalo de 1 a 10!")
    numero_user = int(input("Digite novamente um número de 1 a 10: "))
print(f"Você digitou: {numero_user}. O número está no intervalo de 1 a 10.")


### Exercício 3. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

pagina = 1
paginacao_max = 6

while pagina < paginacao_max:
    pagina_user = print(f"Você está na página {pagina}!")
    pagina += 1
print("Todas as páginas foram acessadas!")


### Exercício 4. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

import random

reconexão = random.randint(1, 10)
numero_user_reconexao = int(input("Ops! Você caiu! Digite um número de 0 a 10 para continuar, e se acertar o número você reconecta: "))
tentativas = 5
while numero_user_reconexao != reconexão:
    print("Você não acertou! E consequentemente perdeu uma tentativa")
    numero_user_reconexao = int(input(f"Você tem o total de {tentativas} tentativas para tentar reconectar! Digite mais uma vez: "))
    tentativas -= 1
    if tentativas == 0:
        print("Você perdeu todas as tentativas :( ")
        break
print("Reconexão estabelecida!")


### Exercício 5. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

# Uma lista com valores.
# FOR para iterar os valores da lista.
# Até WHILE achar valor especifico, roda o bloco, se achar break.

lista_de_codigos = ["200", "301", "302", "307", "429", "500"] # Códigos HTTP que são tipo WARNING, aqueles que recebemos
# mas não damos atenção no ínicio até dar problema :)
codigo = 0
while codigo != "500":
    print("WARNING!!!")
    if lista_de_codigos[codigo] == '500':      # Se locomovemos pela lista para o próximo valor através de 'codigo',
                                               # onde 'codigo' é igual a 0 no ínicio e se adiciona +1 a cada volta do loop.
                                               # A váriavel código funciona como index da lista, até encontrar o index
                                               # igual a 500, ele não para.
                                               # A iteração ocorre através de uma simulação de index com uma váriavel que
                                               # de valor númerico que se adiciona +1 através do loop.
                                               # Seria por exemplo eu armazenar em uma váriavel o valor de
                                               # lista_de_codigos[5] = "500".
        print("ERROR!!! PARADA ENCONTRADA!")
        break
    print(f"Resposta do Servidor: {lista_de_codigos[codigo]}")
    codigo += 1