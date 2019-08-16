from antlr4 import *
from generated.SimpleMathParserVisitor import SimpleMathParserVisitor
from generated.SimpleMathParser import SimpleMathParser
from calc.AstClasses import *
from calc.Enums import *

# This class defines a complete listener for a parse tree produced by SimpleMathParser.
class InterpreterMathParserVisitor(SimpleMathParserVisitor):

    def __init__(self):
        self._loopDepth = 0
        self._functionDepth = 0

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
        if ctx.elseBody != None:
            return IfCommand(self.visit(ctx.value()), self.visit(ctx.body()), self.visit(ctx.elseBody))
        else:
            return IfCommand(self.visit(ctx.value()), self.visit(ctx.body()))


    # Visit a parse tree produced by SimpleMathParser#IfCommandSingle.
    def visitIfCommandSingle(self, ctx:SimpleMathParser.IfCommandSingleContext):
        if ctx.elseBody != None:
            return IfCommand(self.visit(ctx.value()), self.visit(ctx.command()), self.visit(ctx.elseBody))
        else:
            return IfCommand(self.visit(ctx.value()), self.visit(ctx.command()))


    # Visit a parse tree produced by SimpleMathParser#ElseCommandBody.
    def visitElseCommandBody(self, ctx:SimpleMathParser.ElseCommandBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#ElseCommandSingle.
    def visitElseCommandSingle(self, ctx:SimpleMathParser.ElseCommandSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleMathParser#WhileCommandBody.
    def visitWhileCommandBody(self, ctx:SimpleMathParser.WhileCommandBodyContext):
        self._loopDepth += 1
        command = WhileCommand(self.visit(ctx.value()), self.visit(ctx.body()))
        self._loopDepth -= 1

        return command


    # Visit a parse tree produced by SimpleMathParser#WhileCommandSingle.
    def visitWhileCommandSingle(self, ctx:SimpleMathParser.WhileCommandSingleContext):
        self._loopDepth += 1
        command = WhileCommand(self.visit(ctx.value()), self.visit(ctx.command()))
        self._loopDepth -= 1

        return command

    # Visit a parse tree produced by SimpleMathParser#BreakCommand.
    def visitBreakCommand(self, ctx:SimpleMathParser.BreakCommandContext):
        if self._loopDepth == 0:
            raise Exception("'break' command found outside loop.")
        return BreakCommand()


    # Visit a parse tree produced by SimpleMathParser#PrintCommand.
    def visitPrintCommand(self, ctx:SimpleMathParser.PrintCommandContext):
        return PrintCommand(self.visit(ctx.value()))


    # Visit a parse tree produced by SimpleMathParser#FunctionCommand.
    def visitFunctionCommand(self, ctx:SimpleMathParser.FunctionCommandContext):
        parameters = [param.symbol.text for param in ctx.VARIABLE()]
        return FunctionCommand(ctx.funcName.text, parameters, self.visit(ctx.body()))


    # Visit a parse tree produced by SimpleMathParser#FunctionCall.
    def visitFunctionCall(self, ctx:SimpleMathParser.FunctionCallContext):
        parameters = [self.visit(param) for param in ctx.value()]
        self._functionDepth += 1
        command = FunctionCall(ctx.funcName.text, parameters)
        self._functionDepth -= 1

        return command


        # Visit a parse tree produced by SimpleMathParser#ReturnCommand.
    def visitReturnCommand(self, ctx:SimpleMathParser.ReturnCommandContext):
        if self._functionDepth == 0:
            raise Exception("'return' command found outside a function.")
        return ReturnCommand(self.visit(ctx.value()))


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
            return Value((int)(ctx.NUMBER().symbol.text), ValueType.NUMCONST)
        elif ctx.STR() != None:
            return Value(ctx.STR().symbol.text[1:-1], ValueType.STRCONST)
        elif ctx.unaryMin != None:
            return Calculate(None, OperatorType.UNARYMIN, self.visit(ctx.right))
        elif ctx.unaryNot != None:
            return Calculate(None, OperatorType.UNARYNOT, self.visit(ctx.right))
        elif ctx.funcCall != None:
            return Calculate(None, OperatorType.FUNCCALL, self.visit(ctx.funcCall))
        elif ctx.bracedValue != None:
            return self.visit(ctx.bracedValue)
        elif ctx.mul != None or ctx.add != None or ctx.cmp != None:
            operators = {
                "+": OperatorType.ADD,
                "-": OperatorType.SUBTRACT,
                "*": OperatorType.MULTIPLY,
                "/": OperatorType.DIVIDE,
                "==": OperatorType.COMPARE_EQ,
                "!=": OperatorType.COMPARE_NE,
                ">": OperatorType.COMPARE_G,
                ">=": OperatorType.COMPARE_GE,
                "<": OperatorType.COMPARE_L,
                "<=": OperatorType.COMPARE_LE,
            }
            if ctx.mul != None:
                op = operators[ctx.mul.text]
            elif ctx.cmp != None:
                op = operators[ctx.cmp.text]
            else:
                op = operators[ctx.add.text]

            return Calculate(self.visit(ctx.left), op, self.visit(ctx.right))
        else:
            return self.visitChildren(ctx)


