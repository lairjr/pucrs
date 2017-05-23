JFLEX  = jflex
BYACCJ = yacc -tv -J
JAVAC  = javac

# targets:

all: Parser.class

run: Parser.class
	java Parser

build: clean Parser.class

clean:
	rm -f *~ *.class *.java *.output

Parser.class: Yylex.java Parser.java
	$(JAVAC) Parser.java

Yylex.java: lex.flex
	$(JFLEX) lex.flex

Parser.java: grammar.y
	$(BYACCJ) grammar.y
