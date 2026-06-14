import pandas as pd



def lista_dict_para_dataframe(lista_de_dict: list[dict], caminho_para_csv_salvo: str):
    try:
        if len(lista_de_dict) == 0:
            raise BaseException("A lista está vázia! Impossível fazer o DataFrame!")
        
        for dados_dict in lista_de_dict:

            if not type(dados_dict) == dict:
                raise BaseException("A estrutura de dados não é uma lista de dicionários, impossível criar o DataFrame com colunas e valores.")
        
        lista_de_dict = pd.DataFrame(lista_de_dict).to_csv(f"{caminho_para_csv_salvo}pedidos.csv", index=0)

        
    except TypeError:
        print(f"Parece que você passou algum valor errado! Certifique-se que os dados estejam em uma lista de dicionários!")
    
    return print("Os dados foram transformados em CSV!")
