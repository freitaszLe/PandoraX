# Generated from PandoraX.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,27,101,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,57,8,5,
        1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,5,8,69,8,8,10,8,12,8,72,
        9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,83,8,9,1,9,1,9,1,9,1,
        9,1,9,1,9,5,9,91,8,9,10,9,12,9,94,9,9,1,10,1,10,1,10,1,10,1,10,1,
        10,0,1,18,11,0,2,4,6,8,10,12,14,16,18,20,0,3,1,0,9,10,1,0,13,16,
        1,0,18,23,100,0,25,1,0,0,0,2,35,1,0,0,0,4,37,1,0,0,0,6,39,1,0,0,
        0,8,46,1,0,0,0,10,51,1,0,0,0,12,58,1,0,0,0,14,62,1,0,0,0,16,66,1,
        0,0,0,18,82,1,0,0,0,20,95,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,
        27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,
        0,28,29,5,0,0,1,29,1,1,0,0,0,30,36,3,6,3,0,31,36,3,8,4,0,32,36,3,
        10,5,0,33,36,3,12,6,0,34,36,3,14,7,0,35,30,1,0,0,0,35,31,1,0,0,0,
        35,32,1,0,0,0,35,33,1,0,0,0,35,34,1,0,0,0,36,3,1,0,0,0,37,38,7,0,
        0,0,38,5,1,0,0,0,39,40,5,1,0,0,40,41,5,17,0,0,41,42,3,4,2,0,42,43,
        5,24,0,0,43,44,3,20,10,0,44,45,5,25,0,0,45,7,1,0,0,0,46,47,5,11,
        0,0,47,48,5,24,0,0,48,49,5,3,0,0,49,50,5,25,0,0,50,9,1,0,0,0,51,
        52,5,6,0,0,52,53,3,18,9,0,53,56,3,16,8,0,54,55,5,7,0,0,55,57,3,16,
        8,0,56,54,1,0,0,0,56,57,1,0,0,0,57,11,1,0,0,0,58,59,5,8,0,0,59,60,
        3,18,9,0,60,61,3,16,8,0,61,13,1,0,0,0,62,63,5,1,0,0,63,64,5,17,0,
        0,64,65,3,18,9,0,65,15,1,0,0,0,66,70,5,26,0,0,67,69,3,2,1,0,68,67,
        1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,
        72,70,1,0,0,0,73,74,5,27,0,0,74,17,1,0,0,0,75,76,6,9,-1,0,76,77,
        5,24,0,0,77,78,3,18,9,0,78,79,5,25,0,0,79,83,1,0,0,0,80,83,5,2,0,
        0,81,83,5,1,0,0,82,75,1,0,0,0,82,80,1,0,0,0,82,81,1,0,0,0,83,92,
        1,0,0,0,84,85,10,5,0,0,85,86,7,1,0,0,86,91,3,18,9,6,87,88,10,4,0,
        0,88,89,7,2,0,0,89,91,3,18,9,5,90,84,1,0,0,0,90,87,1,0,0,0,91,94,
        1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,19,1,0,0,0,94,92,1,0,0,0,
        95,96,5,12,0,0,96,97,5,24,0,0,97,98,5,3,0,0,98,99,5,25,0,0,99,21,
        1,0,0,0,7,25,35,56,70,82,90,92
    ]

