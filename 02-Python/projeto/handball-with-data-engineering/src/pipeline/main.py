from src.extract.extracao_leitura_dados import leitura_budeshandball_csv
from src.cleaning.transformacao_dados import transform_budeshandball_csv
from src.save.carga import carregar_dados_parquet


def pipeline_bundeshandball(pastas_com_arquivo_csv: str, 
                            nome_arquivo_csv: str,
                            pastas_para_salvar_parquet: str,
                            nome_arquivo_para_salvamento: str):
    
    print("\n==========================")
    print("  INICIANDO PIPELINE>>>")
    print("==========================")

    budeshandball_leitura = leitura_budeshandball_csv(nome_pasta_com_arquivo_csv=pastas_com_arquivo_csv, nome_arquivo=nome_arquivo_csv)
    budeshandball_limpado = transform_budeshandball_csv(budeshandball_dataframe=budeshandball_leitura)
    carregar_dados_parquet(budeshandball_dataframe_csv=budeshandball_limpado, 
                        nome_das_pastas_para_salvar=pastas_para_salvar_parquet,
                        nome_que_arquivo_tera=nome_arquivo_para_salvamento)
    
    print("\n========================")
    print("  PIPELINE CONCLUÍDO!")
    print("========================")

if __name__ == "__main__":
    pipeline_bundeshandball(pastas_com_arquivo_csv = 'data/raw/',
                            nome_arquivo_csv = 'bundeshandball.csv',
                            pastas_para_salvar_parquet = 'data/trusted/',
                            nome_arquivo_para_salvamento = 'bundeshandball.parquet')