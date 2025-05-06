%{
#include "parser.tab.h"
%}

%%
[ \t\n]+           ;
"int"              { return INT; }
"return"           { return RETURN; }
[a-zA-Z_][a-zA-Z0-9_]*   { return ID; }
[0-9]+             { return NUM; }
.                  { return yytext[0]; }
%%
