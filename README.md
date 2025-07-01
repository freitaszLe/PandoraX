
# 🧙‍♂️ PandoraX: A Linguagem de Programação do Desconhecido

**PandoraX** é uma linguagem de programação personalizada, desenvolvida como parte do projeto final da disciplina de Construção de Compiladores (2025/1). Inspirada em uma temática mágica, PandoraX oferece uma experiência de escrita de código parecida com Python, com uma gramática própria e recursos de controle de fluxo, tipos primitivos e análise semântica.

Este projeto envolve o desenvolvimento de um compilador completo para a linguagem, incluindo as etapas de análise léxica, análise sintática, análise semântica, geração de AST e execução interpretada.


## 🎯 Objetivo do Projeto

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
   java -jar antlr4-4.13.2-complete.jar -Dlanguage=Python3 -visitor PandoraX.g4
   pip install llvmlite
   python PandoraX_compilador.py NomeArquivo.pandoraX
   winget install LLVM.LLVM
   
2. *Gerar árvore:*
   ```bash
   dot -Tpng NomeDoArquivo_ast.dot -o ast.png && start ast.png
   ou
   "C:\Program Files\Graphviz\bin\dot.exe" -Tpng ClassificadorTriangulo_ast.dot -o arvore_sintatica.png

2. *Gerar TAC:*
   ```bash
   python PandoraX_compilador.py NomeArquivo.pandoraX --tac



