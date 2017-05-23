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
"extends" { return Parser.EXTENDS; }
"return" { return Parser.RETURN; } 
"int" { return Parser.INT; }
"boolean" { return Parser.BOOL; }
"if" { return Parser.IF; }
"else" { return Parser.ELSE; }
"while" { return Parser.WHILE; }
"length" { return Parser.LENGTH; }
"System.out.println" { return Parser.PRINT; }
"true" { return Parser.TRUE; }
"false" { return Parser.FALSE; }
"this" { return Parser.THIS; }
"new" { return Parser.NEW; }
"&&" { return Parser.AND; }



[a-zA-Z][a-zA-Z_0-9]* { return Parser.IDENTIFIER; }

[0-9]+ { return Parser.INTEGER_LITERAL; }


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






