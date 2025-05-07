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


    # Visit a parse tree produced by PandoraXParser#AndExpr.
    def visitAndExpr(self, ctx:PandoraXParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#BoolExpr.
    def visitBoolExpr(self, ctx:PandoraXParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:PandoraXParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#EqualityExpr.
    def visitEqualityExpr(self, ctx:PandoraXParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#IdExpr.
    def visitIdExpr(self, ctx:PandoraXParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#ComparisonExpr.
    def visitComparisonExpr(self, ctx:PandoraXParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#NotExpr.
    def visitNotExpr(self, ctx:PandoraXParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#IntExpr.
    def visitIntExpr(self, ctx:PandoraXParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#ParenExpr.
    def visitParenExpr(self, ctx:PandoraXParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:PandoraXParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PandoraXParser#OrExpr.
    def visitOrExpr(self, ctx:PandoraXParser.OrExprContext):
        return self.visitChildren(ctx)



del PandoraXParser