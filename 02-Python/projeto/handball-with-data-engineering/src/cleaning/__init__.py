import pandas as pd
from src.extract.extracao_leitura_dados import leitura_csv

leitura =  leitura_csv(nome_pasta_com_arquivo_csv="data/raw", nome_arquivo="bundeshandball.csv")
