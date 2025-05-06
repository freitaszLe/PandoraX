# Generated from C:/Users/Leticia/OneDrive/Desktop/myCompiler/grammar/PandoraX.g4 by ANTLR 4.13.2
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
        4,1,21,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,52,8,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,3,5,61,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,4,8,73,
        8,8,11,8,12,8,74,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,84,8,9,1,9,1,9,
        1,9,5,9,89,8,9,10,9,12,9,92,9,9,1,10,1,10,1,10,1,10,1,10,1,10,0,
        1,18,11,0,2,4,6,8,10,12,14,16,18,20,0,2,1,0,1,2,1,0,12,15,98,0,25,
        1,0,0,0,2,35,1,0,0,0,4,37,1,0,0,0,6,39,1,0,0,0,8,46,1,0,0,0,10,53,
        1,0,0,0,12,62,1,0,0,0,14,67,1,0,0,0,16,72,1,0,0,0,18,83,1,0,0,0,
        20,93,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,
        0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,0,0,1,29,
        1,1,0,0,0,30,36,3,6,3,0,31,36,3,8,4,0,32,36,3,10,5,0,33,36,3,12,
        6,0,34,36,3,14,7,0,35,30,1,0,0,0,35,31,1,0,0,0,35,32,1,0,0,0,35,
        33,1,0,0,0,35,34,1,0,0,0,36,3,1,0,0,0,37,38,7,0,0,0,38,5,1,0,0,0,
        39,40,5,17,0,0,40,41,5,3,0,0,41,42,3,4,2,0,42,43,5,4,0,0,43,44,3,
        20,10,0,44,45,5,5,0,0,45,7,1,0,0,0,46,47,5,6,0,0,47,48,5,4,0,0,48,
        49,5,19,0,0,49,51,5,5,0,0,50,52,5,7,0,0,51,50,1,0,0,0,51,52,1,0,
        0,0,52,9,1,0,0,0,53,54,5,8,0,0,54,55,3,18,9,0,55,56,5,9,0,0,56,60,
        3,16,8,0,57,58,5,10,0,0,58,59,5,9,0,0,59,61,3,16,8,0,60,57,1,0,0,
        0,60,61,1,0,0,0,61,11,1,0,0,0,62,63,5,11,0,0,63,64,3,18,9,0,64,65,
        5,9,0,0,65,66,3,16,8,0,66,13,1,0,0,0,67,68,5,17,0,0,68,69,5,3,0,
        0,69,70,3,18,9,0,70,15,1,0,0,0,71,73,3,2,1,0,72,71,1,0,0,0,73,74,
        1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,17,1,0,0,0,76,77,6,9,-1,0,
        77,78,5,4,0,0,78,79,3,18,9,0,79,80,5,5,0,0,80,84,1,0,0,0,81,84,5,
        18,0,0,82,84,5,17,0,0,83,76,1,0,0,0,83,81,1,0,0,0,83,82,1,0,0,0,
        84,90,1,0,0,0,85,86,10,4,0,0,86,87,7,1,0,0,87,89,3,18,9,5,88,85,
        1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,19,1,0,0,0,
        92,90,1,0,0,0,93,94,5,16,0,0,94,95,5,4,0,0,95,96,5,19,0,0,96,97,
        5,5,0,0,97,21,1,0,0,0,7,25,35,51,60,74,83,90
    ]

class PandoraXParser ( Parser ):

    grammarFileName = "PandoraX.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'inter'", "'strin'", "'='", "'('", "')'", 
                     "'pandora.expose'", "';'", "'when'", "':'", "'whenever'", 
                     "'loopX'", "'+'", "'-'", "'*'", "'/'", "'summon.x'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "STRING", "WS", "COMMENT" ]

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
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    ID=17
    INT=18
    STRING=19
    WS=20
    COMMENT=21

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 133440) != 0):
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
            if not(_la==1 or _la==2):
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

        def typeCast(self):
            return self.getTypedRuleContext(PandoraXParser.TypeCastContext,0)


        def summonCall(self):
            return self.getTypedRuleContext(PandoraXParser.SummonCallContext,0)


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
            self.match(PandoraXParser.T__2)
            self.state = 41
            self.typeCast()
            self.state = 42
            self.match(PandoraXParser.T__3)
            self.state = 43
            self.summonCall()
            self.state = 44
            self.match(PandoraXParser.T__4)
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

        def STRING(self):
            return self.getToken(PandoraXParser.STRING, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(PandoraXParser.T__5)
            self.state = 47
            self.match(PandoraXParser.T__3)
            self.state = 48
            self.match(PandoraXParser.STRING)
            self.state = 49
            self.match(PandoraXParser.T__4)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 50
                self.match(PandoraXParser.T__6)


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

        def expression(self):
            return self.getTypedRuleContext(PandoraXParser.ExpressionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PandoraXParser.BlockContext)
            else:
                return self.getTypedRuleContext(PandoraXParser.BlockContext,i)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(PandoraXParser.T__7)
            self.state = 54
            self.expression(0)
            self.state = 55
            self.match(PandoraXParser.T__8)
            self.state = 56
            self.block()
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 57
                self.match(PandoraXParser.T__9)
                self.state = 58
                self.match(PandoraXParser.T__8)
                self.state = 59
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
            self.state = 62
            self.match(PandoraXParser.T__10)
            self.state = 63
            self.expression(0)
            self.state = 64
            self.match(PandoraXParser.T__8)
            self.state = 65
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
            self.state = 67
            self.match(PandoraXParser.ID)
            self.state = 68
            self.match(PandoraXParser.T__2)
            self.state = 69
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 71
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 74 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PandoraXParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PandoraXParser.ExpressionContext,i)


        def INT(self):
            return self.getToken(PandoraXParser.INT, 0)

        def ID(self):
            return self.getToken(PandoraXParser.ID, 0)

        def getRuleIndex(self):
            return PandoraXParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
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
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 77
                self.match(PandoraXParser.T__3)
                self.state = 78
                self.expression(0)
                self.state = 79
                self.match(PandoraXParser.T__4)
                pass
            elif token in [18]:
                self.state = 81
                self.match(PandoraXParser.INT)
                pass
            elif token in [17]:
                self.state = 82
                self.match(PandoraXParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PandoraXParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 85
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 86
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 87
                    self.expression(5) 
                self.state = 92
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

        def STRING(self):
            return self.getToken(PandoraXParser.STRING, 0)

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
            self.state = 93
            self.match(PandoraXParser.T__15)
            self.state = 94
            self.match(PandoraXParser.T__3)
            self.state = 95
            self.match(PandoraXParser.STRING)
            self.state = 96
            self.match(PandoraXParser.T__4)
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
                return self.precpred(self._ctx, 4)
         




