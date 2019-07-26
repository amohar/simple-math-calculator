# Generated from SimpleMathParser.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleMathParser import SimpleMathParser
else:
    from SimpleMathParser import SimpleMathParser

# This class defines a complete listener for a parse tree produced by SimpleMathParser.
class SimpleMathParserListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleMathParser#script.
    def enterScript(self, ctx:SimpleMathParser.ScriptContext):
        pass

    # Exit a parse tree produced by SimpleMathParser#script.
    def exitScript(self, ctx:SimpleMathParser.ScriptContext):
        pass


    # Enter a parse tree produced by SimpleMathParser#command.
    def enterCommand(self, ctx:SimpleMathParser.CommandContext):
        pass

    # Exit a parse tree produced by SimpleMathParser#command.
    def exitCommand(self, ctx:SimpleMathParser.CommandContext):
        pass


    # Enter a parse tree produced by SimpleMathParser#comment.
    def enterComment(self, ctx:SimpleMathParser.CommentContext):
        pass

    # Exit a parse tree produced by SimpleMathParser#comment.
    def exitComment(self, ctx:SimpleMathParser.CommentContext):
        pass


    # Enter a parse tree produced by SimpleMathParser#assign.
    def enterAssign(self, ctx:SimpleMathParser.AssignContext):
        pass

    # Exit a parse tree produced by SimpleMathParser#assign.
    def exitAssign(self, ctx:SimpleMathParser.AssignContext):
        pass


    # Enter a parse tree produced by SimpleMathParser#calculate.
    def enterCalculate(self, ctx:SimpleMathParser.CalculateContext):
        pass

    # Exit a parse tree produced by SimpleMathParser#calculate.
    def exitCalculate(self, ctx:SimpleMathParser.CalculateContext):
        pass


    # Enter a parse tree produced by SimpleMathParser#value.
    def enterValue(self, ctx:SimpleMathParser.ValueContext):
        pass

    # Exit a parse tree produced by SimpleMathParser#value.
    def exitValue(self, ctx:SimpleMathParser.ValueContext):
        pass


    # Enter a parse tree produced by SimpleMathParser#variable.
    def enterVariable(self, ctx:SimpleMathParser.VariableContext):
        pass

    # Exit a parse tree produced by SimpleMathParser#variable.
    def exitVariable(self, ctx:SimpleMathParser.VariableContext):
        pass


    # Enter a parse tree produced by SimpleMathParser#digit.
    def enterDigit(self, ctx:SimpleMathParser.DigitContext):
        pass

    # Exit a parse tree produced by SimpleMathParser#digit.
    def exitDigit(self, ctx:SimpleMathParser.DigitContext):
        pass


