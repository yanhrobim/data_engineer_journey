from pathlib import Path

def encontrar_caminho_dados_csv(pasta_com_dados:str, nome_dados: str) -> Path:


    raiz = Path(__file__).parent.parent.parent  # 3x .parent, para se localizar na raiz do projeto.

    caminho_para_dados = raiz / pasta_com_dados / nome_dados

    if caminho_para_dados.exists() == False:    # Verificação se caminho/caminho existe. .exists() retorna False, caso não existir.
        print("\nO caminho que foi desenvolvido não existe! Verifique os parâmetros que você passou!")
        print(f"Parâmetros passados: '{pasta_com_dados}'; '{nome_dados}'. \nCaminho Final: '{caminho_para_dados}'")

    else:
        print("\nO path para o arquivo.csv foi criado com sucesso! Todos os parâmetros passados encontram um arquivo.csv!")
        print(f"Path criado: {caminho_para_dados}")
        return caminho_para_dados
    
def criar_caminho(pastas: str, nome_arquivo: str | None =  None):

    raiz = Path(__file__).parent.parent.parent

    if not nome_arquivo == None:
        caminho = raiz / pastas / nome_arquivo

        if caminho.parent.exists() == False:    # Verificação se caminho/caminho existe. .exists() retorna False, caso não existir.
            print("\nAs pastas que foram passadas para desenvolver o caminho não existem! Verifique os parâmetros que você passou!")
            print(f"Parâmetros passados: '{pastas}'; '{nome_arquivo}'. \nCaminho Final: '{caminho}'")

        else:
            print("\nO path foi criado com sucesso!")
            print(f"Path criado: {caminho}")
            return caminho
        
    else:
        caminho = raiz / pastas
        if caminho.exists() == False:    # Verificação se caminho/caminho existe. .exists() retorna False, caso não existir.
            print("\nAs pastas que foram passadas para desenvolver o caminho não existem! Verifique os parâmetros que você passou!")
            print(f"Parâmetros passados: '{pastas}';  \nCaminho Final: '{caminho}'")

        else:
            print("\nO path foi criado com sucesso!")
            print(f"Path criado: {caminho}")
            return caminho

    return caminho

