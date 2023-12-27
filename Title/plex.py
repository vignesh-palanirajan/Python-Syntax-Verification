import ply.lex as lex

tokens = (
    'OPEN',              
    'CLOSE',           
    'ID',
)

t_OPEN = r'<title>'
t_CLOSE = r'</title>'
t_ID = r'\w'

t_ignore = ' \t'

def t_error(t):
    # print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
    return t

lexer = lex.lex()