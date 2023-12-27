import ply.yacc as yacc
from plex import tokens, lexer

def p_html_tag(p):
    '''
    html_tag : OPEN SRC ALT args END 
    '''           
    p[0] = "\nACCEPTED\n"             

def p_args(p):
    'args : ID'
    p[0] = [p[1]]

def p_args_multiple(p):
    'args : args ID'
    p[0] = p[1] + [p[2]]


def p_error(p):
    pass

parser = yacc.yacc()


while True:
    try:
        s = input('check > ')

        lexer.input(s)
        
        print()
        first = []
        for tok in lexer:
            print(tok)
            first.append(tok.type)

        
        result = parser.parse(s)

        if (first[0] == 'OPEN') and (result is not None):
            print(result)
        else:
            print("\nNOT ACCEPTED\n")


    except EOFError:
        break

    if not s: 
        continue