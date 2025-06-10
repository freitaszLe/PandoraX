# semantic_analyzer.py

from PandoraXVisitor import PandoraXVisitor

# =====================================================================
#  FASE 4: ANALISADOR SEMÂNTICO 
# Classe Visitor para verificar regras semânticas (tipos, variáveis, etc.).
# =====================================================================

class PandoraXSemanticAnalyzer(PandoraXVisitor):
    def __init__(self):
        self.symbol_table = {}  # nome da variável -> tipo ('inter', 'strin', 'bool')
        self.errors = []
        self.log = []

    def visitProgram(self, ctx):
        self.log.append("Iniciando análise semântica.")
        for stmt in ctx.statement():
            self.visit(stmt)
        self.log.append("Análise semântica finalizada.")
        return self.errors, self.log

    # Visita uma declaração (com ou sem 'summon')
    def visitDeclaration(self, ctx):
        var_name = ctx.ID().getText()
        
        # Verifica se a variável já foi declarada
        if var_name in self.symbol_table:
            self.errors.append(f"Erro na linha {ctx.start.line}: Variável '{var_name}' já foi declarada.")
            return

        # Declaração com atribuição normal
        if ctx.expression():
            var_type = ctx.typeCast().getText().lower()
            expr_type = self.visit(ctx.expression())
            
            if expr_type != "erro" and expr_type != var_type:
                self.errors.append(f"Erro na linha {ctx.start.line}: Atribuição incompatível. Tentando atribuir '{expr_type}' para a variável '{var_name}' do tipo '{var_type}'.")
            
            self.symbol_table[var_name] = var_type
            self.log.append(f"Variável '{var_name}' declarada como '{var_type}'.")
        # Declaração com 'summon' (input do usuário)
        else:
            var_type = ctx.typeCast(0).getText().lower()
            self.symbol_table[var_name] = var_type
            self.log.append(f"Variável '{var_name}' declarada como '{var_type}' via summon.")


    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        if var_name not in self.symbol_table:
            self.errors.append(f"Erro na linha {ctx.start.line}: Variável '{var_name}' não foi declarada antes da atribuição.")
            return

        var_type = self.symbol_table[var_name]
        expr_type = self.visit(ctx.expression())

        if expr_type != "erro" and expr_type != var_type:
            self.errors.append(f"Erro na linha {ctx.start.line}: Tipo incompatível ao atribuir '{expr_type}' para variável '{var_name}' do tipo '{var_type}'.")

    def visitIdExpr(self, ctx):
        name = ctx.ID().getText()
        if name not in self.symbol_table:
            self.errors.append(f"Erro na linha {ctx.start.line}: Variável '{name}' usada sem declaração.")
            return "erro"
        return self.symbol_table[name]

    def visitIntExpr(self, ctx):
        return "inter"

    def visitBoolExpr(self, ctx):
        return "bool"
        
    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != "inter" or right != "inter":
            self.errors.append(f"Erro na linha {ctx.start.line}: Operação de soma/subtração requer operandos inteiros.")
            return "erro"
        return "inter"

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        # Detectar divisão por zero literal (simples)
        if op == "/" and hasattr(ctx.expression(1), 'INT') and ctx.expression(1).getText() == "0":
            self.errors.append(f"Erro na linha {ctx.start.line}: Divisão por zero literal detectada.")
        if left != "inter" or right != "inter":
            self.errors.append(f"Erro na linha {ctx.start.line}: Operação de multiplicação/divisão requer operandos inteiros.")
            return "erro"
        return "inter"

    def visitAndExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != "bool" or right != "bool":
            self.errors.append(f"Erro na linha {ctx.start.line}: Operação 'and' requer operandos booleanos.")
            return "erro"
        return "bool"

    def visitOrExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != "bool" or right != "bool":
            self.errors.append(f"Erro na linha {ctx.start.line}: Operação 'or' requer operandos booleanos.")
            return "erro"
        return "bool"

    def visitEqualityExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != "erro" and right != "erro" and left != right:
            self.errors.append(f"Erro na linha {ctx.start.line}: Comparação de igualdade entre tipos diferentes ('{left}' e '{right}').")
            return "erro"
        return "bool"

    def visitComparisonExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != "inter" or right != "inter":
            self.errors.append(f"Erro na linha {ctx.start.line}: Comparação (>, <, >=, <=) requer operandos inteiros.")
            return "erro"
        return "bool"

    def visitNotExpr(self, ctx):
        expr = self.visit(ctx.expression())
        if expr != "bool":
            self.errors.append(f"Erro na linha {ctx.start.line}: Operação 'not' requer operando booleano.")
            return "erro"
        return "bool"

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expression())