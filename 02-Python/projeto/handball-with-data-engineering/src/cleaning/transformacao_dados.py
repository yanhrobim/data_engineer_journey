import pandera.pandas as pa
import pandas as pd
from src.cleaning.limpeza import padronizando_nome_colunas, formatacao_duas_casas_decimais, removendo_linhas_duplicadas, lidar_com_colunas_null, padronizar_formato_season_para_ano_completo, remover_caracteres_especiais, lidando_com_valores_impossiveis_invalidos, padronizando_posicoes_para_abreviacao, remover_espacos_desnecessarios
from src.utils.utils import criar_relatorio_qualidade_de_dados_json
from src.validation.validacao_schema import RawSchemaBundesHandball, TrustedSchemaBundesHandball


def transform_budeshandball_csv(budeshandball_dataframe: pd.DataFrame):

    print("\n====================================================")
    print("  PRÉ-TRANSFORM: CONTRATO DE DADOS (SCHEMA BRUTO)")
    print("====================================================")

    try:
        RawSchemaBundesHandball.validate(budeshandball_dataframe, lazy=True)
        # O parâmetro 'lazy=' do método validade() nos permite encontrar mais de um erro em apenas uma execução. 
        # Resumidamente, mesmo que ele encontre o primeiro erro, 
        # com 'lazy' ele continuara até encontrar todos os erros e no final te entregar tudo de uma única vez, invés de parar no
        # primeiro erro encontrado.

    except pa.errors.SchemaErrors as exc:
        criar_relatorio_qualidade_de_dados_json(relatorios=dict(exc.message), 
                                            pastas_onde_relatorio_deve_ser_salvo="data/reports/data_quality_reports",
                                            nome_para_relatorio="pre_transform_data_quality_report.json")
        print("\nErro ao validar o schema dos dados brutos! Detalhes na pasta de relatórios: './data/report/data_quality_reports/'")

    else:
        print("\nO schema dos dados brutos foi validado com sucesso, nenhum erro encontrado!")

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

        (remover_caracteres_especiais, {"colunas_com_caracteres_especiais_que_sujam_os_dados": ["position", "games_played"]}),

        (lidando_com_valores_impossiveis_invalidos, {}),

        (padronizando_posicoes_para_abreviacao, {"nome_coluna_de_posicoes_jogadores": "position"}),

        (remover_espacos_desnecessarios, {})
    ]

    print("\n=====================================")
    print("  ETAPA DE TRANSFORMAÇÃO DOS DADOS")
    print("======================================")

    for funcao, parametros_extras_funcoes in lista_funcoes_de_limpeza:
        print(f"\nExecutando função: {funcao.__name__}...")
        budeshandball_dataframe, relatorio_func = funcao(budeshandball_dataframe, **parametros_extras_funcoes)
        # Aqui, o famoso '**kwargs' tem o objetivo de descompactar o dicionário dentro da tupla, e transforma-los em parâmetros e valores.
        # Basicamente, ele reescreve assim para o Python: 
        # leitura, relatorio = formatacao_duas_casas_decimais(df, coluna_decimal="shooting_accuracy")

        print(f"Função: {funcao.__name__} executada com sucesso!")

        relatorios.append(relatorio_func)

    print("\n============================================================")
    print("  RELATÓRIO DE QUALIDADE DOS DADOS (DATA QUALITY REPORT)")
    print("============================================================")

    criar_relatorio_qualidade_de_dados_json(relatorios=relatorios, 
                                            pastas_onde_relatorio_deve_ser_salvo="data/reports/data_quality_reports",
                                            nome_para_relatorio="transform_data_quality_report.json")
    
    print("\n==========================================================")
    print("  PÓS-TRANSFORM: CONTRATO DE DADOS (DADOS APÓS LIMPEZA)")
    print("==========================================================")

    try:

        budeshandball_dataframe = TrustedSchemaBundesHandball.validate(budeshandball_dataframe, lazy=True)

    except pa.errors.SchemaErrors as exc:
        criar_relatorio_qualidade_de_dados_json(relatorios=dict(exc.message), 
                                            pastas_onde_relatorio_deve_ser_salvo="data/reports/data_quality_reports",
                                            nome_para_relatorio="pos_transform_data_quality_report.json")
        print("Erro: Erro na validação dos dados após a limpeza! Detalhes na pasta de relatórios: './data/report/data_quality_reports/'")
        raise
    else:
        print("\nO schema dos dados após a limpeza foi validado com sucesso, nenhum erro encontrado!")


    return budeshandball_dataframe
