
parser grammar SimpleMathParser;

options { tokenVocab=SimpleMathLexer; }

script : command*;
command : assign SEMI
        | comment;
comment : COMMENT;
assign : VARIABLE EQUAL value
       | VARIABLE EQUAL calculate;
calculate : value ADD value
          | value SUBTRACT value
          | value MULTIPLY value
          | value DIVIDE value;
value : VARIABLE
      | number;
number : NUMBER;
