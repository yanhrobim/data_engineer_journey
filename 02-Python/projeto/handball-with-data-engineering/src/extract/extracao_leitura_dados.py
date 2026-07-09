import pandas as pd
import pandas.errors
from src.utils.utils import encontrar_caminho_dados_csv

def leitura_budeshandball_csv(nome_pasta_com_arquivo_csv: str, nome_arquivo: str) -> pd.DataFrame:

    print("\n========================================")
    print("  ETAPA DE LEITURA DO ARQUIVO (.CSV)")
    print("========================================")

    caminho = encontrar_caminho_dados_csv(pasta_com_dados=nome_pasta_com_arquivo_csv, nome_dados=nome_arquivo)
    try:
        dados = pd.read_csv(filepath_or_buffer=caminho)

        if len(dados) == 0:
            print("Erro: O arquivo CSV passado parece ter colunas, porém não tem valores (dados)! Verifique o parâmetro que você passou para a função de leitura!")

    except pandas.errors.EmptyDataError:
        print("Erro: O arquivo CSV passado não possui dados! Verifique o parâmetro que você passou para a função de leitura!")
    
    except ValueError:
        print("\nErro: O caminho passado ao método: pd.read_csv() não encontra um arquivo CSV! Revise o caminho passado!")

    else:
        print("\nA Leitura do CSV foi executada sem exeções!")
        return dados
    
