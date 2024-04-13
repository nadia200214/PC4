import sqlite3
import requests

def obtener_datos_sunat(mes, anio):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year={anio}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al obtener los datos:", response.status_code)
        return []

def crear_base_datos():
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT,
            compra REAL,
            venta REAL
        );
    """)
    conexion.commit()
    conexion.close()

def almacenar_datos(datos):
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    for registro in datos:
        cursor.execute("""
            INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)
        """, (registro['fecha'], registro['compra'], registro['venta']))
    conexion.commit()
    conexion.close()

def mostrar_datos():
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM sunat_info")
    registros = cursor.fetchall()
    conexion.close()
    return registros

def main():
    # Crear la base de datos
    crear_base_datos()
    
    # API de SUNAT
    datos = obtener_datos_sunat(3, 2023)
    if datos:
        # Almacenar los datos
        almacenar_datos(datos)
    
    # Mostrar los datos 
    registros = mostrar_datos()
    for registro in registros:
        print(registro)

if __name__ == "__main__":
    main()