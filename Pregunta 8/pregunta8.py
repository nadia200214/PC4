import sqlite3
import requests
from datetime import datetime

def obtener_precio_bitcoin():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if response.status_code == 200:
        data = response.json()
        return {
            'USD': data['bpi']['USD']['rate_float'],
            'GBP': data['bpi']['GBP']['rate_float'],
            'EUR': data['bpi']['EUR']['rate_float']
        }
    else:
        print("Error al obtener los datos de Bitcoin:", response.status_code)
        return {}

def obtener_tipo_cambio_sunat():
    response = requests.get("https://api.apis.net.pe/v1/tipo-cambio-sunat")
    if response.status_code == 200:
        data = response.json()
        return data['venta']
    else:
        print("Error al obtener los datos del tipo de cambio:", response.status_code)
        return None

def crear_tabla_bitcoin():
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bitcoin (
            fecha TEXT,
            precio_usd REAL,
            precio_gbp REAL,
            precio_eur REAL,
            precio_pen REAL
        );
    """)
    conexion.commit()
    conexion.close()

def almacenar_precios_bitcoin(precios, tipo_cambio_pen):
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    precio_pen = precios['USD'] * tipo_cambio_pen
    
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen) VALUES (?, ?, ?, ?, ?)
    """, (fecha_actual, precios['USD'], precios['GBP'], precios['EUR'], precio_pen))
    conexion.commit()
    conexion.close()

def consultar_precios():
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT fecha, precio_pen, precio_eur FROM bitcoin")
    resultados = cursor.fetchall()
    conexion.close()
    
    for fecha, precio_pen, precio_eur in resultados:
        print(f"Fecha: {fecha}, Costo de 10 bitcoins en PEN: {precio_pen * 10}, en EUR: {precio_eur * 10}")

def main():
    crear_tabla_bitcoin()
    precios = obtener_precio_bitcoin()
    tipo_cambio_pen = obtener_tipo_cambio_sunat()
    if precios and tipo_cambio_pen:
        almacenar_precios_bitcoin(precios, tipo_cambio_pen)
    consultar_precios()

if __name__ == "__main__":
    main()