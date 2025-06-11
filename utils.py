# =====================================================================
# 🔎 IMPRESSÃO DE TOKENS 🔍
# =====================================================================

from antlr4 import Token

def print_tokens(token_stream, lexer):
    """Imprime todos os tokens identificados pelo analisador léxico."""
    print("\n=== TOKENS IDENTIFICADOS ===")
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            token_name = lexer.symbolicNames[token.type]
            print(f"{token_name}: '{token.text}' (linha {token.line}, coluna {token.column})")
    print("============================\n")