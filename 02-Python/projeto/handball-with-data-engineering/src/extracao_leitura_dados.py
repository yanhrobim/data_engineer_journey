import pandas as pd
from utils.find_path import encontrar_caminho_dados_csv

def leitura_csv(nome_pasta_com_arquivo_csv: str, nome_arquivo: str):
    caminho = encontrar_caminho_dados_csv(pasta_com_dados=nome_pasta_com_arquivo_csv, nome_dados=nome_arquivo)
    dados = pd.read_csv(caminho)
    return dados

