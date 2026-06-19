from pathlib import Path

def encontrar_caminho_dados_csv(pasta_com_dados:str, nome_dados: str):

    raiz = Path(__file__).parent.parent.parent

    caminho_para_dados = raiz / pasta_com_dados / nome_dados

    return caminho_para_dados

caminho_path = encontrar_caminho_dados_csv(pasta_com_dados='data', nome_dados='bundeshandball_sujo.csv')

# Resposta Função:
# /home/usuario/Projetos/data_engineer_journey/02-Python/projeto/handball-with-data-engineering/data/bundeshandball_sujo.csv
