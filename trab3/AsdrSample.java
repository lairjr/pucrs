import java.io.*;

/*****  Nova gramática

    Prog --> Decl  ListaFuncoes

    Decl --> Tipo LId ';'  Decl
 |     //produção vazia

    Tipo --> int | double |boolean

   LId -->  LId ',' IDENT
 | IDENT

   ListaFuncoes --> umaFuncao ListaFuncoes
 |  umaFuncao

   umaFuncao --> FUNC tipoOuVoid IDENT () Bloco
 | FUNC tipoOuVoid IDENT ( ListaParametros ) Bloco

   tipoOuVoid --> VOID | Tipo

   ListaParametros --> Tipo IDENT
 | Tipo IDENT , ListaParametros

   Bloco -->  '{' LCmd '}'

   LCmd -->  Cmd LCmdo
 |     //produção vazia

   Cmd --> Bloco
 | if E Cmd
 | if E Cmd else Cmd
 | while E Cmd
 | IDENT '=' E ';'

   E --> E + T
 | T

   T --> T * F
 | F

   F --> NUM
 | IDENT
 | '(' E ')'

 ****/

public class AsdrSample {

    private static final int BASE_TOKEN_NUM = 301;
    public static final int IDENT  = 301;
    public static final int NUM    = 302;
    public static final int WHILE  = 303;
    public static final int IF   = 304;
    public static final int INT    = 305;
    public static final int BOOL   = 306;
    public static final int DOUBLE = 307;
    public static final int ELSE = 308;
    public static final int VOID = 309;
    public static final int FUNC = 310;
    public static final int BOOLEAN = 311;

    public static final String tokenList[] = {
        "IDENT",
        "NUM",
        "WHILE",
        "IF",
        "INT",
        "BOOL",
        "DOUBLE",
        "ELSE",
        "VOID",
        "FUNC",
        "BOOLEAN"
    };

/* referencia ao objeto Scanner gerado pelo JFLEX */
    public ParserVal yylval;
    private Yylex lexer;
    private static int laToken;
    private boolean debug;

/* construtor da classe */
    public AsdrSample (Reader r) {
        lexer = new Yylex (r, this);
    }

    private void Prog() {
        if (laToken == INT || laToken == DOUBLE || laToken == BOOLEAN || laToken == '{') {
            if (debug) System.out.println("Prog --> Decl  ListaFuncoes");
            Decl();
            ListaFuncoes();
        } else {
            yyerror("Esperado: int, double, boolean ou {");
        }
    }

    private void ListaFuncoes() {
        if (laToken == FUNC) {
            if (debug) System.out.println("ListaFuncoes --> umaFuncao ListaFuncoes");
            umaFuncao()
            ListaFuncoes();
        } else {
            if (debug) System.out.println("ListaFuncoes --> // prod. vazia");
        }
    }

    private void umaFuncao () {
        verifica(FUNC);
        tipoOuVoid();
        verifica(IDENT);
        verifica('(');
        if (laToken != ')') {
            ListaParametros();
        }
        verifica(')');
        Bloco();
    }

    private void tipoOuVoid() {
        if (laToken == VOID) {
            if (debug) System.out.println("tipoOuVoid --> void");
            verifica(VOID);
        } else if (laToken == INT || laToken == DOUBLE || laToken == BOOLEAN) {
            if (debug) System.out.println("tipoOuVoid --> Tipo");
            Tipo();
        } else {
            yyerror("Esperado: void, int, double, boolean");
        }
    }

    private void ListaParametros() {
        if (debug) System.out.println("ListaParametros --> Tipo IDENT RestoListaParametros");
        Tipo();
        verifica(IDENT);
        RestoListaParametros();
    }

    private void RestoListaParametros() {
        if (laToken == ',') {
            if (debug) System.out.println("RestoListaParametros --> , Tipo IDENT RestoListaParametros");
            verifica(',');
            Tipo();
            verifica(IDENT);
            RestoListaParametros();
        } else {
            if (debug) System.out.println("RestoListaParametros --> // prod. vazia");
        }
    }

    private void Decl() {
        if (laToken == INT || laToken == DOUBLE || laToken == BOOLEAN) {
            if (debug) System.out.println("Tipo LId ';'  Decl");
            Tipo();
            LId();
            verifica(';');
            Decl();
        } else {
            if (debug) System.out.println("Decl --> // prod. vazia");
        }
    }

    private void LId(){
        if (debug) System.out.println("LId -->  IDENT  RestoLID");
        verifica(IDENT);
        RestoLID();
    }

    private void RestoLID() {
        if (laToken == ',' ) {
            if (debug) System.out.println("RestoLId --> , IDENT RestoLID");
            verifica(',');
            verifica(IDENT);
            RestoLID();
        } else {
            if (debug) System.out.println("RestoLId --> vazio");
        }
    }

    private void Tipo() {
        if (laToken == INT) {
            if (debug) System.out.println("Tipo --> int");
            verifica(INT);
        } else if (laToken == DOUBLE) {
            if (debug) System.out.println("Tipo --> double");
            verifica(DOUBLE);
        } else if (laToken == BOOLEAN) {
            if (debug) System.out.println("Tipo --> boolean");
            verifica(BOOLEAN);
        } else {
            yyerror("Esperado: int, double, boolean");
        }
    }

