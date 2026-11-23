# Archivo: bodega.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Administrar existencias, precios y pedidos de repuestos.

STOCK_MINIMO = 2
inventario = {"cadena": 2, "parche": 10, "pastillas": 4, "camara": 3}
precios = {"cadena": 15.00, "parche": 0.50, "pastillas": 6.00, "camara": 7.50}
while True:
    print("\nBODEGA\n1. Inventario\n2. Consultar\n3. Usar\n4. Recibir pedido")
    print("5. Agregar repuesto\n6. Descontinuar\n7. Actualizar precios\n8. Valor total\n0. Salir")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        for nombre, stock in inventario.items():
            aviso = " <- pedir más" if stock <= STOCK_MINIMO else ""
            print(f"{nombre}: {stock}{aviso}")
        print(f"Repuestos distintos: {len(inventario)}")
    elif opcion in ("2", "3", "6"):
        nombre = input("Repuesto: ").strip().lower()
        if nombre not in inventario:
            print("Ese repuesto no existe. Registrados:", ", ".join(inventario.keys()))
        elif opcion == "2":
            print(f"{nombre}: {inventario[nombre]} unidades a ${precios[nombre]:.2f}")
        elif opcion == "6":
            stock = inventario.pop(nombre)
            precios.pop(nombre, None)
            print(f"{nombre} eliminado. Tenía {stock} unidades.")
        else:
            texto = input("Unidades usadas: ").strip()
            if not texto.isdecimal():
                print("Ingrese un entero no negativo.")
            elif int(texto) > inventario[nombre]:
                print(f"Solo hay {inventario[nombre]} unidades.")
            else:
                inventario[nombre] -= int(texto)
                print(f"Quedan {inventario[nombre]} unidades de {nombre}.")
    elif opcion == "4":
        pedido = {}
        while True:
            nombre = input("Repuesto recibido (FIN para terminar): ").strip().lower()
            if nombre == "fin":
                break
            texto = input("Unidades: ").strip()
            if nombre and texto.isdecimal():
                pedido[nombre] = pedido.get(nombre, 0) + int(texto)
            else:
                print("Ingrese un nombre y una cantidad entera no negativa.")
        for nombre, unidades in pedido.items():
            inventario[nombre] = inventario.get(nombre, 0) + unidades
            precios.setdefault(nombre, 0.0)
        print(f"Pedido registrado: {len(pedido)} repuesto(s) distinto(s).")
    elif opcion == "5":
        nombre = input("Repuesto nuevo: ").strip().lower()
        if not nombre or nombre in inventario:
            print("Se necesita un nombre nuevo.")
            continue
        unidades = int(input("Unidades iniciales: "))
        precio = float(input("Precio por unidad ($): "))
        if unidades >= 0 and precio >= 0:
            inventario[nombre] = unidades
            precios[nombre] = precio
            print(f"{nombre} agregado a la bodega.")
        else:
            print("El stock y el precio deben ser no negativos.")
    elif opcion == "7":
        cambios = {"cadena": 16.50, "camara": 8.00}
        precios.update(cambios)
        print("Precios actualizados:", ", ".join(cambios.keys()))
    elif opcion == "8":
        valor = 0.0
        for nombre, unidades in inventario.items():
            valor += unidades * precios[nombre]
        print(f"Valor de la bodega: ${valor:.2f}")
    elif opcion == "0":
        print("Bodega cerrada.")
        break
    else:
        print("Opción no válida.")
