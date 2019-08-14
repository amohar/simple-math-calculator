
class Body(object):
    def __init__(self, lines):
        self._lines = lines

class IfCommand(object):
    def __init__(self, condition, body):
        self._condition = condition
        self._body = body

class Value(object):
    def __init__(self, value, type):
        self._value = value
        self._type = type

class Calculate(object):
    def __init__(self, left, op, right):
        self._left = left
        self._op = op
        self._right = right

class Assign(object):
    def __init__(self, varibale, value):
        self._variable = varibale
        self._value = value