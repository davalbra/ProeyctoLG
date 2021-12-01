def verificarCodigo(codigo_area):
    texto = codigo_area.get("1.0", 'end-1c')

    if texto == "":
        return False
    else:
        guardarArchivo(texto)

        return True

def guardarArchivo(txt):
    file = open("prueba_lexica.txt", "w")
    linea = ""
    for caracter in txt:
        linea += caracter
    file.write(linea)
    file.close
