grammar PandoraX;

program: statement* EOF;

statement
    : declaration
    | outputStatement
    | conditionalStatement
    | loopStatement
    | assignment
    ;

declaration
    : typeCast ID EQ expression
    | typeCast ID 
    ;

typeCast: INTER | STRIN;

outputStatement
    : PANDORAEXPOSE LPAREN INTERPOLATED_STRING RPAREN
    ;

conditionalStatement
    : WHEN expression block (WHENEVER block)?
    ;

loopStatement
    : LOOPX expression block
    ;

assignment
    : ID EQ expression
    ;

block: LBRACE statement* RBRACE;

expression
    : expression (MULT | DIV) expression           # MulDivExpr
    | expression (PLUS | MINUS) expression         # AddSubExpr
    | expression (GT | LT | GE | LE) expression    # ComparisonExpr
    | expression (EQEQ | NEQ) expression           # EqualityExpr
    | expression AND expression                    # AndExpr
    | expression OR expression                     # OrExpr
    | NOT expression                               # NotExpr
    | LPAREN expression RPAREN                     # ParenExpr
    | INT                                          # IntExpr
    | BOOL                                         # BoolExpr
    | ID                                           # IdExpr
    | typeCast LPAREN SUMMON LPAREN INTERPOLATED_STRING RPAREN RPAREN # SummonExpr
    ;

// Tokens
INTER: 'inter';
STRIN: 'strin';
WHEN: 'when';
WHENEVER: 'whenever';
LOOPX: 'loopX';
PANDORAEXPOSE: 'pandora.expose';
SUMMON: 'summon.x';
AND: 'and';
OR: 'or';
NOT: 'not';
TRUE: 'true';
FALSE: 'false';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
BOOL: TRUE | FALSE;
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
