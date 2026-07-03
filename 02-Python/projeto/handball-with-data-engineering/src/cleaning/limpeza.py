import pandas as pd

def padronizando_nome_colunas(return_leitura_csv: pd.DataFrame) -> pd.DataFrame:

    nome_minusculo = [str.lower(coluna).strip().replace(" ", "_") for coluna in return_leitura_csv.columns]

    return_leitura_csv.columns = nome_minusculo

    relatorio = {
        "funcao": "padronizando_nome_colunas",
        "decisao": "padronizar nome de colunas para todas as letras em minúsculo."
    }

    return return_leitura_csv, relatorio

def formatacao_duas_casas_decimais(return_leitura_csv: pd.DataFrame, coluna_decimal: str) -> pd.DataFrame:

    return_leitura_csv[f'{coluna_decimal}'] = (round(return_leitura_csv[f'{coluna_decimal}'], 2))

    relatorio = {
        "funcao": "formatacao_duas_casas_decimais",
        "decisao": "formatação de colunas com números com mais de duas casas decimais, visando ter números mais legiveis e próximos a realidade."
    }
    
    return return_leitura_csv, relatorio

def removendo_linhas_duplicadas(return_leitura_csv: pd.DataFrame):

    linhas_antes = len(return_leitura_csv)
    
    return_leitura_csv = return_leitura_csv.drop_duplicates()

    linhas_depois = len(return_leitura_csv)

    relatorio = {
        "funcao": "removendo_linhas_duplicadas",
        "total_linhas_sem_limpeza": linhas_antes,
        "total_linhas_depois_limpeza": linhas_depois,
        "total_linhas_duplicadas_removidas": linhas_antes - linhas_depois,
        "decisao": "remover linhas duplicadas."
    }

    return return_leitura_csv, relatorio

def lidar_com_colunas_null(return_leitura_csv: pd.DataFrame):

    colunas_com_null = return_leitura_csv.columns[return_leitura_csv.isnull().any()].tolist() 
    # O objetivo dessa linha é obter as colunas que possuem algum valor nulo. Faço isso utilizando alguns métodos do pandas: .columns, .isnull(),.any() e .tolist().
    # .isnull() retorna True para valores, registros, que possuem nulo. O .any() retorna como resultado tudo aquilo que é True, 
    # se fosse o filtro em linha, ele só retornaria a coluna e dado da linha que é nulo.
    # o .columns() entra para dar os nomes das colunas ao isnull() fazendo com que ele diga qual coluna ou não possuí valores nulos
    # e o any() nos retorna o nome das colunas no qual são True (Possuem valores nulos), .tolist() coloca o resultado em lista.



    # Tive a decisão de que, colunas que possuem valores númericos os dados nulos serão substituidos por 0.
    # Essa decisão é tomada pois na validação de dados, colunas de valores númericos só poderam ter tipos de dados númericos.

    nulos_transformados = 0

    for coluna in colunas_com_null:

        if return_leitura_csv[coluna].dtype == float or return_leitura_csv[coluna].dtype == int:

            nulos_transformados += int(return_leitura_csv[coluna].isnull().sum())
            
            coluna_numerica_sem_null =  return_leitura_csv[coluna].fillna(0)    
            # finllna() é um método utilizado para sobrescrever valores nulos. Além de encontrar os valores sozinhos, sobrescreve pelo parâmetro que é passado.
            return_leitura_csv[coluna] = coluna_numerica_sem_null
                                                                    # Se caso tivesse colunas com outros tipos de dados seria necessario adicionar mais if.
        if return_leitura_csv[coluna].dtype == 'str':

            nulos_transformados += int(return_leitura_csv[coluna].isnull().sum())
            
            coluna_str_sem_null = return_leitura_csv[coluna].fillna("missing_value") # Dados em inglês, transformações em inglês.
            return_leitura_csv[coluna] = coluna_str_sem_null

    
    relatorio = {
        "funcao": "lidar_com_colunas_null",
        "colunas_afetadas": colunas_com_null,
        "total_linhas_nulas_tratadas": nulos_transformados,
        "decisao": "substituir nulos seguindo o tipo de dados, se nulo for string/texto para 'missing_value', se tipo do nulo for numérico para 0."
    }
    
    return return_leitura_csv, relatorio


