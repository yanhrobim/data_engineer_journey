import pandas as pd

def leitura_dados_csv(caminho_para_dados_csv: str):
    dados_csv = pd.read_csv(filepath_or_buffer=caminho_para_dados_csv, sep=',')
    return dados_csv


