# Generated from SimpleMathParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("Y\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\3\3\3\5\3\35\n\3\3\4\3\4\6\4!\n\4\r\4\16\4\"\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5-\n\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6?\n\6")
        buf.write("\3\7\3\7\5\7C\n\7\3\b\3\b\6\bG\n\b\r\b\16\bH\3\t\6\tL")
        buf.write("\n\t\r\t\16\tM\3\t\3\t\7\tR\n\t\f\t\16\tU\13\t\5\tW\n")
        buf.write("\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\2\2\\\2\27\3\2\2\2\4")
        buf.write("\34\3\2\2\2\6\36\3\2\2\2\b,\3\2\2\2\n>\3\2\2\2\fB\3\2")
        buf.write("\2\2\16D\3\2\2\2\20K\3\2\2\2\22\23\5\4\3\2\23\24\7\16")
        buf.write("\2\2\24\26\3\2\2\2\25\22\3\2\2\2\26\31\3\2\2\2\27\25\3")
        buf.write("\2\2\2\27\30\3\2\2\2\30\3\3\2\2\2\31\27\3\2\2\2\32\35")
        buf.write("\5\b\5\2\33\35\5\6\4\2\34\32\3\2\2\2\34\33\3\2\2\2\35")
        buf.write("\5\3\2\2\2\36 \7\r\2\2\37!\7\3\2\2 \37\3\2\2\2!\"\3\2")
        buf.write("\2\2\" \3\2\2\2\"#\3\2\2\2#\7\3\2\2\2$%\5\16\b\2%&\7\b")
        buf.write("\2\2&\'\5\f\7\2\'-\3\2\2\2()\5\16\b\2)*\7\b\2\2*+\5\n")
        buf.write("\6\2+-\3\2\2\2,$\3\2\2\2,(\3\2\2\2-\t\3\2\2\2./\5\f\7")
        buf.write("\2/\60\7\t\2\2\60\61\5\f\7\2\61?\3\2\2\2\62\63\5\f\7\2")
        buf.write("\63\64\7\n\2\2\64\65\5\f\7\2\65?\3\2\2\2\66\67\5\f\7\2")
        buf.write("\678\7\13\2\289\5\f\7\29?\3\2\2\2:;\5\f\7\2;<\7\f\2\2")
        buf.write("<=\5\f\7\2=?\3\2\2\2>.\3\2\2\2>\62\3\2\2\2>\66\3\2\2\2")
        buf.write(">:\3\2\2\2?\13\3\2\2\2@C\5\16\b\2AC\5\20\t\2B@\3\2\2\2")
        buf.write("BA\3\2\2\2C\r\3\2\2\2DF\7\7\2\2EG\7\4\2\2FE\3\2\2\2GH")
        buf.write("\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\17\3\2\2\2JL\7\5\2\2KJ\3")
        buf.write("\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NV\3\2\2\2OS\7\6\2")
        buf.write("\2PR\7\5\2\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T")
        buf.write("W\3\2\2\2US\3\2\2\2VO\3\2\2\2VW\3\2\2\2W\21\3\2\2\2\f")
        buf.write("\27\34\",>BHMSV")
        return buf.getvalue()


