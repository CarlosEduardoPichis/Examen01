# Funcion para el desplazamiento
def cifrado_rot13(texto):
    """
    Definí los alfabetos en minúsculas y mayúsculas como cadenas de texto.
    Utilicé el método str.maketrans() para cada letra del alfabeto a su correspondiente desplazamiento de 13 posiciones.
    Retorno el método texto.translate() para aplicar la tabla de traducción al texto de entrada.
    """
    alfabeto_minusculas = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_mayusculas = alfabeto_minusculas.upper()
    tabla_traduccion = str.maketrans(alfabeto_minusculas + alfabeto_mayusculas, 
                                    alfabeto_minusculas[13:] + alfabeto_minusculas[:13] + 
                                    alfabeto_mayusculas[13:] + alfabeto_mayusculas[:13])
    return texto.translate(tabla_traduccion)

# Variable guarda lo ingresado y imprime la funcion con el resultado
texto = input("str_in: ")
print("str_out:", cifrado_rot13(texto))

