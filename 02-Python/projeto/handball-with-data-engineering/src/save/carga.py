import pandas as pd
from src.utils.utils import criar_caminho

def carregar_dados_parquet(budeshandball_dataframe_csv: pd.DataFrame, 
                           nome_das_pastas_para_salvar: str, 
                           nome_que_arquivo_tera: str,):
    
    print("\n=====================================================")
    print("  ETAPA DE CARREGAMENTO DO ARQUIVO LIMPO (.PARQUET)")
    print("=====================================================")

    try:

        caminho_para_salvamento = criar_caminho(pastas=nome_das_pastas_para_salvar, nome_arquivo=nome_que_arquivo_tera)
        budeshandball_dataframe_csv.to_parquet(path=caminho_para_salvamento, 
                                                        engine='pyarrow',   # Para salvar em .parquet, o 'pyarrow' é a melhor escolha
                                                        # entre as ferramentas disponíveis, gerando mais rapidez na leitura/escrita.
                                                        compression='snappy',   # Padrão do 'pyarrow'.
                                                        index=False)
        
    except ImportError:
        print("\nErro: Parece que você não possuí uma engine instalada para o salvamento do arquivo .parquet! Para este projeto deve ser utilizado o 'pyarrow'.")
        print("Instale com pip: 'pip install pyarrow' ou com poetry: 'poetry add pyarrow'. Tente novamente após a instalação da ferramenta.")
        raise

    else:
        print(f"\nO arquivo foi carregado e salvo em .parquet com sucesso! Está localizado em: {caminho_para_salvamento}")
