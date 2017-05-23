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

Yylex.java: TF.flex
	$(JFLEX) TF.flex

Parser.java: TF.y
	$(BYACCJ) TF.y
