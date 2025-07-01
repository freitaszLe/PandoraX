# compiler.py (Versão com Geração de TAC e LLVM IR)

import sys
import os
import argparse # Módulo para argumentos de linha de comando

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
from tac_generator import TACGenerator

# --- NOVO: Importa o gerador de LLVM ---
from llvm_generator import LLVMGenerator

# =====================================================================
# ⚙️ FUNÇÃO PRINCIPAL (ORQUESTRADOR) ⚙️
# =====================================================================

def main():
    # --- ALTERADO: Adicionada a opção --llvm ---
    parser = argparse.ArgumentParser(description="Compilador para a linguagem PandoraX.")
    parser.add_argument('input_file', help='O arquivo .pandoraX a ser compilado.')
    parser.add_argument('--tac', action='store_true', help='Gera e salva o Código de Três Endereços (TAC).')
    parser.add_argument('--llvm', action='store_true', help='Gera o código final LLVM IR (implica gerar o TAC internamente).')
    args = parser.parse_args()

    input_file = args.input_file
    print(f"Compilando o arquivo: {input_file}")

    try:
        # Fases 1, 2, 3 e 4 (Análises) continuam iguais
        # ...
        input_stream = FileStream(input_file, encoding='utf-8')
        lexer = PandoraXLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(PandoraXLexerErrorListener())

        stream = CommonTokenStream(lexer)
        stream.fill()
        
        print_tokens(stream, lexer)
        
        parser = PandoraXParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(PandoraXErrorListener())
        tree = parser.program()
        print("✅ Análise sintática concluída com sucesso.")
        
        ast_generator = PandoraXASTGenerator()
        dot_code = ast_generator.visit(tree)
        if dot_code:
            base_name = os.path.splitext(input_file)[0]
            dot_file = f"{base_name}_ast.dot"
            with open(dot_file, "w", encoding='utf-8') as f:
                f.write(dot_code)
            print(f"📄 Arquivo AST gerado: {dot_file}")
        
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

        # --- ALTERADO: Estrutura condicional para as etapas finais ---
        
        # Etapa 5: Geração de Código Intermediário (Sempre ocorre se uma flag de compilação for usada)
        # O TAC é a base para a geração de código final.
        if args.tac or args.llvm:
            print("\n--- Gerando Código de Três Endereços (TAC) ---")
            tac_gen = TACGenerator()
            tac_gen.visit(tree)
            tac_code = tac_gen.tac_code # Lista de objetos TACInstruction
            
            # Se a opção for --tac, apenas salvamos o arquivo e terminamos.
            if args.tac:
                tac_file_name = os.path.splitext(input_file)[0] + ".tac"
                with open(tac_file_name, "w", encoding='utf-8') as f:
                    for instr in tac_code:
                        f.write(str(instr) + "\n")
                print(f"📄 Arquivo TAC gerado: {tac_file_name}")

            # Se a opção for --llvm, usamos o TAC gerado para ir para a próxima etapa.
            if args.llvm:
                print("\n--- Gerando Código Final (LLVM IR) ---")
                llvm_gen = LLVMGenerator(tac_code)
                llvm_ir_code = llvm_gen.generate() # O método que traduz TAC para LLVM IR

                # Salva o código LLVM IR em um arquivo .ll
                llvm_file_name = os.path.splitext(input_file)[0] + ".ll"
                with open(llvm_file_name, "w", encoding='utf-8') as f:
                    f.write(llvm_ir_code)
                print(f"📄 Arquivo LLVM IR gerado: {llvm_file_name}")
                print("\nPara compilar o código gerado, use: clang {0} -o seu_executavel".format(llvm_file_name))

        # Se nenhuma flag de compilação for usada, executa com o interpretador.
        else:
            print("\n--- Executando o Código PandoraX (Modo Interpretador) ---")
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