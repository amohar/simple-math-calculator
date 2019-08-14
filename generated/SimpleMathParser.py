# Generated from SimpleMathParser.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\7\3\31\n\3\f\3\16")
        buf.write("\3\34\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4&\n\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\5\5\66\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\6F\n\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nY\n\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\7\na\n\n\f\n\16\nd\13\n\3\n\2\3\22")
        buf.write("\13\2\4\6\b\n\f\16\20\22\2\4\3\2\6\7\3\2\4\5\2h\2\24\3")
        buf.write("\2\2\2\4\32\3\2\2\2\6%\3\2\2\2\b\65\3\2\2\2\nE\3\2\2\2")
        buf.write("\fG\3\2\2\2\16I\3\2\2\2\20K\3\2\2\2\22X\3\2\2\2\24\25")
        buf.write("\5\4\3\2\25\3\3\2\2\2\26\31\5\6\4\2\27\31\5\16\b\2\30")
        buf.write("\26\3\2\2\2\30\27\3\2\2\2\31\34\3\2\2\2\32\30\3\2\2\2")
        buf.write("\32\33\3\2\2\2\33\5\3\2\2\2\34\32\3\2\2\2\35\36\5\20\t")
        buf.write("\2\36\37\7\b\2\2\37&\3\2\2\2 &\5\b\5\2!&\5\n\6\2\"#\5")
        buf.write("\f\7\2#$\7\b\2\2$&\3\2\2\2%\35\3\2\2\2% \3\2\2\2%!\3\2")
        buf.write("\2\2%\"\3\2\2\2&\7\3\2\2\2\'(\7\20\2\2()\7\t\2\2)*\5\22")
        buf.write("\n\2*+\7\n\2\2+,\7\13\2\2,-\5\4\3\2-.\7\f\2\2.\66\3\2")
        buf.write("\2\2/\60\7\20\2\2\60\61\7\t\2\2\61\62\5\22\n\2\62\63\7")
        buf.write("\n\2\2\63\64\5\6\4\2\64\66\3\2\2\2\65\'\3\2\2\2\65/\3")
        buf.write("\2\2\2\66\t\3\2\2\2\678\7\21\2\289\7\t\2\29:\5\22\n\2")
        buf.write(":;\7\n\2\2;<\7\13\2\2<=\5\4\3\2=>\7\f\2\2>F\3\2\2\2?@")
        buf.write("\7\21\2\2@A\7\t\2\2AB\5\22\n\2BC\7\n\2\2CD\5\6\4\2DF\3")
        buf.write("\2\2\2E\67\3\2\2\2E?\3\2\2\2F\13\3\2\2\2GH\7\22\2\2H\r")
        buf.write("\3\2\2\2IJ\7\16\2\2J\17\3\2\2\2KL\7\r\2\2LM\7\3\2\2MN")
        buf.write("\5\22\n\2N\21\3\2\2\2OP\b\n\1\2PQ\7\5\2\2QY\5\22\n\bR")
        buf.write("S\7\t\2\2ST\5\22\n\2TU\7\n\2\2UY\3\2\2\2VY\7\r\2\2WY\7")
        buf.write("\17\2\2XO\3\2\2\2XR\3\2\2\2XV\3\2\2\2XW\3\2\2\2Yb\3\2")
        buf.write("\2\2Z[\f\6\2\2[\\\t\2\2\2\\a\5\22\n\7]^\f\5\2\2^_\t\3")
        buf.write("\2\2_a\5\22\n\6`Z\3\2\2\2`]\3\2\2\2ad\3\2\2\2b`\3\2\2")
        buf.write("\2bc\3\2\2\2c\23\3\2\2\2db\3\2\2\2\n\30\32%\65EX`b")
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
    RULE_value = 8

    ruleNames =  [ "script", "body", "command", "if_command", "while_command", 
                   "break_command", "comment", "assign", "value" ]

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
            self.state = 18
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
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleMathParser.VARIABLE) | (1 << SimpleMathParser.COMMENT) | (1 << SimpleMathParser.IF) | (1 << SimpleMathParser.WHILE) | (1 << SimpleMathParser.BREAK))) != 0):
                self.state = 22
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SimpleMathParser.VARIABLE, SimpleMathParser.IF, SimpleMathParser.WHILE, SimpleMathParser.BREAK]:
                    self.state = 20
                    self.command()
                    pass
                elif token in [SimpleMathParser.COMMENT]:
                    self.state = 21
                    self.comment()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 26
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = SimpleMathParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimpleMathParser.VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.assign()
                self.state = 28
                self.match(SimpleMathParser.SEMI)
                pass
            elif token in [SimpleMathParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.if_command()
                pass
            elif token in [SimpleMathParser.WHILE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.while_command()
                pass
            elif token in [SimpleMathParser.BREAK]:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.break_command()
                self.state = 33
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


        def getRuleIndex(self):
            return SimpleMathParser.RULE_if_command

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfCommandSingleContext(If_commandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleMathParser.If_commandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(SimpleMathParser.IF, 0)
        def BRACE_L(self):
            return self.getToken(SimpleMathParser.BRACE_L, 0)
        def value(self):
            return self.getTypedRuleContext(SimpleMathParser.ValueContext,0)

        def BRACE_R(self):
            return self.getToken(SimpleMathParser.BRACE_R, 0)
        def command(self):
            return self.getTypedRuleContext(SimpleMathParser.CommandContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfCommandSingle" ):
                return visitor.visitIfCommandSingle(self)
            else:
                return visitor.visitChildren(self)


    class IfCommandBodyContext(If_commandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleMathParser.If_commandContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfCommandBody" ):
                return visitor.visitIfCommandBody(self)
            else:
                return visitor.visitChildren(self)



    def if_command(self):

        localctx = SimpleMathParser.If_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_if_command)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = SimpleMathParser.IfCommandBodyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(SimpleMathParser.IF)
                self.state = 38
                self.match(SimpleMathParser.BRACE_L)
                self.state = 39
                self.value(0)
                self.state = 40
                self.match(SimpleMathParser.BRACE_R)
                self.state = 41
                self.match(SimpleMathParser.CURLY_L)
                self.state = 42
                self.body()
                self.state = 43
                self.match(SimpleMathParser.CURLY_R)
                pass

            elif la_ == 2:
                localctx = SimpleMathParser.IfCommandSingleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(SimpleMathParser.IF)
                self.state = 46
                self.match(SimpleMathParser.BRACE_L)
                self.state = 47
                self.value(0)
                self.state = 48
                self.match(SimpleMathParser.BRACE_R)
                self.state = 49
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


        def getRuleIndex(self):
            return SimpleMathParser.RULE_while_command

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileCommandSingleContext(While_commandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleMathParser.While_commandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(SimpleMathParser.WHILE, 0)
        def BRACE_L(self):
            return self.getToken(SimpleMathParser.BRACE_L, 0)
        def value(self):
            return self.getTypedRuleContext(SimpleMathParser.ValueContext,0)

        def BRACE_R(self):
            return self.getToken(SimpleMathParser.BRACE_R, 0)
        def command(self):
            return self.getTypedRuleContext(SimpleMathParser.CommandContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileCommandSingle" ):
                return visitor.visitWhileCommandSingle(self)
            else:
                return visitor.visitChildren(self)


    class WhileCommandBodyContext(While_commandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleMathParser.While_commandContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileCommandBody" ):
                return visitor.visitWhileCommandBody(self)
            else:
                return visitor.visitChildren(self)



    def while_command(self):

        localctx = SimpleMathParser.While_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_while_command)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = SimpleMathParser.WhileCommandBodyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(SimpleMathParser.WHILE)
                self.state = 54
                self.match(SimpleMathParser.BRACE_L)
                self.state = 55
                self.value(0)
                self.state = 56
                self.match(SimpleMathParser.BRACE_R)
                self.state = 57
                self.match(SimpleMathParser.CURLY_L)
                self.state = 58
                self.body()
                self.state = 59
                self.match(SimpleMathParser.CURLY_R)
                pass

            elif la_ == 2:
                localctx = SimpleMathParser.WhileCommandSingleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(SimpleMathParser.WHILE)
                self.state = 62
                self.match(SimpleMathParser.BRACE_L)
                self.state = 63
                self.value(0)
                self.state = 64
                self.match(SimpleMathParser.BRACE_R)
                self.state = 65
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


        def getRuleIndex(self):
            return SimpleMathParser.RULE_break_command

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BreakCommandContext(Break_commandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleMathParser.Break_commandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BREAK(self):
            return self.getToken(SimpleMathParser.BREAK, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakCommand" ):
                return visitor.visitBreakCommand(self)
            else:
                return visitor.visitChildren(self)



    def break_command(self):

        localctx = SimpleMathParser.Break_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_break_command)
        try:
            localctx = SimpleMathParser.BreakCommandContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 69
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
            self.state = 71
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


        def getRuleIndex(self):
            return SimpleMathParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = SimpleMathParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(SimpleMathParser.VARIABLE)
            self.state = 74
            self.match(SimpleMathParser.EQUAL)
            self.state = 75
            self.value(0)
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
            self.left = None # ValueContext
            self.unaryMin = None # Token
            self.right = None # ValueContext
            self.mul = None # Token
            self.add = None # Token

        def SUBTRACT(self):
            return self.getToken(SimpleMathParser.SUBTRACT, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleMathParser.ValueContext)
            else:
                return self.getTypedRuleContext(SimpleMathParser.ValueContext,i)


        def BRACE_L(self):
            return self.getToken(SimpleMathParser.BRACE_L, 0)

        def BRACE_R(self):
            return self.getToken(SimpleMathParser.BRACE_R, 0)

        def VARIABLE(self):
            return self.getToken(SimpleMathParser.VARIABLE, 0)

        def NUMBER(self):
            return self.getToken(SimpleMathParser.NUMBER, 0)

        def MULTIPLY(self):
            return self.getToken(SimpleMathParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(SimpleMathParser.DIVIDE, 0)

        def ADD(self):
            return self.getToken(SimpleMathParser.ADD, 0)

        def getRuleIndex(self):
            return SimpleMathParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)



    def value(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleMathParser.ValueContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_value, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimpleMathParser.SUBTRACT]:
                self.state = 78
                localctx.unaryMin = self.match(SimpleMathParser.SUBTRACT)
                self.state = 79
                localctx.right = self.value(6)
                pass
            elif token in [SimpleMathParser.BRACE_L]:
                self.state = 80
                self.match(SimpleMathParser.BRACE_L)
                self.state = 81
                self.value(0)
                self.state = 82
                self.match(SimpleMathParser.BRACE_R)
                pass
            elif token in [SimpleMathParser.VARIABLE]:
                self.state = 84
                self.match(SimpleMathParser.VARIABLE)
                pass
            elif token in [SimpleMathParser.NUMBER]:
                self.state = 85
                self.match(SimpleMathParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 94
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = SimpleMathParser.ValueContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_value)
                        self.state = 88
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 89
                        localctx.mul = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SimpleMathParser.MULTIPLY or _la==SimpleMathParser.DIVIDE):
                            localctx.mul = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 90
                        localctx.right = self.value(5)
                        pass

                    elif la_ == 2:
                        localctx = SimpleMathParser.ValueContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_value)
                        self.state = 91
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 92
                        localctx.add = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SimpleMathParser.ADD or _la==SimpleMathParser.SUBTRACT):
                            localctx.add = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 93
                        localctx.right = self.value(4)
                        pass

             
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.value_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def value_sempred(self, localctx:ValueContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




