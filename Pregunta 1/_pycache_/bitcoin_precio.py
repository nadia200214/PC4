import requests

def obtener_precio_bitcoin():
    """Obtiene el precio actual del Bitcoin desde la API de CoinDesk."""
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # El precio viene en formato con comas, se necesita eliminar las comas antes de convertir a float
        precio_btc_usd = float(data['bpi']['USD']['rate'].replace(',', ''))
        return precio_btc_usd
    except requests.RequestException as e:
        print(f"Error al hacer la petición a la API: {e}")
        return None

def calcular_valor_bitcoins(n, precio_btc):
    """Calcula el valor en USD de 'n' Bitcoins."""
    return n * precio_btc