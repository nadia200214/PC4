def generar_tabla_multiplicar(n):
    """Genera un archivo con la tabla de multiplicar del número n."""
    filename = f"tabla-{n}.txt"
    with open(filename, 'w') as file:
        for i in range(1, 11):
            file.write(f"{n} x {i} = {n*i}\n")
    print(f"Tabla de multiplicar del {n} guardada en '{filename}'.")

def leer_tabla_multiplicar(n):
    """Lee y muestra la tabla de multiplicar de n desde un archivo."""
    try:
        filename = f"tabla-{n}.txt"
        with open(filename, 'r') as file:
            print(f"Tabla de multiplicar del {n}:")
            print(file.read())
    except FileNotFoundError:
        print(f"El archivo '{filename}' no existe.")

def mostrar_linea_tabla_multiplicar(n, m):
    """Muestra la m-ésima línea del archivo de la tabla de multiplicar de n."""
    try:
        filename = f"tabla-{n}.txt"
        with open(filename, 'r') as file:
            lines = file.readlines()
            if m <= len(lines):
                print(lines[m-1].strip())
            else:
                print(f"La línea {m} no existe en el archivo.")
    except FileNotFoundError:
        print(f"El archivo '{filename}' no existe.")

def main():
    while True:
        print("\nOpciones:")
        print("1. Generar tabla de multiplicar")
        print("2. Leer tabla de multiplicar")
        print("3. Mostrar línea específica de la tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            n = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= n <= 10:
                generar_tabla_multiplicar(n)
            else:
                print("Número fuera de rango.")
        elif opcion == '2':
            n = int(input("Ingrese un número entre 1 y 10 para leer su tabla de multiplicar: "))
            if 1 <= n <= 10:
                leer_tabla_multiplicar(n)
            else:
                print("Número fuera de rango.")
        elif opcion == '3':
            n = int(input("Ingrese un número entre 1 y 10 para la tabla de multiplicar: "))
            m = int(input("Ingrese el número de línea a mostrar: "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                mostrar_linea_tabla_multiplicar(n, m)
            else:
                print("Número fuera de rango.")
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()