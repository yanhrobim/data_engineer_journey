import pandas as pd
from src.extract.extracao_leitura_dados import leitura_csv

leitura =  leitura_csv(nome_pasta_com_arquivo_csv="data/raw", nome_arquivo="bundeshandball.csv")


def lidar_com_colunas_null(return_leitura_csv: pd.DataFrame):

    colunas_com_null = return_leitura_csv.columns[return_leitura_csv.isnull().any()].tolist() 
    # O objetivo dessa linha é obter as colunas que possuem algum valor nulo. Faço isso utilizando alguns métodos do pandas: .columns, .isnull(),.any() e .tolist().
    # .isnull() retorna True para valores, registros, que possuem nulo. O .any() retorna como resultado tudo aquilo que é True, 
    # se fosse o filtro em linha, ele só retornaria a coluna e dado da linha que é nulo.
    # o .columns() entra para dar os nomes das colunas ao isnull() fazendo com que ele diga qual coluna ou não possuí valores nulos
    # e o any() nos retorna o nome das colunas no qual são True (Possuem valores nulos), .tolist() coloca o resultado em lista.



    # Tive a decisão de que, colunas que possuem valores númericos os dados nulos serão substituidos por 0.
    # Essa decisão é tomada pois na validação de dados, colunas de valores númericos só poderam ter tipos de dados númericos.

    for coluna in colunas_com_null:

        if return_leitura_csv[coluna].dtype == float:
            coluna_numerica_sem_null =  return_leitura_csv[coluna].fillna(0)
            return_leitura_csv[coluna] = coluna_numerica_sem_null

        if return_leitura_csv[coluna].dtype == 'str': 
            coluna_str_sem_null = return_leitura_csv[coluna].fillna("valor_faltante")
            return_leitura_csv[coluna] = coluna_str_sem_null
        
    return return_leitura_csv
              
