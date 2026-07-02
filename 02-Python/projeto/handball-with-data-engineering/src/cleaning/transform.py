import pandera.pandas as pa
import pandas as pd
from src.cleaning.limpeza import padronizando_nome_colunas, formatacao_duas_casas_decimais, removendo_linhas_duplicadas, lidar_com_colunas_null, padronizar_formato_season_para_ano_completo, remover_caracteres_especiais, lidando_com_valores_impossiveis_invalidos
from src.utils.utils import criar_relatorio_qualidade_de_dados_json
from src.validation.validacao_schema import RawSchemaBudesHandball

def transform_budeshandball_csv(budeshandball_dataframe: pd.DataFrame):
    try:
        RawSchemaBudesHandball.validate(budeshandball_dataframe, lazy=True)
        # O parâmetro 'lazy=' do método validade() nos permite encontrar mais de um erro em apenas uma execução. 
        # Resumidamente, mesmo que ele encontre o primeiro erro, 
        # com 'lazy' ele continuara até encontrar todos os erros e no final te entregar tudo de uma única vez, invés de parar no
        # primeiro erro encontrado.

    except pa.errors.SchemaErrors as exc:
        print(exc)

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
        budeshandball_dataframe, relatorio_func = funcao(budeshandball_dataframe, **parametros_extras_funcoes)
        # Aqui, o famoso '**kwargs' tem o objetivo de descompactar o dicionário dentro da tupla, e transforma-los em parâmetros e valores.
        # Basicamente, ele reescreve assim para o Python: 
        # leitura, relatorio = formatacao_duas_casas_decimais(df, coluna_decimal="shooting_accuracy")

        relatorios.append(relatorio_func)

    criar_relatorio_qualidade_de_dados_json(relatorios=relatorios, 
                                            pastas_onde_relatorio_deve_ser_salvo="data/reports/data_quality_report",
                                            nome_para_relatorio="data_quality_report.json")

    return budeshandball_dataframe

