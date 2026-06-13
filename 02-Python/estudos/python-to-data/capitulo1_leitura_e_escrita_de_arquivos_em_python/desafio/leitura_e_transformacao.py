import pandas as pd

def leitura_dados_csv(caminho_para_dados_csv: str):
    dados_csv = pd.read_csv(filepath_or_buffer=caminho_para_dados_csv, sep=',')
    return dados_csv

def calculo_valor_total(dados_csv, nome_coluna_de_quantidade: str, nome_coluna_de_preco_unitario: str):
    return dados_csv[f'{nome_coluna_de_quantidade}'] * dados_csv[f'{nome_coluna_de_preco_unitario}']


