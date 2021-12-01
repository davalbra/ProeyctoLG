import tkinter
from tkinter import Tk

from ejemplo import lexer
from sictactico_javascript import parser
import Funciones as fnc

root = Tk()
root.title("Analizador Javascript")
#root.iconbitmap('C:\\Users\\EvilFourier\\Desktop\\Proyecto David\\ProeyctoLG\\javascript.ico')
root['bg'] = '#404254'
root.geometry("900x568")

def analizar(dato, result_text_area):
    lexer.input(dato)
    while True:
        tok = lexer.token()
        if not tok:
            break
        line = str(tok)+ "\n"
        result_text_area.insert(tkinter.INSERT, line)
        print(tok)



def analizadorLexico(result_text_area):
    result_text_area.delete("1.0", 'end-1c')
    archivo = open("prueba_lexica.txt", "r")
    for l in archivo:
        if len(l) == 0:
            break
        print(">>>" + l)
        analizar(l, result_text_area)


def analizadorSintactico(result_text_area):
    result_text_area.delete("1.0", 'end-1c')
    file = open("prueba_lexica.txt", "r")
    for l in file:
        if l != "\n":
            if l[:3] == "for" or l[:5] == "while" or l[:2] == "if":
                newL = l
                for line in file:
                    newL += " " + line
                    if line[:3] == "end":
                        break
                l = newL
            result = parser.parse(l)
            if result is not None:
                resultLinea = str(result) + "\n"
                result_text_area.insert(tkinter.INSERT, resultLinea)
            else:
                resultLinea = "Error de sintaxis \n"
                result_text_area.insert(tkinter.INSERT, resultLinea)


def lexico(codigo):
    if(fnc.verificarCodigo(codigo)):
        analizadorLexico(result_text_area)

def sintactico(codigo):
    if(fnc.verificarCodigo(codigo)):
        analizadorSintactico(result_text_area)

codigo = tkinter.Text(root, height=10, width=30,)
codigo.configure(relief = "sunken", borderwidth=5)
codigo.place(x=50, y=50, width=300, height=200)

lexic_button = tkinter.Button(root, text= "Lexico", padx=40, pady=30,
                              command= lambda: lexico(codigo))

lexic_button.place(x=300, y=300, width=100, height = 75)

sintactic_button = tkinter.Button(root, text="Sintáctico", padx=40, pady=30,
                                  command=lambda: sintactico(codigo))

sintactic_button.place(x=470, y=300, width=100, height = 75)

result_text_area = tkinter.Text(root, height=10, width=30)
result_text_area.configure(relief="sunken", borderwidth=5)
result_text_area.place(x=470, y=50, width=350, height=195)

root.mainloop()