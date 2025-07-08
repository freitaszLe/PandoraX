# tac_generator.py

from PandoraXVisitor import PandoraXVisitor
from PandoraXParser import PandoraXParser
from tac_ir import TACOperand, TACInstruction

class TACGenerator(PandoraXVisitor):
    def __init__(self):
        self.tac_code = []
        self.temp_count = 0
        self.label_count = 0

    def new_temp(self):
        temp_name = f"_t{self.temp_count}"
        self.temp_count += 1
        return TACOperand(temp_name)

    def new_label(self):
        label_name = f"L{self.label_count}"
        self.label_count += 1
        return TACOperand(label_name)

    # --- Métodos de Estrutura ---
    def visitProgram(self, ctx:PandoraXParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitBlock(self, ctx:PandoraXParser.BlockContext):
        for stmt in ctx.statement():
            self.visit(stmt)
            
    # --- Métodos de Statements ---
    def visitDeclaration(self, ctx:PandoraXParser.DeclarationContext):
        var_name_op = TACOperand(ctx.ID().getText())
        if ctx.expression():
            expr_op = self.visit(ctx.expression())
            self.tac_code.append(TACInstruction('COPY', var_name_op, expr_op))

    def visitAssignment(self, ctx:PandoraXParser.AssignmentContext):
        var_name_op = TACOperand(ctx.ID().getText())
        expr_op = self.visit(ctx.expression())
        self.tac_code.append(TACInstruction('COPY', var_name_op, expr_op))

    def visitOutputStatement(self, ctx:PandoraXParser.OutputStatementContext):
        string_literal = TACOperand(ctx.INTERPOLATED_STRING().getText())
        self.tac_code.append(TACInstruction('PRINT', arg1=string_literal))

    def visitConditionalStatement(self, ctx:PandoraXParser.ConditionalStatementContext):
        condition_op = self.visit(ctx.expression())
        else_label = self.new_label()
        end_label = self.new_label()
        
        self.tac_code.append(TACInstruction('IF_FALSE', else_label, condition_op))
        self.visit(ctx.block(0))
        self.tac_code.append(TACInstruction('GOTO', end_label))
        
        self.tac_code.append(TACInstruction('LABEL', else_label))
        if ctx.WHENEVER():
            self.visit(ctx.block(1))
            
        self.tac_code.append(TACInstruction('LABEL', end_label))

    # --- Métodos de Expressões ---
    def visitSummonExpr(self, ctx:PandoraXParser.SummonExprContext):
        result_temp = self.new_temp()
        prompt_op = TACOperand(ctx.INTERPOLATED_STRING().getText())
        self.tac_code.append(TACInstruction('SUMMON', result_temp, prompt_op))
        return result_temp
        
    def visitStrinExpr(self, ctx:PandoraXParser.StrinExprContext):
        return TACOperand(ctx.getText())

    def visitParenExpr(self, ctx:PandoraXParser.ParenExprContext):
        return self.visit(ctx.expression())

    def visitIdExpr(self, ctx:PandoraXParser.IdExprContext):
        return TACOperand(ctx.getText())

    def visitIntExpr(self, ctx:PandoraXParser.IntExprContext):
        return TACOperand(ctx.getText())
    
    # Adicione visitBoolExpr se tiver
    def visitBoolExpr(self, ctx:PandoraXParser.BoolExprContext):
        val = 1 if ctx.getText() == 'true' else 0
        return TACOperand(str(val))

    def _generate_binary_expr(self, ctx, opcode):
        op1 = self.visit(ctx.expression(0))
        op2 = self.visit(ctx.expression(1))
        result_temp = self.new_temp()
        self.tac_code.append(TACInstruction(opcode, result_temp, op1, op2))
        return result_temp

    def visitAddSubExpr(self, ctx:PandoraXParser.AddSubExprContext):
        return self._generate_binary_expr(ctx, ctx.getChild(1).getText())

    def visitMulDivExpr(self, ctx:PandoraXParser.MulDivExprContext):
        return self._generate_binary_expr(ctx, ctx.getChild(1).getText())

    def visitComparisonExpr(self, ctx:PandoraXParser.ComparisonExprContext):
        return self._generate_binary_expr(ctx, ctx.getChild(1).getText())

    def visitEqualityExpr(self, ctx:PandoraXParser.EqualityExprContext):
        return self._generate_binary_expr(ctx, ctx.getChild(1).getText())

    def visitAndExpr(self, ctx:PandoraXParser.AndExprContext):
        return self._generate_binary_expr(ctx, 'and')

    def visitOrExpr(self, ctx:PandoraXParser.OrExprContext):
        return self._generate_binary_expr(ctx, 'or')