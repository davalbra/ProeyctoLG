import ply.lex as lex
#Javascript
reserved = {
    'default': 'DEFAULT',
    'delete' : 'DELETE',
    'break' : 'BREAK',
    'case' : 'CASE',
    'catch' : 'CATCH',
    'this' : 'THIS',
    'try' : 'TRY',
    'typeof' : 'TYPEOF',
    'var' : 'VAR',
    'let' : 'LET',
    'while' : 'WHILE',
    'finally' : 'FINALLY',
    'instanceof' : 'INSTANCEOF',
    'new' : 'NEW',
    'void' : 'VOID',
    'for' : 'FOR',
    'function' : 'FUNCTION',
    'else' : 'ELSE',
    'do' : 'DO',
    'case' : 'CASE',
    'catch' : 'CATCH',
    'continue' : 'CONTINUE',
    'in' : 'IN',
    'return' : 'RETURN',
    'switch' : 'SWITCH',
    'throw' : 'THROW',
    'await' : 'AWAIT',
    'class' : 'CLASS',
    'const' : 'CONST',
    'debugger' : 'DEBUGGER',
    'enum' : 'ENUM',
    'export' : 'EXPORT',
    'extends' : 'EXTENDS',
    'false' : 'FALSE',
    'implements' : 'IMPLEMENTS',
    'interface' : 'INTERFACE',
    'package' : 'PACKAGE',
    'private' : 'PRIVATE',
    'protected' : 'PROTECTED',
    'public' : 'PUBLIC',
    'super' : 'SUPER',
    'switch' : 'SWITCH',
    'static' : 'STATIC',
    'true' : 'TRUE',
    'with' : 'WITH',
    'yield' : 'YIELD',
    'abstract' : 'ABSTRACT',
    'arguments' : 'ARGUMENTS',
    'if': 'IF',
    'null' : 'NULL'
}

# List of token names.   This is always required
tokens = (
             'NUMBER',
             'MAS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'LPAREN',
             'RPAREN',
             'FLOTANTE',
             'VARIABLE',
             'NOESIGUAL',
             'MAYORIGUAL',
             'ASIGNAR'
         ) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_MAS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBER = r'\d+'
t_FLOTANTE = r'\d+\.\d+'
t_NOESIGUAL = r'!\='
t_MAYORIGUAL = r'>='
t_ASIGNAR = r'='
t_IGUALDADESTRICTA = r'a{3}'





# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_VARIABLE(t):
    r'[a-zA-Z_$][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t





# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''estoesunComentario $hola = == = temp99 $2_2 if for this 4sas class await != >=
22121-2 null'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)

