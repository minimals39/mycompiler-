from ply import *
import flex

tokens = flex.tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV','MOD'),
    ('left', 'LESS','MORE'),
)

#--------------------------------------------------------------------------------------------------------------

# def p_statement_multiple(p):
#    '''statement : statement NEWLINE statement
#                 | statement NEWLINE statement NEWLINE'''
#    p[0] = ('multiple_stm', p[1], p[3])

#def p_statement_simple(p):
#    '''statement : assignexp
#                 | defineexp
#                 | printexp
#                 | sleepexp
#                 | ifexp
#                 | ifelseexp
#                 | whileexp
#                 | statement NEWLINE
#                 | NEWLINE statement
#                 '''
    #  | loopexp NEWLINE
#    if p[1] == '\n':
#        p[0] = p[2]
#    else:
#        p[0] = p[1]

#--------------------------------------expression----------------------------------------------------------------------------------
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
    if p[2] == 'PLUS':
        p[0] = ('PLUS',p[1],p[3])
    elif p[2] == 'MINUS':
        p[0] = ('MINUS',p[1],p[3])
    elif p[2] == 'MUL':
        p[0] = ('MUL',p[1],p[3])
    elif p[2] == 'DIV':
        p[0] = ('DIV',p[1],p[3])
    elif p[2] == 'MOD':
        p[0] = ('MOD',p[1],p[3])

def p_expression_negative(p):
    'expression : MINUS expression'
    p[0] = ('negative', p[1])


def p_expression_parenthesis(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_assign(p):
    '''exassign : TYPE_T EQU expression
                  | TYPE_N EQU expression
                  | expression EQU expression
                  | '''
    p[0] = ('assign',p[1],p[3])


#----------------declare----------------------
def p_term(p):
    'term : TYPE_N EQU '


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

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

