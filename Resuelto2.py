import pyfiglet
import random

def main():
    # Lista de fuentes disponibles
    fuentes_disponibles = pyfiglet.FigletFont.getFonts()
    
    # Solicitar al usuario el nombre de una fuente
    nombre_fuente = input("Ingrese el nombre de la fuente o presione Enter para seleccionar una aleatoria: ")
    
    # Elegir una fuente aleatoriamente si no se proporciona una
    if not nombre_fuente:
        nombre_fuente = random.choice(fuentes_disponibles)
    
    # Verificar si la fuente ingresada es válida
    if nombre_fuente not in fuentes_disponibles:
        print("Fuente no disponible. Se seleccionará una fuente aleatoria.")
        nombre_fuente = random.choice(fuentes_disponibles)
    
    # Crear el objeto Figlet con la fuente seleccionada
    figlet = pyfiglet.Figlet(font=nombre_fuente)
    
    # Solicitar al usuario el texto a convertir
    texto = input("Ingrese el texto que desea convertir: ")
    
    # Generar y mostrar el texto en arte ASCII
    resultado = figlet.renderText(texto)
    print(resultado)

if __name__ == "__main__":
    main()
