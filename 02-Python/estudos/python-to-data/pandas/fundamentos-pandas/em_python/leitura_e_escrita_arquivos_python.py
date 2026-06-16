# Dados que serão utilizados para a prática do conteúdo aprendido. :)
clientes = [
    {"id": 1, "nome": "Ana Lima", "cidade": "São Paulo", "compras": 5},
    {"id": 2, "nome": "Carlos Souza", "cidade": "Curitiba", "compras": 2},
    {"id": 3, "nome": "Fernanda Rocha", "cidade": "Belo Horizonte", "compras": 8},
    {"id": 4, "nome": "João Pedro", "cidade": "Recife", "compras": 1},
    {"id": 5, "nome": "Mariana Costa", "cidade": "Porto Alegre", "compras": 4},
    {"id": 6, "nome": "Rafael Mendes", "cidade": "Salvador", "compras": 7},
    {"id": 7, "nome": "Beatriz Alves", "cidade": "Fortaleza", "compras": 3},
    {"id": 8, "nome": "Lucas Teixeira", "cidade": "Manaus", "compras": 6},
    {"id": 9, "nome": "Camila Nunes", "cidade": "Brasília", "compras": 9},
    {"id": 10, "nome": "Diego Ferreira", "cidade": "Goiânia", "compras": 2},
]


# ===========================================
#    ESCRITA DE ARQUIVOS UTILIZANDO PYTHON
# ===========================================

with open("./dados_para_pratica/clientes.txt", "w", encoding="utf-8") as escrita:
    # with open é como se fosse uma função que abre e fecha automaticamente.
    # No segundo parâmetro pode ser "w" (write) que sobscrevre toda vez o arquivo com os dados novos ou
    # "a"(append) que adiciona os novos dados no arquivo.
    # O nome e caminho do arquivo é definido no primeiro parâmetro.

    for cliente in clientes:    # É preciso de um loop for para indivualizar os elementos, caso contrário, tudo é escrito na mesma linha.
        escrita.write(str(cliente) + "\n")  # É preciso transformar em string, para o write() aceitar, caso contrário, gera erro.
    
# Também existe a opção sem 'with' como feito acima, adicionando a função de abertura do arquivo a um parâmetro.
# Porém, é necessário adicionar ao código '.close()' para sinalizar quando fechar.


# ============================================
#    LEITURA DE ARQUIVOS UTILIZANDO PYTHON
# ============================================

with open("./dados_para_pratica/clientes.txt", "r", encoding="utf-8") as leitura: # Invés de 'w', aqui utilizamos 'r'(read) para ler o arquivo.
    leitura_arquivo = leitura.read()
print(leitura_arquivo)

# Resposta:
# {'id': 1, 'nome': 'Ana Lima', 'cidade': 'São Paulo', 'compras': 5}
# {'id': 2, 'nome': 'Carlos Souza', 'cidade': 'Curitiba', 'compras': 2}
# {'id': 3, 'nome': 'Fernanda Rocha', 'cidade': 'Belo Horizonte', 'compras': 8}
# {'id': 4, 'nome': 'João Pedro', 'cidade': 'Recife', 'compras': 1}
# {'id': 5, 'nome': 'Mariana Costa', 'cidade': 'Porto Alegre', 'compras': 4}
# {'id': 6, 'nome': 'Rafael Mendes', 'cidade': 'Salvador', 'compras': 7}
# {'id': 7, 'nome': 'Beatriz Alves', 'cidade': 'Fortaleza', 'compras': 3}
# {'id': 8, 'nome': 'Lucas Teixeira', 'cidade': 'Manaus', 'compras': 6}
# {'id': 9, 'nome': 'Camila Nunes', 'cidade': 'Brasília', 'compras': 9}
# {'id': 10, 'nome': 'Diego Ferreira', 'cidade': 'Goiânia', 'compras': 2}


# ======================================================
#    TIPO DE ARQUIVO CSV (UTILIZANDO SOMENTE PYTHON)
# ======================================================
# Para a leitura ou escrita de arquivos '.csv', é necessário a importação do módulo 'csv' disponibilizado pelo próprio Python.

# 1. Escrita de arquivos '.csv':

import csv

with open("./dados_para_pratica/clientes.csv", 'w', encoding="utf-8") as escrita_csv:

    colunas = ['id', 'nome', 'cidade', 'compras']   # O tipo de arquivo '.csv' possuí cabeçalho, que representa a coluna de cada dado.
                                                # Basicamente, significa as chaves de um dict, e aqui coloquei na ordem das chaves do dict 'clientes' para evitar dados em colunas erradas.

    csv_config = csv.DictWriter(escrita_csv, fieldnames=colunas)    
# O módulo 'csv' proporciona dois métodos para a escrita sendo o '.DictWriter()' ou o '.writer()'.
# A diferença é que '.DictWriter()' Espera receber um iterável do tipo dicionário.
# 'writer()' Espera receber um iterável do tipo lista.

    csv_config.writeheader()        # Aqui dizemos ao código que queremos escrever o cabeçalho.
                                # Caso contrário, somente os dados são escritos dentro do arquivo, sem colunas para referencia-los.

    for cliente in clientes:
        csv_config.writerow(cliente)    # Após individualizarmos cada elemento, escrevemos com 'writerow()'.

# 2. Leitura de arquivos '.csv':

with open("./dados_para_pratica/clientes.csv", 'r', encoding="utf-8") as leitura:

    leitura_csv = csv.DictReader(leitura)
# O módulo 'csv' proporciona dois métodos para a leitura sendo o '.DictReader()' ou o '.reader()'.
# A diferença é que '.DictReader()' retorna um dicionário, a váriavel que le o arquivo se torna um dict.
# Sendo melhor para em processos futuros lidar com estes dados, tendo em vista que cada um contém sua chave, ao invés de uma sequência bagunçada.
# E '.reader()' nos retorna uma lista, para pegar dados precisariamos do index. Depende do tipo de dado, porém os dois tem suas vantagens e desvantagens.

    for linha in leitura_csv:
        print(linha)

