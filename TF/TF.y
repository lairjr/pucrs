%{
  import java.io.*;
%}
   

%token CLASS, PUBLIC, STATIC, VOID, MAIN, STRING, EXTENDS, RETURN, INT, BOOL, IF, ELSE, WHILE, LENGTH, PRINT, TRUE, FALSE, THIS, NEW, AND, IDENTIFIER
%token INTEGER_LITERAL 

%right '='
%nonassoc '<'
%left  AND
%left  '-' '+'
%left '*' 
%right '!'
%left '.'
%left '['


%%

Goal: MainClass CD;

CD:  CD ClassDeclaration
  | 
  ;

MainClass: CLASS Identifier '{' PUBLIC STATIC VOID MAIN '(' STRING '[' ']' Identifier ')' '{' Statement '}' '}'
         ;   
        

ClassDeclaration: 	CLASS Identifier AOPC '{' VD MD '}'
		;
 

AOPC: EXTENDS Identifier 
    |
    ;

VD: VD VarDeclaration
    |
    ;

MD: MD MethodDeclaration
    |
    ;


VarDeclaration: Type Identifier ';'
              ;


MethodDeclaration: 	PUBLIC Type Identifier '(' ParamListOpc ')' '{' LDV RETURN Expression ';' '}' 
				 ;

LDV: Type Identifier LDV
   | Statement ST
   |
   ;

ParamListOpc: Type Identifier ListaIdentifier
			|
			;
			
		
ListaIdentifier: ListaIdentifier ',' Type Identifier 
			   |
			   ;
	
Type: 	INT '[' ']'
	| 	BOOL
	| 	INT
	| 	Identifier
    ;
	

Statement: 	'{' ST '}'
	| 	IF '(' Expression ')' Statement ELSE Statement
	| 	WHILE '(' Expression ')' Statement
	| 	PRINT '(' Expression ')' ';'
	| 	Identifier '=' Expression ';'
	| 	Identifier '[' Expression ']' '=' Expression ';'
    ;

ST: ST Statement
  |
  ;

Expression: 	Expression AND Expression
                  | Expression '<' Expression
                  | Expression '+' Expression
                  | Expression '-' Expression
                  | Expression '*' Expression
		  | 	Expression '[' Expression ']'
		  | 	Expression '.' LENGTH
		  | 	Expression "." Identifier '(' LE ')'
		  | 	INTEGER_LITERAL
		  | 	TRUE
		  | 	FALSE
		  | 	Identifier
		  | 	THIS
		  | 	NEW INT '[' Expression ']'
		  | 	NEW Identifier '(' ')'
		  | 	'!' Expression
		  | 	'(' Expression ')'
		  ;



Identifier: IDENTIFIER
          ;

LE: LE ',' Expression
  | Expression
  | 
  ;
	
%%

  private Yylex lexer;


  private int yylex () {
    int yyl_return = -1;
    try {
      yylval = new ParserVal(0);
      yyl_return = lexer.yylex();
    }
    catch (IOException e) {
      System.err.println("IO error :"+e.getMessage());
    }
    return yyl_return;
  }


  public void yyerror (String error) {
    System.err.println ("Error: " + error);
  }


  public Parser(Reader r) {
    lexer = new Yylex(r, this);
  }


  static boolean interactive;

  public static void main(String args[]) throws IOException {
    System.out.println("");

    Parser yyparser;
    if ( args.length > 0 ) {
      // parse a file
      yyparser = new Parser(new FileReader(args[0]));
    }
    else {
      // interactive mode
      System.out.println("[Quit with CTRL-D]");
      System.out.print("> ");
      interactive = true;
	    yyparser = new Parser(new InputStreamReader(System.in));
    }

    yyparser.yyparse();
    
    if (interactive) {
      System.out.println();
      System.out.println("done!");
    }
  }

