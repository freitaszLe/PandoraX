
# =====================================================================
#  ANALISADOR SEMÂNTICO 
# Classe Visitor para verificar regras semânticas (tipos, variáveis, etc.).
# =====================================================================
# semantic_analyzer.py

from PandoraXVisitor import PandoraXVisitor
from PandoraXParser import PandoraXParser

class PandoraXSemanticAnalyzer(PandoraXVisitor):
    def __init__(self):
        # A tabela de símbolos armazena o TIPO de cada variável declarada.
        self.symbol_table = {}
        self.errors = []
        self.log = []

    def visitProgram(self, ctx:PandoraXParser.ProgramContext):
        self.log.append("Iniciando análise semântica.")
        # O método 'visit' padrão do ANTLR já visita todos os filhos,
        # então um loop explícito aqui não é necessário se chamarmos super().visitProgram(ctx)
        # Mas para clareza, vamos visitar cada statement.
        for stmt in ctx.statement():
            self.visit(stmt)
        self.log.append("Análise semântica finalizada.")
        return self.errors, self.log

    def visitDeclaration(self, ctx:PandoraXParser.DeclarationContext):
        var_name = ctx.ID().getText()

        # Usa a TABELA DE SÍMBOLOS para verificar se a variável já existe.
        if var_name in self.symbol_table:
            self.errors.append(f"Erro na linha {ctx.start.line}: Variável '{var_name}' já foi declarada.")
            return

        var_type = ctx.typeCast().getText().lower()
        expr_type = self.visit(ctx.expression())

        if expr_type is not None and expr_type != "erro" and expr_type != var_type:
            self.errors.append(f"Erro de tipo na declaração de '{var_name}'. Esperava '{var_type}', recebeu '{expr_type}'.")

        # Adiciona a nova variável e seu TIPO à TABELA DE SÍMBOLOS.
        self.symbol_table[var_name] = var_type
        self.log.append(f"Variável '{var_name}' declarada como '{var_type}'.")

    # Em semantic_analyzer.py, adicione este novo método:

    def visitSummonExpr(self, ctx:PandoraXParser.SummonExprContext):
        # A expressão retorna o tipo especificado no typeCast.
        # Ex: inter(summon.x(...)) retorna o tipo "inter".
        return ctx.typeCast().getText().lower()
    # Em semantic_analyzer.py, adicione este novo método

    def visitStrinExpr(self, ctx:PandoraXParser.StrinExprContext):
        # Quando o analisador encontra uma string literal, o tipo dela é sempre 'strin'.
        return "strin"

    def visitAssignment(self, ctx:PandoraXParser.AssignmentContext):
        var_name = ctx.ID().getText()

        # Usa a TABELA DE SÍMBOLOS para verificar se a variável existe antes de atribuir.
        if var_name not in self.symbol_table:
            self.errors.append(f"Erro na linha {ctx.start.line}: Variável '{var_name}' não foi declarada.")
            return

        expected_type = self.symbol_table[var_name]
        expr_type = self.visit(ctx.expression())

        if expr_type != "erro" and expr_type != expected_type:
            self.errors.append(f"Erro de tipo na atribuição para '{var_name}'. Esperava '{expected_type}', recebeu '{expr_type}'.")

    def visitIdExpr(self, ctx:PandoraXParser.IdExprContext):
        var_name = ctx.ID().getText()

        # Usa a TABELA DE SÍMBOLOS para obter o TIPO de uma variável quando ela é usada numa expressão.
        if var_name not in self.symbol_table:
            self.errors.append(f"Erro na linha {ctx.start.line}: Variável '{var_name}' usada sem ser declarada.")
            return "erro"
        return self.symbol_table[var_name]

    # --- Métodos de verificação de tipo para expressões ---

    def visitIntExpr(self, ctx:PandoraXParser.IntExprContext):
        return "inter"

    def visitBoolExpr(self, ctx:PandoraXParser.BoolExprContext):
        return "bool"
        
    def visitAddSubExpr(self, ctx:PandoraXParser.AddSubExprContext):
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        if left_type != "inter" or right_type != "inter":
            self.errors.append(f"Erro na linha {ctx.start.line}: Operações aritméticas (+, -) só podem ser feitas com o tipo 'inter'.")
            return "erro"
        return "inter"

    # Adicione aqui outros métodos visit para expressões (MulDiv, Comparison, etc.)
    # seguindo o mesmo padrão de verificar os tipos dos filhos.
    def visitMulDivExpr(self, ctx:PandoraXParser.MulDivExprContext):
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        if left_type != "inter" or right_type != "inter":
            self.errors.append(f"Erro na linha {ctx.start.line}: Operações aritméticas (*, /) só podem ser feitas com o tipo 'inter'.")
            return "erro"
        return "inter"

    def visitComparisonExpr(self, ctx:PandoraXParser.ComparisonExprContext):
        left_type = self.visit(ctx.expression(0))
        right_type = self.visit(ctx.expression(1))
        if left_type != "inter" or right_type != "inter":
            self.errors.append(f"Erro na linha {ctx.start.line}: Comparações (>, <, etc.) só podem ser feitas com o tipo 'inter'.")
            return "erro"
        return "bool"
        
    def visitEqualityExpr(self, ctx:PandoraXParser.EqualityExprContext):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        return "bool"

    def visitParenExpr(self, ctx:PandoraXParser.ParenExprContext):
        return self.visit(ctx.expression())