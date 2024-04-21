import requests
import datetime

def obtener_precio_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción para respuestas no exitosas
        data = respuesta.json()
        precio_bitcoin_usd = data['bpi']['USD']['rate_float']
        return precio_bitcoin_usd
    except requests.RequestException as e:
        print(f"Error al obtener el precio del Bitcoin: {e}")
        return None

def guardar_precio_bitcoin(precio):
    # Obtener la fecha y hora actual
    ahora = datetime.datetime.now()
    fecha_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")
    
    # Formatear el mensaje a guardar
    mensaje = f"Fecha y Hora: {fecha_hora}, Precio del Bitcoin (USD): {precio:.2f}\n"
    
    # Guardar el mensaje en un archivo
    with open("precio_bitcoin.txt", "a") as archivo:
        archivo.write(mensaje)
    print("Precio almacenado correctamente.")

def main():
    precio_bitcoin_usd = obtener_precio_bitcoin()
    if precio_bitcoin_usd is not None:
        guardar_precio_bitcoin(precio_bitcoin_usd)
    else:
        print("No fue posible obtener o almacenar el precio del Bitcoin.")

if __name__ == "__main__":
    main()
