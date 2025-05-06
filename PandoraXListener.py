# Generated from C:/Users/Leticia/OneDrive/Desktop/myCompiler/grammar/PandoraX.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by PandoraXParser#typeCast.
    def enterTypeCast(self, ctx:PandoraXParser.TypeCastContext):
        pass

    # Exit a parse tree produced by PandoraXParser#typeCast.
    def exitTypeCast(self, ctx:PandoraXParser.TypeCastContext):
        pass


    # Enter a parse tree produced by PandoraXParser#inputStatement.
    def enterInputStatement(self, ctx:PandoraXParser.InputStatementContext):
        pass

    # Exit a parse tree produced by PandoraXParser#inputStatement.
    def exitInputStatement(self, ctx:PandoraXParser.InputStatementContext):
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


    # Enter a parse tree produced by PandoraXParser#expression.
    def enterExpression(self, ctx:PandoraXParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PandoraXParser#expression.
    def exitExpression(self, ctx:PandoraXParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PandoraXParser#summonCall.
    def enterSummonCall(self, ctx:PandoraXParser.SummonCallContext):
        pass

    # Exit a parse tree produced by PandoraXParser#summonCall.
    def exitSummonCall(self, ctx:PandoraXParser.SummonCallContext):
        pass



del PandoraXParser