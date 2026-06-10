# 📒 Diário de Estudos - Python para Dados

## 📌 Objetivos dos Estudos

Este diário será focado em documentar o meu processo de aprendizado sobre Python no mundo de dados. Anteriormente em `python-basics` documentei sobre minha aprendizagem a **Linguagem de Programação Python**, como lógica de programação, sintaxe, fundamentos e conceitos. Portanto, agora o objetivo é entender e aprender como a linguagem se conecta à prática com dados: Leitura e escrita de arquivos, manipulação de dados, bibliotecas e ferramentas presentes no dia a dia da área.

--- 

### | 📚 Capítulo 1
#### **Dia 1 — 4 (05/06/26 a 10/06/2026)**

**🖋️ Tópicos da Aula:**
- Leitura e Escrita de Arquivos.
    - **Python**
    - **Pandas**

**🧠 Aprendizados da aula:**
- Leitura e escrita de arquivos utilizando somente **Python:**
    - `with open()` para o fechamento do método (leitura, escrita) escolhido automaticamente. Existe também a possibilidade de adicionar o método open() a uma variável e seus parâmetros, porém é preciso em algum momento do código sinalizar que quer fechar com close().
    - `write()` para escrever arquivos. No with open() ou na variável que armazena open() é necessário especificar que o método escolhido é *"w"(write)*.
    - `read()` para a leitura de arquivos. No with open() ou na variável que armazena open() é necessário especificar que o método escolhido é *"r"(read)*.
    - Para tipos específicos como *csv* e *json* é necessário a importação de módulos para lidar com o tipo de arquivo.
        - Para arquivos `.csv`, o módulo oferece dois métodos de escrita e leitura: `DictWriter()` / `DictReader()` que trabalham com dicionários, e `writer()` / `reader()` que trabalham com listas. O DictWriter/DictReader é mais legível pois acessa os dados pelo nome da chave, enquanto o writer/reader acessa por index.
- Leitura e escrita de arquivos utilizando **Pandas:**
    - A leitura e escrita de arquivos utilizando Pandas seria sempre manipulando um DataFrame, tanto para ler e temos esta estrutura como retorno ou para escrever que precisamos transformar os dados em DataFrame. O objeto DataFrame possuí vários métodos para lidar com os tipos de arquivos, como: `read_csv()`, `to_csv()`, `read_json()`, `to_json()`, entre outros.
    - Um DataFrame é uma estrutura de dados podendo ser criada com Pandas em Python. Ela é mais complexa que listas e dicionários, porém é muito semelhante a uma lista de dicionários, onde por trás dos panos se torna uma lista, que armazena dados que são separados por chaves e valores.
    No entanto, o DataFrame não é uma lista de dicionários, e sim uma tabela dentro de  Python, onde é organizada por Colunas (Chaves), Linhas (Cada Registro; Cada dado) e Index (Representa a posição desta linha na tabela).
    A diferença entre uma lista de dicionários e um DataFrame é justamente esta organização e separação, conseguindo aplicar transformações em nível de linha, coluna e por index.
