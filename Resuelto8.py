import sqlite3

def crear_tabla_bitcoin():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bitcoin (
            fecha TEXT PRIMARY KEY,
            precio_usd REAL,
            precio_gbp REAL,
            precio_eur REAL,
            precio_pen REAL
        )
    ''')
    conn.commit()
    conn.close()

crear_tabla_bitcoin()

import requests
import datetime

def obtener_precio_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        precios = {
            'USD': data['bpi']['USD']['rate_float'],
            'GBP': data['bpi']['GBP']['rate_float'],
            'EUR': data['bpi']['EUR']['rate_float']
        }
        return precios
    else:
        return None

def obtener_tipo_cambio_pen(fecha):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT venta FROM sunat_info WHERE fecha = ?', (fecha,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def almacenar_datos_bitcoin(fecha, precios, tipo_cambio_pen):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    precios['PEN'] = precios['USD'] * tipo_cambio_pen
    cursor.execute('INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen) VALUES (?, ?, ?, ?, ?)',
                   (fecha, precios['USD'], precios['GBP'], precios['EUR'], precios['PEN']))
    conn.commit()
    conn.close()

fecha_actual = datetime.date.today().strftime("%Y-%m-%d")
precios = obtener_precio_bitcoin()
tipo_cambio_pen = obtener_tipo_cambio_pen(fecha_actual)

if precios and tipo_cambio_pen:
    almacenar_datos_bitcoin(fecha_actual, precios, tipo_cambio_pen)
