# Generated from SimpleMathParser.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleMathParser import SimpleMathParser
else:
    from SimpleMathParser import SimpleMathParser

# This class defines a complete generic visitor for a parse tree produced by SimpleMathParser.

class SimpleMathParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleMathParser#script.
    def visitScript(self, ctx:SimpleMathParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#body.
    def visitBody(self, ctx:SimpleMathParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#command.
    def visitCommand(self, ctx:SimpleMathParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#IfCommandBody.
    def visitIfCommandBody(self, ctx:SimpleMathParser.IfCommandBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#IfCommandSingle.
    def visitIfCommandSingle(self, ctx:SimpleMathParser.IfCommandSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#ElseCommandBody.
    def visitElseCommandBody(self, ctx:SimpleMathParser.ElseCommandBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#ElseCommandSingle.
    def visitElseCommandSingle(self, ctx:SimpleMathParser.ElseCommandSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#WhileCommandBody.
    def visitWhileCommandBody(self, ctx:SimpleMathParser.WhileCommandBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#WhileCommandSingle.
    def visitWhileCommandSingle(self, ctx:SimpleMathParser.WhileCommandSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#BreakCommand.
    def visitBreakCommand(self, ctx:SimpleMathParser.BreakCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#PrintCommand.
    def visitPrintCommand(self, ctx:SimpleMathParser.PrintCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#print_params.
    def visitPrint_params(self, ctx:SimpleMathParser.Print_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#comment.
    def visitComment(self, ctx:SimpleMathParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#assign.
    def visitAssign(self, ctx:SimpleMathParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#value.
    def visitValue(self, ctx:SimpleMathParser.ValueContext):
        return self.visitChildren(ctx)



del SimpleMathParser