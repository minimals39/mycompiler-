import ply.lex as lex

#list token
tokens = (
	'INT64','WORD','NUM','HEX','TEXT','LOOP','REPEAT',
	'SO','NOTSO','OTHERWISE','EQU','PLUS','MINUS','MUL','DIV',
	'SEMI','COMMA','MOD','DECADE','LPAREN','RPAREN','LARRY','RARRY',
	'LSTATE','RSTATE','BACK','NEWLINE','LESS','MORE','EQUTO','NOEQU','DECL', )
#Reseved word
RESERVED = {
	"int64":"INT64",
	"so" : "SO" ,
	"notso" : "NOTSO",
	"otherwise" : "OTHERWISE",
	"back" : "BACK",
	"loop" : "LOOP",
	"repeat" : "REPEAT",
	"decade" : "DECADE",
	"hex" : "HEX",
	"decl" : "DECL",
     "text" : "TEXT"
}


#SImple token
t_INT64 = r"int64"
t_SO = r"so"
t_NOTSO = r"notso"
t_OTHERWISE = r"otherwise"
t_BACK = r"back"
t_LOOP = r"loop"
t_REPEAT = r"repeat"
t_DECADE = r"decade"
t_EQU = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_COMMA = r','
t_SEMI = r';'
t_MOD = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSTATE = r'\{'
t_RSTATE = r'\}'
t_LARRY = r'\['
t_RARRY = r'\]'
t_LESS = r'<<'
t_MORE = r'>>'
t_EQUTO = r'=='
t_NOEQU = r'<=>'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.type = 'NEWLINE'
    return t


def t_WORD(t):
     r'[a-zA-Z_][a-zA-Z0-9_]*'
     t.type = RESERVED.get(t.value, "WORD")
     return t

def t_NUM(t):
    r'\d+|-\d+'
    t.value = int(t.value)
    return t

def t_HEX(t):
    r'0[hH][0-9a-fA-F]+|\d+|-\d+'
    if t.value[:2] == '0h':
        t.value = str(int(t.value.replace('0h', '0x'), 16))
    t.type = 'HEX'
    return t

 # A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 # Error handling rule

 
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)
 
 # Build the lexer
lexer = lex.lex()
 
 
#To use the lexer, you first need to feed it some input text using its input() method. After that, repeated calls to token() produce tokens. The following code shows how this works:

 
 # Test it out
data = '''
TEXT( << >> {} []) 2 f + - * / %



'''
 
 # Give the lexer some input
lexer.input(data)
 
 # Tokenize
while True:
     tok = lexer.token()
     if not tok: 
         break      # No more input
     print(tok)
 
#When executed, the example will produce the following output: