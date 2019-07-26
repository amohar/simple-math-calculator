
parser grammar SimpleMathParser;

options { tokenVocab=SimpleMathLexer; }

script : (command SEMI)*;
command : assign
        | comment;
comment : HASH COMMENTCHARACTER+;
assign : variable EQUAL value
       | variable EQUAL calculate;
calculate : value ADD value
          | value SUBTRACT value
          | value MULTIPLY value
          | value DIVIDE value;
value : variable
      | digit;
variable : DOLLAR VARCHARACTER+;
digit : DIGIT+ (DOT DIGIT*)?;