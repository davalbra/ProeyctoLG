from ejemplo import tokens

import ply.yacc as yacc


#BRAVO
def p_STATEMENT(p):
    ''' STATEMENT : EXPRESSION
    '''
    p[0] = ('P_STATEMENT', p[1])

def p_OPERATOR_MAT(p):
    '''OPERATOR_MAT : MAS
                    | MENOS
                    | MULTIPLICAR
                    | DIVIDIR
    '''
    p[0] = ('OPERADOR_MATEMATICO', p[1])

def p_EXPRESSION(p):
    '''EXPRESSION : asignar_variable
                | ESTRUCTURA_FOR
                | ESTRUCTURA_WHILE
                | grupo_datos
                | FUNCTIONS
                | declarar_variable
                | NUMERO
                | FLOTANTE
                | EXPRESSION_MAT
                | EXPRESSION_CONDICION_BOOLEANA
                | metodos_estructuras
                | PRINT
                | LEER
                | ESTRUCTURA_DOWHILE
                | EXPRESSION
                | CONDICION_IF

    '''
    p[0] = ('EXPRESSION', p[1])

def p_EXPRESSION_MAT(p):
    ''' EXPRESSION_MAT : EXPRESSION_MAT_OPTIONS

        EXPRESSION_MAT_OPTIONS : EXPRESSION_MAT_NUMERO
                      | EXPRESSION_MAT_FLOTANTE

        EXPRESSION_MAT_NUMERO : EXPRESSION_MAT_NUMERO OPERATOR_MAT EXPRESSION_MAT_NUMERO
                      | EXPRESSION_MAT_NUMERO OPERATOR_MAT NUMERO
                      | LPAREN EXPRESSION_MAT_NUMERO RPAREN
                      | NUMERO OPERATOR_MAT NUMERO
                      | VARIABLE OPERATOR_MAT VARIABLE
                      | VARIABLE OPERATOR_MAT NUMERO
                      | NUMERO OPERATOR_MAT VARIABLE

        EXPRESSION_MAT_FLOTANTE : EXPRESSION_MAT_FLOTANTE OPERATOR_MAT EXPRESSION_MAT_FLOTANTE
                      | EXPRESSION_MAT_FLOTANTE OPERATOR_MAT FLOTANTE
                      | FLOTANTE OPERATOR_MAT FLOTANTE
                      | LPAREN EXPRESSION_MAT_FLOTANTE RPAREN
                      | VARIABLE OPERATOR_MAT VARIABLE
                      | VARIABLE OPERATOR_MAT FLOTANTE
                      | FLOTANTE OPERATOR_MAT VARIABLE
    '''
    p[0] = ('EXPRESSION_MATEMATICA')


def p_EXPRESSION_CONDICION_BOOLEANA(p):
    ''' EXPRESSION_CONDICION_BOOLEANA : COMPARACION OPERATOR_COMP_MAT COMPARACION
                                        | COMPARACION_LOGICA OPERATOR_COMP_LOGICO COMPARACION_LOGICA


    '''
    p[0] = "EXPRESSION_COMP_BOOLEAN"
def p_COMPARACION(p):
    '''COMPARACION : VARIABLE
                    | BOOLEANO
    '''
    p[0] = ('OPERADOR_COMPARACION', p[1])

def p_COMPARACION_LOGICA(p):
    '''COMPARACION_LOGICA : VARIABLE
                            | NUMERO
    '''

    p[0] = ('COMPARACIO_LOGICA', p[1])

def p_OPERATOR_COMP_LOGICO(p):
    '''OPERATOR_COMP_LOGICO : IGUALDADESTRICTA
                    | MAYORIGUAL
                    | MENORIGUAL
                    | MENOR_QUE
                    | MAYOR_QUE
                    | NOESIGUAL'''
    p[0] = ('OPERATOR_COMP_LOGICO', p[1])

#se usa para la funcion p_EXPRESSION_CONDICION_BOOLEANA lo usa para comparar
def p_OPERATOR_COMP_MAT(p):
    '''OPERATOR_COMP_MAT : IGUALDADESTRICTA
                    | AND
                    | OR
                    | NOESIGUAL
    '''
    p[0] = ('OPERADOR_MATEMATICO_COMPARACION', p[1])

#Nos permite agrupar
def p_grupo_datos(p):
    '''grupo_datos : tipos_datos
                    | tipos_datos COMA grupo_datos'''
    p[0] = ('grupo_datos', p[1])



