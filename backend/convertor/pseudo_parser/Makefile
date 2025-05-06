all:
	bison -d parser.y
	flex parser.l
	gcc -o c_to_pseudo parser.tab.c lex.yy.c -lfl
