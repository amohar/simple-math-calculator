from enum import Enum

class ValueType(Enum):
    VALUE = 1
    VARIABLE = 2

class OperatorType(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    UNARYMIN = 5