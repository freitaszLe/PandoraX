# Generated from PandoraX.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PandoraXParser import PandoraXParser
else:
    from PandoraXParser import PandoraXParser

# This class defines a complete listener for a parse tree produced by PandoraXParser.
class PandoraXListener(ParseTreeListener):

    # Enter a parse tree produced by PandoraXParser#program.
    def enterProgram(self, ctx:PandoraXParser.ProgramContext):
        pass

    # Exit a parse tree produced by PandoraXParser#program.
    def exitProgram(self, ctx:PandoraXParser.ProgramContext):
        pass


    # Enter a parse tree produced by PandoraXParser#statement.
    def enterStatement(self, ctx:PandoraXParser.StatementContext):
        pass

    # Exit a parse tree produced by PandoraXParser#statement.
    def exitStatement(self, ctx:PandoraXParser.StatementContext):
        pass


    # Enter a parse tree produced by PandoraXParser#declaration.
    def enterDeclaration(self, ctx:PandoraXParser.DeclarationContext):
        pass

    # Exit a parse tree produced by PandoraXParser#declaration.
    def exitDeclaration(self, ctx:PandoraXParser.DeclarationContext):
        pass


    # Enter a parse tree produced by PandoraXParser#typeCast.
    def enterTypeCast(self, ctx:PandoraXParser.TypeCastContext):
        pass

    # Exit a parse tree produced by PandoraXParser#typeCast.
    def exitTypeCast(self, ctx:PandoraXParser.TypeCastContext):
        pass


    # Enter a parse tree produced by PandoraXParser#outputStatement.
    def enterOutputStatement(self, ctx:PandoraXParser.OutputStatementContext):
        pass

    # Exit a parse tree produced by PandoraXParser#outputStatement.
    def exitOutputStatement(self, ctx:PandoraXParser.OutputStatementContext):
        pass


    # Enter a parse tree produced by PandoraXParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:PandoraXParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by PandoraXParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:PandoraXParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by PandoraXParser#loopStatement.
    def enterLoopStatement(self, ctx:PandoraXParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by PandoraXParser#loopStatement.
    def exitLoopStatement(self, ctx:PandoraXParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by PandoraXParser#assignment.
    def enterAssignment(self, ctx:PandoraXParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PandoraXParser#assignment.
    def exitAssignment(self, ctx:PandoraXParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PandoraXParser#block.
    def enterBlock(self, ctx:PandoraXParser.BlockContext):
        pass

    # Exit a parse tree produced by PandoraXParser#block.
    def exitBlock(self, ctx:PandoraXParser.BlockContext):
        pass


    # Enter a parse tree produced by PandoraXParser#AndExpr.
    def enterAndExpr(self, ctx:PandoraXParser.AndExprContext):
        pass

    # Exit a parse tree produced by PandoraXParser#AndExpr.
    def exitAndExpr(self, ctx:PandoraXParser.AndExprContext):
        pass


    # Enter a parse tree produced by PandoraXParser#BoolExpr.
    def enterBoolExpr(self, ctx:PandoraXParser.BoolExprContext):
        pass

    # Exit a parse tree produced by PandoraXParser#BoolExpr.
    def exitBoolExpr(self, ctx:PandoraXParser.BoolExprContext):
        pass


    # Enter a parse tree produced by PandoraXParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:PandoraXParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by PandoraXParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:PandoraXParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by PandoraXParser#EqualityExpr.
    def enterEqualityExpr(self, ctx:PandoraXParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by PandoraXParser#EqualityExpr.
    def exitEqualityExpr(self, ctx:PandoraXParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by PandoraXParser#IdExpr.
    def enterIdExpr(self, ctx:PandoraXParser.IdExprContext):
        pass

    # Exit a parse tree produced by PandoraXParser#IdExpr.
    def exitIdExpr(self, ctx:PandoraXParser.IdExprContext):
        pass


    # Enter a parse tree produced by PandoraXParser#ComparisonExpr.
    def enterComparisonExpr(self, ctx:PandoraXParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by PandoraXParser#ComparisonExpr.
    def exitComparisonExpr(self, ctx:PandoraXParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by PandoraXParser#NotExpr.
    def enterNotExpr(self, ctx:PandoraXParser.NotExprContext):
        pass

    # Exit a parse tree produced by PandoraXParser#NotExpr.
    def exitNotExpr(self, ctx:PandoraXParser.NotExprContext):
        pass


    # Enter a parse tree produced by PandoraXParser#IntExpr.
    def enterIntExpr(self, ctx:PandoraXParser.IntExprContext):
        pass

    # Exit a parse tree produced by PandoraXParser#IntExpr.
    def exitIntExpr(self, ctx:PandoraXParser.IntExprContext):
        pass


    # Enter a parse tree produced by PandoraXParser#ParenExpr.
    def enterParenExpr(self, ctx:PandoraXParser.ParenExprContext):
        pass

    # Exit a parse tree produced by PandoraXParser#ParenExpr.
    def exitParenExpr(self, ctx:PandoraXParser.ParenExprContext):
        pass


    # Enter a parse tree produced by PandoraXParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:PandoraXParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by PandoraXParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:PandoraXParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by PandoraXParser#OrExpr.
    def enterOrExpr(self, ctx:PandoraXParser.OrExprContext):
        pass

    # Exit a parse tree produced by PandoraXParser#OrExpr.
    def exitOrExpr(self, ctx:PandoraXParser.OrExprContext):
        pass



del PandoraXParser