# Funcion que permite declarar variables con su tipo de dato respectivo
#Tambien permite asignar a una variable otra variable
#Permite asignar a una variable ya creada otro tipo de dato
#Permite declarar las instancias de las estructuras Set y Map

def p_asignar_variable(p):
    '''asignar_variable : declarar_variable ASIGNAR tipos_datos PUNTOCOMA
                        | VARIABLE ASIGNAR VARIABLE PUNTOCOMA
                        | VARIABLE ASIGNAR tipos_datos PUNTOCOMA
                        | declarar_variable ASIGNAR iniciar_estructuras
                        | declarar_variable ASIGNAR iniciar_array
                        | declarar_variable ASIGNAR LEER
                        '''
    p[0] = ('p_asignar_variable', p[1])
#Funcion para inicializar variables
def p_declarar_variable(p):
    '''declarar_variable : tipo_variable VARIABLE PUNTOCOMA
                        | tipo_variable VARIABLE
                        '''
    p[0] = ('p_asignar_variable', p[1])

#Estructuras hace uso de metodos
#OJO por revisar
def p_metodos_estructuras(p):
    '''metodos_estructuras :  VARIABLE metodos_array
                            | VARIABLE metodos_set
                            | VARIABLE metodos_map'''
    p[0] = ('p_asignar_variable', p[1])

def p_metodos_array(p):
    '''metodos_array : METODO_POP_ARRAY LPAREN RPAREN PUNTOCOMA
                    | push_array'''
    p[0] = ('p_metodos_array', p[1])

def p_metodos_set(p):
    '''metodos_set : METODO_ADD_SET LPAREN MASPARAMETROS RPAREN PUNTOCOMA
                    | METODO_SIZE_SET PUNTOCOMA'''
    p[0] = ('p_metodos_set', p[1])

def p_metodos_map(p):
    '''metodos_map : METODO_SET LPAREN tipos_datos COMA tipos_datos RPAREN PUNTOCOMA
                    | METODO_HAS LPAREN tipos_datos RPAREN PUNTOCOMA'''
    p[0] = ('p_metodos_map', p[1])

#Instanciar las estructuras de datos Map y Set
def p_iniciar_estructuras(p):
    '''iniciar_estructuras : NEW VARIABLE LPAREN RPAREN PUNTOCOMA '''
    p[0] = ('p_iniciar_estructuras', p[1])



#Yonkani Cedeño
def p_variable_metodo(p):
    '''variable_metodo : tipo_variable VARIABLE ASIGNAR iniciar_numero PUNTOCOMA numero_iguales_array'''
    p[0] = ('p_variable_metodo', p[1])

def p_push_array(p):
    '''push_array : flotante_iguales_array
                    | numero_iguales_array
                    | bool_iguales_array'''
    p[0] = ('p_push_array', p[1])

def p_bool_iguales_array(p):
    '''bool_iguales_array : VARIABLE METODO_PUSH_ARRAY LPAREN repeticion_bool RPAREN PUNTOCOMA'''
    p[0] = ('p_bool_iguales_array', p[1])

def p_flotante_iguales_array(p):
    '''flotante_iguales_array : VARIABLE METODO_PUSH_ARRAY LPAREN repeticion_flotante RPAREN PUNTOCOMA'''
    p[0] = ('p_flotante_iguales_array', p[1])

def p_numero_iguales_array(p):
    '''numero_iguales_array : VARIABLE METODO_PUSH_ARRAY LPAREN repeticion_numero RPAREN PUNTOCOMA '''
    p[0] = ('p_numero_iguales_array', p[1])

def p_iniciar_numero(p):
    '''iniciar_numero : ICORCHETE repeticion_numero DCORCHETE '''
    p[0] = ('p_iniciar_numero', p[1])

def p_iniciar_flotante(p):
    '''iniciar_flotante : ICORCHETE repeticion_flotante DCORCHETE '''
    p[0] = ('p_iniciar_flotante', p[1])

def p_iniciar_bool(p):
    '''iniciar_bool : ICORCHETE repeticion_bool DCORCHETE '''
    p[0] = ('p_iniciar_bool', p[1])


#Fin

# Aqui se declarar los tipos de datos
def p_tipos_datos(p):
    '''tipos_datos : booleano_tipo
                    | NUMERO
                    | CADENA
                    | FLOTANTE
                    | NULL'''
    p[0] = ('p_tipos_datos', p[1])




