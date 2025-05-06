import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from PandoraXLexer import PandoraXLexer
from PandoraXParser import PandoraXParser
from PandoraXVisitor import PandoraXVisitor


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"ERRO SINTÁTICO na linha {line}, coluna {column}: {msg}")
        sys.exit(1)


class CustomLexer(PandoraXLexer):
    def notifyListeners(self, e):
        line = self._tokenStartLine
        column = self._tokenStartColumn
        msg = f"ERRO LÉXICO na linha {line}, coluna {column}: símbolo inválido '{self._input.getText(self._tokenStartCharIndex, self._input.index)}'"
        print(msg)
        sys.exit(1)


class PandoraXExecutor(PandoraXVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)

    def visitOutputStatement(self, ctx):
        interpolated_str = ctx.INTERPOLATED_STRING().getText()[1:-1]  # Remove < e >
        # Processa interpolação
        parts = []
        current = interpolated_str
        while True:
            start = current.find('{')
            end = current.find('}')
            if start == -1 or end == -1:
                parts.append(current)
                break
            parts.append(current[:start])
            var_name = current[start+1:end]
            parts.append(str(self.variables.get(var_name, '')))
            current = current[end+1:]
        print(''.join(parts))

    def visitInputStatement(self, ctx):
        var_name = ctx.ID().getText()
        prompt = ctx.summonCall().INTERPOLATED_STRING().getText()[1:-1]  # Remove < e >
        user_input = input(prompt)
        
        if ctx.typeCast().INTER():
            try:
                self.variables[var_name] = int(user_input)
            except ValueError:
                print(f"Erro: '{user_input}' não é um número inteiro válido")
                sys.exit(1)
        else:  # STRIN
            self.variables[var_name] = user_input

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value

    def visitArithmeticExpression(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        
        if op == '+': return left + right
        if op == '-': return left - right
        if op == '*': return left * right
        if op == '/': return left // right  # Divisão inteira

    def visitComparisonExpression(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        
        if op == '>': return left > right
        if op == '<': return left < right
        if op == '>=': return left >= right
        if op == '<=': return left <= right
        if op == '==': return left == right
        if op == '!=': return left != right

    def visitParenExpression(self, ctx):
        return self.visit(ctx.expression())

    def visitIntExpression(self, ctx):
        return int(ctx.INT().getText())

    def visitIdExpression(self, ctx):
        var_name = ctx.ID().getText()
        return self.variables.get(var_name, 0)

    def visitConditionalStatement(self, ctx):
        condition = self.visit(ctx.expression())
        if condition:
            self.visit(ctx.block(0))
        elif ctx.WHENEVER() and len(ctx.block()) > 1:
            self.visit(ctx.block(1))

    def visitLoopStatement(self, ctx):
        while self.visit(ctx.expression()):
            self.visit(ctx.block())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python executor.py <arquivo.pandoraX>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    input_stream = FileStream(input_path, encoding='utf-8')

    lexer = CustomLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    
    # Mostrar tokens (opcional - para debug)
    print("=== TOKENS IDENTIFICADOS ===")
    token_stream.fill()
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            print(f"{lexer.symbolicNames[token.type]}: '{token.text}' (linha {token.line}, coluna {token.column})")
    print("============================\n")

    parser = PandoraXParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    try:
        tree = parser.program()
        executor = PandoraXExecutor()
        executor.visit(tree)
    except Exception as e:
        print(f"Erro durante execução: {str(e)}")
        sys.exit(1)