%%

%byaccj

%{
  private Parser yyparser;

  public Yylex(java.io.Reader r, Parser yyparser) {
    this(r);
    this.yyparser = yyparser;
  }
%}

NL  = \n | \r | \r\n

%%

"class" { return Parser.CLASS; }
"public" { return Parser.PUBLIC; }
"static" { return Parser.STATIC; }
"void" { return Parser.VOID; }
"main" { return Parser.MAIN; }
"String" { return Parser.STRING; }

[a-zA-Z][a-zA-Z_0-9]* { return Parser.IDENTIFIER; }

"!" |
"=" |
"<" |
"-" |
"*" |
"." |
";" |
"{" |
"}" |
"(" |
")" |
"[" |
"]" |
"+"     { return (int) yycharat(0); }

[ \t]+ { }
{NL}+  { }

.    { System.err.println("Error: unexpected character '"+yytext()+"' na linha "+yyline); return YYEOF; }
