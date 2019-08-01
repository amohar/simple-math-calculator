
lexer grammar SimpleMathLexer;

EQUAL: '=';
ADD: '+';
SUBTRACT: '-';
MULTIPLY: '*';
DIVIDE: '/';
SEMI: ';';

VARIABLE: '$' ('0'..'9'|'a'..'z'|'A'..'Z'|'_'|'-')+;
COMMENT: '#' ('0'..'9'|'a'..'z'|'A'..'Z'|'_'|'-'|' ')*;
NUMBER: DIGIT+ (DOT DIGIT+)?;

WS: [ \n\t\r]+ -> skip;

fragment DIGIT: ('0'..'9');
fragment DOT: '.';
