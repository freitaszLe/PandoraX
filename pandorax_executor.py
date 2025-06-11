# Conteúdo COMPLETO para o arquivo: executor.py

from PandoraXVisitor import PandoraXVisitor
from PandoraXParser import PandoraXParser
import re
# =====================================================================
# 🚀 CLASSE DE EXECUÇÃO (INTERPRETADOR)  🚀
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
        # Em executor.py, adicione este novo método

    def visitStrinExpr(self, ctx:PandoraXParser.StrinExprContext):
        # Pega o texto completo, incluindo os <>
        text_com_aspas = ctx.getText()
        # Retorna o texto removendo o primeiro caractere ('<') e o último ('>')
        return text_com_aspas[1:-1]
    
    def visitAssignment(self, ctx:PandoraXParser.AssignmentContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value

    def visitOutputStatement(self, ctx:PandoraXParser.OutputStatementContext):
        # 1. Pega o texto da string, sem os <>
        text = ctx.INTERPOLATED_STRING().getText()[1:-1]
        
        # 2. Define uma função auxiliar que sabe como substituir uma variável
        def replacer(match):
            # Pega o nome da variável que foi encontrado dentro das chaves {}
            var_name = match.group(1)
            # Busca o valor da variável na memória do executor
            value = self.variables.get(var_name, "nulo") # Usa "nulo" se não encontrar
            # Retorna o valor como string
            return str(value)

        # 3. Usa o módulo 're' para encontrar todas as ocorrências de {variavel}
        # e chamar a função 'replacer' para cada uma, fazendo a substituição.
        final_text = re.sub(r'\{([a-zA-Z_][a-zA-Z_0-9]*)\}', replacer, text)
        
        # 4. Imprime o texto final com os valores já substituídos
        print(final_text)

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


    def visitSummonExpr(self, ctx:PandoraXParser.SummonExprContext):
        target_type = ctx.typeCast().getText().lower()
        prompt_message = ctx.INTERPOLATED_STRING().getText()[1:-1]
        
        user_input = input(prompt_message + " ")
        
        try:
            if target_type == 'inter':
                return int(user_input)
            elif target_type == 'strin':
                return str(user_input)
            # Adicione outros tipos aqui se necessário
            return user_input
        except ValueError:
            print(f"\nERRO DE EXECUÇÃO: Valor '{user_input}' é inválido para o tipo '{target_type}'.")
            if target_type == 'inter':
                return 0  # Retorna um valor padrão em caso de erro
            return None
        
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