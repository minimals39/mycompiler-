from ply import *
import flex
import sys
tokens = flex.tokens 

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV','MOD'),
    ('left', 'LESS','MORE'),
)

#--------------------------------------------------------------------------------------------------------------

def p_statement_multiple(p):
    '''statement : statement NEWLINE statement
                 | statement NEWLINE statement NEWLINE'''
    p[0] = ('multiple_stm', p[1], p[3])

def p_statement_simple(p):
    '''statement : exassign
                 | declare
                 | exprint
                 | exif
                 | exelif
                 | exloop
                 | exrepeat
                 | statement NEWLINE
                 | NEWLINE statement
                 | exloop NEWLINE
                 '''
    if p[1] == '\n':
        p[0] = p[2]
    else:
        p[0] = p[1]

#--------------------------------------expression-conditions----------------------------------------------------------------------------------


def p_exif(p):
    '''exif : SO LPAREN expression RPAREN LSTATE statement RSTATE
             | SO LPAREN expression RPAREN NEWLINE LSTATE statement RSTATE'''
    if p[5] == '\n':
        p[0] = ('if', p[3], p[7])
    else:
        p[0] = ('if', p[3], p[6])


def p_exelif(p):
    '''exelif : exif exelse'''
    p[0] = ('elif', p[1], p[2])


def p_exelse(p):
    '''exelse : OTHERWISE LSTATE statement LSTATE OTHERWISE
               | OTHERWISE LSTATE NEWLINE statement RSTATE'''
    if p[3] == '\n':
        p[0] = ('else', p[4])
    else:
        p[0] = ('else', p[3])


def p_exloop(p):
    '''exloop : LOOP LPAREN expression RPAREN LSTATE statement RSTATE
             | LOOP LPAREN expression RPAREN LSTATE NEWLINE statement RSTATE'''
    if p[6] == '\n':
        p[0] = ('loop', p[3], p[7])
    else:
        p[0] = ('loop', p[3], p[6])

def p_exrepeat(p):
    '''exrepeat : REPEAT LPAREN expression RPAREN LSTATE statement RSTATE
                | REPEAT LPAREN expression RPAREN NEWLINE LSTATE statement RSTATE'''
    if p[5] == '\n':
        p[0] = ('repeat', p[3], p[7])
    else:
        p[0] = ('repeat', p[3], p[6])        

#-----------------------------------valuestuffs-----------------------------------------------------
def p_expression_operators(p):
    '''expression : expression PLUS expression                  
                  | term PLUS term
                  | term PLUS expression
                  | expression MINUS expression
                  | term MINUS term
                  | term MINUS expression
                  | expression MUL expression
                  | term MUL term
                  | term MUL expression
                  | expression DIV expression
                  | term DIV term
                  | term DIV expression
                  | expression MOD expression
                  | term MOD term
                  | term MOD expression'''
    if p[2] == '+':
        p[0] = ('PLUS',p[1],p[3])
    elif p[2] == '-':
        p[0] = ('MINUS',p[1],p[3])
    elif p[2] == '*':
        p[0] = ('MUL',p[1],p[3])
    elif p[2] == '/':
        p[0] = ('DIV',p[1],p[3])
    elif p[2] == '%':
        p[0] = ('MOD',p[1],p[3])

def p_value(p):
    '''term : WORD
           | arraysh
           | NUM'''
    p[0] = p[1]

def p_value_hex(p):
    '''term : HEXT HEX'''
    p[0] = p[2]


def p_expression_standalone(p):
    '''expression : term'''
    p[0] = p[1]


def p_expression_negative(p):
    'expression : MINUS expression'
    p[0] = ('negative', p[1])


def p_expression_parenthesis(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_assign(p):
    '''exassign : WORD EQU expression
                  | arraysh EQU expression
                  '''
    p[0] = ('assign',p[1],p[3])


def p_expression_EQUTO(p):
    '''expression : expression EQUTO expression'''
    p[0] = ('==', p[1], p[3])

def p_expression_NEQU(p):
    'expression : expression NOEQU expression'
    p[0] = ('<=>', p[1], p[3])


def p_expression_LESS(p):
    '''expression : expression LESS expression'''
    p[0] = ('<<', p[1], p[3])


def p_expression_MORE(p):
    '''expression : expression MORE expression'''
    p[0] = ('>>', p[1], p[3])



#----------------declare----------------------

def p_declare_const(p):
    '''declare : DECL WORD
               | DECL WORD EQU term'''
    if(len(p) == 3) :
        p[0] = ("decl", p[2], 0)
    else : 
        p[0] = ("decl", p[2], p[4])

#----------------declare array-------------

def p_defineexp_arrayshort(p):
    '''arraysh : WORD LARRY NUM RARRY
               | WORD LARRY WORD RARRY'''
    p[0] = ("array", p[1], p[3])

def p_defineexp_arraya(p):
    'declare : DECL WORD EQU LSTATE arrayX RSTATE'
    p[0] = ("var_array", p[2], p[5])


def p_defineexp_arrayb(p):
    'declare : DECL WORD LARRY NUM RARRY'
    p[0] = ("var_array", p[2], p[4], 0)


def p_defineexp_arrayc(p):
    'declare : DECL WORD LARRY NUM RARRY EQU LSTATE arrayX RSTATE'
    p[0] = ("var_array", p[2], p[4], p[8])


def p_arrayX_simple(p):
    'arrayX : NUM arrayY'
    p[0] = ("argument", p[1], p[2])


def p_arrayY_simple(p):
    '''arrayY : COMMA NUM arrayY
              | empty empty empty'''
    p[0] = ("argument", p[2], p[3])

    

# print ----------------------------------------


def p_exprint(p):
    'exprint : TEXT LPAREN WORD printMore RPAREN'
    p[0] = ('print', p[3], p[4])


def p_print_content(p):
    '''printMore : "," expression printMore
                 | empty empty empty'''
    p[0] = ('argument', p[2], p[3])


# Error rule for syntax errors

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        if p.value == '\n':
            print("Syntax error at line %d" % p.lineno)
        else:
            print("Syntax error at '%s' at line %d" %
                  (p.value, p.lexer.lineno))
    else:
        print("Syntax error at EOF")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)

