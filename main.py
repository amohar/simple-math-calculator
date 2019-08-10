import sys
import antlr4
from generated.SimpleMathLexer import SimpleMathLexer
from generated.SimpleMathParser import SimpleMathParser
from generated.SimpleMathParserVisitor import SimpleMathParserVisitor

def main(argv):
    istream = antlr4.FileStream(argv[1])
    lexer = SimpleMathLexer(istream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = SimpleMathParser(stream)
    tree = parser.script()
    #print(tree.toStringTree(recog=parser))

    visitor = SimpleMathParserVisitor()
    visitor.visit(tree)
    #print()

if __name__ == '__main__':
    main(sys.argv)

