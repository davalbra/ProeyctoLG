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
    'CADENA',
    'NUMERO',
    'MAS',
    'MENOS',
    'MULTIPLICAR',
    'DIVIDIR',
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
    'MAYOR_QUE',
    'MENOR_QUE',
    'NEGACION',
    'MASIGUAL',
    'PUNTOCOMA',
    'BOOLEANO',
    'MODULO',
    'PUNTO',
    'DOSPUNTOS',
    'MENOSIGUAL',
    'PORIGUAL',
    'DIVISIONIGUAL',
    'COMENTARIO',
    'MENORIGUAL',
    'METODO_POP_ARRAY',
    'METODO_PUSH_ARRAY',
    'METODO_ADD_SET',
    'METODO_SIZE_SET',
    'METODO_SET',
    'METODO_HAS'
         ) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICAR = r'\*'
t_DIVIDIR = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_FLOTANTE = r'\d+\.\d+'
t_NOESIGUAL = r'!\='
t_MAYORIGUAL = r'>='
t_ASIGNAR = r'='
t_MAYOR_QUE = r'>'
t_MENOR_QUE = r'<'
t_DOSPUNTOS = r':'
t_IGUALDADESTRICTA = r'==='
#"cambios David Bravo"
t_ILLAVE= r'\{'
t_DLLAVE= r'\}'
t_COMA=r'\,'
t_PUNTO=r'\.'
t_DCORCHETE= r'\['
t_ICORCHETE= r'\]'
t_MENORIGUAL= r'<='
t_METODO_SET= r'\.set'
t_METODO_HAS= r'\.has'
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
t_METODO_ADD_SET= r'\.add'
t_METODO_SIZE_SET= r'\.size'


def t_NUMERO(t):
    r'\d+'
    t.value =int(t.value)
    return t

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
def t_CADENA(t):
    r'\".*\"'
    t.value = t.value[1:-1]  # remuevo las comillas
    return t


#Fin Genesis Baquerizo

#Yonkani Cedeño
def t_COMENTARIO(t):
    r'\/{2}.{1,30}'
    t.type = reserved.get(t.value, 'COMENTARIO')
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

#Yonkani, Genesis
# Test it out
data = '''let var1 = "HOla Mundo"; 
//estoesun comentario de 30 cara
const _Mi_variable = 14.2;
let mapa1 = new Map();
const cj1 = new Set();
let arr1 = [1,2,3,4,54,1];
let arr2 = ["HOla", "minuto", "segundos"]
function nombre(o1,o2,o3) {
   let resultado = var1 * var2;
   let res *= resultado;
   return res; 
   cj1.pop();
   arr1.Size();
   resultado.Add() 
   mapa1.has(); 
   cj1.set();
   const variable_2 = true;
   if( variable_2 != _Mi_variable){
        variable_2 === cj1;
   }
   else if( variable_2 <= var1){
        while(!variable_2){
            res + variable_2;
            res - variable_2;
            _Mi_variable * 32;
        }
   }
   switch(variable){
        case "a":
        case "b":
        default:
   }
   do{}while(true);
   try {
        nonExistentFunction();
   } catch (error) {
    for(int i = 0; i< 2; i++){
    }

}
}'''
#Fin Yonkani, Genesis
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)

