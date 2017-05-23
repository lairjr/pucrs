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

Yylex.java: lexico.flex
	$(JFLEX) lexico.flex

Parser.java: exemplo1.y
	$(BYACCJ) exemplo1.y
