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
    : 'inter'
    | 'strin'
    ;

// Entrada do usuário com conversão de tipo
inputStatement
    : ID '=' typeCast '(' summonCall ')'
    ;

// Saída para o usuário (string interpolada dentro de <>)
outputStatement
    : 'pandora.expose' '(' STRING ')' ';'?
    ;

// Condicional com when / whenever
conditionalStatement
    : 'when' expression ':' block ('whenever' ':' block)?
    ;

// Laço loopX
loopStatement
    : 'loopX' expression ':' block
    ;

// Atribuição direta
assignment
    : ID '=' expression
    ;

// Bloco de múltiplas instruções
block
    : statement+
    ;

// Expressões aritméticas e lógicas
expression
    : expression ('+' | '-' | '*' | '/') expression
    | '(' expression ')'
    | INT
    | ID
    ;

// Chamada de summon.x(<...>)
summonCall
    : 'summon.x' '(' STRING ')'
    ;

// Tokens
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
INT     : [0-9]+ ;
STRING : '<' (~'>')* '>' ; // Suporte para interpolação entre <>
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;
