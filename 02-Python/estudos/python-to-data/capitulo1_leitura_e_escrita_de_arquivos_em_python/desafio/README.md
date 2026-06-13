# Desafio: Processamento de Pedidos de Clientes 📦

## 🤔 Por que? (Introdução) 

Na alura, em uma aula do curso "Python: Inteligência Artificial Aplicada" o tutor aplicou um desafio para consolidar aprendizagens sobre com o uso de LLMs e Pandas com Python em projetos. Neste momento atual do meu repositório não é meu objetivo aplicar LLM, e sim aprender e praticar com a biblioteca **Pandas**. Visando que, neste processo o objetivo é a criação de código de forma autêntica, com frustações, para consequentemente aprender de verdade.

Tendo este conexto em vista, utilizei o desafio do tutor como base e criei um desafio para mim próprio, a fim de praticar com **Pandas** em forma de um exercício mais próximo a um cenário da vida real.

---

## 📌 Objetivos


```python
pedidos = [
    {"id_pedido": 1, "cliente": "Mariana Souza", "produto": "Notebook", "quantidade": 1, "preco_unitario": 3500.00, "data_pedido": "2026-01-05"},
    {"id_pedido": 2, "cliente": "João Pereira", "produto": "Mouse", "quantidade": 3, "preco_unitario": 45.90, "data_pedido": "2026-01-06"},
    {"id_pedido": 3, "cliente": "Mariana Souza", "produto": "Teclado", "quantidade": 1, "preco_unitario": 120.00, "data_pedido": "2026-01-08"},
    {"id_pedido": 4, "cliente": "Carlos Lima", "produto": "Monitor", "quantidade": 2, "preco_unitario": 890.00, "data_pedido": "2026-01-10"},
    {"id_pedido": 5, "cliente": "Ana Ribeiro", "produto": "Notebook", "quantidade": 1, "preco_unitario": 3200.00, "data_pedido": "2026-01-11"},
    {"id_pedido": 6, "cliente": "João Pereira", "produto": "Headset", "quantidade": 2, "preco_unitario": 199.90, "data_pedido": "2026-01-12"},
    {"id_pedido": 7, "cliente": "Beatriz Costa", "produto": "Cadeira Gamer", "quantidade": 1, "preco_unitario": 1450.00, "data_pedido": "2026-01-13"},
    {"id_pedido": 8, "cliente": "Carlos Lima", "produto": "Mousepad", "quantidade": 4, "preco_unitario": 35.00, "data_pedido": "2026-01-14"},
    {"id_pedido": 9, "cliente": "Mariana Souza", "produto": "Webcam", "quantidade": 1, "preco_unitario": 250.00, "data_pedido": "2026-01-15"},
    {"id_pedido": 10, "cliente": "Ana Ribeiro", "produto": "Mouse", "quantidade": 2, "preco_unitario": 45.90, "data_pedido": "2026-01-16"},
    {"id_pedido": 11, "cliente": "Pedro Santos", "produto": "Monitor", "quantidade": 1, "preco_unitario": 890.00, "data_pedido": "2026-01-17"},
    {"id_pedido": 12, "cliente": "Beatriz Costa", "produto": "Teclado", "quantidade": 1, "preco_unitario": 120.00, "data_pedido": "2026-01-18"},
    {"id_pedido": 13, "cliente": "João Pereira", "produto": "Notebook", "quantidade": 1, "preco_unitario": 3500.00, "data_pedido": "2026-01-19"},
    {"id_pedido": 14, "cliente": "Pedro Santos", "produto": "Cadeira Gamer", "quantidade": 1, "preco_unitario": 1450.00, "data_pedido": "2026-01-20"},
    {"id_pedido": 15, "cliente": "Ana Ribeiro", "produto": "Headset", "quantidade": 1, "preco_unitario": 199.90, "data_pedido": "2026-01-21"},
    {"id_pedido": 16, "cliente": "Carlos Lima", "produto": "Webcam", "quantidade": 2, "preco_unitario": 250.00, "data_pedido": "2026-01-22"},
    {"id_pedido": 17, "cliente": "Mariana Souza", "produto": "Monitor", "quantidade": 1, "preco_unitario": 890.00, "data_pedido": "2026-01-23"},
    {"id_pedido": 18, "cliente": "Pedro Santos", "produto": "Mouse", "quantidade": 5, "preco_unitario": 45.90, "data_pedido": "2026-01-24"},
    {"id_pedido": 19, "cliente": "Beatriz Costa", "produto": "Notebook", "quantidade": 1, "preco_unitario": 3500.00, "data_pedido": "2026-01-25"},
    {"id_pedido": 20, "cliente": "João Pereira", "produto": "Mousepad", "quantidade": 3, "preco_unitario": 35.00, "data_pedido": "2026-01-26"},
]
```

- ### 1 | Transforme essa lista em um DataFrame e salve em um arquivo CSV (pedidos.csv).

---

- ### 2 | Crie uma função que leia esse CSV de volta como DataFrame.

---

- ### 3 | Dentro dessa função, adicione uma nova coluna chamada valor_total, representando o valor total de cada pedido (quantidade * preco_unitario).

---

- ### 4 | Após o loop, use groupby() para agrupar os pedidos por cliente e somar o valor_total de cada um — gerando um resumo de "quanto cada cliente gastou no total".

---

- ### 5 | Salve esse resumo final em um arquivo JSON (resumo_clientes.json), de forma organizada.

---

