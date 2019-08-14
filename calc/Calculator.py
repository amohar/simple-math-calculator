from calc.Enums import *
from calc.AstClasses import *

class Calculator(object):

    def __init__(self):
        self._variables = {}

    def calculate(self, astTree):
        switcher = {
            list: self._handleList,
            Body: self._handleBody,
            Assign: self._handleAssign,
            Calculate: self._handleCalculate,
            Value: self._handleValue,
            PrintCommand: self._handlePrintCommand
        }

        command = switcher.get(type(astTree), None)
        if command == None:
            print("Unknown AST item type: {0}".format(astTree.__class__.__name__))
        else:
            return command(astTree)

    def _handleList(self, tree):
        for item in tree:
            self.calculate(item)

    def _handleBody(self, tree:Body):
        self.calculate(tree.lines)

    def _handleAssign(self, tree:Assign):
        self._variables[tree.variable] = self.calculate(tree.value)

    def _handleCalculate(self, tree:Calculate):
        switcher = {
            OperatorType.ADD: lambda: self.calculate(tree.left) + self.calculate(tree.right),
            OperatorType.SUBTRACT: lambda: self.calculate(tree.left) - self.calculate(tree.right),
            OperatorType.MULTIPLY: lambda: self.calculate(tree.left) * self.calculate(tree.right),
            OperatorType.DIVIDE: lambda: self.calculate(tree.left) / self.calculate(tree.right),
            OperatorType.COMPARE_EQ: lambda: 1 if self.calculate(tree.left) == self.calculate(tree.right) else 0,
            OperatorType.COMPARE_NE: lambda: 1 if self.calculate(tree.left) != self.calculate(tree.right) else 0,
            OperatorType.COMPARE_G: lambda: 1 if self.calculate(tree.left) > self.calculate(tree.right) else 0,
            OperatorType.COMPARE_GE: lambda: 1 if self.calculate(tree.left) >= self.calculate(tree.right) else 0,
            OperatorType.COMPARE_L: lambda: 1 if self.calculate(tree.left) < self.calculate(tree.right) else 0,
            OperatorType.COMPARE_LE: lambda: 1 if self.calculate(tree.left) <= self.calculate(tree.right) else 0,
            OperatorType.UNARYMIN: lambda: -self.calculate(tree.right),
            OperatorType.UNARYNOT: lambda: 0 if self.calculate(tree.right) else 1,
        }
        test = switcher.get(tree.op, None)()
        return test

    def _handleValue(self, tree:Value):
        if tree.type == ValueType.VALUE:
            return tree.value
        else:
            return self._variables[tree.value]

    def _handlePrintCommand(self, tree:PrintCommand):
        params = [self._handlePrintParam(param) for param in tree.params]
        print("".join(params))
    
    def _handlePrintParam(self, param):
        if (type(param) == str):
            return param
        else:
            return str(self.calculate(param))