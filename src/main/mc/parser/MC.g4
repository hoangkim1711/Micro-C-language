/*
ID: 1711872
Name: Dinh Hoang Kim
Assignment 02 - Micro C Language
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
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        result.text = result.text[1:]
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    elif tk == self.STRINGLIT:
        result = super().emit();
        result.text = result.text[1:-1]
        return result
    else:
        return super().emit();
}

options{
	language=Python3;
}

//______________________________________________Work on______________________________________________!!!

//Section 2. Program structure
program:    decls EOF;

decls:      one_decl | one_decl decls;

one_decl:   var_decl | func_decl;

//  2.1.    Variable declaration
var_decl:   prim_type id_list  SEMI;

prim_type:  INT_TYPE
            | FLOAT_TYPE
            | BOOLEAN_TYPE
            | STRING_TYPE;

id_list:    ID COMA id_list 
            | ID LSB INTLIT RSB COMA id_list
            | ID
            | ID LSB INTLIT RSB;

//id_list:    (id_var COMA)* id_var;

//id_var:     ID | (ID LSB INTLIT RSB);


//prim_var:  ID;
//arr_var:   ID LSB INTLIT RSB;

//  2.2.    Function declaration
func_decl:  (prim_type | VOID_TYPE) ID LB para_list RB block_state
            | prim_type LSB RSB ID LB para_list RB block_state;

para_list:  (para_decl re_para)?;

re_para:    (COMA para_decl re_para)?;

para_decl:  prim_type ID (LSB RSB)?;

//  7.8. The block statement 
block_state:    LP statement* RP;

statement:   var_decl
            | do_while_state
            | if_state
            | for_state
            | break_state
            | continue_state
            | return_state
            | exp SEMI
            | block_state; 

//func_call:  ID LB (exp(COMA exp)*)? RB;

//Section 7. Statements and Control Flow 
do_while_state: 'do' statement+ 'while' exp SEMI;

if_state:       'if' LB exp RB statement (ELSE statement)?;

for_state:      'for' LB exp SEMI exp SEMI exp RB statement;

break_state:    'break' SEMI;

continue_state: 'continue' SEMI;

return_state:   'return' exp? SEMI;

//Section 6. Expressions 

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

exp_7:  (NOT | SUB) exp_7
        | exp_8;

exp_8:  exp_9  LSB exp_5 RSB
        | exp_9;

exp_9:  LB exp_1 RB
        | exp_0;

exp_0:  primid_lit 
        | ID LB (exp (COMA exp)*)? RB;  //function call

primid_lit: INTLIT
            | FLOATLIT
            | STRINGLIT
            | BOOLEANLIT
            | ID;


//Lexer | keywork ...

fragment EXPONENT:  ('e'|'E') ('+'|'-')? INTLIT;
                        
fragment ESC_SEQ:   '\\' ('b'|'t'|'n'|'f'|'r'|'"'|'\''|'\\');

fragment STR_CHAR:  ~('\\'|'"');

fragment NOT_ESC_SEQ:   '\\'~('b'|'f'| '\'' | '"' | '\\') |'\\''r''\\'~('n');

COMMENT:    ( '//' ~[\r\n]*             // comment line
            | '/*' .*? '*/' )           // comment block
            -> skip;

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

//Section 4. Type and Values
INT_TYPE:        'int';        //available in file @@
FLOAT_TYPE:     'float';
BOOLEAN_TYPE:   'boolean';
STRING_TYPE:    'string';
VOID_TYPE:       'void';       //available in file @@

ELSE: 'else';

//ARRAY_TYPE:     ID LSB INTLIT RSB;

//ARRAY_POINTER_TYPE: PRIM_TYPE ( ID LSB RSB | LSB RSB);

//  3.5.    Literal
INTLIT:     [0-9]+; //available in file

FLOATLIT:   INTLIT '.' [0-9]* EXPONENT?
            | '.' INTLIT EXPONENT?
            | INTLIT EXPONENT; 

BOOLEANLIT: 'true' | 'false';
            
//          Identifiers:
ID:         [a-zA-Z_] [a-zA-Z_0-9]*;

//  3.4.    Separators
LSB:        '[';
RSB:        ']';

LP:         '{';    //available in file
RP:         '}';    //available in file

LB:         '(';    //available in file
RB:         ')';    //available in file

SEMI:       ';';    //available in file
COMA:       ',';

//DOT:        '.';

WS:             [ \t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' (ESC_SEQ | STR_CHAR)* ~('"')
                | '"' ((ESC_SEQ | STR_CHAR)*('\n'|'\r')(ESC_SEQ | STR_CHAR)*) '"'
                | '"' <EOF>;

ILLEGAL_ESCAPE: '"' ( STR_CHAR | ESC_SEQ )* NOT_ESC_SEQ;

STRINGLIT:      '"' ( ESC_SEQ | ~('\\'|'"') )* '"';

ERROR_CHAR:     .;

//Section 8. Built-in Functions            ##########################################################_8
//Section 9. Scrope Rules                  ##########################################################_9
//Section 10. The main function            #########################################################_10
//main_func:  main_type 'main' LB RB block_state;
//main_type:  INTTYPE | VOIDTYPE;