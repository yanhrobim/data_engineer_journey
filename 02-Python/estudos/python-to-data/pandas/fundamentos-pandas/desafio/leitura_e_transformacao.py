import pandas as pd

def leitura_dados_csv(caminho_para_dados_csv: str):
    dados_csv = pd.read_csv(filepath_or_buffer=f'{caminho_para_dados_csv}pedidos.csv', sep=',')
    return dados_csv

def calculo_valor_total(dados_csv, nome_coluna_de_quantidade: str, nome_coluna_de_preco_unitario: str):
    return dados_csv[f'{nome_coluna_de_quantidade}'] * dados_csv[f'{nome_coluna_de_preco_unitario}']

def apply_valor_total(dados_csv: pd.DataFrame, nome_coluna_de_quantidade: str, nome_coluna_de_preco_unitario: str):


    dados_csv['valor_total'] = dados_csv.apply(calculo_valor_total, axis=1, args=(nome_coluna_de_quantidade,
                                                                                  nome_coluna_de_preco_unitario))
    
    return dados_csv


