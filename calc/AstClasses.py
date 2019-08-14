
class Body(object):
    def __init__(self, lines):
        self.lines = lines

class IfCommand(object):
    def __init__(self, condition, body, elseBody=None):
        self.condition = condition
        self.body = body
        self.elseBody = elseBody

class Value(object):
    def __init__(self, value, type):
        self.value = value
        self.type = type

class Calculate(object):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Assign(object):
    def __init__(self, varibale, value):
        self.variable = varibale
        self.value = value