import sys
# Función para verificar argumentos
def type_argv():
    """
    "if" Verifica si se han proporcionado argumentos en la línea de comandos.
    "else" Obtiene los argumentos de la línea de comandos
    """
    if len(sys.argv) < 2:
        args = input().split()
        if not args:
            print("ERROR ARGV: Enter an argument")
            return
    else:
        args = sys.argv[1:]

    # Procesa cada argumento
    for arg in args:
        try:
            print(f"int: {int(arg)}")
        except ValueError:
            print(f"ERROR ARGV: {arg} is not INT")
            return

# Ejecuta la función principal
if __name__ == "__main__":
    type_argv()