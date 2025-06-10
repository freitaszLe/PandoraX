# Conteúdo COMPLETO para o arquivo: executor.py

from PandoraXVisitor import PandoraXVisitor
from PandoraXParser import PandoraXParser

# =====================================================================
# 🚀 CLASSE DE EXECUÇÃO (INTERPRETADOR) - VERSÃO CORRIGIDA E COMPLETA 🚀
# =====================================================================

class PandoraX_executor(PandoraXVisitor):
    def __init__(self):
        # Dicionário para armazenar as variáveis durante a execução
        self.variables = {}

    # --- Métodos para ESTRUTURAS da Linguagem ---

    def visitProgram(self, ctx:PandoraXParser.ProgramContext):
        # Visita cada uma das declarações (statements) do programa
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitDeclaration(self, ctx:PandoraXParser.DeclarationContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value

    def visitAssignment(self, ctx:PandoraXParser.AssignmentContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value

    def visitOutputStatement(self, ctx:PandoraXParser.OutputStatementContext):
        text = ctx.INTERPOLATED_STRING().getText()[1:-1]
        # Lógica para substituir variáveis na string, se houver
        # (Esta parte pode ser expandida depois)
        print(text)

    def visitConditionalStatement(self, ctx:PandoraXParser.ConditionalStatementContext):
        condition = self.visit(ctx.expression())
        if condition:
            self.visit(ctx.block(0))
        elif ctx.WHENEVER() and len(ctx.block()) > 1:
            self.visit(ctx.block(1))

    def visitBlock(self, ctx:PandoraXParser.BlockContext):
        # Executa cada statement dentro de um bloco { ... }
        for stmt in ctx.statement():
            self.visit(stmt)


    # --- Métodos para EXPRESSÕES (A PARTE QUE FALTAVA!) ---

    def visitAddSubExpr(self, ctx:PandoraXParser.AddSubExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '+':
            return left + right
        return left - right

    def visitMulDivExpr(self, ctx:PandoraXParser.MulDivExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '*':
            return left * right
        return left // right # Divisão inteira

    def visitComparisonExpr(self, ctx:PandoraXParser.ComparisonExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '>': return left > right
        if op == '<': return left < right
        if op == '>=': return left >= right
        if op == '<=': return left <= right

    def visitEqualityExpr(self, ctx:PandoraXParser.EqualityExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '==': return left == right
        if op == '!=': return left != right

    def visitAndExpr(self, ctx:PandoraXParser.AndExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left and right

    def visitOrExpr(self, ctx:PandoraXParser.OrExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left or right

    def visitNotExpr(self, ctx:PandoraXParser.NotExprContext):
        return not self.visit(ctx.expression())

    def visitParenExpr(self, ctx:PandoraXParser.ParenExprContext):
        return self.visit(ctx.expression())

    # --- Métodos para EXPRESSÕES Atômicas (Valores) ---

    def visitIntExpr(self, ctx:PandoraXParser.IntExprContext):
        return int(ctx.INT().getText())

    def visitBoolExpr(self, ctx:PandoraXParser.BoolExprContext):
        return ctx.BOOL().getText() == 'true'

    def visitIdExpr(self, ctx:PandoraXParser.IdExprContext):
        var_name = ctx.ID().getText()
        return self.variables.get(var_name)