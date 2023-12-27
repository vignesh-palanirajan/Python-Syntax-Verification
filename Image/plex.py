import ply.lex as lex
#<img src="img_girl.jpg" alt="ID">

# Tokens
tokens = (
    'OPEN',
    'ID',
    'SRC',
    'INV',
    'END',
    'ALT',
)

# Lexer rules
t_OPEN = r'<img\s+src\s*="'

t_ID = r'\w+'
t_END = r'">'
t_ALT = r'"\s*alt="'
#t_SRC = r'"(https?://[^"]+)">'

def t_SRC(t):
    '"(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?\/[a-zA-Z0-9]{2,}|((https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?)|(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})?'
    return t


t_ignore = ' \t'


def t_error(t):
    # print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
    i = 0
    try:
        while t.value[i] not in (' \t:\n'):
            t.lexer.skip(1)
            i+=1
    except:
        pass

    t.type = 'INV'
    t.value = t.value[0]
    return t


lexer = lex.lex()
