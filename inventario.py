# Colores para la terminal
verde = "\033[92m"
rojo = "\033[91m"
azul = "\033[94m"
amarillo = "\033[93m"
reset = "\033[0m"

while True:
    # Mensaje de Bienvenida
    print("")
    print(azul + "============================================================")
    print("== Bienvenido a nuestro Programa para registrar productos ==")
    print("============================================================" + reset)
    print("")

    try:
        # Solicitar nombre
        nombre = input(amarillo + "Colocar Nombre de producto: " + reset)

        # Solicitar Precio
        precio = int(input(amarillo + "Colocar Precio Unitario de producto: " + reset))

        # Solicitar Cantidad
        cantidad = int(input(amarillo + "Colocar Cantidad de producto: " + reset))

        # Calcular Costo
        Costo_Total = precio * cantidad

        # Mostrar resultados
        print("")
        print(verde + "=========== INFORMACIÓN DEL PRODUCTO ===========")
        print(f"Nombre del producto: {nombre}")
        print(f"Precio Unitario del producto: {precio}")
        print(f"Cantidad: {cantidad}")
        print(f"Total: {Costo_Total}")
        print("================================================" + reset)
        print("")

    except:
        print("")
        print(rojo + "Valor no valido" + reset)
        print("")


# Comentario del programa
# Este programa permite registrar productos desde la terminal.
# Solicita al usuario el nombre del producto, el precio unitario y la cantidad.
# Luego calcula el costo total multiplicando el precio por la cantidad.
# Finalmente muestra en pantalla la información del producto y el total.
# El programa se ejecuta en un ciclo infinito para permitir registrar varios productos.
# Si el usuario introduce un valor no válido, el programa muestra un mensaje de error.
