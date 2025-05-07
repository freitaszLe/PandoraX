
# 🧙‍♂️ PandoraX: A Linguagem de Programação do Desconhecido

**PandoraX** é uma linguagem de programação personalizada criada como parte do projeto final da disciplina de **Construção de Compiladores (2025/1)**. Com uma gramática própria, PandoraX possui suporte a tipos primitivos, controle de fluxo, entrada/saída, expressões aritméticas e lógicas, além de geração de AST e tratamento de erros.


## ❗Objetivo do Projeto

O objetivo principal deste projeto é criar um compilador que leia o código-fonte escrito na linguagem Pandora e o traduza para uma linguagem de mais baixo nível, como *Python, ou até mesmo o execute diretamente. O compilador é uma ferramenta educacional para compreender o funcionamento de compiladores e interpretar os conceitos de **análise léxica, **análise sintática* e *execução de código*.

## ✨ Funcionalidades

- ✅ Dois tipos primitivos: `inter` (inteiro), `strin` (string)
- 📥 Entrada com `summon.x`
- 📤 Saída com `pandora.expose`
- 🔁 Estrutura de repetição com `loopX`
- 🔀 Condicional com `when`...`whenever`
- ➕ Expressões com `+`, `-`, `*`, `/`, `==`, `!=`, `>`, `<`, `>=`, `<=`, `and`, `or`, `not`
- 📊 Geração de AST (árvore sintática abstrata) visualizável com Graphviz
- ❗ Tratamento de erros léxicos e sintáticos com mensagens informativas
- ✅  *Analisador léxico (Lexer):* Converte o código-fonte em tokens.

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


