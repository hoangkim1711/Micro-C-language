/*
ID: 1711872
Name: Dinh Hoang Kim
Assignment 01 - Micro C Language
 */
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        result.text = result.text[1:]
        for i in range(len(result.text)):
            if result.text[i] == '\n' or result.text[i] == '\r':
                result.text = result.text[0:i]
                break
        raise UncloseString(result.text);
    elif tk == self.STRINGLIT:
        result = super().emit();
        result.text = result.text[1:-1]
        return result
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        result.text = result.text[1:]
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

//______________________________________________Work on______________________________________________!!!

WS :                    [\t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR:             [@#?$~`^\\];

UNCLOSE_STRING:         '"' (ESC_SEQ | STR_CHAR)* ~('"')
                        | '"' ((ESC_SEQ | STR_CHAR)*('\n'|'\r')(ESC_SEQ | STR_CHAR)*) '"'
                        | '"' <EOF>;

ILLEGAL_ESCAPE:         '"' ( STR_CHAR | ESC_SEQ )* NOT_ESC_SEQ;

fragment NOT_ESC_SEQ:   '\\'~('b'|'f'| '\'' | '"' | '\\') 
                        | '\\''r''\\'~('n');

fragment STR_CHAR:      ~('\\'|'"');

//Section 4. Type and Values            #############################################################_4

PRIM_TYPE:      BOOLEAN_TYPE 
                | INTTYPE 
                | FLOAT_TYPE 
                | STRING_TYPE;

VOIDTYPE:       VOID;       //available in file @@

BOOLEAN_TYPE:   BOOLEAN;

INTTYPE:        INT;        //available in file @@

FLOAT_TYPE:     FLOAT;

STRING_TYPE:    STRING;

ARRAY_TYPE:     ID LSB INTLIT RSB;

ARRAY_POINTER_TYPE: PRIM_TYPE ( ID LSB RSB | LSB RSB);

//Section 2. Program structure          ##############################################################_2

program:    decl EOF;

decl:       (func_decl | var_decl)+;

//  2.2.    Function declaration

func_decl:  func_type ID LB para_list RB block_state;   //block_statement in Section 7.8

func_type:  (ARRAY_POINTER_TYPE | VOIDTYPE | PRIM_TYPE) ;

para_list:  (para_decl (COMA para_decl)*)?;

para_decl:  (PRIM_TYPE ID) | (PRIM_TYPE ID LSB RSB);

//  2.1.    Variable declaration

var_decl:   PRIM_TYPE id_list SEMI;                    //PRIM_TYPE in Section 4    

id_list:    id_var (COMA id_var)*; 

id_var:     ID | ARRAY_TYPE;

//Section 3.Lexical Specification       #############################################################_3
//  3.1.    Character set
//  3.2.    Comment

COMMENT:    ( '//' ~[\r\n]*             // comment line
            | '/*' .*? '*/' )           // comment block
            -> skip;

//  3.5.    Literal

INTLIT:     [0-9]+; //available in file

FLOATLIT:   INTLIT '.' [0-9]* EXPONENT?
            | '.' INTLIT EXPONENT?
            | INTLIT EXPONENT;      

fragment    EXPONENT: ('e'|'E') ('+'|'-')? INTLIT;
 
BOOLEANLIT: TRUE | FALSE;

STRINGLIT:  '"' ( ESC_SEQ | ~('\\'|'"') )* '"';

fragment    ESC_SEQ: '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\''|'\\');

//Section 5. Variable (Section 2.1)     #############################################################_5
//  5.1.    Global variable
//  5.2.    Local variable
//Section 6. Expressions                #############################################################_6

exp:    exp_1 ASSIGN exp 
        | exp_1;

exp_1:  exp_1 OR exp_2
        | exp_2;

exp_2:  exp_2 AND exp_3
        | exp_3;

exp_3:  exp_3 (EQUAL | NOT_EQUAL) exp_3
        | exp_4;

exp_4:  exp_4 (LESS_THAN | LESS_EQ | GREAT_THAN | GREAT_EQ) exp_4
        | exp_5;

exp_5:  exp_5 (ADD | SUB) exp_6
        | exp_6;

exp_6:  exp_6 (MUL | DIV | MOD) exp_7
        | exp_7;

exp_7:  (NOT | '-') exp_7
        | exp_8;

exp_8:  exp_8 LSB exp_8? RSB
        | exp_9;

exp_9:  LB exp_1 RB
        | exp_0;

exp_0:  INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT
        | PRIM_TYPE | ARRAY_TYPE
        | func_call
        | ID
        | exp_0 LB exp_0 ( COMA exp_0 )* RB 
        | exp_0'.'ID;

//Section 7. Statements and Control Flow    #########################################################_7

if_state:       IF LB exp RB statement (ELSE statement)?;

do_while_state: DO (statement)+ WHILE exp SEMI;

for_state:      FOR LB exp SEMI exp SEMI exp RB statement;

break_state:    BREAK SEMI;

continue_state: CONTINUE SEMI;

return_state:   RETURN (exp)? SEMI;

exp_state:      exp SEMI;

assign_state:   exp (ASSIGN exp)+ SEMI;

//  7.8. The block statement          

block_state:    LP statement? RP;

statement:  ( var_decl 
            | block_state
            | if_state 
            | do_while_state 
            | for_state 
            | break_state 
            | continue_state 
            | return_state 
            | exp_state 
            | assign_state 
            | func_call )+;

func_call:  ID LB (exp(COMA exp)*)? RB;

//  3.3.    Token set
//          Keywords:

BOOLEAN:    'boolean';
BREAK:      'break';
CONTINUE:   'continue';
ELSE:       'else';
FOR:        'for';
FLOAT:      'float';
IF:         'if';
INT:        'int';
RETURN:     'return';
VOID:       'void';
DO:         'do';
WHILE:      'while';
TRUE:       'true';
FALSE:      'false';
STRING:     'string';

//          Identifiers:

ID:         ([a-zA-Z_] [a-zA-Z_0-9]*);

//          Operators:
ADD:        '+';
SUB:        '-';
MUL:        '*';
DIV:        '/';
NOT:        '!';
MOD:        '%';
OR:         '||';
AND:        '&&';
NOT_EQUAL:  '!=';
EQUAL:      '==';
LESS_THAN:  '<';
GREAT_THAN: '>';
LESS_EQ:    '<=';
GREAT_EQ:   '>=';
ASSIGN:     '=';

//  3.4.    Separators
LSB:        '[';
RSB:        ']';

LP:         '{';    //available in file
RP:         '}';    //available in file

LB:         '(';    //available in file
RB:         ')';    //available in file

SEMI:       ';';    //available in file
COMA:       ',';

DOT:        '.';

//Section 8. Built-in Functions            ##########################################################_8
//Section 9. Scrope Rules                  ##########################################################_9
//Section 10. The main function            #########################################################_10
//main_func:  main_type 'main' LB RB block_state;
//main_type:  INTTYPE | VOIDTYPE;