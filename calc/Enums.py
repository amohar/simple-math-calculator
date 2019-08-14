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
    UNARYNOT = 6
    COMPARE_EQ = 7
    COMPARE_NE = 8
    COMPARE_G = 9
    COMPARE_GE = 10
    COMPARE_L = 11
    COMPARE_LE = 12