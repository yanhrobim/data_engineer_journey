# ======================
#       TYPE HINT
# ======================
# Type Hint = Dicas de Tipo.
# Type Hint tem o principal objetivo de declarar o tipo esperado de uma váriavel.
# Apesar de ser muito benéfico, não "substitui" try-excepts ou validação de dados.  
# (Sempre é bom junta-los, visando ter dados com tipos corretos.)
# A principal utilização do Type Hint é se ter uma melhor interpretação de código, ler o código de forma mais fácil, entender variáveis etc.


# 1. Sem Type Hint:

idade = 30
altura = 1.75   # Pela linguagem dinâmica, mesmo sem declarar os tipos, o Python reconhece eles sozinho na execução do código.
nome = "Alice"  
is_estudante = True 

# 2. Com Type Hint:

idade: int = 30
altura: float = 1.88    # Aqui declaramos explicitamente o tipo esperado da variável. Justamente para quem lê o código e gerar melhor interpretação.
nome: str = "Arthur"
estudante: bool = True