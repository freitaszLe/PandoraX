from PandoraXVisitor import PandoraXVisitor

class PandoraXSemanticAnalyzer(PandoraXVisitor):
    def __init__(self):
        self.symbol_table = {}  # nome da variável -> tipo ('inter', 'strin', 'bool')
        self.errors = []
        self.log = []

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        return self.errors, self.log

    def visitDeclaration(self, ctx):
        # Pode ser:
        # 1) typeCast ID EQ expression
        # 2) ID EQ typeCast LPAREN SUMMON LPAREN INTERPOLATED_STRING RPAREN RPAREN

        if ctx.typeCast() is not None:
            # Caso 1
            var_type = ctx.typeCast().getText().lower()
            var_name = ctx.ID().getText()
            expr_type = self.visit(ctx.expression())
            if var_name in self.symbol_table:
                self.errors.append(f"Erro: variável '{var_name}' já foi declarada.")
            else:
                if expr_type != var_type and expr_type != "erro":
                    self.errors.append(f"Erro: atribuição incompatível: '{expr_type}' para '{var_type}' na declaração da variável '{var_name}'.")
                self.symbol_table[var_name] = var_type
                self.log.append(f"Variável '{var_name}' declarada como '{var_type}'.")
        else:
            # Caso 2 (summon)
            var_name = ctx.ID().getText()
            var_type = ctx.typeCast().getText().lower()
            if var_name in self.symbol_table:
                self.errors.append(f"Erro: variável '{var_name}' já foi declarada.")
            else:
                self.symbol_table[var_name] = var_type
                self.log.append(f"Variável '{var_name}' declarada como '{var_type}' via summon.")

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        if var_name not in self.symbol_table:
            self.errors.append(f"Erro: variável '{var_name}' não foi declarada antes da atribuição.")
            return

        var_type = self.symbol_table[var_name]
        expr_type = self.visit(ctx.expression())

        if expr_type == "erro":
            return

        if expr_type != var_type:
            self.errors.append(f"Erro: tipo incompatível ao atribuir '{expr_type}' para variável '{var_name}' do tipo '{var_type}'.")

    def visitIdExpr(self, ctx):
        name = ctx.ID().getText()
        if name not in self.symbol_table:
            self.errors.append(f"Erro: variável '{name}' usada sem declaração.")
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
            self.errors.append("Erro: operação de soma/subtração requer operandos inteiros.")
            return "erro"
        return "inter"

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        # Detectar divisão por zero literal (simples)
        if op == "/" and ctx.expression(1).getText() == "0":
            self.errors.append("Erro: divisão por zero detectada.")
        if left != "inter" or right != "inter":
            self.errors.append("Erro: operação de multiplicação/divisão requer operandos inteiros.")
            return "erro"
        return "inter"

    def visitAndExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != "bool" or right != "bool":
            self.errors.append("Erro: operação 'and' requer operandos booleanos.")
            return "erro"
        return "bool"

    def visitOrExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != "bool" or right != "bool":
            self.errors.append("Erro: operação 'or' requer operandos booleanos.")
            return "erro"
        return "bool"

    def visitEqualityExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != right:
            self.errors.append("Erro: comparação entre tipos diferentes.")
            return "erro"
        return "bool"

    def visitComparisonExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if left != "inter" or right != "inter":
            self.errors.append("Erro: comparação requer operandos inteiros.")
            return "erro"
        return "bool"

    def visitNotExpr(self, ctx):
        expr = self.visit(ctx.expression())
        if expr != "bool":
            self.errors.append("Erro: operação 'not' requer operando booleano.")
            return "erro"
        return "bool"

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expression())