    private void Bloco() {
        if (debug) System.out.println("Bloco --> { Cmd }");

        verifica('{');
        LCmd();
        verifica('}');
    }

    private void LCmd() {
        if (laToken == '{' || laToken == WHILE || laToken == IDENT || laToken == IF) {
            if (debug) System.out.println("LCmd --> Cmd LCmd");
            Cmd();
            LCmd();
        } else {
            if (debug) System.out.println("LCmd --> // prod. vazia");
        }
    }

    private void Cmd() {
        if (laToken == '{') {
            if (debug) System.out.println("Cmd --> Bloco");
            Bloco();
        }
        else if (laToken == WHILE) {
            if (debug) System.out.println("Cmd --> WHILE ( E ) Cmd");
            verifica(WHILE);             // laToken = this.yylex();
            verifica('(');
            E();
            verifica(')');
            Cmd();
        }
        else if (laToken == IDENT) {
            if (debug) System.out.println("Cmd --> ident = E ;");
            verifica(IDENT);
            verifica('=');
            E();
            verifica(';');
        }
        else if (laToken == IF) {
            if (debug) System.out.println("Cmd --> if E Cmd RestoIF");
            verifica(IF);
            verifica('(');
            E();
            verifica(')');
            Cmd();
            RestoIF();
        }
        else yyerror("Esperado {, if, while ou identificador");
    }

    private void RestoIF() {
        if (laToken == ELSE) {
            if (debug) System.out.println("RestoIF --> else Cmd ");
            verifica(ELSE);
            Cmd();
        } else {
            if (debug) System.out.println("RestoIF -->     // producao vazia");
        }
    }

    private void E() {
        if (laToken == IDENT || laToken == NUM || laToken == '(') {
            if (debug) System.out.println("E --> F RestoE");
            F();
            RestoE();
        }
    }

    private void RestoE() {
        if (laToken == '+') {
            if (debug) System.out.println("RestoE --> + F RestoE");
            verifica('+');
            F();
            RestoE();
        } else if (laToken == '*') {
            T();
        } else {
            if (debug) System.out.println("RestoE --> // prod. vazia");
        }
    }

    private void T() {
        if (laToken == '*') {
            if (debug) System.out.println("T --> * F T");
            vefirica('*');
            F();
            T();
        } else {
            if (debug) System.out.println("T --> // prod. vazia");
        }
    }

    private void F() {
        if (laToken == IDENT) {
            if (debug) System.out.println("F --> IDENT");
            verifica(IDENT);
        }
        else if (laToken == NUM) {
            if (debug) System.out.println("F --> NUM");
            verifica(NUM);
        }
        else if (laToken == '(') {
            if (debug) System.out.println("F --> ( F )");
            verifica('(');
            F();
            verifica(')');
        }
        else yyerror("Esperado operando (, identificador ou numero");
    }

    private void verifica(int expected) {
        if (laToken == expected)
            laToken = this.yylex();
        else {
            String expStr, laStr;

            expStr = ((expected < BASE_TOKEN_NUM )
                      ? ""+(char)expected
                      : tokenList[expected-BASE_TOKEN_NUM]);

            laStr = ((laToken < BASE_TOKEN_NUM )
                     ? new Character((char)laToken).toString()
                     : tokenList[laToken-BASE_TOKEN_NUM]);

            yyerror( "esperado token : " + expStr +
                     " na entrada: " + laStr);
        }
    }

/* metodo de acesso ao Scanner gerado pelo JFLEX */
    private int yylex() {
        int retVal = -1;
        try {
            yylval = new ParserVal(0);             //zera o valor do token
            retVal = lexer.yylex();             //le a entrada do arquivo e retorna um token
        } catch (IOException e) {
            System.err.println("IO Error:" + e);
        }
        return retVal;         //retorna o token para o Parser
    }

/* metodo de manipulacao de erros de sintaxe */
    public void yyerror (String error) {
        System.err.println("Erro: " + error);
        System.err.println("Entrada rejeitada");
        System.out.println("\n\nFalhou!!!");
        System.exit(1);

    }

    public void setDebug(boolean trace) {
        debug = true;
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
        AsdrSample parser = null;
        try {
            if (args.length == 0)
                parser = new AsdrSample(new InputStreamReader(System.in));
            else
                parser = new  AsdrSample( new java.io.FileReader(args[0]));

            parser.setDebug(false);
            laToken = parser.yylex();

            parser.Prog();

            if (laToken== Yylex.YYEOF)
                System.out.println("\n\nSucesso!");
            else
                System.out.println("\n\nFalhou - esperado EOF.");

        }
        catch (java.io.FileNotFoundException e) {
            System.out.println("File not found : \""+args[0]+"\"");
        }
//        catch (java.io.IOException e) {
//          System.out.println("IO error scanning file \""+args[0]+"\"");
//          System.out.println(e);
//        }
//        catch (Exception e) {
//          System.out.println("Unexpected exception:");
//          e.printStackTrace();
//      }

    }

}
