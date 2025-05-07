grammar PandoraX;

program: statement* EOF;

statement
    : inputStatement
    | outputStatement
    | conditionalStatement
    | loopStatement
    | assignment
    ;

// Tipos de cast
typeCast: INTER | STRIN;

// Declaração de entrada
inputStatement
    : ID EQ typeCast LPAREN SUMMON LPAREN INTERPOLATED_STRING RPAREN RPAREN
    ;

// Chamada summon.x
summonCall
    : SUMMON LPAREN INTERPOLATED_STRING RPAREN
    ;

// Saída
outputStatement
    : PANDORAEXPOSE LPAREN INTERPOLATED_STRING RPAREN
    ;

// Condicionais
conditionalStatement
    : WHEN expression block (WHENEVER block)?
    ;

// Loops
loopStatement
    : LOOPX expression block
    ;

// Atribuição
assignment
    : ID EQ expression
    ;

// Bloco de código
block: LBRACE statement* RBRACE;

// Expressões
expression
    : expression (MULT | DIV) expression       # MulDivExpr
    | expression (PLUS | MINUS) expression     # AddSubExpr
    | expression (GT | LT | GE | LE) expression # ComparisonExpr
    | expression (EQEQ | NEQ) expression       # EqualityExpr
    | LPAREN expression RPAREN                 # ParenExpr
    | INT                                      # IntExpr
    | ID                                       # IdExpr
    ;

// Tokens
INTER: 'inter';
STRIN: 'strin';
WHEN: 'when';
WHENEVER: 'whenever';
LOOPX: 'loopX';
PANDORAEXPOSE: 'pandora.expose';
SUMMON: 'summon.x';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
INTERPOLATED_STRING: '<' ( ~[<>{}] | '{' ID '}' )* '>';

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
EQ: '=';
GT: '>';
LT: '<';
GE: '>=';
LE: '<=';
EQEQ: '==';
NEQ: '!=';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';

WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;