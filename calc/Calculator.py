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
            Value: self._handleValue
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
            OperatorType.UNARYMIN: lambda: -self.calculate(tree.right),
        }
        test = switcher.get(tree.op, None)()
        return test

    def _handleValue(self, tree:Value):
        if tree.type == ValueType.VALUE:
            return tree.value
        else:
            return self._variables[tree.value]