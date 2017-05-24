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
"if" { return Parser.IF; }
"else" { return Parser.ELSE; }

"o" { return (int) yycharat(0); }
"e" { return (int) yycharat(0); }

[a-zA-Z][a-zA-Z_0-9]* { return Parser.ID; }


[ \t]+ { }
{NL}+  { }

.    { System.err.println("Error: unexpected character '"+yytext()+"' na linha "+yyline); return YYEOF; }
