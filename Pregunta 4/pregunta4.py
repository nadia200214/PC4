import requests
import datetime

def obtener_datos_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error al hacer la petición a la API: {e}")
        return None

def almacenar_datos_bitcoin(data):
    
    fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    precio_btc_usd = data['bpi']['USD']['rate_float']
    fecha_actualizacion = data['time']['updated']
    disclaimer = data['disclaimer']
    codigo = data['bpi']['USD']['code']
    descripcion = data['bpi']['USD']['description']

    contenido = (
        f"Registro obtenido el {fecha_hora_actual}:\n"
        f"Fecha de Actualización: {fecha_actualizacion}\n"
        f"Descripción: {descripcion} ({codigo})\n"
        f"Precio de Bitcoin: ${precio_btc_usd}\n"
        f"Disclaimer: {disclaimer}\n\n"
    )
    
    with open("datos_bitcoin.txt", "a") as archivo:
        archivo.write(contenido)
        print("Datos almacenados correctamente.")

datos_bitcoin = obtener_datos_bitcoin()
if datos_bitcoin is not None:
    almacenar_datos_bitcoin(datos_bitcoin)