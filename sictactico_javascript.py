from ejemplo import tokens

import ply.yacc as yacc

#yonkani

def p_expresion(p):
    '''expresion : asignar_variable
                | FUNCTIONS
    '''


def p_asigar_variable(p):
    '''asignar_variable : tipo_variable VARIABLE ASIGNAR tipos_datos'''

def p_tipos_datos(p):
    '''tipos_datos : booleano_tipo
                    | CADENA
                    | NUMERO
                    | NULL'''



def p_tipo_variable(p):
    '''tipo_variable : VAR
                    | LET
                    | CONST'''

def p_booleano_tipo(p):
    '''booleano_tipo : TRUE
                    | FALSE'''
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
