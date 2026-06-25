import pandas as pd
from src.extract.extracao_leitura_dados import leitura_csv

leitura =  leitura_csv(nome_pasta_com_arquivo_csv="data/raw", nome_arquivo="bundeshandball.csv")

def padronizando_nome_colunas(return_leitura_csv: pd.DataFrame) -> pd.DataFrame:
    nome_minusculo = [str.lower(coluna).strip().replace(" ", "_") for coluna in return_leitura_csv.columns]
    return_leitura_csv.columns = nome_minusculo
    return return_leitura_csv


def lidar_com_colunas_null(return_leitura_csv: pd.DataFrame) -> pd.DataFrame:

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
            # finllna() é um método utilizado para sobrescrever valores nulos. Além de encontrar os valores sozinhos, sobrescreve pelo parâmetro que é passado.
            return_leitura_csv[coluna] = coluna_numerica_sem_null
                                                                    # Se caso tivesse colunas com outros tipos de dados seria necessario adicionar mais if.
        if return_leitura_csv[coluna].dtype == 'str': 
            coluna_str_sem_null = return_leitura_csv[coluna].fillna("missing_value") # Dados em inglês, transformações em inglês.
            return_leitura_csv[coluna] = coluna_str_sem_null
        
    return return_leitura_csv

leitura = padronizando_nome_colunas(leitura)

def remover_caracteres_especiais(return_leitura_csv: pd.DataFrame) -> pd.DataFrame:
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

    print(colunas_com_caracter_especial)

    sem_caracteres_especial = return_leitura_csv[colunas_com_caracter_especial].astype("str").replace(to_replace=r"[_\\-]", value="", regex=True)
    # Além de "_" tive a decisão de adicionar para limpar "-", pois por exemplo na coluna "games_played" existia números negativos,
    # não faz muito sentido ter "jogos jogados" negativos.

    return_leitura_csv[colunas_com_caracter_especial] = sem_caracteres_especial

    return return_leitura_csv

def lidando_com_valores_impossiveis_invalidos(return_leitura_csv: pd.DataFrame) -> pd.DataFrame:
    colunas_com_valores_impossiveis = return_leitura_csv.columns[return_leitura_csv.isin([999, -1]).any()].tolist()
    # Como o str.contains, o método .isin() encontra valores seguindo um parâmetro, o que for passado a ele.

    coluna_sem_valor_impossivel = return_leitura_csv[colunas_com_valores_impossiveis].replace(to_replace=999, value=0)

    return_leitura_csv[colunas_com_valores_impossiveis] = coluna_sem_valor_impossivel
    
    return return_leitura_csv


# Vamos ter a coluna Season.
# Utilizar o método Counter() para contar quais e quantos padrões existem na coluna 'Season'
# Dentre as estruturas de data de sessão, tomar uma decisão de qual sera imposto a todos os dados.
# (21/22, 22/23, 20/21, 18/19, 23/24, 19/20, 17/18)   
# Aplicar provavelmente a nível de linha, com condições de controle a nova estrutura a dados que agora são errados.
# Ex: Se a estrutura escolhida for 17/18, aplicar um if para apenas filtrar as linhas que não são 17/18.
# Aplicar a nova estrutura a dados que não seguem.
# Devolver o df.


def padronizar_coluna_season_com_anos_2000(return_leitura_csv):

    estruturas_season = return_leitura_csv["season"].value_counts().index.tolist()

    for estrutura in estruturas_season:

        if len(estrutura) == 5:
            return_leitura_csv.loc[return_leitura_csv['season'] == estrutura].apply(lambda dados_season_sem_20: ''.join(['20', str(dados_season_sem_20)[:0], str(dados_season_sem_20)[:2], '/', '20', str(dados_season_sem_20)[-2:]]))
            
        if len(estrutura) > 5:
            return_leitura_csv['season'].replace("-", "/")

    return return_leitura_csv

leitura = padronizar_coluna_season_com_anos_2000(leitura)
print(leitura['season'])


    
