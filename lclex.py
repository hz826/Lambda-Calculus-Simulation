import ply.lex as lex

tokens = (
    'FNAME',
    'ASSIGN',
    'LAMBDA',
    'ARROW',
    'LPAREN',
    'RPAREN',
)

t_FNAME   = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ASSIGN = r'='
t_LAMBDA = r'\\'
t_ARROW  = r'->'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == '__main__' :
    data = r'if    = \b -> \t -> \f -> b t f'
    lexer.input(data)
    for tok in lexer:
        print(tok.type, tok.value, tok.lineno, tok.lexpos)