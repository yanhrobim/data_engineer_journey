import pandera.pandas as pa
from pandera.typing import Series
import pandas as pd

class RawSchemaBudesHandball(pa.DataFrameModel):
# Está classe é criada com o objetivo de ser utilziada como uma pré-transformação.
# Utilizando este contrato de dados, mesmo que seja nos dados brutos, evito de alguma forma que dados que não se encaixem 
# sejam barrados antes mesmo de tentar o processo de limpeza.
    Lastname: Series[str] 
    Name: Series[str] = pa.Field(nullable=True) # O método pa.Field() nos permite adicionar validações por Coluna do DataFrame.
                                                # Dentre vários parâmetros, o nullable=True diz ao pandera que nesta coluna é permitido conter dados nulos.
    Team: Series[str] = pa.Field(nullable=True)
    Position: Series[str] = pa.Field(nullable=True)
    Games_Played: Series[str] = pa.Field(alias="Games Played", nullable=True)   # Todas possuem 'nullable=True' pois como são dados brutos, qualquer coluna pode conter valores nulos e aqui, se não for especificado o código quebra.
    Goals: Series[int] = pa.Field(nullable=True)
    Missed: Series[int] = pa.Field(nullable=True)
    Field_Goals: Series[int] = pa.Field(alias="Field Goals", nullable=True)
    Penalty_Goals: Series[int] = pa.Field(alias="Penalty Goals", nullable=True)
    Shooting_Accuracy: Series[float] = pa.Field(alias="Shooting Accuracy", nullable=True)
    Assists: Series[int] = pa.Field(nullable=True)
    Technical_Faults: Series[int] = pa.Field(alias="Technical Faults", nullable=True)  # o parâmetro alias= nos permite apontar a qual coluna o 
                                                                        # objeto da classe aponta no DataFrame.
                                                                        # Utilizo ele em colunas que possuem espaços no nome,
                                                                        # pois em criação de classes não é permitido objeto com nomes que contém espaço.
    Steals: Series[int]
    Blocks: Series[int]
    Yellow_Cards: Series[int] = pa.Field(alias="Yellow Cards")
    TwoMin_Exclusion: Series[int] = pa.Field(alias="2 Min Exclusion")
    Red_Cards: Series[int] = pa.Field(alias="Red Cards")
    Blue_Cards: Series[int] = pa.Field(alias="Blue Cards")
    Season: Series[str]
    Tier: Series[str]


    class Config():
        strict = True       # o parâmetro 'strict' diz ao pandera que o DataFrame que será validado precisa ter as colunas especificadas na classe, se não gera erro.
        coerce = True       # o parâmetro 'coerce' diz ao pandera que mesmo que a coluna não tenha o tipo especificado na classe,
                            # ele tente converter o dado. Ex: dado é int, com coerce ele tenta converter o dado e se conseguir
                            # ele passa no contrato, se não gera erro.


class TrustedSchemaBudesHandball(pa.DataFrameModel):
    lastname: Series[str]
    name: Series[str]
    team: Series[str]
    position: Series[str]
    games_played: Series[str]
    goals: Series[int]
    missed: Series[int]
    field_goals: Series[int]
    penalty_goals: Series[int]
    shooting_accuracy: Series[float]
    assists: Series[int]
    steals: Series[int]
    technical_faults: Series[int]
    blocks: Series[int]
    yellow_cards: Series[int]
    two_min_exclusion: Series[int] = pa.Field(alias="2_min_exclusion")
    red_cards: Series[int]
    blue_cards: Series[int]
    season: Series[str]
    tier: Series[str]

    pa.check("position", 
             name = "Posições Válidas",
             error = "Posição Não existe!")
    def validar_posicoes(cls, posicoes: Series[str]) -> Series[bool]:
        posicoes_validas = ["LB", "P", "GK", "CB","RB", "LW","RW"]
        return posicoes.isin(posicoes_validas)
    
    pa.check("season", 
             name = "Ano da Temporada",
             error = "Ano da Temporada inválido no Dataset!")
    def validar_posicoes(cls, posicoes: Series[str]) -> Series[bool]:
        posicoes_validas = ["2022/2023", "2021/2022", "2020/2021", "2018/2019", "2023/2024", "2017/2018", "2019/2020"]
        return posicoes.isin(posicoes_validas)
    
    pa.check("team",
             name =  "Times válidos da liga!",
             error = "Este time não existe dentro da liga!")
    def validar_times_liga(cls, times: Series[str]) -> Series[bool]:
        times_da_liga = ['BER', 'GWD', 'LEI', 'HBW', 'TVB', 'TBV', 'TVH', 'HAN', 'ELB', 'DOR', 'RNL', 
                         'BHC', 'HCE', 'LUD', 'VFL', 'GUM', 'SGB', 'COB', 'FAG', 'THW', 'SCM', 'ASV', 
                         'SGF', 'MTM', 'WET', 'TUE', 'NOL', 'AUE', 'HSV', 'NLB', 'EIS', 'HAG', 'WÖW', 
                         'DES', 'TVG', 'KON', 'TVE', 'FER', 'WHV', 'HRO', 'VIK', 'POT', 'KRF', 'FFB', 
                         'HIL', 'HGS', 'HCM', 'VIN']
        return times.isin(times_da_liga)
    
    pa.check("tier", 
             name = "Divisões",
             error = "Esta divisão não existe!")
    def validar_posicoes(cls, divisao: Series[str]) -> Series[bool]:
        divisoes_validas = ["A", "B"]
        return divisao.isin(divisoes_validas)


    pa.check(["games_played", "goals", "missed", "field_goals", "penalty_goals", "shooting_accuracy", "assists",
              "technical_faults", "steals", "blocks", "yellow_cards", "2_min_exclusion", "red_cards", "blue_cards"],
             name = "Valores númericos não podem ser negativos destas colunas!",
             error = "O valor é negativo!")
    def validar_se_numeros_sao_positivos(cls, colunas: list[Series[int]]) -> Series[bool]:
        return colunas >= 0
    
    pa.dataframe_check(name = "Cálculo da Métrica 'Shooting Accuracy'.",
                       error = "O valor do cálculo na coluna 'shooting_accuracy' está errado!")
    def metrica_shooting_accuracy(cls, df_handball: pd.DataFrame) -> Series[bool]:
        calculo_shooting_accuracy = round(df_handball['goals'] / (df_handball['missed'], df_handball['field_goals'], df_handball['penalty_goals']), 2)
        return df_handball['shooting_accuracy'] != calculo_shooting_accuracy
    
    class Config():
        strict = True
        coerce = True 
    
    

    
    




