import sys
import os
import argparse # NOVO: Módulo para argumentos de linha de comando

from antlr4 import FileStream, CommonTokenStream


from PandoraXLexer import PandoraXLexer
from PandoraXParser import PandoraXParser
from utils import print_tokens
from error_listeners import PandoraXLexerErrorListener, PandoraXErrorListener
from ast_generator import PandoraXASTGenerator
from PandoraXSemanticAnalyzer import PandoraXSemanticAnalyzer 
from PandoraX_executor import PandoraX_executor                 
from tac_generator import TACGenerator

# =====================================================================
# ⚙️ FUNÇÃO PRINCIPAL (ORQUESTRADOR) ⚙️
# =====================================================================

def main():
    # --- NOVO: Lendo argumentos com argparse ---
    parser = argparse.ArgumentParser(description="Compilador para a linguagem PandoraX.")
    parser.add_argument('input_file', help='O arquivo .pandoraX a ser compilado.')
    parser.add_argument('--tac', action='store_true', help='Gera o Código de Três Endereços (TAC) em vez de executar.')
    args = parser.parse_args()

    input_file = args.input_file
    print(f"Compilando o arquivo: {input_file}")

    try:
        # --- As fases de análise continuam exatamente as mesmas ---

        # Configuração inicial
        input_stream = FileStream(input_file, encoding='utf-8')
        lexer = PandoraXLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(PandoraXLexerErrorListener())

        stream = CommonTokenStream(lexer)
        stream.fill()
        
        # 1. Análise Léxica
        print_tokens(stream, lexer)
        
        # 2. Análise Sintática
        parser = PandoraXParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(PandoraXErrorListener())
        tree = parser.program()
        print("✅ Análise sintática concluída com sucesso.")
        
        # 3. Geração da AST (Visual)
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

        # --- ALTERADO: Etapa 5 agora é condicional ---
        # Verifica se o argumento --tac foi passado na linha de comando
        if args.tac:
            # Se sim, gera o código TAC
            print("\n--- Gerando Código de Três Endereços (TAC) ---")
            tac_gen = TACGenerator()
            tac_gen.visit(tree) # O visitor preenche a lista de código tac_gen.tac_code
            
            # Salva o código TAC em um arquivo .tac
            tac_file_name = os.path.splitext(input_file)[0] + ".tac"
            with open(tac_file_name, "w", encoding='utf-8') as f:
                for instr in tac_gen.tac_code:
                    f.write(str(instr) + "\n")
            print(f"📄 Arquivo TAC gerado: {tac_file_name}")
        else:
            # Se não, executa o código com o interpretador (comportamento antigo)
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