import ply.lex as lex

tokens = (
    'OPEN',              
    'CLOSE',           
    'ID',
)

t_OPEN = r'<p>'
t_CLOSE = r'</p>'
t_ID = r'\w'

t_ignore = ' \t'

def t_error(t):
    # print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
    return t

lexer = lex.lex()