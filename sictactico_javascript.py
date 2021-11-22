from ejemplo import tokens

import ply.yacc as yacc

#yonkani


def p_expresion(p):
    '''expresion : asignar_variable
                | grupo_datos
                | FUNCTIONS
                | declarar_variable'''

#Nos permite agrupar
def p_grupo_datos(p):
    '''grupo_datos : tipos_datos
                    | tipos_datos COMA grupo_datos'''



# Funcion que permite declarar variables con su tipo de dato respectivo
#Tambien permite asignar a una variable otra variable
#Permite asignar a una variable ya creada otro tipo de dato
#Permite declarar las instancias de las estructuras Set y Map
def p_asignar_variable(p):
    '''asignar_variable : declarar_variable ASIGNAR tipos_datos PUNTOCOMA
                        | VARIABLE ASIGNAR VARIABLE PUNTOCOMA
                        | VARIABLE ASIGNAR tipos_datos PUNTOCOMA
                        | declarar_variable ASIGNAR iniciar_estructuras
                        '''

#Funcion para inicializar variables
def p_declarar_variable(p):
    '''declarar_variable : tipo_variable VARIABLE PUNTOCOMA
                        | tipo_variable VARIABLE
                        '''


# Aqui se declarar los tipos de datos
def p_tipos_datos(p):
    '''tipos_datos : booleano_tipo
                    | NUMERO
                    | CADENA
                    | FLOTANTE
                    | NULL'''

#Instanciar las estructuras de datos Map y Set
def p_iniciar_estructuras(p):
    '''iniciar_estructuras : NEW VARIABLE LPAREN RPAREN PUNTOCOMA '''



#Para declarar el tipo de variable
def p_tipo_variable(p):
    '''tipo_variable : VAR
                    | LET
                    | CONST'''

#Datos booleanos
def p_booleano_tipo(p):
    '''booleano_tipo : TRUE
                    | FALSE'''


# HAcer uso de cadena de caracteres
def p_cadenas_caracteres(p):
    '''cadenas_caracteres : CADENA'''

#yonkani

#Daniela
def p_FUNCTIONS(p):
    ''' FUNCTIONS : FUNCTION VARIABLE LPAREN MASPARAMETROS RPAREN ILLAVE DLLAVE
    '''
    p[0] = ('FUNCTION')


def p_MASPARAMETROS(p):
    '''MASPARAMETROS : PARAMETROS
                    | PARAMETROS COMA MASPARAMETROS
    '''
    p[0] = 'MASPARAMETROS'

def p_PARAMETROS(p):

    '''PARAMETROS :  tipos_datos
                    | VARIABLE
    '''
    p[0] = 'PARAMETROS'




#Daniela

#David

#David


def p_error(p):
    print("Syntax error in input", p)


# Build the parser
parser = yacc.yacc()
###



while True:
    try:
        s = input('parser > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)


def analizador_sintactico(data):
    result = parser.parse(data)
    return result
