# compiler.py

import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees

# Importa as classes geradas pelo ANTLR
from PandoraXLexer import PandoraXLexer
from PandoraXParser import PandoraXParser
from PandoraXVisitor import PandoraXVisitor

# --- NOSSAS PARTES DO COMPILADOR ---
from PandoraXSemanticAnalyzer import PandoraXSemanticAnalyzer # <-- Importado!
from PandoraX_executor import PandoraX_executor                 # <-- Importado!

# =====================================================================
# 🔎 FASE 1: ANÁLISE LÉXICA 🔍
# =====================================================================

def print_tokens(token_stream, lexer):
    """Imprime todos os tokens identificados pelo analisador léxico."""
    print("\n=== TOKENS IDENTIFICADOS ===")
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = lexer.symbolicNames[token.type]
            print(f"{token_name}: '{token.text}' (linha {token.line}, coluna {token.column})")
    print("============================\n")

# =====================================================================
# 🏛️ FASE 2: ANALISADOR SINTÁTICO 🏛️
# =====================================================================

class PandoraXErrorListener(ErrorListener):
    """Listener customizado para parar a execução ao encontrar um erro sintático."""
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"\n‼️ ERRO SINTÁTICO na linha {line}, coluna {column}: {msg}")
        sys.exit(1)

# =====================================================================
# 🌳 FASE 3: GERAÇÃO DA ÁRVORE SINTÁTICA ABSTRATA (AST) 🌳
# =====================================================================

class PandoraXASTGenerator(PandoraXVisitor):
    """Gera uma representação da AST no formato .dot para visualização."""
    # (Cole aqui a classe PandoraXASTGenerator da resposta anterior, ela não muda)
    def __init__(self):
        self.dot = ['digraph AST {', '  node [shape=box, fontname="Courier"];']
        # ... resto da classe ...


# =====================================================================
# ⚙️ FUNÇÃO PRINCIPAL (ORQUESTRADOR) ⚙️
# =====================================================================

def main():
    if len(sys.argv) < 2:
        print("Uso: python compiler.py <arquivo.pandoraX>")
        sys.exit(1)

    input_file = sys.argv[1]
    print(f"Compilando o arquivo: {input_file}")

    try:
        # Configuração inicial
        input_stream = FileStream(input_file, encoding='utf-8')
        lexer = PandoraXLexer(input_stream)
        stream = CommonTokenStream(lexer)
        stream.fill()
        
        # --- Executa as fases do compilador ---
        
        # 1. Análise Léxica
        print_tokens(stream, lexer)
        
        # 2. Análise Sintática
        parser = PandoraXParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(PandoraXErrorListener())
        tree = parser.program()
        print("✅ Análise sintática concluída com sucesso.")
        
        # 3. Geração da AST
        ast_generator = PandoraXASTGenerator()
        # (O código para gerar e salvar o .dot vai aqui)
        
        # 4. Análise Semântica (usando a classe importada)
        semantic_analyzer = PandoraXSemanticAnalyzer()
        errors, log = semantic_analyzer.visit(tree)
        print("\n--- Log de Análise Semântica ---")
        for entry in log: print(entry)
        if errors:
            print("\n‼️ ERROS SEMÂNTICOS DETECTADOS ‼️")
            for err in errors: print(f"Erro: {err}")
            sys.exit(1)
        else:
            print("✅ Análise semântica concluída com sucesso.")

        # 5. Execução (usando a classe importada)
        print("\n--- Executando o Código PandoraX ---")
        executor = PandoraX_executor()
        executor.visit(tree)
        print("----------------------------------")
        print("🚀 Execução finalizada.")
        
    except SystemExit:
        print("\nCompilação interrompida devido a erros.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()