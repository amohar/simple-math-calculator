
lexer grammar SimpleMathLexer;

EQUAL: '=';
ADD: '+';
SUBTRACT: '-';
MULTIPLY: '*';
DIVIDE: '/';
SEMI: ';';
BRACE_L: '(';
BRACE_R: ')';
CURLY_L: '{';
CURLY_R: '}';
EXCL: '!';
COMMA: ',';
VARIABLE: '$' NAME_CHAR+;
COMMENT: '#' .*?;
NUMBER: DIGIT+ (DOT DIGIT+)?;
STR: '"' .*? '"';

COMPARE_EQ: '==';
COMPARE_NE: '!=';
COMPARE_G: '>';
COMPARE_GE: '>=';
COMPARE_L: '<';
COMPARE_LE: '<=';

IF: 'if';
ELSE: 'else';
WHILE: 'while';
BREAK: 'break';
PRINT: 'print';
DEF: 'def';
RETURN: 'return';
NAME: NAME_CHAR+;

WS: [ \n\t\r]+ -> skip;

fragment DIGIT: ('0'..'9');
fragment DOT: '.';
fragment NAME_CHAR: ('0'..'9'|'a'..'z'|'A'..'Z'|'_'|'-');
