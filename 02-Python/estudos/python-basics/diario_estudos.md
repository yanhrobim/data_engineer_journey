# 📒 Diário de Estudos - (Python Básico)

## 📌 Objetivos dos Estudos

Aprender fundamentos e conceitos básicos da Linguagem de Programação **Python** orientados a área de dados, utilizando aulas e exercícios do Roadmap **Jornada de Dados**.
Com o objetivo de aprender sobre a linguagem, consolidar conhecimento e posteriormente utiliza-la em projetos reais de Engenharia de Dados.

---

## 📝 Registro Por Aula

### | 📚 Aula 01 

#### **Dia 1 (24/04/26)**

**🖋️ Tópicos da Aula:**
- Introdução a linguagem de programação **Python**.
- Tipos de Dados e Variáveis.
    - int()
    - str()
    - float()
    - bool()

**🧠 Aprendizados da aula:**
- Python é uma linguagem interpretada que serve de meio de comunicação entre o usuário e computador.
- Cada variável possui um valor e cada valor possui um tipo de dados.
- Quando utilizamos variáveis estamos armazenando e salvando-as em nossa memória RAM.
- Tudo em Python é Objeto e Estrutura de Dados.
- Boas práticas com nomes de variávies.
- Em Python, temos a possibilidade de mudar os tipos de dados a uma única variável em Python.

---


### | 📚 Aula 02 

#### **Dia 2 — 8 (27/04/26 a 06/05/26)**

**🖋️ Tópicos da Aula:**
- Exercícios aplicando comportamentos dos objetos de tipos primitivos em Python:
    - int()
    - float()
    - str()
    - bool()
Estruturas de Controle:
    - TypeError
    - TypeCheck
    - Type Conversion
    - try-except
    - if

