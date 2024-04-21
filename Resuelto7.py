import sqlite3
import requests
from datetime import date, timedelta

def crear_base_datos():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT PRIMARY KEY,
            compra REAL,
            venta REAL
        )
    ''')
    conn.commit()
    conn.close()

def obtener_datos_api(api_key, fecha):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha={fecha}"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return (data['fecha'], data['compra'], data['venta'])
    else:
        return None

def almacenar_datos(fecha, compra, venta):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)',
                   (fecha, compra, venta))
    conn.commit()
    conn.close()

def mostrar_datos():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sunat_info')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def main(api_key):
    crear_base_datos()
    start_date = date(2023, 1, 1)
    end_date = date(2023, 12, 31)
    delta = timedelta(days=1)

    while start_date <= end_date:
        fecha = start_date.strftime("%Y-%m-%d")
        resultado = obtener_datos_api(api_key, fecha)
        if resultado:
            almacenar_datos(*resultado)
        start_date += delta

    mostrar_datos()

if __name__ == "__main__":
    api_key = input("Ingrese su API Key de apis.net.pe: ")
    main(api_key)
