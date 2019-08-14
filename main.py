import sys
import antlr4
from generated.SimpleMathLexer import SimpleMathLexer
from generated.SimpleMathParser import SimpleMathParser
from interpreter.InterpreterMathParserVisitor import InterpreterMathParserVisitor
from calc.Calculator import Calculator

def main(argv):
    istream = antlr4.FileStream(argv[1])
    lexer = SimpleMathLexer(istream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = SimpleMathParser(stream)
    tree = parser.script()
    #print(tree.toStringTree(recog=parser))

    visitor = InterpreterMathParserVisitor()
    astTree = visitor.visit(tree)
    calculator = Calculator()
    calculator.calculate(astTree)

    print(astTree)

if __name__ == '__main__':
    main(sys.argv)

