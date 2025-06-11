# =====================================================================
# ⚙️ FUNÇÃO PRINCIPAL (ORQUESTRADOR) ⚙️
# =====================================================================

import sys
import os
from antlr4 import FileStream, CommonTokenStream

# Importa as classes geradas pelo ANTLR
from PandoraXLexer import PandoraXLexer
from PandoraXParser import PandoraXParser

# Importa os nossos módulos separados
from utils import print_tokens
from error_listeners import PandoraXLexerErrorListener, PandoraXErrorListener
from ast_generator import PandoraXASTGenerator
from PandoraXSemanticAnalyzer import PandoraXSemanticAnalyzer 
from PandoraX_executor import PandoraX_executor                 

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
        lexer.removeErrorListeners()
        lexer.addErrorListener(PandoraXLexerErrorListener())

        stream = CommonTokenStream(lexer)
        stream.fill()
        
        # 1. Análise Léxica (impressão de tokens)
        print_tokens(stream, lexer)
        
        # 2. Análise Sintática
        parser = PandoraXParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(PandoraXErrorListener())
        tree = parser.program()
        print("✅ Análise sintática concluída com sucesso.")
        
        # 3. Geração da AST
        ast_generator = PandoraXASTGenerator()
        dot_code = ast_generator.visit(tree)
        if dot_code:
            base_name = os.path.splitext(input_file)[0]
            dot_file = f"{base_name}_ast.dot"
            with open(dot_file, "w", encoding='utf-8') as f:
                f.write(dot_code)
            print(f"📄 Arquivo AST gerado: {dot_file}")
        
        # 4. Análise Semântica
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

        # 5. Execução
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