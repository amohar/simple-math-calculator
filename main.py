import sys
import antlr4
from generated.SimpleMathLexer import SimpleMathLexer
from generated.SimpleMathParser import SimpleMathParser
from interpreter.InterpreterMathParserVisitor import InterpreterMathParserVisitor

def main(argv):
    istream = antlr4.FileStream(argv[1])
    lexer = SimpleMathLexer(istream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = SimpleMathParser(stream)
    tree = parser.script()
    #print(tree.toStringTree(recog=parser))

    visitor = InterpreterMathParserVisitor()
    test = visitor.visit(tree)
    print(test)

if __name__ == '__main__':
    main(sys.argv)

