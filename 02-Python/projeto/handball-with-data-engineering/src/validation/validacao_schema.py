import pandera as pa
from pandera.typing import Series

class RawSchemaBudesHandball(pa.DataFrameModel):
    Lastname: Series[str]
    Name: Series[str]
    Team: Series[str]
    Position: Series[str]
    Games_Played: Series[str] = pa.Field(alias="Games Played")
    Goals: Series[int]
    Missed: Series[int]
    Field_Goals: Series[int] = pa.Field(alias="Field Goals")
    Penalty_Goals: Series[int] = pa.Field(alias="Penalty Goals")
    Shooting_Accuracy: Series[float] = pa.Field(alias="Shooting Accuracy")
    Assists: Series[int]
    Technical_Faults: Series[int] = pa.Field(alias="Technical Faults")
    Steals: Series[int]
    Blocks: Series[int]
    Yellow_Cards: Series[int] = pa.Field(alias="Yellow Cards")
    TwoMin_Exclusion: Series[int] = pa.Field(alias="2 Min Exclusion")
    Red_Cards: Series[int] = pa.Field(alias="Red Cards")
    Blue_Cards: Series[int] = pa.Field(alias="Blue_Cards")
    Season: Series[str]
    Tier: Series[str]


    class Config():
        nullable = True
        coerce = True