def padronizar_formato_season_para_ano_completo(return_leitura_csv: pd.DataFrame, nome_coluna_season: str):
    # A coluna "Season" veio com a inconsistência de se ter mais de um formato de data dentro da coluna.
    # ('21/22', '22/23', '20/21', '18/19', '23/24', '19/20', '17/18', '2017-2018')  
    # Isso poderia atrapalhar em contrução de futuros filtros, ou até mesmo para obter dados estratégicos.
    # Tive a decisão de aplicar um padrão a cada data da coluna, sendo 2017/2018.

    formatos_sem_transformacao = return_leitura_csv['season'].value_counts().index.values.tolist()

    return_leitura_csv[f'{nome_coluna_season}'] = return_leitura_csv[f'{nome_coluna_season}'].str.replace(pat=r'(\d{2})\/(\d{2})', repl=r'20\1/20\2', regex=True)
    # Utilizei os metodos 'str.replace()' do Pandas, o 'str' nos possibilita obter as operações de texto para um Dataframe e o
    # 'replace()' tem o objetivo de encontrar e substituir strings de acordo com o parâmetro passado a ele.
    # Além dos métodos, utilizei um padrão regex para auxiliar a encontrar o formato desejado.
    # O padrão se baseia em (\d{2}) significa que deveria ter dois números, '\/' significa que a string contém '/'. (\d{2})\/(\d{2}) == '17/18'...
    # Simplificando digo ao .replace() para encontrar strings que estão neste padrão com o parâmetro 'pat'.
    # As () são o que captura cada valor e guarda temporariamente. Por isso \d{2} estão em () pois a cada parentêses o regex salva como grupo de captura,.
    # Basicamente '17' foi salvo em \1, e '18' foi salvo em \2, cada data se tornou um grupo de captura. 
    # Com cada data do formato '17/18' em um grupo de captura, passo o novo formato que quero para o .replace() reescrever a cada string que ele encontrar seguindo o padrão regex.
            

    return_leitura_csv[f'{nome_coluna_season}'] = return_leitura_csv[f'{nome_coluna_season}'].str.replace(pat="-", repl="/")
    # No dataset, a coluna 'season' também possuí os dados '2017-2018', então se caso ele encontrar estes dados, apenas substituir o '-'
    # para colocar no padrão decidido.

    relatorio = {
        "funcao": "padronizar_formato_season_para_ano_completo",
        "coluna_afetada": [f"{nome_coluna_season}"],
        "formatos_encontrados": formatos_sem_transformacao,
        "formatos_apos_transformacao": return_leitura_csv['season'].value_counts().index.values.tolist(),
        "decisao": "Padronizar datas de forma completa ao invés de abreviação. Estrutura decidida como correta: 'xxxx/xxxx'."
    }

    return return_leitura_csv, relatorio


def remover_caracteres_especiais(return_leitura_csv: pd.DataFrame):

    colunas_com_caracter_especial = return_leitura_csv.columns[return_leitura_csv.astype("str")
                                                                                 .apply(lambda dados: 
                                                                                  dados.str.contains(r"[_\\-]", regex=True)
                                                                                  .any())].tolist()
    # Antes de tudo, o único caracter especial que o dataset possui em dados são "_" e "-" (Valores númericos que não são negativos).
    # Ex: Position, Games Played.
    # Existe mais códigos Regex que abrangem mais opções de caracteres especiais, mas neste cenário iria pegar colunas desnecessárias para fazer uma limpeza nos dados.

    # Lógica muito semelhante a como pegamos colunas na função 'lidar com nulos', mas ao invés de termos isnull(), utilizo o apply() para
    # obter o filtro, o filtro se baseia em encontrar quais colunas que possuem dados com caracter especial.
    # Lembrando que o apply() passa o primeiro parâmetro ao lambda, no caso sendo a resposta de return_leitura_csv.columns().
    # str.contains() é um método do pandas frequentemente utlizado para obter valores seguindo a regra/padrão que é passado a função.
    # Passo um código regex ao método como regra, e juntamente com o .columns() passado anteriormemte, ele busca no DataFrame
    # seguindo pelas colunas, quais dados possuem o(s) caractere(s) que o código Regex atribiui (No caso sendo "_" e "-"),
    # então ele retorna True para colunas que possuem seguindo a regra e False para as que não. Com o .any() e .tolist() obtenho as colunas
    # que possuem dados que contém caracteres especiais.

    linhas_com_caracteres_especiais = len(return_leitura_csv[return_leitura_csv[colunas_com_caracter_especial].astype(str).apply(lambda dados: dados.str.contains(r"[_\\-]", regex=True)).any(axis=1)])

    sem_caracteres_especial = return_leitura_csv[colunas_com_caracter_especial].astype("str").replace(to_replace=r"[_\\-]", value="", regex=True)
    # Além de "_" tive a decisão de adicionar para limpar "-", pois por exemplo na coluna "games_played" existia números negativos,
    # não faz muito sentido ter "jogos jogados" negativos.

    return_leitura_csv[colunas_com_caracter_especial] = sem_caracteres_especial

    relatorio = {
        "funcao": "remover_caracteres_especiais",
        "caracteres_considerados_especiais_dataset": ["_", "-"],
        "colunas_afetadas": colunas_com_caracter_especial,
        "total_linhas_caracteres_especiais_tratadas": linhas_com_caracteres_especiais,
        "decisao": "Remover caracteres especiais, pois no contexto atual são desnecessários e sujam os dados."
    }

    return return_leitura_csv, relatorio

