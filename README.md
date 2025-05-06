# Pandora - Compilador

*Pandora* é uma linguagem de programação simples, projetada para o aprendizado de conceitos de compiladores e análise sintática. Este repositório contém a implementação de um *compilador funcional* para a linguagem Pandora, desenvolvido para fins educacionais.

## Objetivo do Projeto

O objetivo principal deste projeto é criar um compilador que leia o código-fonte escrito na linguagem Pandora e o traduza para uma linguagem de mais baixo nível, como *Python, ou até mesmo o execute diretamente. O compilador é uma ferramenta educacional para compreender o funcionamento de compiladores e interpretar os conceitos de **análise léxica, **análise sintática* e *execução de código*.

## Funcionalidades

- *Analisador léxico (Lexer):* Converte o código-fonte em tokens.
- *Analisador sintático (Parser):* Constrói a árvore de sintaxe abstrata (AST).
- *Interpretação ou Transpilação:* O código pode ser interpretado diretamente ou transpilado para Python ou C.
- *Controle de Fluxo:* Suporte para estruturas de controle, como if, while e atribuições.
- *Entrada/Saída:* Funções básicas como leia (entrada de dados) e escreva (saída de dados).
- *Tipos de Dados:* Suporte a tipos básicos, como *inteiro* (int) e *string* (string).

## Tecnologias Usadas

- *Python:* Linguagem principal para a implementação do compilador.
- *Lark/ANTLR:* Ferramentas de parsing (a serem escolhidas de acordo com a implementação).
- *GitHub Actions:* Para integração contínua (opcional).

## Como Usar

1. *Clonar o repositório:*
   ```bash
   git clone https://github.com/seu-usuario/pandora-compilador.git
2. *Executar:*
   ```bash
   python pandoraX_executor.py
