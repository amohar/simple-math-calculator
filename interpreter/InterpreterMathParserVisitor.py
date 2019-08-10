# Generated from SimpleMathParser.g4 by ANTLR 4.7.1
from antlr4 import *
from generated.SimpleMathParserVisitor import SimpleMathParserVisitor

# This class defines a complete listener for a parse tree produced by SimpleMathParser.
class SimpleMathParserListener(SimpleMathParserVisitor):

    # Visit a parse tree produced by SimpleMathParser#script.
    def visitScript(self, ctx:SimpleMathParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#body.
    def visitBody(self, ctx:SimpleMathParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#command.
    def visitCommand(self, ctx:SimpleMathParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#if_command.
    def visitIf_command(self, ctx:SimpleMathParser.If_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#while_command.
    def visitWhile_command(self, ctx:SimpleMathParser.While_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#break_command.
    def visitBreak_command(self, ctx:SimpleMathParser.Break_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#comment.
    def visitComment(self, ctx:SimpleMathParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#assign.
    def visitAssign(self, ctx:SimpleMathParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#calculate.
    def visitCalculate(self, ctx:SimpleMathParser.CalculateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#value.
    def visitValue(self, ctx:SimpleMathParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#number.
    def visitNumber(self, ctx:SimpleMathParser.NumberContext):
        return self.visitChildren(ctx)