def lidando_com_valores_impossiveis_invalidos(return_leitura_csv: pd.DataFrame):

    colunas_com_valores_impossiveis = return_leitura_csv.columns[return_leitura_csv.isin([999, -1]).any()].tolist()
    # Como o str.contains, o método .isin() encontra valores seguindo um parâmetro, o que for passado a ele.

    linhas_com_valores_impossiveis = len(return_leitura_csv.loc[return_leitura_csv[colunas_com_valores_impossiveis].isin([999, -1]).any(axis=1).tolist()])

    coluna_sem_valor_impossivel = return_leitura_csv[colunas_com_valores_impossiveis].replace(to_replace=999, value=0)

    return_leitura_csv[colunas_com_valores_impossiveis] = coluna_sem_valor_impossivel

    relatorio = {
        "funcao": "lidando_com_valores_impossiveis_invalidos",
        "valores_considerados_impossiveis": [999, -1],
        "colunas_afetadas": colunas_com_valores_impossiveis,
        "total_linhas_com_valores_impossiveis_tratadas": linhas_com_valores_impossiveis,
        "decisao": "visando que os valores impossiveis são númericos, substituir eles por 0."
    }
    
    return return_leitura_csv, relatorio


def padronizando_posicoes_para_abreviacao(return_leitura_csv: pd.DataFrame):

    return_leitura_csv['position'] = return_leitura_csv['position'].str.upper()
    return_leitura_csv['position'] = return_leitura_csv['position'].str.strip()

    posicoes = return_leitura_csv['position'].value_counts().index.values.tolist()
    posicoes.remove("NAN")
    # Por algum motivo em meio desenvolvimento da função, estava retornando NAN na contagem dos valores, mesmo o método
    # .value_counts() ter o parâmetro 'dropna=True' como padrão, então caso na contagem devolvesse NAN, iria ser removido aqui.

    for posicao in posicoes:
    
        if " " in posicao.strip().strip():
            index_espaco = posicao.index(" ")   # Pegando o index da posição de espaço. Se fosse por exemplo: "Center Back" iria ser index 6.
            return_leitura_csv['position'] = return_leitura_csv['position'].str.replace(pat=posicao, repl=posicao[0] + posicao[index_espaco + 1])
            # Juntando a primeira letra do valor[0], com a letra depois do " "[index_espaco + 1].
            # Resultado "RIGHT WING": "RW".

    relatorio = {
        "funcao": "padronizando_posicoes_para_abreviacao",
        "posicoes_encontradas": posicoes,
        "posicoes_formato_errado": [posicao for posicao in posicoes if " " in posicao.strip()],
        "posicoes_após_transformacao": return_leitura_csv['position'].value_counts().index.values.tolist(),
        "decisao": "Abreviar nomes de posição para seguir o padrão do Dataset. Exemplos de Nome sem Abreviação: 'Right Back', 'Center Back', etc."
    }

    return return_leitura_csv, relatorio