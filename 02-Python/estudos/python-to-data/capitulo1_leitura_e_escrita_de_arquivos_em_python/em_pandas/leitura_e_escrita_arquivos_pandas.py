# Dados que serão utilizados para a prática do conteúdo aprendido. :)

import pandas as pd

clientes = [
    {"id": 1, "nome": "Ana Lima", "cidade": "São Paulo", "compras": 5},
    {"id": 2, "nome": "Carlos Souza", "cidade": "Curitiba", "compras": 2},
    {"id": 3, "nome": "Fernanda Rocha", "cidade": "Belo Horizonte", "compras": 8},
    {"id": 4, "nome": "João Pedro", "cidade": "Recife", "compras": 1},
    {"id": 5, "nome": "Mariana Costa", "cidade": "Porto Alegre", "compras": 4},
    {"id": 6, "nome": "Rafael Mendes", "cidade": "Salvador", "compras": 7},
    {"id": 7, "nome": "Beatriz Alves", "cidade": "Fortaleza", "compras": 3},
    {"id": 8, "nome": "Lucas Teixeira", "cidade": "Manaus", "compras": 6},
    {"id": 9, "nome": "Camila Nunes", "cidade": "Brasília", "compras": 9},
    {"id": 10, "nome": "Diego Ferreira", "cidade": "Goiânia", "compras": 2},
]


# =================================================
#    ESCRITA DE ARQUIVOS UTILIZANDO PANDAS (CSV)
# =================================================



# ===============================================
#    LEITURA ARQUIVOS UTILIZANDO PANDAS (CSV)
# ===============================================

clientes_df = pd.read_csv("./dados_para_pratica/clientes.csv")


# ===================================================
#    ESTRUTURA DE DADOS BIODIMENSIONAL: DATAFRAME
# ===================================================
# Um DataFrame é uma estrutura de dados podendo ser criada com Pandas em Python. 
# Ela é mais complexa que listas e dicionários, porém é muito semelhante a uma lista de dicionários, 
# onde por trás dos panos se torna uma lista, que armazena dados que são separados por chaves e valores.
# Porém, o DataFrame não é uma lista de dicionários, e sim uma tabela dentro de  Python, 
# aonde é organizada por Colunas (Chaves), Linhas (O dict ao todo; Cada dado) e Index (Representa a posição desta linha na tabela).
# (Por isso biodimensional)
# A diferença entre uma lista de dicionários e um DataFrame é justamente esta organização e separação, 
# conseguindo aplicar transformações em nível de linha, coluna e por index.


# =====================================
#    PRINCIPAIS MÉTODOS (LEITURA)
# =====================================
# Pedi ao Claude para me mandar os comandos mais útlizados no cotidiano de dados para lidar com DataFrame.
# Seguindo a documentação, e em caso de dúvidas perguntando ao Claude, pratiquei e documentei com cada comando que ele me enviou.
# Logicamente, pode não ser os comandos mais útilizados, errado ali ou aqui, mas o objetivo é ao menos entender o básico sobre os métodos do objeto DataFrame.

clientes_df.head()  # .head() nos proporciona adicionar uma filtragem de linhas que queremos pegar do DataFrame.
                    # caso passado nenhum número, nos retorna as 5 primeiras linhas como padrão.

clientes_df.tail()  # Semelhante ao .head(), porém retorna as 5 últimas linhas caso não seja passado nenhum valor.

print(clientes_df.shape) # O método .shape() nos retorna a quantidade de registros dentro do DataFrame e quantidade de colunas.

# clientes_df.info() # O método .info() nos retorna informações mais específicas do nosso DataFrame, como dtypes de colunas, valores nulos entre outras informações.

# RangeIndex: 10 entries, 0 to 9
# Data columns (total 4 columns):
#  #   Column   Non-Null Count  Dtype
# ---  ------   --------------  -----
#  0   id       10 non-null     int64
#  1   nome     10 non-null     str  
#  2   cidade   10 non-null     str  
#  3   compras  10 non-null     int64
# dtypes: int64(2), str(2)
# memory usage: 452.0 bytes

# print(clientes_df['compras'].describe()) # O método describe() nos retorna estásticas sobre nossas colunas númericas como:
#                                          # Valor máximo, dtype da coluna, 25% (primeiro quartil), 75% (último quartil), entre outras.

# print(clientes_df.columns) # .colums() nos retorna o nome das colunas presentes no DataFrame.
# print(clientes_df.dtypes)  # .dtypes() nos retorna o tipo da coluna(s).


# ============================================
#    PRINCIPAIS MÉTODOS (SELEÇÃO / FILTRO)
# ============================================

print(clientes_df.loc[1])   
# O .loc[] nos permite pegar um valor pelo label do registro, podendo ser qualquer valor, string, int, portanto que seja label do registro.
# Em um cenário real, quando fazemos um filtro em um DataFrame, a depender do filtro as linhas não ficam mais em ordem de index 1,2,3,4,
# o .loc[] entra exatemente aqui, se o antigo index de tal linha for '2', ou 'b', você passa este valor e ele nos retorna o registro.

print(clientes_df.iloc[3])  # A diferença com o .loc[] é que aqui pegamos por posição do registro, independente do antigo index,
                            # então quando passamos '3' para pegar um valor, ele retorna o registro
                            # atual que está nesta posição, independente se antes ele era '5'.


# ============================================
#    PRINCIPAIS MÉTODOS (LIMPEZA)
# ============================================

# Sobre valores nulos:
print(clientes_df.isnull()) # O método .isnull() não transforma nada dentro do DataFrame, na verdade, ele verifica linha por linha
                            # tentando encontrar valores nulos. Se valor for nulo igual a 'True', se não igual a 'False'.

print(clientes_df.dropna()) # O método .dropna() é mais agressivo em comparação com o .isnull(). Em um contexto de um loop no DataFrame
                            # se você passar cada elemento e o método encontrar valores nulos na linha, 
                            # ele remove do DataFrame. Em outro contexto, se você passar colunas, ele pode até mesmo excluir uma coluna
                            # se conter valores nulos. Ele remove tudo aquilo que tem algum valor nulo, sendo individual ou não. 

print(clientes_df.fillna('VALOR_FALTANTE'))  # O método .fillna() é poderoso para lidar com valores nulos, além de encontrar os valores,
                                        # você pode passar algum valor para ele substituir por NULL, ou NaN.
                                        # Exemplo: Substituir valores nulos de uma coluna númerica por zero.

# Limpeza

# clientes_df.drop(coluna) O método .drop() resumidamente tem o objetivo de remover colunas ou linhas.

clientes_df.rename(columns={'nome': 'nome_cliente'}) # O método .rename() renomeia colunas do DataFrame, de acordo com a forma que você passa o parâmetro.

clientes_df['compras'].astype(int)      # O método astype() converte o tipo de dado.




