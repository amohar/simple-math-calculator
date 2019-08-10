# Generated from SimpleMathParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("p\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3\3\3")
        buf.write("\7\3\35\n\3\f\3\16\3 \13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4*\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\5\5:\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6J\n\6\3\7\3\7\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\5\tV\n\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nh\n\n")
        buf.write("\3\13\3\13\5\13l\n\13\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\2\2\2p\2\30\3\2\2\2\4\36\3\2\2\2\6)\3\2\2")
        buf.write("\2\b9\3\2\2\2\nI\3\2\2\2\fK\3\2\2\2\16M\3\2\2\2\20U\3")
        buf.write("\2\2\2\22g\3\2\2\2\24k\3\2\2\2\26m\3\2\2\2\30\31\5\4\3")
        buf.write("\2\31\3\3\2\2\2\32\35\5\6\4\2\33\35\5\16\b\2\34\32\3\2")
        buf.write("\2\2\34\33\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2")
        buf.write("\2\2\37\5\3\2\2\2 \36\3\2\2\2!\"\5\20\t\2\"#\7\b\2\2#")
        buf.write("*\3\2\2\2$*\5\b\5\2%*\5\n\6\2&\'\5\f\7\2\'(\7\b\2\2(*")
        buf.write("\3\2\2\2)!\3\2\2\2)$\3\2\2\2)%\3\2\2\2)&\3\2\2\2*\7\3")
        buf.write("\2\2\2+,\7\20\2\2,-\7\t\2\2-.\5\24\13\2./\7\n\2\2/\60")
        buf.write("\7\13\2\2\60\61\5\4\3\2\61\62\7\f\2\2\62:\3\2\2\2\63\64")
        buf.write("\7\20\2\2\64\65\7\t\2\2\65\66\5\24\13\2\66\67\7\n\2\2")
        buf.write("\678\5\6\4\28:\3\2\2\29+\3\2\2\29\63\3\2\2\2:\t\3\2\2")
        buf.write("\2;<\7\21\2\2<=\7\t\2\2=>\5\24\13\2>?\7\n\2\2?@\7\13\2")
        buf.write("\2@A\5\4\3\2AB\7\f\2\2BJ\3\2\2\2CD\7\21\2\2DE\7\t\2\2")
        buf.write("EF\5\24\13\2FG\7\n\2\2GH\5\6\4\2HJ\3\2\2\2I;\3\2\2\2I")
        buf.write("C\3\2\2\2J\13\3\2\2\2KL\7\22\2\2L\r\3\2\2\2MN\7\16\2\2")
        buf.write("N\17\3\2\2\2OP\7\r\2\2PQ\7\3\2\2QV\5\24\13\2RS\7\r\2\2")
        buf.write("ST\7\3\2\2TV\5\22\n\2UO\3\2\2\2UR\3\2\2\2V\21\3\2\2\2")
        buf.write("WX\5\24\13\2XY\7\4\2\2YZ\5\24\13\2Zh\3\2\2\2[\\\5\24\13")
        buf.write("\2\\]\7\5\2\2]^\5\24\13\2^h\3\2\2\2_`\5\24\13\2`a\7\6")
        buf.write("\2\2ab\5\24\13\2bh\3\2\2\2cd\5\24\13\2de\7\7\2\2ef\5\24")
        buf.write("\13\2fh\3\2\2\2gW\3\2\2\2g[\3\2\2\2g_\3\2\2\2gc\3\2\2")
        buf.write("\2h\23\3\2\2\2il\7\r\2\2jl\5\26\f\2ki\3\2\2\2kj\3\2\2")
        buf.write("\2l\25\3\2\2\2mn\7\17\2\2n\27\3\2\2\2\n\34\36)9IUgk")
        return buf.getvalue()


