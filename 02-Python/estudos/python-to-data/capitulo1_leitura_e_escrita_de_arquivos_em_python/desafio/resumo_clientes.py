import pandas as pd

def valor_total_gasto_p_cliente_in_json(dataframe_com_valor_total: pd.DataFrame, path_para_json: str):

    agrupando_p_cliente  = dataframe_com_valor_total.groupby(by=['cliente'], group_keys=True, as_index=False).apply(lambda groupby: sum(groupby['valor_total']))
    pd.DataFrame(agrupando_p_cliente).rename(columns={None: "valor_total_gasto"}).to_json(path_or_buf=path_para_json,
                                                                                      orient='records', indent=4, force_ascii=False)
    return print(f"O JSON foi criado com sucesso! Localizado em: '{path_para_json}'.")
