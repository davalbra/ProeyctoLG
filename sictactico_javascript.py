from ejemplo import tokens

import ply.yacc as yacc

#yonkani

def p_expresion(p):
    '''expresion : asignar_variable'''

def p_asigar_variable(p):
    '''asignar_variable : tipo_variable VARIABLE ASIGNAR tipos_datos'''

def p_tipos_datos(p):
    '''tipos_datos : booleano_tipo
                    | STRING
                    | NUMBER
                    | FLOTANTE
                    | NULL'''



def p_tipo_variable(p):
    '''tipo_variable : VAR
                    | LET
                    | CONST'''

def p_booleano_tipo(p):
    '''booleano_tipo : TRUE
                    | FALSE'''
def p_cadenas_caracteres(p):
    '''cadenas_caracteres : STRING'''

#yonkani

#Daniela

#Daniela

#David
def p_OPERATOR_MAT(p):
    '''OPERATOR_MAT : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE
                    | EXPONENTIATION
    '''
    p[0] = ('OPERADOR_MATEMATICO', p[1])
#David



def p_expression_minus(p):
    "expression_mas : NUMBER MINUS NUMBER"
    p[0] = p[1] - p[3]





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
