from pathlib import Path

def encontrar_caminho_dados_csv(pasta_com_dados:str, nome_dados: str):


    raiz = Path(__file__).parent.parent.parent  # 3x .parent, para se localizar na raiz do projeto.

    caminho_para_dados = raiz / pasta_com_dados / nome_dados

    if caminho_para_dados.exists() == False:    # Verificação se caminho/caminho existe. .exists() retorna False, caso não existir.
        print("\nO caminho que foi desenvolvido não existe! Verifique os parâmetros que você passou!")
        print(f"Parâmetros passados: '{pasta_com_dados}'; '{nome_dados}'. \nCaminho Final: '{caminho_para_dados}'")

    else:
        print("\nO path para o arquivo.csv foi criado com sucesso! Todos os parâmetros passados encontram um arquivo.csv!")
        print(f"Path criado: {caminho_para_dados}\n")
        return caminho_para_dados