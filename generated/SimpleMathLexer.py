# Generated from SimpleMathLexer.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("\63\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3")
        buf.write("\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\2\2\16\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\3\2\4\3\2%%\7\2//\62;C\\aac|\2\62\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2\2\7\37")
        buf.write("\3\2\2\2\t!\3\2\2\2\13#\3\2\2\2\r%\3\2\2\2\17\'\3\2\2")
        buf.write("\2\21)\3\2\2\2\23+\3\2\2\2\25-\3\2\2\2\27/\3\2\2\2\31")
        buf.write("\61\3\2\2\2\33\34\n\2\2\2\34\4\3\2\2\2\35\36\t\3\2\2\36")
        buf.write("\6\3\2\2\2\37 \4\62;\2 \b\3\2\2\2!\"\7\60\2\2\"\n\3\2")
        buf.write("\2\2#$\7&\2\2$\f\3\2\2\2%&\7?\2\2&\16\3\2\2\2\'(\7-\2")
        buf.write("\2(\20\3\2\2\2)*\7/\2\2*\22\3\2\2\2+,\7,\2\2,\24\3\2\2")
        buf.write("\2-.\7\61\2\2.\26\3\2\2\2/\60\7%\2\2\60\30\3\2\2\2\61")
        buf.write("\62\7=\2\2\62\32\3\2\2\2\3\2\2")
        return buf.getvalue()


class SimpleMathLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENTCHARACTER = 1
    VARCHARACTER = 2
    DIGIT = 3
    DOT = 4
    DOLLAR = 5
    EQUAL = 6
    ADD = 7
    SUBTRACT = 8
    MULTIPLY = 9
    DIVIDE = 10
    HASH = 11
    SEMI = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "'$'", "'='", "'+'", "'-'", "'*'", "'/'", "'#'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENTCHARACTER", "VARCHARACTER", "DIGIT", "DOT", "DOLLAR", 
            "EQUAL", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "HASH", "SEMI" ]

    ruleNames = [ "COMMENTCHARACTER", "VARCHARACTER", "DIGIT", "DOT", "DOLLAR", 
                  "EQUAL", "ADD", "SUBTRACT", "MULTIPLY", "DIVIDE", "HASH", 
                  "SEMI" ]

    grammarFileName = "SimpleMathLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


