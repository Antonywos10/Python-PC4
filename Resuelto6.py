def contar_lineas_codigo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        
        lineas_codigo = 0
        for linea in lineas:
            linea_limpia = linea.strip()
            # Considera línea de código si no está vacía y no es un comentario
            if linea_limpia and not linea_limpia.startswith('#'):
                lineas_codigo += 1
        
        return lineas_codigo
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    
    # Validar si la ruta termina en .py
    if not ruta_archivo.endswith('.py'):
        print("El archivo no es un archivo Python (.py).")
        return
    
    lineas_codigo = contar_lineas_codigo(ruta_archivo)
    if lineas_codigo is not None:
        print(f"El número de líneas de código en '{ruta_archivo}' es: {lineas_codigo}")

if __name__ == "__main__":
    main()
