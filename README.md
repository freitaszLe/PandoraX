
# 🧙‍♂️ PandoraX: A Linguagem de Programação do Desconhecido

**PandoraX** é uma linguagem de programação personalizada criada como parte do projeto final da disciplina de **Construção de Compiladores (2025/1)**. Com uma gramática própria, PandoraX possui suporte a tipos primitivos, controle de fluxo, entrada/saída, expressões aritméticas e lógicas, além de geração de AST e tratamento de erros.


## ❗Objetivo do Projeto

O principal objetivo deste projeto é compreender e aplicar os conceitos fundamentais da construção de compiladores. Para isso, foi criada a linguagem PandoraX, permitindo:
- Definir uma gramática personalizada.
- Implementar analisadores léxico, sintático e semântico.
- Gerar e interpretar uma árvore sintática abstrata (AST).
- Fornecer mensagens de erro claras durante as análises.
- A execução do código pode ser feita de forma interpretada (diretamente pela árvore gerada) ou convertida em uma linguagem de mais baixo nível, como Python.

## ✨ Funcionalidades da Linguagem
- 🔸 Tipos Primitivos
- ✅ inter (inteiro)
- ✅ strin (string)
- ✅ bool (booleano)

- 🔸 Entrada e Saída
- 📥 Entrada com o comando summon.x
- 📤 Saída com o comando compandora.expose

- 🔸 Controle de Fluxo
- 🔁 Estrutura de repetição com loopX
- 🔀 Condicional com when e whenever

- 🔸 Expressões Suportadas
- ➕ Aritméticas: +, -, *, /
- ⚖️ Comparações: ==, !=, >, <, >=, <=
- 🔀 Lógicas: and, or, not

- 🔸 Compilador
- 🧾 Analisador Léxico: Geração de tokens a partir do código-fonte
- 🌲 Analisador Sintático: Geração da AST com base na gramática definida
- 🧠 Analisador Semântico: Verificação de tipos, declarações e operações
- 📊 Visualização da AST com Graphviz
- ❗ Detecção de erros léxicos, sintáticos e semânticos com mensagens explicativas
  
---

## Tecnologias Usadas

- *Python:* Linguagem principal para a implementação do compilador.
- *Lark/ANTLR:* Ferramentas de parsing (a serem escolhidas de acordo com a implementação).
- *GitHub Actions:* Para integração contínua (opcional).

## 📚 Sintaxe da Linguagem

### 🧾 Tipos

```pandorax
inter    // tipo inteiro
strin    // tipo string
```

## Como Usar

1. *Clonar o repositório:*
   ```bash
   git clone https://github.com/seu-usuario/pandora-compilador.git
2. *Executar (+ gera dot):*
   ```bash
   python pandoraX_executor.py NomeDoArquivo.pandoraX

2. *Gerar árvore:*
   ```bash
   dot -Tpng NomeDoArquivo_ast.dot -o ast.png && start ast.png




