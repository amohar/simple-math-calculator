
parser grammar SimpleMathParser;

options { tokenVocab=SimpleMathLexer; }

script: body;
body : (command | comment)*;
command : assign SEMI
        | if_command
        | while_command
        | break_command SEMI;
if_command : IF BRACE_L value BRACE_R CURLY_L body CURLY_R
           | IF BRACE_L value BRACE_R command;
while_command : WHILE BRACE_L value BRACE_R CURLY_L body CURLY_R
              | WHILE BRACE_L value BRACE_R command;
break_command : BREAK;
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