class SimpleMathParser ( Parser ):

    grammarFileName = "SimpleMathParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "'-'", "'*'", "'/'", "';'", 
                     "'('", "')'", "'{'", "'}'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'if'", "'while'", "'break'" ]

    symbolicNames = [ "<INVALID>", "EQUAL", "ADD", "SUBTRACT", "MULTIPLY", 
                      "DIVIDE", "SEMI", "BRACE_L", "BRACE_R", "CURLY_L", 
                      "CURLY_R", "VARIABLE", "COMMENT", "NUMBER", "IF", 
                      "WHILE", "BREAK", "WS" ]

    RULE_script = 0
    RULE_body = 1
    RULE_command = 2
    RULE_if_command = 3
    RULE_while_command = 4
    RULE_break_command = 5
    RULE_comment = 6
    RULE_assign = 7
    RULE_calculate = 8
    RULE_value = 9
    RULE_number = 10

    ruleNames =  [ "script", "body", "command", "if_command", "while_command", 
                   "break_command", "comment", "assign", "calculate", "value", 
                   "number" ]

    EOF = Token.EOF
    EQUAL=1
    ADD=2
    SUBTRACT=3
    MULTIPLY=4
    DIVIDE=5
    SEMI=6
    BRACE_L=7
    BRACE_R=8
    CURLY_L=9
    CURLY_R=10
    VARIABLE=11
    COMMENT=12
    NUMBER=13
    IF=14
    WHILE=15
    BREAK=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ScriptContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(SimpleMathParser.BodyContext,0)


        def getRuleIndex(self):
            return SimpleMathParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScript" ):
                return visitor.visitScript(self)
            else:
                return visitor.visitChildren(self)




    def script(self):

        localctx = SimpleMathParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleMathParser.CommandContext)
            else:
                return self.getTypedRuleContext(SimpleMathParser.CommandContext,i)


        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleMathParser.CommentContext)
            else:
                return self.getTypedRuleContext(SimpleMathParser.CommentContext,i)


        def getRuleIndex(self):
            return SimpleMathParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = SimpleMathParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleMathParser.VARIABLE) | (1 << SimpleMathParser.COMMENT) | (1 << SimpleMathParser.IF) | (1 << SimpleMathParser.WHILE) | (1 << SimpleMathParser.BREAK))) != 0):
                self.state = 26
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SimpleMathParser.VARIABLE, SimpleMathParser.IF, SimpleMathParser.WHILE, SimpleMathParser.BREAK]:
                    self.state = 24
                    self.command()
                    pass
                elif token in [SimpleMathParser.COMMENT]:
                    self.state = 25
                    self.comment()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 30
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


        def SEMI(self):
            return self.getToken(SimpleMathParser.SEMI, 0)

        def if_command(self):
            return self.getTypedRuleContext(SimpleMathParser.If_commandContext,0)


        def while_command(self):
            return self.getTypedRuleContext(SimpleMathParser.While_commandContext,0)


        def break_command(self):
            return self.getTypedRuleContext(SimpleMathParser.Break_commandContext,0)


        def getRuleIndex(self):
            return SimpleMathParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = SimpleMathParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimpleMathParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.assign()
                self.state = 32
                self.match(SimpleMathParser.SEMI)
                pass
            elif token in [SimpleMathParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.if_command()
                pass
            elif token in [SimpleMathParser.WHILE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.while_command()
                pass
            elif token in [SimpleMathParser.BREAK]:
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.break_command()
                self.state = 37
                self.match(SimpleMathParser.SEMI)
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

    class If_commandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SimpleMathParser.IF, 0)

        def BRACE_L(self):
            return self.getToken(SimpleMathParser.BRACE_L, 0)

        def value(self):
            return self.getTypedRuleContext(SimpleMathParser.ValueContext,0)


        def BRACE_R(self):
            return self.getToken(SimpleMathParser.BRACE_R, 0)

        def CURLY_L(self):
            return self.getToken(SimpleMathParser.CURLY_L, 0)

        def body(self):
            return self.getTypedRuleContext(SimpleMathParser.BodyContext,0)


        def CURLY_R(self):
            return self.getToken(SimpleMathParser.CURLY_R, 0)

        def command(self):
            return self.getTypedRuleContext(SimpleMathParser.CommandContext,0)


        def getRuleIndex(self):
            return SimpleMathParser.RULE_if_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_command" ):
                listener.enterIf_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_command" ):
                listener.exitIf_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_command" ):
                return visitor.visitIf_command(self)
            else:
                return visitor.visitChildren(self)




    def if_command(self):

        localctx = SimpleMathParser.If_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_if_command)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(SimpleMathParser.IF)
                self.state = 42
                self.match(SimpleMathParser.BRACE_L)
                self.state = 43
                self.value()
                self.state = 44
                self.match(SimpleMathParser.BRACE_R)
                self.state = 45
                self.match(SimpleMathParser.CURLY_L)
                self.state = 46
                self.body()
                self.state = 47
                self.match(SimpleMathParser.CURLY_R)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(SimpleMathParser.IF)
                self.state = 50
                self.match(SimpleMathParser.BRACE_L)
                self.state = 51
                self.value()
                self.state = 52
                self.match(SimpleMathParser.BRACE_R)
                self.state = 53
                self.command()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class While_commandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(SimpleMathParser.WHILE, 0)

        def BRACE_L(self):
            return self.getToken(SimpleMathParser.BRACE_L, 0)

        def value(self):
            return self.getTypedRuleContext(SimpleMathParser.ValueContext,0)


        def BRACE_R(self):
            return self.getToken(SimpleMathParser.BRACE_R, 0)

        def CURLY_L(self):
            return self.getToken(SimpleMathParser.CURLY_L, 0)

        def body(self):
            return self.getTypedRuleContext(SimpleMathParser.BodyContext,0)


        def CURLY_R(self):
            return self.getToken(SimpleMathParser.CURLY_R, 0)

        def command(self):
            return self.getTypedRuleContext(SimpleMathParser.CommandContext,0)


        def getRuleIndex(self):
            return SimpleMathParser.RULE_while_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_command" ):
                listener.enterWhile_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_command" ):
                listener.exitWhile_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_command" ):
                return visitor.visitWhile_command(self)
            else:
                return visitor.visitChildren(self)




    def while_command(self):

        localctx = SimpleMathParser.While_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_while_command)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.match(SimpleMathParser.WHILE)
                self.state = 58
                self.match(SimpleMathParser.BRACE_L)
                self.state = 59
                self.value()
                self.state = 60
                self.match(SimpleMathParser.BRACE_R)
                self.state = 61
                self.match(SimpleMathParser.CURLY_L)
                self.state = 62
                self.body()
                self.state = 63
                self.match(SimpleMathParser.CURLY_R)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(SimpleMathParser.WHILE)
                self.state = 66
                self.match(SimpleMathParser.BRACE_L)
                self.state = 67
                self.value()
                self.state = 68
                self.match(SimpleMathParser.BRACE_R)
                self.state = 69
                self.command()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Break_commandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(SimpleMathParser.BREAK, 0)

        def getRuleIndex(self):
            return SimpleMathParser.RULE_break_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_command" ):
                listener.enterBreak_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_command" ):
                listener.exitBreak_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_command" ):
                return visitor.visitBreak_command(self)
            else:
                return visitor.visitChildren(self)




    def break_command(self):

        localctx = SimpleMathParser.Break_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_break_command)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(SimpleMathParser.BREAK)
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

        def COMMENT(self):
            return self.getToken(SimpleMathParser.COMMENT, 0)

        def getRuleIndex(self):
            return SimpleMathParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = SimpleMathParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(SimpleMathParser.COMMENT)
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

        def VARIABLE(self):
            return self.getToken(SimpleMathParser.VARIABLE, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = SimpleMathParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assign)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(SimpleMathParser.VARIABLE)
                self.state = 78
                self.match(SimpleMathParser.EQUAL)
                self.state = 79
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(SimpleMathParser.VARIABLE)
                self.state = 81
                self.match(SimpleMathParser.EQUAL)
                self.state = 82
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalculate" ):
                return visitor.visitCalculate(self)
            else:
                return visitor.visitChildren(self)




    def calculate(self):

        localctx = SimpleMathParser.CalculateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_calculate)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.value()
                self.state = 86
                self.match(SimpleMathParser.ADD)
                self.state = 87
                self.value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.value()
                self.state = 90
                self.match(SimpleMathParser.SUBTRACT)
                self.state = 91
                self.value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.value()
                self.state = 94
                self.match(SimpleMathParser.MULTIPLY)
                self.state = 95
                self.value()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.value()
                self.state = 98
                self.match(SimpleMathParser.DIVIDE)
                self.state = 99
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

        def VARIABLE(self):
            return self.getToken(SimpleMathParser.VARIABLE, 0)

        def number(self):
            return self.getTypedRuleContext(SimpleMathParser.NumberContext,0)


        def getRuleIndex(self):
            return SimpleMathParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = SimpleMathParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimpleMathParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(SimpleMathParser.VARIABLE)
                pass
            elif token in [SimpleMathParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.number()
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

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SimpleMathParser.NUMBER, 0)

        def getRuleIndex(self):
            return SimpleMathParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = SimpleMathParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(SimpleMathParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





