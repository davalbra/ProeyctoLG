import ply.lex as lex
#Javascript
#Genesis Baquerizo
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
    'continue' : 'CONTINUE',
    'in' : 'IN',
    'return' : 'RETURN',
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
#Fin Genesis Baquerizo

# List of token names.   This is always required
tokens = (
    'STRING',
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
    'ASIGNAR',
    'IGUALDADESTRICTA',
    'DLLAVE',
    'ILLAVE',
    'COMA',
    'DCORCHETE',
    'ICORCHETE',
    'AND',
    'OR',
    'NEGACION',
    'MASIGUAL',
    'PUNTOCOMA',
    'BOOLEANO',
    'MODULO',
    'MENOSIGUAL',
    'PORIGUAL',
    'DIVISIONIGUAL',
    'COMMENT',
    'MENORIGUAL',
    'METODO_POP_ARRAY',
    'METODO_PUSH_ARRAY'

         ) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_MAS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBER = r'\d+\.?\d*'
t_FLOTANTE = r'\d+\.\d+'
t_NOESIGUAL = r'!\='
t_MAYORIGUAL = r'>='
t_ASIGNAR = r'='
t_IGUALDADESTRICTA = r'==='
#"cambios David Bravo"
t_DLLAVE= r'\{'
t_ILLAVE= r'\}'
t_COMA=r'\,'
t_DCORCHETE= r'\['
t_ICORCHETE= r'\]'
t_MENORIGUAL= r'<='
#Yonkani Cedeño
t_AND = r'&{2}'
t_OR = r'\|{2}'
t_NEGACION = r'!'
t_MASIGUAL = r'\+='
t_PUNTOCOMA = r';'
t_MODULO = r'\%'
t_MENOSIGUAL = r'\-='
t_PORIGUAL = r'\*='
t_DIVISIONIGUAL = r'\/='
#t_METODO = r'\.[a-zA-Z]+[A-Za-z0-9]*'
t_METODO_POP_ARRAY=r'\.pop'
t_METODO_PUSH_ARRAY=r'\.push'


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Yonkani Cedeño
def t_VARIABLE(t):
    r'[a-zA-Z_$][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

#Genesis Baquerizo
def t_STRING(t):
    r'\".*\"'
    t.value = t.value[1:-1]  # remuevo las comillas
    return t
#Fin Genesis Baquerizo

#Yonkani Cedeño
def t_COMMENT(t):
    r'\/{2}.{1,30}'
    t.type = reserved.get(t.value, 'COMMENT')
    return t
#Fin Yonkani CEdeño 
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''let var1 = "HOla Mundo"; 
//estoesun comentario de 30 cara
const _Mi_variable = 14.2;
function (o1,o2,o3) {
   let resultado = var1 * var2;
   let res *= resultado;
   return res; 
   resultado.lower.get();
   resultado.pop();
}'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)