class PandoraXParser ( Parser ):

    grammarFileName = "PandoraX.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'when'", "'whenever'", "'loopX'", 
                     "'inter'", "'strin'", "'pandora.expose'", "'summon.x'", 
                     "'+'", "'-'", "'*'", "'/'", "'='", "'<'", "'>'", "'<='", 
                     "'>='", "'=='", "'!='", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "ID", "INT", "INTERPOLATED_STRING", "WS", 
                      "COMMENT", "WHEN", "WHENEVER", "LOOPX", "INTER", "STRIN", 
                      "PANDORAEXPOSE", "SUMMON", "PLUS", "MINUS", "MULT", 
                      "DIV", "EQ", "LT", "GT", "LE", "GE", "EQEQ", "NEQ", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_typeCast = 2
    RULE_inputStatement = 3
    RULE_outputStatement = 4
    RULE_conditionalStatement = 5
    RULE_loopStatement = 6
    RULE_assignment = 7
    RULE_block = 8
    RULE_expression = 9
    RULE_summonCall = 10

    ruleNames =  [ "program", "statement", "typeCast", "inputStatement", 
                   "outputStatement", "conditionalStatement", "loopStatement", 
                   "assignment", "block", "expression", "summonCall" ]

    EOF = Token.EOF
    ID=1
    INT=2
    INTERPOLATED_STRING=3
    WS=4
    COMMENT=5
    WHEN=6
    WHENEVER=7
    LOOPX=8
    INTER=9
    STRIN=10
    PANDORAEXPOSE=11
    SUMMON=12
    PLUS=13
    MINUS=14
    MULT=15
    DIV=16
    EQ=17
    LT=18
    GT=19
    LE=20
    GE=21
    EQEQ=22
    NEQ=23
    LPAREN=24
    RPAREN=25
    LBRACE=26
    RBRACE=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PandoraXParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PandoraXParser.StatementContext)
            else:
                return self.getTypedRuleContext(PandoraXParser.StatementContext,i)


        def getRuleIndex(self):
            return PandoraXParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PandoraXParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2370) != 0):
                self.state = 22
                self.statement()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(PandoraXParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inputStatement(self):
            return self.getTypedRuleContext(PandoraXParser.InputStatementContext,0)


        def outputStatement(self):
            return self.getTypedRuleContext(PandoraXParser.OutputStatementContext,0)


        def conditionalStatement(self):
            return self.getTypedRuleContext(PandoraXParser.ConditionalStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(PandoraXParser.LoopStatementContext,0)


        def assignment(self):
            return self.getTypedRuleContext(PandoraXParser.AssignmentContext,0)


        def getRuleIndex(self):
            return PandoraXParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PandoraXParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.inputStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.outputStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.conditionalStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.loopStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeCastContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTER(self):
            return self.getToken(PandoraXParser.INTER, 0)

        def STRIN(self):
            return self.getToken(PandoraXParser.STRIN, 0)

        def getRuleIndex(self):
            return PandoraXParser.RULE_typeCast

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeCast" ):
                listener.enterTypeCast(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeCast" ):
                listener.exitTypeCast(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeCast" ):
                return visitor.visitTypeCast(self)
            else:
                return visitor.visitChildren(self)




    def typeCast(self):

        localctx = PandoraXParser.TypeCastContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_typeCast)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PandoraXParser.ID, 0)

        def EQ(self):
            return self.getToken(PandoraXParser.EQ, 0)

        def typeCast(self):
            return self.getTypedRuleContext(PandoraXParser.TypeCastContext,0)


        def LPAREN(self):
            return self.getToken(PandoraXParser.LPAREN, 0)

        def summonCall(self):
            return self.getTypedRuleContext(PandoraXParser.SummonCallContext,0)


        def RPAREN(self):
            return self.getToken(PandoraXParser.RPAREN, 0)

        def getRuleIndex(self):
            return PandoraXParser.RULE_inputStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStatement" ):
                listener.enterInputStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStatement" ):
                listener.exitInputStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputStatement" ):
                return visitor.visitInputStatement(self)
            else:
                return visitor.visitChildren(self)




    def inputStatement(self):

        localctx = PandoraXParser.InputStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_inputStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(PandoraXParser.ID)
            self.state = 40
            self.match(PandoraXParser.EQ)
            self.state = 41
            self.typeCast()
            self.state = 42
            self.match(PandoraXParser.LPAREN)
            self.state = 43
            self.summonCall()
            self.state = 44
            self.match(PandoraXParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PANDORAEXPOSE(self):
            return self.getToken(PandoraXParser.PANDORAEXPOSE, 0)

        def LPAREN(self):
            return self.getToken(PandoraXParser.LPAREN, 0)

        def INTERPOLATED_STRING(self):
            return self.getToken(PandoraXParser.INTERPOLATED_STRING, 0)

        def RPAREN(self):
            return self.getToken(PandoraXParser.RPAREN, 0)

        def getRuleIndex(self):
            return PandoraXParser.RULE_outputStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutputStatement" ):
                listener.enterOutputStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutputStatement" ):
                listener.exitOutputStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputStatement" ):
                return visitor.visitOutputStatement(self)
            else:
                return visitor.visitChildren(self)




    def outputStatement(self):

        localctx = PandoraXParser.OutputStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_outputStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(PandoraXParser.PANDORAEXPOSE)
            self.state = 47
            self.match(PandoraXParser.LPAREN)
            self.state = 48
            self.match(PandoraXParser.INTERPOLATED_STRING)
            self.state = 49
            self.match(PandoraXParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHEN(self):
            return self.getToken(PandoraXParser.WHEN, 0)

        def expression(self):
            return self.getTypedRuleContext(PandoraXParser.ExpressionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PandoraXParser.BlockContext)
            else:
                return self.getTypedRuleContext(PandoraXParser.BlockContext,i)


        def WHENEVER(self):
            return self.getToken(PandoraXParser.WHENEVER, 0)

        def getRuleIndex(self):
            return PandoraXParser.RULE_conditionalStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalStatement" ):
                listener.enterConditionalStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalStatement" ):
                listener.exitConditionalStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalStatement" ):
                return visitor.visitConditionalStatement(self)
            else:
                return visitor.visitChildren(self)




    def conditionalStatement(self):

        localctx = PandoraXParser.ConditionalStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_conditionalStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(PandoraXParser.WHEN)
            self.state = 52
            self.expression(0)
            self.state = 53
            self.block()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 54
                self.match(PandoraXParser.WHENEVER)
                self.state = 55
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOPX(self):
            return self.getToken(PandoraXParser.LOOPX, 0)

        def expression(self):
            return self.getTypedRuleContext(PandoraXParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(PandoraXParser.BlockContext,0)


        def getRuleIndex(self):
            return PandoraXParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = PandoraXParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(PandoraXParser.LOOPX)
            self.state = 59
            self.expression(0)
            self.state = 60
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PandoraXParser.ID, 0)

        def EQ(self):
            return self.getToken(PandoraXParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(PandoraXParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PandoraXParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = PandoraXParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(PandoraXParser.ID)
            self.state = 63
            self.match(PandoraXParser.EQ)
            self.state = 64
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(PandoraXParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PandoraXParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PandoraXParser.StatementContext)
            else:
                return self.getTypedRuleContext(PandoraXParser.StatementContext,i)


        def getRuleIndex(self):
            return PandoraXParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = PandoraXParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(PandoraXParser.LBRACE)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2370) != 0):
                self.state = 67
                self.statement()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
            self.match(PandoraXParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PandoraXParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IdExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PandoraXParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(PandoraXParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpression" ):
                listener.enterIdExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpression" ):
                listener.exitIdExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpression" ):
                return visitor.visitIdExpression(self)
            else:
                return visitor.visitChildren(self)


    class IntExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PandoraXParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(PandoraXParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpression" ):
                listener.enterIntExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpression" ):
                listener.exitIntExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpression" ):
                return visitor.visitIntExpression(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PandoraXParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PandoraXParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PandoraXParser.ExpressionContext,i)

        def GT(self):
            return self.getToken(PandoraXParser.GT, 0)
        def LT(self):
            return self.getToken(PandoraXParser.LT, 0)
        def GE(self):
            return self.getToken(PandoraXParser.GE, 0)
        def LE(self):
            return self.getToken(PandoraXParser.LE, 0)
        def EQEQ(self):
            return self.getToken(PandoraXParser.EQEQ, 0)
        def NEQ(self):
            return self.getToken(PandoraXParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpression" ):
                listener.enterComparisonExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpression" ):
                listener.exitComparisonExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpression" ):
                return visitor.visitComparisonExpression(self)
            else:
                return visitor.visitChildren(self)


    class ParenExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PandoraXParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(PandoraXParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(PandoraXParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(PandoraXParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpression" ):
                listener.enterParenExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpression" ):
                listener.exitParenExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpression" ):
                return visitor.visitParenExpression(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PandoraXParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PandoraXParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PandoraXParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(PandoraXParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(PandoraXParser.MINUS, 0)
        def MULT(self):
            return self.getToken(PandoraXParser.MULT, 0)
        def DIV(self):
            return self.getToken(PandoraXParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpression" ):
                listener.enterArithmeticExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpression" ):
                listener.exitArithmeticExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpression" ):
                return visitor.visitArithmeticExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PandoraXParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                localctx = PandoraXParser.ParenExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 76
                self.match(PandoraXParser.LPAREN)
                self.state = 77
                self.expression(0)
                self.state = 78
                self.match(PandoraXParser.RPAREN)
                pass
            elif token in [2]:
                localctx = PandoraXParser.IntExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                self.match(PandoraXParser.INT)
                pass
            elif token in [1]:
                localctx = PandoraXParser.IdExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                self.match(PandoraXParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 92
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 90
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = PandoraXParser.ArithmeticExpressionContext(self, PandoraXParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 84
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 85
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 86
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = PandoraXParser.ComparisonExpressionContext(self, PandoraXParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 87
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 88
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 89
                        self.expression(5)
                        pass

             
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SummonCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMMON(self):
            return self.getToken(PandoraXParser.SUMMON, 0)

        def LPAREN(self):
            return self.getToken(PandoraXParser.LPAREN, 0)

        def INTERPOLATED_STRING(self):
            return self.getToken(PandoraXParser.INTERPOLATED_STRING, 0)

        def RPAREN(self):
            return self.getToken(PandoraXParser.RPAREN, 0)

        def getRuleIndex(self):
            return PandoraXParser.RULE_summonCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSummonCall" ):
                listener.enterSummonCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSummonCall" ):
                listener.exitSummonCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSummonCall" ):
                return visitor.visitSummonCall(self)
            else:
                return visitor.visitChildren(self)




    def summonCall(self):

        localctx = PandoraXParser.SummonCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_summonCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(PandoraXParser.SUMMON)
            self.state = 96
            self.match(PandoraXParser.LPAREN)
            self.state = 97
            self.match(PandoraXParser.INTERPOLATED_STRING)
            self.state = 98
            self.match(PandoraXParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




