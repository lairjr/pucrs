import java.io.*;

public class AsdrJason {

  private static final int BASE_TOKEN_NUM = 301;
  



  public static final int STRING 	 = 301;
  public static final int NUM  = 302;
  
  public static final String tokenList[] = {"STRING", "NUM" };

/*****  Gramática

	JSON --> ARRAY
        | OBJECT 
		
	OBJECT: "{" MEMBERS "}"
	   
	MEMBERS: STRING ":" VALUE  RestoMembers    // fatorada a esquerda

  RestoMembers = "," MEMBERS
               |                             //  produção vazia 
	   
	ARRAY: "[" ELEMENTS "]" 

	ELEMENTS: VALUE  RestoElements             // eliminada a recursao a esquerda

  RestoElements : ',' VALUE RestoElements               
	              |                            //  produção vazia
    
	VALUE: STRING 
	     | NUMBER 
	     | OBJECT 
	     | ARRAY

   

****/
                                      
  /* referencia ao objeto Scanner gerado pelo JFLEX */
  private Yylex lexer;

  public ParserVal yylval;

  private static int la;
  private boolean debug = true;
  
  /* construtor da classe */
  public AsdrJason (Reader r) {
      lexer = new Yylex (r, this);
  }
  
  public void setDebug(boolean dbg) {
      debug = dbg;
  }

  public void Jason() {
       if ( la == '[') 
           Array();
       else if ( la == '{' )
               Object(); 
		   else  yyerror("esperado '[' ou '{'");
  }

  private void Object() {
	    check('{');
      Members();
      check('}');
  }

  private void Members() {
      check(STRING);
      check(':');
      Value();
      RestoMembers();
  }

   private void  RestoMembers() {
       if ( la == ',' ) {
           check(',');
           Members();
       } else  ;            //  produção vazia 
    }
	 
  private void Array() {
	      check('[');
        Elements();
        check(']');
  }  

	private void Elements() {
      if ( la == STRING ||la == NUM ||la == '[' ||la == '{' ) {
          Value();
          RestoElements();
      } else yyerror("esperado STRING, NUM, '[' ou '{'");
  }
  
  private void RestoElements() {
     if ( la == ',' ) {
         check(',');
         Value();
         RestoElements();
      } else ;               //  produção vazia
   }
    
   private void Value() {
       if ( la == STRING ) check(STRING); 
       else if ( la == NUM ) check(NUM);
       else if ( la == '{' ) Object();
       else if ( la == '[' ) Array();
       else yyerror("esperado STRING, NUM, '[' ou '{'");
	  }

  private void check(int expected) {
      if (la == expected)
         la = this.yylex();
      else {
         // erro: esperado token "expected" veio token "la" 
         // System.out.printf("Erro: esperado %d, veio %d\n", expected, la)
         String expStr, laStr;       

		expStr = ((expected < BASE_TOKEN_NUM )
               ? ""+(char)expected
			         : tokenList[expected-BASE_TOKEN_NUM]);
         
		laStr = ((la < BASE_TOKEN_NUM )
                ? new Character((char)la).toString()
                : tokenList[la-BASE_TOKEN_NUM]);

          yyerror( "esperado token : " + expStr +
                   " na entrada: " + laStr);
     }
   }

   /* metodo de acesso ao Scanner gerado pelo JFLEX */
   private int yylex() {
       int retVal = -1;
       try {
           yylval = new ParserVal(0); //zera o valor do token
           retVal = lexer.yylex(); //le a entrada do arquivo e retorna um token
       } catch (IOException e) {
           System.err.println("IO Error:" + e);
          }
       return retVal; //retorna o token para o Parser 
   }

  /* metodo de manipulacao de erros de sintaxe */
  private void yyerror (String error) {
     System.err.println("Erro: " + error);
     System.err.println("Entrada rejeitada");
     System.out.println("\n\nFalhou!!!");
     System.exit(1);
     
  }

  /**
   * Runs the scanner on input files.
   *
   * This main method is the debugging routine for the scanner.
   * It prints debugging information about each returned token to
   * System.out until the end of file is reached, or an error occured.
   *
   * @param args   the command line, contains the filenames to run
   *               the scanner on.
   */
  public static void main(String[] args) {
     AsdrJason parser = null;
     try {
         if (args.length == 0)
            parser = new AsdrJason(new InputStreamReader(System.in));
         else 
            parser = new  AsdrJason( new java.io.FileReader(args[0]));


          la = parser.yylex();          

          parser.Jason();
     
          if (la== Yylex.YYEOF)
             System.out.println("\n\nSucesso!");
          else     
             System.out.println("\n\nFalhou - esperado EOF.");               

        }
        catch (java.io.FileNotFoundException e) {
          System.out.println("File not found : \""+args[0]+"\"");
        }
        catch (Exception e) {
          System.out.println("Unexpected exception:");
          e.printStackTrace();
      }
    
  }
  
}

