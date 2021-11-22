from ejemplo import tokens

import ply.yacc as yacc

#yonkani

#yonkani

#Daniela

#Daniela

#David

#David



def p_expression_mas(p):
    "expression_mas : NUMBER MAS NUMBER"
    p[0] = p[1] + p[3]

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
