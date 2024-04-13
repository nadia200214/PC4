def contar_lineas_codigo_efectivas(archivo):
    try:
        total_lineas = 0
        with open(archivo, 'r') as file:
            for linea in file:
                # Elimina los espacios en blanco y verifica si es una línea de comentario o vacía
                linea_limpiada = linea.strip()
                if linea_limpiada and not linea_limpiada.startswith('#'):
                    total_lineas += 1
        return total_lineas
    except FileNotFoundError:
        print("El archivo no fue encontrado. Asegúrese de que la ruta sea correcta.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def main():

    ruta_archivo = './pregunta6/hello.py'  
    lineas_codigo = contar_lineas_codigo_efectivas(ruta_archivo)
    if lineas_codigo is not None:
        print(f"El número de líneas de código efectivas en '{ruta_archivo}' es: {lineas_codigo}")

if __name__ == "__main__":
    main()