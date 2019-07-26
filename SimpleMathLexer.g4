
lexer grammar SimpleMathLexer;

COMMENTCHARACTER: (~'#');
VARCHARACTER: ('0'..'9'|'a'..'z'|'A'..'Z'|'_'|'-');
DIGIT: ('0'..'9');
DOT: '.';
DOLLAR: '$';
EQUAL: '=';
ADD: '+';
SUBTRACT: '-';
MULTIPLY: '*';
DIVIDE: '/';
HASH: '#';
SEMI: ';';