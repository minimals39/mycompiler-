from ply import *
import basiclex

tokens = basiclex.tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('left', 'POWER'),
    ('right', 'UMINUS')
)

