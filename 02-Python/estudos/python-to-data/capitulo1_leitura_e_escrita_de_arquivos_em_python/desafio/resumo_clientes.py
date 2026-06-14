import pandas as pd
from leitura_e_transformacao import leitura_dados_csv, apply_valor_total

leitura_csv = leitura_dados_csv("./dados_desafio/pedidos.csv")

transformacao = apply_valor_total(dados_csv=leitura_csv,
                                  nome_coluna_de_quantidade='quantidade',
                                  nome_coluna_de_preco_unitario='preco_unitario')

agrupando_p_cliente  = transformacao.groupby(by=['cliente'], group_keys=True, as_index=False).apply(lambda groupby: sum(groupby['valor_total']))
pd.DataFrame(agrupando_p_cliente).rename(columns={None: "valor_total_gasto"}).to_json(path_or_buf="./dados_desafio/resumo_clientes.json",
                                                                                      orient='records', indent=4)

