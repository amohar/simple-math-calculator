
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
VARIABLE: '$' ('0'..'9'|'a'..'z'|'A'..'Z'|'_'|'-')+;
COMMENT: '#' ('0'..'9'|'a'..'z'|'A'..'Z'|'_'|'-'|' ')*;
NUMBER: DIGIT+ (DOT DIGIT+)?;

IF: 'if';
ELSE: 'else';
WHILE: 'while';
BREAK: 'break';
WS: [ \n\t\r]+ -> skip;

fragment DIGIT: ('0'..'9');
fragment DOT: '.';
