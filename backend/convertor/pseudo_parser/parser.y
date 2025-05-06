%{
#include <stdio.h>
int yylex(void);
void yyerror(const char *s);
%}

%token INT RETURN ID NUM

%%
program:
      function
    ;

function:
      INT ID '(' ')' '{' body '}'
    ;

body:
      INT ID '=' NUM ';' RETURN NUM ';'
    ;

%%

void yyerror(const char *s) {
    printf("Pseudo: Error: %s\n", s);
}

int main() {
    printf("Pseudo: Start Function\n");
    yyparse();
    printf("Pseudo: End Function\n");
    return 0;
}