**🧠 Aprendizados da aula:**
- Comportamentos de Objetos como:
    - (**, /, //, +, -, *) para fazer operações aritméticas númericas com tipos de dados int() e float().
    - (AND, OR, !=, ==, NOT) operadores lógicos.
    - (.upper(), .lower(), .split(), .strip()) para a manipulação de strings.
    - Alterando tipo de váriaveis com TypeConversion, e referenciando o tipo que a váriavel deve conter no input().
    - try-except no planejamento e tratamento de erros de um código, antecipando possíveis falhas além do que é esperado. (Como TypeError, ValueError, etc.)
    - Estruturando controle de fluxos através de condições com if.
    - Adição de constantes para a definição de valores fixos dentro de um código/programa.

---


### | 📚 Aula 3 

#### **Dia 9 — 14 (08/05/26 a 16/05/26)**

**🖋️ Tópicos da Aula:**
- Controles de Fluxo.
    - IF
    - FOR
    - WHILE
- DEBUG.
- Básica introdução a listas e dicionários.

**🧠 Aprendizados da aula:**
- Aplicar o DEBUG nos permite encontrar erros de forma mais fácil na aplicação. Essa facilidade se encontra em rodar o código linha por linha para entender onde e quando o erro acontece.
- Estruturas de Controle de Fluxo é tudo aquilo que impede o seu código de seguir em linha reta de cima para baixo.
    - `if` impede o fluxo padrão do código desviando o caminho se condição for verdadeira.
    - `for` impede o fluxo padrão do código prendendo-o em um loop até deixa-lo voltar ao fluxo.
    - Um dos maiores exemplos de controle de fluxo na Engenharia de Dados são os chamados Workflows ou Pipelines, que definem o caminho/fluxo dos dados seguindo lógicas de controle de fluxo.
- **FOR** individualiza cada elemento de uma sequência iterável ou qualquer valor que seja iterável, e executa aquilo definido com cada elemento de forma sequencial até o último e para.
- **WHILE** basicamente enquanto tal condição for verdadeira, ele executa o código dentro do bloco em forma de loop, apenas é abortado se condição não for verdadeira, se rolar um erro ou um `break` intencional.
- A diferença de **FOR** e **WHILE**:
    - **FOR:** Tem um começo e fim do loop definido. (Ex: Uma lista, primeiro valor da lista é o começo, último valor é o fim do loop.)
    - **WHILE:** Não tem um fim definido, caso condição imposta não mudar o loop é infinito.
        - Exercício 5 demonstra muito como utilizar `while` para se fazer uma iteração de uma lista através do index, para transformar condição e abortar o WHILE através de uma *"regra de negócio"* (500).

---


### | 📚 Aula 4

#### **Dia 15 — 20 (18/05/26 a 29/05/26)**

**🖋️ Tópicos da Aula:**
- Tipos complexos e Type Hint.
- Introdução a Estrutura de Dados.
    - Dicionários
    - Listas

**🧠 Aprendizados da aula:**
- **Tipagem Python:**
    - Python é um exemplo de linguagem com tipagem dinâmica, onde não precisamos declarar os tipos explicitamente no código, pois são reconhecidos no processo de execução. A linguagem dinâmica pode oferecer flexibilidade e rapidez no desenvolvimento, porém pode aumentar os riscos de gerar problemas de tipos que somente serão encontrados no processo de execução.
    - Além da tipagem dinâmica, Python possui uma tipagem forte. Portanto, se uma variável for atribuída a um tipo, não pode simplesmente trata-la como outro, sem antes mudar o tipo dela explicitamente. (Ex: Somar 3 + "3". Somar um **int** com uma **string**).
- Com Type Hint conseguimos declarar um tipo esperado explicitamente no código (Ex: nome_usuario: str = "Zezeca"). A principal utilização do Type Hint no código é gerar uma melhor interpretação do código para quem lê, tanto para leitura humana quanto para ferramentas, a fim de gerar melhor comunicação.
- Listas e Dicionários são estruturas de dados, onde podemos armazenar dados e valores. A principal diferença de lista para o dicionário é a sua estrutura e organização, onde a lista são ordenadas e organizadas através de index, porém no dicionário existe a organização e ordenação por chave-valor onde cada valor pertence a uma chave, e cada chave armazena valor.
Principais Métodos Lista:
    - `append()` — Adiciona um item ao final da lista.
    - `extend()` — Adiciona um iterável (lista, sequência, etc) dentro da lista
    - `insert()` — Adiciona um item em um index específico
    - `remove()` — Remove o primeiro item encontrado com o valor passado
    - `pop()` — Remove o último item da lista de forma eficiente. Aceita index como parâmetro, porém perde a vantagem de performance.
    - `index()` — Retorna o index de um valor específico na lista.
    - `count()` — Conta quantas vezes um valor aparece na lista.
    - `sort()` — Ordena os itens da lista.
    - `reverse()` — Reverte a sequência da lista.
    - `copy()` — Retorna uma cópia da lista original.
    - `clear()` — Remove todos os itens da lista.


- Principais Métodos Dict:
    - `get()` — Acessa o valor de uma chave. Aceita parâmetro default para definir o que retornar caso a chave não exista, evitando erros no código.
    - `keys()` — Retorna uma visualização dinâmica com todas as chaves do dicionário.
    - `values()` — Retorna uma visualização dinâmica com todos os valores do dicionário.
    - `items()` — Retorna uma visualização dinâmica com todos os pares chave-valor. Muito utilizado em loops for.
    - `update()` — Atualiza o valor de uma chave existente ou cria a chave caso não exista. Diferente do append() de lista, sobrescreve o valor anterior.
    - `pop()` — Remove uma chave-valor pelo nome da chave, acessando-a diretamente de forma eficiente.
    - `popitem()` — Remove o último par chave-valor inserido no dicionário.
    - `setdefault()` — Cria uma chave com valor padrão se ela não existir. Se já existir, preserva o valor original.
    - `copy()` — Retorna uma cópia do dicionário original.
    - `clear()` — Remove todos os itens do dicionário.

---

### | 📚 Aula 5
#### **Dia 21 — 25 (30/05/26 a 04/06/26)**

**🖋️ Tópicos da Aula:**
    - Built-in function.
    - Criação de Funções.
        - Com Retorno
        - Sem Retorno
    - Funções Lambda.
    - Estrutura de Dados
        - List Comprehension
        - Dict Comprehension
        - Lista de Tuplas

**🧠 Aprendizados da aula:**
- **Built-in functions:** São funções embutidas e disponibilizadas pelo próprio Python, e podem ser utilizadas a qualquer momento. Alguns exemplos de **Built-in functions** como: `type(), list(), sum(), len()`.
- Funções são uma sequência de instruções que criamos em um bloco de código para executar tarefas específicas. Além disso, podem ser reutilzidas em diferentes partes do nosso código.
- Funções lambdas não precisam ser definidas como fazemos com funções normais com o def, por isso muito chamda de funções anônimas, além disso ela pode ser definida apenas em uma linha de código.
    - O `map()` pode potencializar o lambda, fazendo com que possamos executar funções anônimas com o lambda em iteráveis. O map() é muito semelhante a um FOR, ele não é um loop, mas individualiza cada elemento de iteráveis para o lambda executar o que foi instruído.
- Nos exercícios tive uma leve introdução ao `zip()`, para a solução de um dos exercícios presentes.
- **Tuplas** são uma estrutura de dados usadas para armazenar itens em uma única variável, além disso são imutáveis. Ou seja, significa que após uma tupla ser criada, ela não pode ter alterações, adições, ou remoções. Frequentemente utilizadas para garantir que os dados agrupados não sejam ser modificados acidentalmente ou intencionalmente.  
- **List Comprehension** e **Dict Comprehesion** são maneiras que proporcionam mais facilidade em criar listas e dicionários que seguem padrões, como de loops for, condições if-else. Além disso, elas são uma maneira mais eficaz de substituir linhas de código de um loop for com condições por somente uma linha.