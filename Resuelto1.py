import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        return float(data['bpi']['USD']['rate'].replace(',', ''))
    except requests.RequestException as e:
        print("Error al consultar el precio de Bitcoin:", e)
        return None

def main():
    cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
    precio_bitcoin = obtener_precio_bitcoin()

    if precio_bitcoin is not None:
        costo_en_usd = cantidad_bitcoins * precio_bitcoin
        print(f"El costo actual de {cantidad_bitcoins:.4f} Bitcoins es: ${costo_en_usd:,.4f}")

if __name__ == "__main__":
    main()
