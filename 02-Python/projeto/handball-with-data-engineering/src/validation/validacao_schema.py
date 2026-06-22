import pandera.pandas as pa
from pandera.typing import Series

class RawSchemaBudesHandball(pa.DataFrameModel):
# Está classe é criada com o objetivo de ser utilziada como uma pré-transformação.
# Utilizando este contrato de dados, mesmo que seja nos dados brutos, evito de alguma forma que dados que não se encaixem 
# sejam barrados antes mesmo de tentar o processo de limpeza.
    Lastname: Series[str] 
    Name: Series[str] = pa.Field(nullable=True) # O método pa.Field() nos permite adicionar validações por Coluna do DataFrame.
                                                # Dentre vários parâmetros, o nullable=True diz ao pandera que nesta coluna é permitido conter dados nulos.
    Team: Series[str]
    Position: Series[str] = pa.Field(nullable=True)
    Games_Played: Series[str] = pa.Field(alias="Games Played")
    Goals: Series[int]
    Missed: Series[int]
    Field_Goals: Series[int] = pa.Field(alias="Field Goals")
    Penalty_Goals: Series[int] = pa.Field(alias="Penalty Goals")
    Shooting_Accuracy: Series[float] = pa.Field(alias="Shooting Accuracy")
    Assists: Series[int] = pa.Field(nullable=True)
    Technical_Faults: Series[int] = pa.Field(alias="Technical Faults")  # o parâmetro alias= nos permite apontar a qual coluna o 
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

