
while True:
    #Mensaje de Bienvenida
    print("============================================================")
    print("== Bienvenido a nuestro Programa para registrar productos ==")
    print("============================================================")

    try:
        #Solicitar nombre
        nombre = input("Colocar Nombre de producto: ")

        #Solicitar Precio
        precio = int(input("Colocar Precio Unitario de producto: "))

        #Solicitar Cantidad
        cantidad = int(input("Colocar Cantidad de producto: "))

        #Solicitar Costo
        Costo_Total = (precio * cantidad)

        #Mostrar en  pantalla
        print("")
        print(f"Nombre del producto: {nombre}")
        print(f"Precio Unitario del producto: {precio}")
        print(f"Cantidad: {cantidad}")
        print(f"Total: {Costo_Total}")
        print("")


    except:
        print("Valor no valido")

    #el prograa calcula y muestra el precio por producto