#Para declarar el tipo de variable
def p_tipo_variable(p):
    '''tipo_variable : VAR
                    | LET
                    | CONST'''
    p[0] = ('p_tipo_variable', p[1])

#Declarar un array
def p_iniciar_array(p):
   '''iniciar_array : ICORCHETE DCORCHETE
                    | ICORCHETE repeticion_bool DCORCHETE
                    | ICORCHETE repeticion_flotante DCORCHETE
                    | ICORCHETE repeticion_null DCORCHETE
                    | ICORCHETE repeticion_cadena DCORCHETE
                    | ICORCHETE repeticion_numero DCORCHETE

                    '''


   p[0] = ('p_iniciar_array', p[1])


def p_repeticion_flotante(p):
    '''repeticion_flotante : FLOTANTE
                            | repeticion_flotante COMA FLOTANTE'''

def p_repeticion_null(p):
    '''repeticion_null : NULL
                        | repeticion_null COMA NULL'''

def p_repeticion_cadena(p):
    '''repeticion_cadena : CADENA
                            | repeticion_cadena COMA CADENA'''

def p_repeticion_numero(p):
    '''repeticion_numero : NUMERO
                            | repeticion_numero COMA NUMERO'''

def p_repeticion_bool(p):
    '''repeticion_bool : booleano_tipo
                        | repeticion_bool COMA booleano_tipo'''

#Datos booleanos
def p_booleano_tipo(p):
    '''booleano_tipo : TRUE
                    | FALSE'''


# HAcer uso de cadena de caracteres
def p_cadenas_caracteres(p):
    '''cadenas_caracteres : CADENA'''
    p[0] = ('p_cadenas_caracteres', p[1])

#yonkani

#Daniela
def p_FUNCTIONS(p):
    ''' FUNCTIONS : FUNCTION VARIABLE LPAREN MASPARAMETROS RPAREN ILLAVE EXPRESSION DLLAVE
                  | FUNCTION VARIABLE LPAREN MASPARAMETROS RPAREN ILLAVE EXPRESSION RETURN MASPARAMETROS DLLAVE
                  | FUNCTION VARIABLE LPAREN RPAREN ILLAVE EXPRESSION DLLAVE
    '''
    p[0] = ('p_FUNCTIONS', p[1])


def p_MASPARAMETROS(p):
    '''MASPARAMETROS : PARAMETROS
                    | PARAMETROS COMA MASPARAMETROS
    '''
    p[0] = ('p_MASPARAMETROS', p[1])


def p_PARAMETROS(p):

    '''PARAMETROS :  tipos_datos
                    | VARIABLE
    '''
    p[0] = ('p_PARAMETROS', p[1])


def p_PRINT(p):
    ''' PRINT : ALERT LPAREN CADENA RPAREN

    '''
    p[0] = ('p_PRINT', p[1])


def p_READ(p):
    '''LEER : REQUIRED LPAREN CADENA RPAREN'''
    p[0] = ('p_READ', p[1])
#Daniela

#David

def p_ESTRUCTURA_FOR(p):
    '''ESTRUCTURA_FOR : FOR LPAREN asignar_variable EXPRESSION_CONDICION_BOOLEANA PUNTOCOMA VARIABLE MAS MAS RPAREN ILLAVE EXPRESSION DLLAVE
    '''
    p[0] = ('ESTRUCTURA_FOR', p[1])
def p_CONDICION_IF(p):
    '''CONDICION_IF : IF LPAREN EXPRESSION_CONDICION_BOOLEANA RPAREN ILLAVE EXPRESSION DLLAVE'''
    p[0] = ('ESTRUCTURA_IF', p[1])

def p_ESTRUCTURA_DOWHILE(p):
    '''ESTRUCTURA_DOWHILE : DO ILLAVE EXPRESSION DLLAVE WHILE LPAREN EXPRESSION_CONDICION_BOOLEANA RPAREN PUNTOCOMA '''
    p[0] = ('ESTRUCTURA_DOWHILE', p[1])
def p_ESTRUCTURA_WHILE(p):
    '''ESTRUCTURA_WHILE : WHILE LPAREN EXPRESSION_CONDICION_BOOLEANA RPAREN ILLAVE EXPRESSION DLLAVE

    '''
    p[0] = ('ESTRUCTURA_WHILE', p[1])
#David


def p_error(p):
    print("Syntax error in input", p)


# Build the parser
parser = yacc.yacc()
###



def sintaxis():
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