class SimpleMathParser ( Parser ):

    grammarFileName = "SimpleMathParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'", "'$'", "'='", "'+'", "'-'", "'*'", "'/'", "'#'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "COMMENTCHARACTER", "VARCHARACTER", "DIGIT", 
                      "DOT", "DOLLAR", "EQUAL", "ADD", "SUBTRACT", "MULTIPLY", 
                      "DIVIDE", "HASH", "SEMI" ]

    RULE_script = 0
    RULE_command = 1
    RULE_comment = 2
    RULE_assign = 3
    RULE_calculate = 4
    RULE_value = 5
    RULE_variable = 6
    RULE_digit = 7

    ruleNames =  [ "script", "command", "comment", "assign", "calculate", 
                   "value", "variable", "digit" ]

    EOF = Token.EOF
    COMMENTCHARACTER=1
    VARCHARACTER=2
    DIGIT=3
    DOT=4
    DOLLAR=5
    EQUAL=6
    ADD=7
    SUBTRACT=8
    MULTIPLY=9
    DIVIDE=10
    HASH=11
    SEMI=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ScriptContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleMathParser.CommandContext)
            else:
                return self.getTypedRuleContext(SimpleMathParser.CommandContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleMathParser.SEMI)
            else:
                return self.getToken(SimpleMathParser.SEMI, i)

        def getRuleIndex(self):
            return SimpleMathParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)




    def script(self):

        localctx = SimpleMathParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimpleMathParser.DOLLAR or _la==SimpleMathParser.HASH:
                self.state = 16
                self.command()
                self.state = 17
                self.match(SimpleMathParser.SEMI)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(SimpleMathParser.AssignContext,0)


        def comment(self):
            return self.getTypedRuleContext(SimpleMathParser.CommentContext,0)


        def getRuleIndex(self):
            return SimpleMathParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = SimpleMathParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimpleMathParser.DOLLAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.assign()
                pass
            elif token in [SimpleMathParser.HASH]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.comment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASH(self):
            return self.getToken(SimpleMathParser.HASH, 0)

        def COMMENTCHARACTER(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleMathParser.COMMENTCHARACTER)
            else:
                return self.getToken(SimpleMathParser.COMMENTCHARACTER, i)

        def getRuleIndex(self):
            return SimpleMathParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = SimpleMathParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(SimpleMathParser.HASH)
            self.state = 30 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 29
                self.match(SimpleMathParser.COMMENTCHARACTER)
                self.state = 32 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SimpleMathParser.COMMENTCHARACTER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(SimpleMathParser.VariableContext,0)


        def EQUAL(self):
            return self.getToken(SimpleMathParser.EQUAL, 0)

        def value(self):
            return self.getTypedRuleContext(SimpleMathParser.ValueContext,0)


        def calculate(self):
            return self.getTypedRuleContext(SimpleMathParser.CalculateContext,0)


        def getRuleIndex(self):
            return SimpleMathParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = SimpleMathParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign)
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.variable()
                self.state = 35
                self.match(SimpleMathParser.EQUAL)
                self.state = 36
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.variable()
                self.state = 39
                self.match(SimpleMathParser.EQUAL)
                self.state = 40
                self.calculate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CalculateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleMathParser.ValueContext)
            else:
                return self.getTypedRuleContext(SimpleMathParser.ValueContext,i)


        def ADD(self):
            return self.getToken(SimpleMathParser.ADD, 0)

        def SUBTRACT(self):
            return self.getToken(SimpleMathParser.SUBTRACT, 0)

        def MULTIPLY(self):
            return self.getToken(SimpleMathParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(SimpleMathParser.DIVIDE, 0)

        def getRuleIndex(self):
            return SimpleMathParser.RULE_calculate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalculate" ):
                listener.enterCalculate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalculate" ):
                listener.exitCalculate(self)




    def calculate(self):

        localctx = SimpleMathParser.CalculateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_calculate)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.value()
                self.state = 45
                self.match(SimpleMathParser.ADD)
                self.state = 46
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.value()
                self.state = 49
                self.match(SimpleMathParser.SUBTRACT)
                self.state = 50
                self.value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.value()
                self.state = 53
                self.match(SimpleMathParser.MULTIPLY)
                self.state = 54
                self.value()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.value()
                self.state = 57
                self.match(SimpleMathParser.DIVIDE)
                self.state = 58
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(SimpleMathParser.VariableContext,0)


        def digit(self):
            return self.getTypedRuleContext(SimpleMathParser.DigitContext,0)


        def getRuleIndex(self):
            return SimpleMathParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = SimpleMathParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_value)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimpleMathParser.DOLLAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.variable()
                pass
            elif token in [SimpleMathParser.DIGIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.digit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR(self):
            return self.getToken(SimpleMathParser.DOLLAR, 0)

        def VARCHARACTER(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleMathParser.VARCHARACTER)
            else:
                return self.getToken(SimpleMathParser.VARCHARACTER, i)

        def getRuleIndex(self):
            return SimpleMathParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = SimpleMathParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(SimpleMathParser.DOLLAR)
            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                self.match(SimpleMathParser.VARCHARACTER)
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SimpleMathParser.VARCHARACTER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DigitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleMathParser.DIGIT)
            else:
                return self.getToken(SimpleMathParser.DIGIT, i)

        def DOT(self):
            return self.getToken(SimpleMathParser.DOT, 0)

        def getRuleIndex(self):
            return SimpleMathParser.RULE_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigit" ):
                listener.enterDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigit" ):
                listener.exitDigit(self)




    def digit(self):

        localctx = SimpleMathParser.DigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_digit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self.match(SimpleMathParser.DIGIT)
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SimpleMathParser.DIGIT):
                    break

            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimpleMathParser.DOT:
                self.state = 77
                self.match(SimpleMathParser.DOT)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SimpleMathParser.DIGIT:
                    self.state = 78
                    self.match(SimpleMathParser.DIGIT)
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





