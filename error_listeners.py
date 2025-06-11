
# =====================================================================
# ‼️ TRATAMENTO DE ERROS LÉXICOS E SINTÁTICOS ‼️
# =====================================================================

import sys
from antlr4.error.ErrorListener import ErrorListener

class PandoraXLexerErrorListener(ErrorListener):
    """Listener customizado para capturar e relatar erros LÉXICOS de forma clara."""
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"‼️ ERRO LÉXICO na linha {line}, coluna {column}: {msg}")
        sys.exit(1)

class PandoraXErrorListener(ErrorListener):
    """Listener customizado para parar a execução ao encontrar um erro SINTÁTICO."""
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"\n‼️ ERRO SINTÁTICO na linha {line}, coluna {column}: {msg}")
        sys.exit(1)