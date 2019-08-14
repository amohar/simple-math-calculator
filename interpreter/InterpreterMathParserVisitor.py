from enum import Enum
from antlr4 import *
from generated.SimpleMathParserVisitor import SimpleMathParserVisitor
from generated.SimpleMathParser import SimpleMathParser
from calc.AstClasses import *

# This class defines a complete listener for a parse tree produced by SimpleMathParser.
class InterpreterMathParserVisitor(SimpleMathParserVisitor):

    def visitChildren(self, node):
        result = self.defaultResult()
        n = node.getChildCount()
        for i in range(n):
            if not self.shouldVisitNextChild(node, result):
                return result

            c = node.getChild(i)
            childResult = c.accept(self)
            result = self.aggregateResult(result, childResult)

        return result

    def defaultResult(self):
        return []

    def aggregateResult(self, aggregate, childResult):
        if childResult != None:
            if isinstance(childResult, list):
                aggregate.extend(childResult)
            else:
                aggregate.append(childResult)
        return aggregate

    # Visit a parse tree produced by SimpleMathParser#script.
    def visitScript(self, ctx:SimpleMathParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#body.
    def visitBody(self, ctx:SimpleMathParser.BodyContext):
        return Body(self.visitChildren(ctx))


    # Visit a parse tree produced by SimpleMathParser#command.
    def visitCommand(self, ctx:SimpleMathParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#IfCommandBody.
    def visitIfCommandBody(self, ctx:SimpleMathParser.IfCommandBodyContext):
        return IfCommand(self.visit(ctx.value()), self.visit(ctx.body()))


    # Visit a parse tree produced by SimpleMathParser#IfCommandSingle.
    def visitIfCommandSingle(self, ctx:SimpleMathParser.IfCommandSingleContext):
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


    # Visit a parse tree produced by SimpleMathParser#assign.
    def visitAssign(self, ctx:SimpleMathParser.AssignContext):
        if (ctx.value() != None):
            return Assign(ctx.VARIABLE().symbol.text, self.visit(ctx.value()))
        else:
            return Assign(ctx.VARIABLE().symbol.text, self.visit(ctx.calculate()))


    # Visit a parse tree produced by SimpleMathParser#value.
    def visitValue(self, ctx:SimpleMathParser.ValueContext):
        if ctx.VARIABLE() != None:
            return Value(ctx.VARIABLE().symbol.text, ValueType.VARIABLE)
        elif ctx.NUMBER() != None:
            return Value((int)(ctx.NUMBER().symbol.text), ValueType.VALUE)
        elif ctx.unaryMin != None:
            return Calculate(None, OperatorType.UNARYMIN, self.visit(ctx.right))
        elif ctx.mul != None or ctx.add != None:
            operators = {
                "+": OperatorType.ADD,
                "-": OperatorType.SUBTRACT,
                "*": OperatorType.MULTIPLY,
                "/": OperatorType.DIVIDE
            }
            if ctx.mul != None:
                op = operators[ctx.mul.text]
            else:
                op = operators[ctx.add.text]

            return Calculate(self.visit(ctx.left), op, self.visit(ctx.right))
        else:
            return self.visitChildren(ctx)


class ValueType(Enum):
    VALUE = 1
    VARIABLE = 2

class OperatorType(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    UNARYMIN = 5