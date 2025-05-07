import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees
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

class PandoraXASTGenerator(PandoraXVisitor):
    def __init__(self):
        self.dot = ['digraph AST {', '  node [shape=box, fontname="Courier"];']
        self.node_count = 0
        self.parent_stack = []
        self.result = None

    def visit(self, ctx):
        if ctx is None:
            return None

        node_name = Trees.getNodeText(ctx, ruleNames=PandoraXParser.ruleNames)
        node_id = f'node{self.node_count}'
        self.node_count += 1
        
        self.dot.append(f'  {node_id} [label="{node_name}"];')
        
        if self.parent_stack:
            self.dot.append(f'  {self.parent_stack[-1]} -> {node_id};')
        
        self.parent_stack.append(node_id)
        
        # Process children
        try:
            if hasattr(ctx, 'children'):
                for child in ctx.children:
                    if isinstance(child, ParserRuleContext):
                        self.visit(child)
                    elif isinstance(child, TerminalNode) and child.getSymbol().type != Token.EOF:
                        self._add_terminal_node(child)
        except Exception as e:
            print(f"Erro ao visitar filhos: {str(e)}")
        
        self.parent_stack.pop()
        
        if not self.parent_stack:
            self.dot.append('}')
            self.result = '\n'.join(self.dot)
        
        return self.result

    def _add_terminal_node(self, terminal_node):
        node_id = f'node{self.node_count}'
        self.node_count += 1
        token_text = terminal_node.getText().replace('"', '\\"')
        self.dot.append(f'  {node_id} [label="{token_text}", shape=ellipse, color=blue];')
        if self.parent_stack:
            self.dot.append(f'  {self.parent_stack[-1]} -> {node_id};')

    def get_dot(self):
        return self.result
    
class PandoraXExecutor(PandoraXVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitInputStatement(self, ctx):
        var_name = ctx.ID().getText()
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

    def visitAndExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left and right

    def visitOrExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left or right

    def visitNotExpr(self, ctx):
        return not self.visit(ctx.expression())

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expression())

    def visitIntExpr(self, ctx):
        return int(ctx.INT().getText())

    def visitBoolExpr(self, ctx):
        return ctx.BOOL().getText() == 'true'

    def visitIdExpr(self, ctx):
        val = self.variables.get(ctx.ID().getText())
        if isinstance(val, bool):
            return val
        return val if val is not None else 0

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
    
    stream.fill()
    print_tokens(stream, lexer)
    
    parser = PandoraXParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(PandoraXErrorListener())
    
    try:
        tree = parser.program()
        
        # Geração da AST (nova funcionalidade)
        ast_generator = PandoraXASTGenerator()
        ast_generator.visit(tree)  # Isso agora popula o resultado automaticamente
        dot_code = ast_generator.get_dot()
        
        # Salva o arquivo .dot com o mesmo nome do arquivo de entrada
        base_name = os.path.splitext(sys.argv[1])[0]
        dot_file = f"{base_name}_ast.dot"
        with open(dot_file, "w") as f:
            f.write(dot_code)
        print(f"\nArquivo AST gerado: {dot_file}")
        
        # Execução normal do código PandoraX
        executor = PandoraXExecutor()
        executor.visit(tree)
        
    except Exception as e:
        print(f"Erro durante execução: {str(e)}")
        sys.exit(1)