import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from PandoraXLexer import PandoraXLexer
from PandoraXParser import PandoraXParser
from PandoraXVisitor import PandoraXVisitor

def print_tokens(token_stream, lexer):
    print("\n=== TOKENS IDENTIFICADOS ===")
    tokens = token_stream.tokens
    for token in tokens:
        if token.type != Token.EOF:
            token_name = lexer.symbolicNames[token.type]
            print(f"{token_name}: '{token.text}' (linha {token.line}, coluna {token.column})")
    print("============================\n")

class PandoraXErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"ERRO SINTÁTICO na linha {line}, coluna {column}: {msg}")
        sys.exit(1)

class PandoraXExecutor(PandoraXVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitInputStatement(self, ctx):
        var_name = ctx.ID().getText()
        # Encontra o INTERPOLATED_STRING na estrutura
        for i in range(ctx.getChildCount()):
            if isinstance(ctx.getChild(i), TerminalNode) and ctx.getChild(i).getSymbol().type == lexer.INTERPOLATED_STRING:
                prompt = ctx.getChild(i).getText()[1:-1]
                break
        else:
            prompt = ""
        
        user_input = input(prompt)
        
        if ctx.typeCast().INTER():
            try:
                self.variables[var_name] = int(user_input)
            except ValueError:
                print(f"Erro: '{user_input}' não é um número inteiro válido")
                sys.exit(1)
        else:
            self.variables[var_name] = user_input

    def visitOutputStatement(self, ctx):
        text = ctx.INTERPOLATED_STRING().getText()[1:-1]
        while '{' in text and '}' in text:
            start = text.find('{')
            end = text.find('}')
            var_name = text[start+1:end]
            text = text.replace(f'{{{var_name}}}', str(self.variables.get(var_name, '')))
        print(text)

    def visitAssignment(self, ctx):
        self.variables[ctx.ID().getText()] = self.visit(ctx.expression())

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.getChild(1).getText() == '*':
            return left * right
        else:
            return left // right

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.getChild(1).getText() == '+':
            return left + right
        else:
            return left - right

    def visitComparisonExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '>': return left > right
        if op == '<': return left < right
        if op == '>=': return left >= right
        if op == '<=': return left <= right

    def visitEqualityExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '==': return left == right
        if op == '!=': return left != right

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expression())

    def visitIntExpr(self, ctx):
        return int(ctx.INT().getText())

    def visitIdExpr(self, ctx):
        return self.variables.get(ctx.ID().getText(), 0)

    def visitConditionalStatement(self, ctx):
        if self.visit(ctx.expression()):
            self.visit(ctx.block(0))
        elif ctx.WHENEVER() and len(ctx.block()) > 1:
            self.visit(ctx.block(1))

    def visitLoopStatement(self, ctx):
        while self.visit(ctx.expression()):
            self.visit(ctx.block())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python pandorax_executor.py arquivo.pandoraX")
        sys.exit(1)

    input_stream = FileStream(sys.argv[1], encoding='utf-8')
    lexer = PandoraXLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # Preenche o stream com todos os tokens
    stream.fill()
    
    # Mostra os tokens antes de executar
    print_tokens(stream, lexer)
    
    parser = PandoraXParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(PandoraXErrorListener())
    
    try:
        tree = parser.program()
        executor = PandoraXExecutor()
        executor.visit(tree)
    except Exception as e:
        print(f"Erro durante execução: {str(e)}")
        sys.exit(1)