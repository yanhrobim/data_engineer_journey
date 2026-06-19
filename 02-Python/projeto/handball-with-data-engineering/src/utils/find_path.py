from pathlib import Path

def encontrar_caminho_dados_csv(pasta_com_dados:str, nome_dados: str):

    try:
        raiz = Path(__file__).parent.parent.parent

        caminho_para_dados = raiz / pasta_com_dados / nome_dados

        if caminho_para_dados.exists() == False:
            raise FileNotFoundError
                    
    except FileNotFoundError:
        print("O caminho que foi desenvolvido não existe! Verifique os parâmetros que você passou!")
        print(f"Parâmetros passados: '{pasta_com_dados}'; '{nome_dados}'. \nCaminho Final: '{caminho_para_dados}'")

    else:
        print("O path para o arquivo.csv foi criado com sucesso! Todos os parâmetros passados encontram um arquivo.csv!")
        print(f"Path criado: {caminho_para_dados}")
        return caminho_para_dados

caminho_path = encontrar_caminho_dados_csv(pasta_com_dados='dat', nome_dados='bundeshandball_sujo.csv')

# Resposta Função:
# /home/usuario/Projetos/data_engineer_journey/02-Python/projeto/handball-with-data-engineering/data/bundeshandball_sujo.csv
