import bitcoin_precio

def main():
    try:
        n = float(input("Ingrese la cantidad de bitcoins que posee: "))
        precio_btc = bitcoin_precio.obtener_precio_bitcoin()
        if precio_btc is not None:
            valor_total_usd = bitcoin_precio.calcular_valor_bitcoins(n, precio_btc)
            print(f"El valor actual de sus {n} Bitcoins es: ${valor_total_usd:,.4f} USD")
    except ValueError:
        print("Error: Por favor, ingrese un número válido para la cantidad de bitcoins.")

if __name__ == "__main__":
    main()