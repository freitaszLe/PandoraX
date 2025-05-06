grammar PandoraX;

// Ponto de entrada
program
    : statement* EOF
    ;

// Declarações
statement
    : inputStatement
    | outputStatement
    | conditionalStatement
    | loopStatement
    | assignment
    ;

// Tipagem de variáveis PandoraX
typeCast
    : INTER
    | STRIN
    ;

// Entrada do usuário com conversão de tipo
inputStatement
    : ID EQ typeCast LPAREN summonCall RPAREN
    ;

// Saída para o usuário (string interpolada dentro de <>)
outputStatement
    : PANDORAEXPOSE LPAREN INTERPOLATED_STRING RPAREN
    ;

// Condicional com when / whenever
conditionalStatement
    : WHEN expression block (WHENEVER block)?
    ;

// Laço loopX
loopStatement
    : LOOPX expression block
    ;

// Atribuição direta
assignment
    : ID EQ expression
    ;

// Bloco de múltiplas instruções entre chaves
block
    : LBRACE statement* RBRACE
    ;

// Expressões aritméticas e lógicas
expression
    : expression (PLUS | MINUS | MULT | DIV) expression   # arithmeticExpression
    | expression (GT | LT | GE | LE | EQEQ | NEQ) expression # comparisonExpression
    | LPAREN expression RPAREN                            # parenExpression
    | INT                                                 # intExpression
    | ID                                                  # idExpression
    ;

// Chamada de summon.x(<...>)
summonCall
    : SUMMON LPAREN INTERPOLATED_STRING RPAREN
    ;

// Tokens
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
INT     : [0-9]+ ;
INTERPOLATED_STRING : '<' ( ~[<>{}] | '{' ID '}' )* '>' ;
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;

// Palavras-chave
WHEN          : 'when';
WHENEVER      : 'whenever';
LOOPX         : 'loopX';
INTER         : 'inter';
STRIN         : 'strin';
PANDORAEXPOSE : 'pandora.expose';
SUMMON        : 'summon.x';

// Operadores
PLUS    : '+';
MINUS   : '-';
MULT    : '*';
DIV     : '/';
EQ      : '=';
LT      : '<';
GT      : '>';
LE      : '<=';
GE      : '>=';
EQEQ    : '==';
NEQ     : '!=';

// Delimitadores
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';