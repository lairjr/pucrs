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



"a" | 
"b" |
"c" |
"v" |
"x" |
"(" | 
")" |
"+"     { return (int) yycharat(0); }

[ \t]+ { }
{NL}+  { } 

.    { System.err.println("Error: unexpected character '"+yytext()+"' na linha "+yyline); return YYEOF; }






