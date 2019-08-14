
parser grammar SimpleMathParser;

options { tokenVocab=SimpleMathLexer; }

script : body;
body : (command | comment)*;
command : assign SEMI
        | if_command
        | while_command
        | break_command SEMI;
if_command : IF BRACE_L value BRACE_R CURLY_L body CURLY_R (elseBody=else_command)?    # IfCommandBody
           | IF BRACE_L value BRACE_R command (elseBody=else_command)?                 # IfCommandSingle;
else_command : ELSE CURLY_L elseBody=body CURLY_R                                    # ElseCommandBody
             | ELSE elseLine=command                                                 # ElseCommandSingle;
while_command : WHILE BRACE_L value BRACE_R CURLY_L body CURLY_R                     # WhileCommandBody
              | WHILE BRACE_L value BRACE_R command                                  # WhileCommandSingle;
break_command : BREAK                                                                # BreakCommand;
comment : COMMENT;
assign : VARIABLE EQUAL value;

// The order of the following matters - operator priority:
value : unaryMin=SUBTRACT right=value
      | BRACE_L value BRACE_R
      | left=value mul=(MULTIPLY | DIVIDE) right=value
      | left=value add=(ADD | SUBTRACT) right=value
      | VARIABLE
      | NUMBER;
