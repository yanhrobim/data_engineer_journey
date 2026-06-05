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

with open("./dados_para_pratica/clientes.txt", "w", encoding="utf-8") as arquivo:       
    # with open é como se fosse uma função que abre e fecha automaticamente.
    # No segundo parâmetro pode ser "w" (write) que sobscrevre toda vez o arquivo com os dados novos ou
    # "a"(append) que adiciona os novos dados no arquivo.


    for cliente in clientes:    # É preciso de um loop for para indivualizar os elementos, caso contrário, tudo é escrito na mesma linha.

        arquivo.write(str(cliente) + "\n")  # É preciso transformar em string, para o write() aceitar, caso contrário, gera erro.
    
# ============================================
#    LEITURA DE ARQUIVOS UTILIZANDO PYTHON
# ============================================



