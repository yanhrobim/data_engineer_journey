# 📒 Diário de Estudos - Python para Dados

## 📌 Objetivos dos Estudos

Este diário será focado em documentar o meu processo de aprendizado sobre Python no mundo de dados. Anteriormente em `python-basics` documentei sobre minha aprendizagem a **Linguagem de Programação Python**, como lógica de programação, sintaxe, fundamentos e conceitos. Portanto, agora o objetivo é entender e aprender como a linguagem se conecta à prática com dados: Leitura e escrita de arquivos, manipulação de dados, bibliotecas e ferramentas presentes no dia a dia da área.

--- 

### | 📚 Capítulo 1
#### **Dia 1 (05/06/26)**

**🖋️ Tópicos da Aula:**
- Leitura e Escrita de Arquivos.
    - **Python**
    - **Pandas**

**🧠 Aprendizados da aula:**
- Leitura e escrita de arquivos utilizando somente **Python:**
    - `with open()` para o fechamento do método (leitura, escrita) escolhido automaticamente. Existe também a possibilidade de adicionar o método open() a uma variável e seus parâmetros, porém é preciso em algum momento do código sinalizar que quer fechar com close().
    - `write()` para escrever arquivos. No with open() ou na variável que armazena open() é necessário especificar que o método escolhido é *"w"(write)*.
    - `read()` para a leitura de arquivos. No with open() ou na variável que armazena open() é necessário especificar que o método escolhido é *"r"(read)*.
    - Para tipos específicos como `.csv` e `json` é necessário a importação de módulos para lidar com o tipo de arquivo.
        - Para arquivos `.csv`, o módulo oferece dois métodos de escrita e leitura: **DictWriter() / DictReader()** que trabalham com dicionários, e **writer() / reader()** que trabalham com listas. O DictWriter/DictReader é mais legível pois acessa os dados pelo nome da chave, enquanto o writer/reader acessa por index.

