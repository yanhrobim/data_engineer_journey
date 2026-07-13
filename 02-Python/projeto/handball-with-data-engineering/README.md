
<h2 align="center">🤾 Handball With Data Engineering </h2>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" height="22" />
  <img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white" height="22" />
  <img src="https://img.shields.io/badge/Pandera-2E7D32?logoColor=white" height="22" />
  <img src="https://img.shields.io/badge/PyArrow-333333?logoColor=white" height="22" />
</p>

Um pipeline que lê dados brutos a partir de um arquivo CSV, limpa as suas inconsistências, valida sua estrutura antes e depois da limpeza, devolve os dados limpos e confiáveis em parquet, visando o uso dos dados para futuras análises.

## 🗺️ Visão Geral

1. Extração/Leitura dos dados presentes em um arquivo CSV, utilizando pandas.
2. Comparação dos dados brutos vs contrato de dados (Pré-Transform com Pandera).
3. Transformação modular de inconsistências com Pandas. (Funções de limpeza dedicadas uma por tipo de inconsistência)
4. Validação de regras de negócio e schema pós-limpeza, sendo como um portão de qualidade. (Pós-Transform com Pandera)
5. Carregamento dos dados limpos e confiáveis em `.parquet`, utilizando **PyArrow** como engine.

## ℹ️ Sobre o Pipeline


O projeto **Handball With Data Engineering** simula na prática o fluxo de trabalho de um pipeline de dados real. A estrutura segue um modelo de **"ETL" (Extract, Transform, Load)** , extraindo os dados brutos de um arquivo CSV, limpando suas inconsistências através de transformações, e os dados limpos sendo carregados em um formato otimizado para análise.

Antes de qualquer transformação, o pipeline compara os dados que chegam contra um **"contrato de dados"**, chamado por mim de etapa **Pré-Transform**. Após toda a limpeza de inconsistências, os dados são comparados com um segundo **"contrato de dados"** com verificações mais exigentes e regras de negócio, chamado dentro do pipeline de **Pós-Transform**. Estas etapas são adicionadas ao projeto com o objetivo de evitar que os dados inconsistentes avancem silenciosamente.
- **Pré-Transform:** Definição de quais colunas são esperadas, tipo de dados que cada uma deve ter.
- **Pós-Transform:** Base do contrato anterior, mas adicionado regras mais exigentes como os valores que são permitidos em tal coluna, se uma coluna feita por cálcuclo possui os valores corretos. Caso os dados não estiverem de acordo, esta etapa para o pipeline.

No fim da etapa de limpeza, é gerado um **"Data Quality Report (Relatório de Qualidade de Dados)"**, que documenta as inconsistências encontradas, a decisão para lidar com elas e por quê.


### 🔁 Fluxo do Pipeline
![Diagrama do pipeline ETL](./assets/pipeline_diagram.png)

---

## ⚙️ Etapas do Pipeline

### 📥 Extract

A etapa de extração/leitura do pipeline é dividida em duas responsabilidades: Uma função para encontrar o arquivo CSV (`encontrar_caminho_dados_csv`) e outra realiza a leitura dos dados. Essa separação ocorre com o objetivo de cada função ter responsabilidade única, visando que se caso houvesse alterações no armazenamento dos dados no futuro, a etapa não precisasse ser totalmente modificada e sim a função que possui a responsabilidade de encontrar o arquivo.


O tratamento de erros se diferencia em dois tipos de situação: 
- Problemas que são imprevisíveis (fora do controle do código), como remoção do arquivo, localização alterada durante o pipeline, ou até mesmo, arquivo sem permissão para ser lido. 
- Problemas que podem ser encontrados antes mesmo do código ser executado, como confirmar se o caminho é inexistente, se arquivo possui dados, assim por diante.

Para o primeiro cenário, foi decidido o pipeline utilizar `try-except`, capturando o erro sem interromper a execução de forma brusca. Para o segundo, a utilização de `if-else`, já que é uma verificação previsível.
O tratamento de erros também segue o princípio de responsabilidade única. Por exemplo, a função (`encontrar_caminho_dados_csv`) somente lida com situações que envolvem **Path**. 

**Contruindo..**


