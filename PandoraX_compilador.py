# compiler.py (Versão final com tratamento de erro léxico)

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
# Corrigindo os imports para o padrão que definimos e funcionou
from PandoraXSemanticAnalyzer import PandoraXSemanticAnalyzer
from PandoraX_executor import PandoraX_executor

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
# 🏛️ FASE 2: TRATAMENTO DE ERROS LÉXICOS E SINTÁTICOS 🏛️
# =====================================================================

# --- NOVO! Listener para Erros Léxicos ---
class PandoraXLexerErrorListener(ErrorListener):
    """
    Listener customizado para capturar e relatar erros LÉXICOS de forma clara.
    """
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"‼️ ERRO LÉXICO na linha {line}, coluna {column}: {msg}")
        sys.exit(1)

# --- Listener para Erros Sintáticos (que você já tinha) ---
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
    def __init__(self):
        self.dot = ['digraph AST {', '  node [shape=box, fontname="Courier"];']
        self.node_count = 0
        self.parent_stack = []
        self.result = None

    def visit(self, ctx):
        if ctx is None: return None
        # Limpa o nome do nó para evitar problemas com caracteres especiais no .dot
        node_name = Trees.getNodeText(ctx, ruleNames=PandoraXParser.ruleNames).replace('"', '\\"')
        node_id = f'node{self.node_count}'
        self.node_count += 1
        self.dot.append(f'  {node_id} [label="{node_name}"];')
        if self.parent_stack:
            self.dot.append(f'  {self.parent_stack[-1]} -> {node_id};')
        self.parent_stack.append(node_id)

        if hasattr(ctx, 'children') and ctx.children is not None:
            for child in ctx.children:
                if isinstance(child, ParserRuleContext):
                    self.visit(child)
                elif isinstance(child, TerminalNode):
                     self._add_terminal_node(child)

        self.parent_stack.pop()
        if not self.parent_stack:
            self.dot.append('}')
            self.result = '\n'.join(self.dot)
        return self.result

    def _add_terminal_node(self, terminal_node):
        if terminal_node.getSymbol().type == Token.EOF: return
        node_id = f'node{self.node_count}'
        self.node_count += 1
        token_text = terminal_node.getText().replace('"', '\\"')
        self.dot.append(f'  {node_id} [label="{token_text}", shape=ellipse, color=blue];')
        if self.parent_stack:
            self.dot.append(f'  {self.parent_stack[-1]} -> {node_id};')

    def get_dot(self):
        return self.result

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
        
        # --- ALTERAÇÃO APLICADA AQUI ---
        # Anexando nosso listener de erro customizado ao LEXER
        lexer.removeErrorListeners()
        lexer.addErrorListener(PandoraXLexerErrorListener())
        # --- FIM DA ALTERAÇÃO ---

        stream = CommonTokenStream(lexer)
        stream.fill()
        
        # --- Executa as fases do compilador ---
        
        # 1. Análise Léxica (impressão de tokens)
        print_tokens(stream, lexer)
        
        # 2. Análise Sintática
        parser = PandoraXParser(stream)
        # Anexando o listener de erro customizado ao PARSER
        parser.removeErrorListeners()
        parser.addErrorListener(PandoraXErrorListener())
        tree = parser.program()
        print("✅ Análise sintática concluída com sucesso.")
        
        # 3. Geração da AST
        ast_generator = PandoraXASTGenerator()
        dot_code = ast_generator.visit(tree)
        
        # Salvando o arquivo .dot
        base_name = os.path.splitext(input_file)[0]
        dot_file = f"{base_name}_ast.dot"
        if dot_code:
            with open(dot_file, "w", encoding='utf-8') as f:
                f.write(dot_code)
            print(f"📄 Arquivo AST gerado: {dot_file}")
        
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
        executor = PandoraX_executor() # Corrigido para o nome da classe correto
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