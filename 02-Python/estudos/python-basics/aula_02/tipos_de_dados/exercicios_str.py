# ==========================================
#        EXERCICÍCIOS STRINGS(str)
# ==========================================

# 1. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

string = input("Digite um texto: ")
print(f"Nome em maiúsculas: {string.upper()}")    # Comportamento de Objetos str(), que transforma toda a string em letras maiúsculas.


# 2. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome_completo = input("Digite seu nome completo: ")
print(f"Nome em minúsculas: {nome_completo.lower()}")     # Comportamento de Objetos str(), que transforma toda a string em letras minúsculas.


# 3. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input("Digite sua frase (Com espaços em brancos no inicio e final): ")
print(f"Frase sem espaços em brancos inicio e final: {frase.strip()}")       # O comando strip() remove todos os espaços em branco no início e no final de uma string.

# 4. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input("Digite sua data de nascimento em formato (dd/mm/aa) com barras: ")
dia, mes, ano = data.split("/")      # split() é um comando Python que divide uma string em uma lista de substrings, por padrão sendo dividido por espaços dentro da string.
                                     # Com a adição do parâmetro 'sep' conseguimos dizer ao comando qual será o caractere que irá dividir a string em substrings. No caso sendo '/'.
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

# 5. Escreva um programa que concatene duas strings fornecidas pelo usuário.

string1 = input("Digite uma string para concatenação: ")
string2 = input("Digite a segunda string para concatenação: ")
print(f"Texto Concatenado: {string1 + " " + string2}")  # Uso de um espaço entre " " para as strings não serem imprimidas juntas.
