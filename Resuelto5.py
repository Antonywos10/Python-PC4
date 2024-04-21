class TablaMultiplicar:
    def __init__(self, n):
        self.numero = n
        self.filename = f"tabla-{n}.txt"
    
    def generar_tabla(self):
        with open(self.filename, 'w') as file:
            for i in range(1, 11):
                file.write(f"{self.numero} x {i} = {self.numero * i}\n")
        print(f"Tabla de multiplicar del {self.numero} guardada en '{self.filename}'.")
    
    def mostrar_tabla(self):
        try:
            with open(self.filename, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print(f"El archivo '{self.filename}' no existe.")
    
    def mostrar_linea(self, m):
        try:
            with open(self.filename, 'r') as file:
                lineas = file.readlines()
                if m <= len(lineas):
                    print(lineas[m-1].strip())
                else:
                    print(f"No hay línea número {m} en el archivo.")
        except FileNotFoundError:
            print(f"El archivo '{self.filename}' no existe.")

def solicitar_numero(prompt):
    while True:
        try:
            numero = int(input(prompt))
            if 1 <= numero <= 10:
                return numero
            else:
                print("Por favor, ingrese un número entre 1 y 10.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def main():
    while True:
        print("\nMenú:")
        print("1. Generar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea específica de la tabla de multiplicar")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            n = solicitar_numero("Ingrese un número entre 1 y 10 para generar su tabla de multiplicar: ")
            tabla = TablaMultiplicar(n)
            tabla.generar_tabla()
        elif opcion == '2':
            n = solicitar_numero("Ingrese un número entre 1 y 10 para mostrar su tabla de multiplicar: ")
            tabla = TablaMultiplicar(n)
            tabla.mostrar_tabla()
        elif opcion == '3':
            n = solicitar_numero("Ingrese un número de tabla de multiplicar (1-10): ")
            m = solicitar_numero("Ingrese el número de línea que desea ver (1-10): ")
            tabla = TablaMultiplicar(n)
            tabla.mostrar_linea(m)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
