import ply.yacc as yacc
from lclex import lexer
from lclex import tokens

def p_line(p):
    '''line : func
            | FNAME ASSIGN func'''
    if len(p) == 2 :
        p[0] = p[1]
    else :
        p[0] = ('ASSIGN', '_' + p[1], p[3])

def p_func(p):
    '''func : term
            | LAMBDA FNAME ARROW func'''
    if len(p) == 2 :
        p[0] = p[1]
    else : 
        p[0] = ('LAMBDA', '_' + p[2], p[4])
    
def p_term(p):
    '''term : single
            | term single'''
    if len(p) == 2 :
        p[0] = p[1]
    else :
        p[0] = ('CALL', p[1], p[2])

def p_single(p):
    '''single : FNAME
              | LPAREN func RPAREN'''
    if len(p) == 2 :
        p[0] = '_' + p[1]
    else :
        p[0] = p[2]

class MyError(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)

# Error rule for syntax errors
def p_error(p):
    raise MyError("Syntax error in input!")

parser = yacc.yacc()
global_func = {}

rename_counter = 0
rename_map = {}
def rename(p) :
    global rename_counter, rename_map

    if type(p) == str :
        return rename_map[p] if p in rename_map else p
    
    if p[0] == 'LAMBDA' :
        rename_counter += 1
        new_name = 'x' + str(rename_counter)
        rename_map[p[1]] = new_name
        ret = ('LAMBDA', new_name, rename(p[2]))
        rename_map.pop(p[1])
        return ret
    
    else :
        return ('CALL', rename(p[1]), rename(p[2]))

def replace(p, s, q) :
    if type(p) == str :
        return rename(q) if p == s else p
    else :
        return (p[0], replace(p[1], s, q), replace(p[2], s, q))

simplify_flag = False
def simplify(p) :
    global simplify_flag

    if type(p) == str or simplify_flag :
        return p

    if p[0] == 'LAMBDA' :
        return ('LAMBDA', p[1], simplify(p[2]))
    
    else :
        p1 = simplify(p[1])
        p2 = simplify(p[2])

        if not simplify_flag and type(p1) == tuple and p[1][0] == 'LAMBDA' :
            simplify_flag = True
            return replace(p1[2], p1[1], p2)
        else :
            return ('CALL', p1, p2)

lambda_func = set()
def inline(p) :
    global lambda_func

    if type(p) == str :
        if p not in lambda_func and p not in global_func :
            raise MyError('unknown function ' + p)
        return rename(global_func[p]) if p not in lambda_func else p
    
    if p[0] == 'LAMBDA' :
        lambda_func.add(p[1])
        ret = ('LAMBDA', p[1], inline(p[2]))
        lambda_func.remove(p[1])
        return ret
    
    else :
        return ('CALL', inline(p[1]), inline(p[2]))

def analysis(p) :
    global rename_counter, rename_map, simplify_flag
    p = rename(p)
    p = inline(p)
    # print(p)

    while True :
        # show(p)
        simplify_flag = False
        p = simplify(p)
        if not simplify_flag : break
    rename_counter, rename_map = 0, {}
    p = rename(p)
    return p

def show(p, header='') :
    if type(p) == str :
        print(p)
        return
    
    print(p[0], end='')
    print('─┬─', end='')
    header += ' ' * len(p[0])
    header += ' │ '
    show(p[1], header)
    header = header[:-2] + '└─'
    print(header, end='')
    header = header[:-2] + '  '
    show(p[2], header)

while True :
    try :
        s = input('>>> ')
    except EOFError :
        break
    if not s: continue

    try :
        lexer.input(s)
        print([tok for tok in lexer])

        AST_raw = parser.parse(s)
        # print(AST_raw)
        show(AST_raw)

        if AST_raw[0] == 'ASSIGN' :
            AST = analysis(AST_raw[2])
        else :
            AST = analysis(AST_raw)

        # print(AST)
        show(AST)
        for k, v in global_func.items() :
            if str(v) == str(AST) :
                print('<same as ' + k + '>')

        if AST_raw[0] == 'ASSIGN' :
            global_func[AST_raw[1]] = AST

    except MyError as e :
        print('! ', e)