# Generated from PandoraX.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PandoraXParser import PandoraXParser
else:
    from PandoraXParser import PandoraXParser

# This class defines a complete generic visitor for a parse tree produced by PandoraXParser.

class PandoraXVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PandoraXParser#program.
    def visitProgram(self, ctx:PandoraXParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#statement.
    def visitStatement(self, ctx:PandoraXParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#typeCast.
    def visitTypeCast(self, ctx:PandoraXParser.TypeCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#inputStatement.
    def visitInputStatement(self, ctx:PandoraXParser.InputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#outputStatement.
    def visitOutputStatement(self, ctx:PandoraXParser.OutputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#conditionalStatement.
    def visitConditionalStatement(self, ctx:PandoraXParser.ConditionalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#loopStatement.
    def visitLoopStatement(self, ctx:PandoraXParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#assignment.
    def visitAssignment(self, ctx:PandoraXParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#block.
    def visitBlock(self, ctx:PandoraXParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#idExpression.
    def visitIdExpression(self, ctx:PandoraXParser.IdExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#intExpression.
    def visitIntExpression(self, ctx:PandoraXParser.IntExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:PandoraXParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#parenExpression.
    def visitParenExpression(self, ctx:PandoraXParser.ParenExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#arithmeticExpression.
    def visitArithmeticExpression(self, ctx:PandoraXParser.ArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#summonCall.
    def visitSummonCall(self, ctx:PandoraXParser.SummonCallContext):
        return self.visitChildren(ctx)



del PandoraXParser