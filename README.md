# 🧙‍♂️ PandoraX Compiler

**Um compilador completo, do código-fonte a um executável nativo, para uma linguagem mágica criada do zero.**

**PandoraX** é uma linguagem de programação imperativa e com tipagem estática, desenvolvida como projeto final da disciplina de Construção de Compiladores (2025/1). Este repositório contém não apenas a especificação da linguagem, mas também seu compilador completo, capaz de transformar código PandoraX em executáveis nativos.

## 📜 Tabela de Conteúdos

1.  [Sobre o Projeto](sobre-o-projeto)
2.  [Arquitetura do Compilador](https://www.google.com/search?q=%23-arquitetura-do-compilador)
3.  [Funcionalidades da Linguagem](https://www.google.com/search?q=%23-funcionalidades-da-linguagem)
4.  [Tecnologias Utilizadas](https://www.google.com/search?q=%23-tecnologias-utilizadas)
5.  [Como Usar](https://www.google.com/search?q=%23-como-usar)
6.  [Exemplo de Código](https://www.google.com/search?q=%23-exemplo-de-c%C3%B3digo)
7.  [Autores](https://www.google.com/search?q=%23-autores)

## 🎯 Sobre o Projeto

O objetivo deste projeto foi aplicar na prática os conceitos fundamentais da construção de compiladores. O resultado é um pipeline de compilação completo que inclui:

  - **Análise Lexica, Sintática e Semântica** para validar o código-fonte.
  - Geração de **Árvore Sintática Abstrata (AST)** e sua visualização com Graphviz.
  - Geração de **Código Intermediário** no formato de Código de Três Endereços (TAC).
  - Geração de **Código Final** em LLVM Intermediate Representation (IR).
  - Compilação do código LLVM IR para um **executável nativo** usando Clang.

## ⛓️ Arquitetura do Compilador

O compilador processa o código em um fluxo de múltiplas etapas:

```
Código Fonte (.pandoraX)
       |
       v
[ Frontend do Compilador (Python) ]
 |--> Análise Léxica (Tokens)
 |--> Análise Sintática (AST)
 |--> Análise Semântica (Tabela de Símbolos)
       |
       v
[ Backend do Compilador (Python) ]
 |--> Geração de Código Intermediário (TAC)
 |--> Geração de Código Final (LLVM IR)
       |
       v
Arquivo de Código LLVM (.ll)
       |
       v
[ Compilador Externo (Clang) ]
 |--> Compilação e Linkedição
       |
       v
Programa Executável (.exe)
```

## ✨ Funcionalidades da Linguagem

  - **Tipos Primitivos:**

      - `inter`: Números inteiros.
      - `strin`: Sequência de caracteres (delimitada por `<` e `>`).
      - `bool`: Valores `true` ou `false`.

  - **Entrada e Saída:**

      - `summon.x(<prompt>)`: Lê um valor do teclado do usuário.
      - `pandora.expose(<mensagem>)`: Imprime uma mensagem na tela, com suporte para interpolação de variáveis (ex: `<Olá, {nome}>`).

  - **Controle de Fluxo:**

      - `when <condição> { ... }`: Estrutura condicional "se".
      - `whenever { ... }`: Estrutura condicional "senão".

  - **Expressões Suportadas:**

      - **Aritméticas:** `+`, `-`, `*`, `/`
      - **Comparações:** `==`, `!=`, `>`, `<`, `>=`, `<=`
      - **Lógicas:** `and`, `or`, `not`

## 🛠️ Tecnologias Utilizadas

  - **Python 3:** Linguagem principal para a implementação de todas as fases do compilador.
  - **ANTLR4:** Ferramenta geradora de parser que lê nossa gramática (`.g4`) e cria o Analisador Léxico e Sintático.
  - **llvmlite:** Biblioteca Python que fornece bindings para a API do LLVM, permitindo a construção programática de código LLVM IR.
  - **LLVM / Clang:** Infraestrutura de compilação utilizada como backend final para otimizar e compilar o código LLVM IR em um executável nativo.
  - **Graphviz:** Ferramenta para visualizar a Árvore Sintática Abstrata a partir dos arquivos `.dot` gerados.

## 🚀 Como Usar

Siga estes passos para configurar o ambiente e executar o compilador.

### 1\. Pré-requisitos

Garanta que você tenha as seguintes ferramentas instaladas e configuradas no `PATH` do seu sistema:

  - **Python** (versão 3.8+)
  - **Java** (JDK/JRE, versão 11+ para rodar o ANTLR)
  - **Git** (para clonar o repositório)
  - **LLVM e Clang** (instalador do site oficial do LLVM)
  - **Graphviz** (para visualizar a AST)

### 2\. Instalação do Projeto

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/freitaszLe/PandoraX.git
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual (Recomendado):**

    ```bash
    # Criar o ambiente
    python -m venv venv

    # Ativar no Windows (PowerShell)
    .\venv\Scripts\activate

    # Ativar no Linux/macOS
    source venv/bin/activate
    ```

3.  **Instale as dependências Python:**

    ```bash
    pip install antlr4-python3-runtime llvmlite
    ```

4.  **Gere o Parser com ANTLR:**
    (Você só precisa fazer isso uma vez ou sempre que alterar o arquivo `.g4`)

    ```bash
    java -jar antlr4-4.13.2-complete.jar -Dlanguage=Python3 -visitor PandoraX.g4
    ```

### 3\. Fluxo de Compilação e Execução

Use o `PandoraX_compilador.py` com diferentes flags para cada etapa.

#### Modo 1: Gerar Código Intermediário (TAC)

Gera um arquivo `.tac` com as instruções de três endereços.

```bash
python PandoraX_compilador.py seu_arquivo.pandoraX --tac
```

#### Modo 2: Gerar, Compilar e Executar (LLVM)

Este é o fluxo completo para criar um executável.

1.  **Gere o código LLVM IR (`.ll`):**

    ```bash
    python PandoraX_compilador.py seu_arquivo.pandoraX --llvm
    ```

2.  **Compile o `.ll` com Clang e crie o executável:**

      * **No Windows (usando o `x64 Native Tools Command Prompt`):**
        ```bash
        clang seu_arquivo.ll -o programa.exe -llegacy_stdio_definitions.lib
        ```
      * **No Linux (Ubuntu):**
        ```bash
        clang seu_arquivo.ll -o programa
        ```

3.  **Execute seu programa final:**

      * **No Windows:**
        ```bash
        programa.exe
        ```
      * **No Linux:**
        ```bash
        ./programa
        ```

#### Utilidade: Visualizar a Árvore Sintática (AST)

O compilador sempre gera um arquivo `_ast.dot`. Para convertê-lo em uma imagem:

```bash
dot -Tpng seu_arquivo_ast.dot -o arvore.png
```

## 📝 Exemplo de Código

`exemplo_interativo.pandoraX`

```pandorax
// Classificação de Triângulos com input do usuário

inter a = inter(summon.x(<Digite o lado A: >))
inter b = inter(summon.x(<Digite o lado B: >))
inter c = inter(summon.x(<Digite o lado C: >))

when (a + b > c) and (a + c > b) and (b + c > a) {
    when a == b and b == c {
        pandora.expose(<Triângulo equilátero válido>)
    }
    whenever {
        when a == b or a == c or b == c {
            pandora.expose(<Triângulo isósceles válido>)
        }
        whenever {
            pandora.expose(<Triângulo escaleno válido>)
        }
    }
}
whenever {
    pandora.expose(<Medidas inválidas para um triângulo.>)
}
```

## 👥 Autores

  - Leticia Arruda de Freitas
  - Anthony Gabriel Oliveira Cruz
