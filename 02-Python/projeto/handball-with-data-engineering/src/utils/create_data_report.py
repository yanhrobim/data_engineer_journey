from src.cleaning.limpeza import padronizando_nome_colunas, formatacao_duas_casas_decimais, removendo_linhas_duplicadas, lidar_com_colunas_null, padronizar_formato_season_para_ano_completo, remover_caracteres_especiais, lidando_com_valores_impossiveis_invalidos
from utils.utils import criar_caminho
import pandas as pd
import json

relatorios = []

lista_funcoes_de_limpeza = [
    (padronizando_nome_colunas, {}),

    (formatacao_duas_casas_decimais, {"coluna_decimal": "shooting_accuracy"}),
    # Se função, precisar mais do que o DataFrame como argumento, é preciso transforma-la aqui em uma tupla, dois valores.
    # Na tupla, o primeiro valor é a função, e o segundo valor são os argumentos extras, aqueles que são necessários tirando o DataFrame.
    # Então, se função precisa do argumento 'df' e 'coluna', no dict você somente passa a chave 'coluna' e o valor que é necessário.

    (removendo_linhas_duplicadas, {}),

    (lidar_com_colunas_null, {}),

    (padronizar_formato_season_para_ano_completo, {"nome_coluna_season": "season"}),

    (remover_caracteres_especiais, {}),

    (lidando_com_valores_impossiveis_invalidos, {})
]

for funcao, parametros_extras_funcoes in lista_funcoes_de_limpeza:
    leitura, relatorio = funcao(leitura, **parametros_extras_funcoes)
    # Aqui, o famoso '**kwargs' tem o objetivo de descompactar o dicionário dentro da tupla, e transforma-los em parâmetros e valores.
    # Basicamente, ele reescreve assim para o Python: 
    # leitura, relatorio = formatacao_duas_casas_decimais(df, coluna_decimal="shooting_accuracy")


pd.DataFrame(relatorio).to_json(criar_caminho(pastas='data/reports/data_report/', nome_arquivo='relatorio.json'))