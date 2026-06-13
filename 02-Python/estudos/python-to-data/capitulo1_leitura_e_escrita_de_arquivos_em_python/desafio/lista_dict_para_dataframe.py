import pandas as pd



def lista_dict_para_dataframe(lista_de_dict: list[dict]):
    try:
        if len(lista_de_dict) == 0:
            raise BaseException("A lista está vázia! Impossível fazer o DataFrame!")
        
        for dados_dict in lista_de_dict:

            if not type(dados_dict) == dict:
                raise BaseException("A estrutura de dados não é uma lista de dicionários, impossível criar o DataFrame com colunas e valores.")
        
        lista_de_dict = pd.DataFrame(lista_de_dict).to_csv("pedidos.csv", index=0)

        
    except TypeError:
        print(f"Parece que você passou algum valor errado! Certifique-se que os dados estejam em uma lista de dicionários!")
    
    return print("Os dados foram transformados em CSV!")


pedidos = [
    {"id_pedido": 1, "cliente": "Mariana Souza", "produto": "Notebook", "quantidade": 1, "preco_unitario": 3500.00, "data_pedido": "2026-01-05"},
    {"id_pedido": 2, "cliente": "João Pereira", "produto": "Mouse", "quantidade": 3, "preco_unitario": 45.90, "data_pedido": "2026-01-06"},
    {"id_pedido": 3, "cliente": "Mariana Souza", "produto": "Teclado", "quantidade": 1, "preco_unitario": 120.00, "data_pedido": "2026-01-08"},
    {"id_pedido": 4, "cliente": "Carlos Lima", "produto": "Monitor", "quantidade": 2, "preco_unitario": 890.00, "data_pedido": "2026-01-10"},
    {"id_pedido": 5, "cliente": "Ana Ribeiro", "produto": "Notebook", "quantidade": 1, "preco_unitario": 3200.00, "data_pedido": "2026-01-11"},
    {"id_pedido": 6, "cliente": "João Pereira", "produto": "Headset", "quantidade": 2, "preco_unitario": 199.90, "data_pedido": "2026-01-12"},
    {"id_pedido": 7, "cliente": "Beatriz Costa", "produto": "Cadeira Gamer", "quantidade": 1, "preco_unitario": 1450.00, "data_pedido": "2026-01-13"},
    {"id_pedido": 8, "cliente": "Carlos Lima", "produto": "Mousepad", "quantidade": 4, "preco_unitario": 35.00, "data_pedido": "2026-01-14"},
    {"id_pedido": 9, "cliente": "Mariana Souza", "produto": "Webcam", "quantidade": 1, "preco_unitario": 250.00, "data_pedido": "2026-01-15"},
    {"id_pedido": 10, "cliente": "Ana Ribeiro", "produto": "Mouse", "quantidade": 2, "preco_unitario": 45.90, "data_pedido": "2026-01-16"},
    {"id_pedido": 11, "cliente": "Pedro Santos", "produto": "Monitor", "quantidade": 1, "preco_unitario": 890.00, "data_pedido": "2026-01-17"},
    {"id_pedido": 12, "cliente": "Beatriz Costa", "produto": "Teclado", "quantidade": 1, "preco_unitario": 120.00, "data_pedido": "2026-01-18"},
    {"id_pedido": 13, "cliente": "João Pereira", "produto": "Notebook", "quantidade": 1, "preco_unitario": 3500.00, "data_pedido": "2026-01-19"},
    {"id_pedido": 14, "cliente": "Pedro Santos", "produto": "Cadeira Gamer", "quantidade": 1, "preco_unitario": 1450.00, "data_pedido": "2026-01-20"},
    {"id_pedido": 15, "cliente": "Ana Ribeiro", "produto": "Headset", "quantidade": 1, "preco_unitario": 199.90, "data_pedido": "2026-01-21"},
    {"id_pedido": 16, "cliente": "Carlos Lima", "produto": "Webcam", "quantidade": 2, "preco_unitario": 250.00, "data_pedido": "2026-01-22"},
    {"id_pedido": 17, "cliente": "Mariana Souza", "produto": "Monitor", "quantidade": 1, "preco_unitario": 890.00, "data_pedido": "2026-01-23"},
    {"id_pedido": 18, "cliente": "Pedro Santos", "produto": "Mouse", "quantidade": 5, "preco_unitario": 45.90, "data_pedido": "2026-01-24"},
    {"id_pedido": 19, "cliente": "Beatriz Costa", "produto": "Notebook", "quantidade": 1, "preco_unitario": 3500.00, "data_pedido": "2026-01-25"},
    {"id_pedido": 20, "cliente": "João Pereira", "produto": "Mousepad", "quantidade": 3, "preco_unitario": 35.00, "data_pedido": "2026-01-26"},
]

escrever = lista_dict_para_dataframe(pedidos)