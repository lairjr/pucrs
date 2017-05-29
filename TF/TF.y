%{
  import java.io.*;
%}

%token CLASS, IDENTIFIER, PUBLIC, STATIC, VOID, MAIN, STRING, IF, ELSE, WHILE
%token PRINT, AND, LENGTH, TRUE, FALSE, THIS, NEW, INT, INTEGER_LITERAL, EXTENDS
%token BOOL, RETURN

%right '='
%nonassoc '<'
%left AND
%left '-' '+'
%left '*'
%right '!'
%left '.'
%left '['

%%

Goal : MainClass ClassDeclarationR;

ClassDeclaration:   CLASS IDENTIFIER EXTENDS IDENTIFIER '{' VarDeclarationR MethodDeclarationR '}'
                  | CLASS IDENTIFIER '{' VarDeclarationR MethodDeclarationR '}'
                  ;

ClassDeclarationR:  ClassDeclaration ClassDeclarationR
                  |
                  ;

VarDeclaration: Type IDENTIFIER ';'

VarDeclarationR : VarDeclaration VarDeclarationR
                |
                ;

MethodDeclaration: PUBLIC Type IDENTIFIER '(' Param ')' '{' StatementR RETURN Expression ';' '}'

MethodDeclarationR: MethodDeclaration MethodDeclarationR
                  |
                  ;

Param : Type IDENTIFIER ParamR
      |
      ;

ParamR: ParamR ',' Type IDENTIFIER
      |
      ;

Type: INT  '[' ']'
    | INT
    | BOOL
    | IDENTIFIER
    ;

MainClass : CLASS IDENTIFIER '{' PUBLIC STATIC VOID MAIN '(' STRING '[' ']' IDENTIFIER ')' '{' Statement '}' '}'

Statement : '{' StatementR '}'
          | IF '(' Expression ')' Statement ELSE Statement
          | WHILE '(' Expression ')' Statement
          | PRINT '(' Expression ')' ';'
          | IDENTIFIER '=' Expression ';'
          | IDENTIFIER '[' Expression ']' '=' Expression ';'
          ;

StatementR : StatementR Statement
          |
          ;

Expression :  Expression AND Expression
            | Expression '<' Expression
            | Expression '-' Expression
            | Expression '*' Expression
            | Expression '[' Expression ']'
            | Expression '.' LENGTH
            | Expression '.' IDENTIFIER '(' ArgumentsR ')'
            | INTEGER_LITERAL
            | TRUE
            | FALSE
            | IDENTIFIER
            | THIS
            | NEW INT '[' Expression ']'
            | NEW IDENTIFIER '(' ')'
            | '!' Expression
            | '(' Expression ')'
            ;

ArgumentsR :  Expression
            | Expression ',' ArgumentsR
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
