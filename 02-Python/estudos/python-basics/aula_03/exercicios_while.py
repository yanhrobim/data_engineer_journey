# ==========================================
#     EXERCICÍCIOS CONTROLES DE FLUXO
# ==========================================

# ======================
#        WHILE
# ======================

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

palavra_chave = ''

while palavra_chave != 'sair':
    print("Digite 'sair' para sair do loop...")
    palavra_chave = input("Digite se quer continuar no loop ou sair! ")
print("Você saiu do loop!")

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

numero_user = int(input("Digite um número de 1 a 10: "))

while numero_user < 1 or numero_user > 10:
    print("Você digitou um número que não corresponde com o intervalo de 1 a 10!")
    numero_user = int(input("Digite novamente um número de 1 a 10: "))
print(f"Você digitou: {numero_user}. O número está no intervalo de 1 a 10.")


### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.