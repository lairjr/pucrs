/* Autor: Lair Junior */

%%

%{
  private int comment_count = 0;

  private Asdr yyparser;

  public Yylex(java.io.Reader r, Asdr yyparser) {
    this(r);
    this.yyparser = yyparser;
  }
%}

%integer
%line
%char

WHITE_SPACE_CHAR=[\n\r\ \t\b\012]
InputCharacter = [^\r\n]
LineTerminator = \r|\n|\r\n

%%

"$TRACE_ON"   { yyparser.setDebug(true); }
"$TRACE_OFF"  { yyparser.setDebug(false); }

"data" 		{ return Asdr.DATA; }
"prova"	{ return Asdr.PROVA; }

[:jletter:][:jletterdigit:]* { return Asdr.IDENT; }

[0-9]+("." [0-9]+)? 	{ return Asdr.NUM; }
[0-9][0-9][0-9]-[0-9] 	{ return Asdr.MATR; }


"," |
"." |
"(" |
")" { return yytext().charAt(0); }

"#"{InputCharacter}*{LineTerminator} { }

{WHITE_SPACE_CHAR}+ { }

. { System.out.println("Erro lexico: caracter invalido: <" + yytext() + ">"); }
