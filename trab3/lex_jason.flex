
%%

%{
  private int comment_count = 0;

  private AsdrJason yyparser;

  public Yylex(java.io.Reader r, AsdrJason yyparser) {
    this(r);
    this.yyparser = yyparser;
  }


%} 

%integer
%line
%char

WHITE_SPACE_CHAR=[\n\r\ \t\b\012]

%% 

\"[^\"]*\"  { return AsdrJason.STRING; }  

[0-9]+(\.[0-9]+)? 	{ return AsdrJason.NUM; }


":" |
"," |
"{" |
"}" |
"[" |
"]"    { return yytext().charAt(0); } 


{WHITE_SPACE_CHAR}+ { }

. { System.out.println("Erro lexico: caracter invalido: <" + yytext() + ">"); }





