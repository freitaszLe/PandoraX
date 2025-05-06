import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from PandoraXLexer import PandoraXLexer
from PandoraXParser import PandoraXParser
from PandoraXVisitor import PandoraXVisitor


# Custom Error Listener para erros léxicos e sintáticos
class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"ERRO SINTÁTICO na linha {line}, coluna {column}: {msg}")

class CustomLexer(PandoraXLexer):
    def notifyListeners(self, e):
        line = self._tokenStartLine
        column = self._tokenStartColumn
        msg = f"ERRO LÉXICO na linha {line}, coluna {column}: símbolo inválido '{self._input.getText(self._tokenStartCharIndex, self._input.index)}'"
        print(msg)
        super().notifyListeners(e)


# Executor da linguagem PandoraX
class PandoraXExecutor(PandoraXVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)

    def visitInputStatement(self, ctx):
        varName = ctx.ID().getText()
        castType = ctx.typecast().getText()
        prompt = ctx.STRING().getText()[1:-1]
        val = input(prompt)
        if castType == "inter":
            self.variables[varName] = int(val)
        elif castType == "strin":
            self.variables[varName] = val

    def visitPrintStatement(self, ctx):
        full = ctx.STRING().getText()[1:-1]
        for key in self.variables:
            full = full.replace(f"{{{key}}}", str(self.variables[key]))
        print(full)

    def visitAssignment(self, ctx):
        varName = ctx.ID().getText()
        val = eval(self.visit(ctx.expression()), {}, self.variables)
        self.variables[varName] = val

    def visitConditional(self, ctx):
        condition = eval(ctx.condition().getText(), {}, self.variables)
        if condition:
            self.visit(ctx.statement(0))
        else:
            self.visit(ctx.statement(1))

    def visitLoopStatement(self, ctx):
        while eval(ctx.condition().getText(), {}, self.variables):
            for stmt in ctx.statement():
                self.visit(stmt)

    def visitExpressionStatement(self, ctx):
        return ctx.getText()


# Execução principal
if __name__ == "__main__":
    input_path = "exemplo1.pandoraX"  # Caminho fixo do arquivo
    input_stream = FileStream(input_path, encoding='utf-8')

    # Lexer com erro léxico tratado
    lexer = CustomLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Mostrar tokens
    print("=== TOKENS IDENTIFICADOS ===")
    token_stream.fill()
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            print(f"{lexer.symbolicNames[token.type]}: '{token.text}' (linha {token.line}, coluna {token.column})")
    print("============================\n")

    # Parser com erro sintático tratado
    parser = PandoraXParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    # Interpretar
    tree = parser.program()
    executor = PandoraXExecutor()
    executor.visit(tree)