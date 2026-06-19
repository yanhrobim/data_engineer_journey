import pandas as pd
import pandas.errors
from utils.find_path import encontrar_caminho_dados_csv

class DataFrameSomenteColunas(Exception):
    pass

def leitura_csv(nome_pasta_com_arquivo_csv: str, nome_arquivo: str):
    caminho = encontrar_caminho_dados_csv(pasta_com_dados=nome_pasta_com_arquivo_csv, nome_dados=nome_arquivo)
    if caminho:
        try:
            dados = pd.read_csv(filepath_or_buffer=caminho)
            
            dados_alem_de_colunas = [linha for linha in dados.values]

            if dados_alem_de_colunas == []:
                raise DataFrameSomenteColunas("O arquivo CSV passado parece ter colunas, porém não tem valores (dados)! Verifique o parâmetro que você passou para a função de leitura!")
    
        except pandas.errors.EmptyDataError as e:
            print("O arquivo CSV passado não possui dados! Verifique o parâmetro que você passou para a função de leitura!")

        except DataFrameSomenteColunas as e:
            print(e)

        else:
            return dados

leitura = leitura_csv(nome_pasta_com_arquivo_csv='data', nome_arquivo='bundeshandball_sujo.csv')

