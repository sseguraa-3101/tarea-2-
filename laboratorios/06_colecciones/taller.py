# Archivo: taller.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Registrar servicios, controlar inventario y cobrar órdenes entregadas.

SERVICIOS = {
    "FR": ("Ajuste de frenos", 8.00, "pastillas"),
    "CA": ("Cambio de cadena", 15.00, "cadena"),
    "PA": ("Parchado de llanta", 5.00, "parche"),
    "MG": ("Mantenimiento general", 35.00, None),
}
inventario = {"pastillas": 4, "cadena": 2, "parche": 10}
ordenes = []
while True:
    print("\nTALLER RUEDA LIBRE\n1. Catálogo\n2. Registrar orden\n3. Pendientes")
    print("4. Entregar orden\n5. Ver inventario\n6. Reporte del día\n0. Salir")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        for codigo, (nombre, precio, repuesto) in SERVICIOS.items():
            print(f"{codigo}  {nombre:<24} ${precio:6.2f}")
    elif opcion == "2":
        cliente = input("Nombre del cliente: ").strip()
        codigos = []
        total = 0.0
        while True:
            codigo = input("Servicio (FIN para terminar): ").strip().upper()
            if codigo == "FIN":
                break
            if codigo not in SERVICIOS:
                print("Código no existe.")
                continue
            nombre, precio, repuesto = SERVICIOS[codigo]
            if repuesto is not None:
                if inventario[repuesto] == 0:
                    print(f"Sin {repuesto} en bodega. No se puede agregar.")
                    continue
                inventario[repuesto] -= 1
            codigos.append(codigo)
            total += precio
            print(f"+ {nombre} (${precio:.2f})")
        if codigos:
            numero = len(ordenes) + 1
            ordenes.append({"numero": numero, "cliente": cliente, "servicios": codigos,
                            "total": total, "estado": "pendiente"})
            print(f"Orden #{numero} registrada. Total: ${total:.2f}")
        else:
            print("Orden cancelada: no tiene servicios.")
    elif opcion == "3":
        hay_pendientes = False
        for orden in ordenes:
            if orden["estado"] == "pendiente":
                hay_pendientes = True
                print(f"#{orden['numero']} {orden['cliente']} | {', '.join(orden['servicios'])} | ${orden['total']:.2f}")
        if not hay_pendientes:
            print("No hay órdenes pendientes.")
    elif opcion == "4":
        texto = input("Número de orden: ").strip()
        if not texto.isdecimal():
            print("Escriba un número.")
            continue
        for orden in ordenes:
            if orden["numero"] == int(texto):
                if orden["estado"] == "entregada":
                    print("Esa orden ya fue entregada.")
                else:
                    orden["estado"] = "entregada"
                    print(f"Orden #{texto} entregada a {orden['cliente']}. Cobrar ${orden['total']:.2f}")
                break
        else:
            print("No existe esa orden.")
    elif opcion == "5":
        for repuesto, unidades in inventario.items():
            aviso = " <- reabastecer" if unidades <= 1 else ""
            print(f"{repuesto}: {unidades}{aviso}")
    elif opcion == "6":
        frecuencia = {}
        ingresos = 0.0
        entregadas = 0
        for orden in ordenes:
            if orden["estado"] == "entregada":
                entregadas += 1
                ingresos += orden["total"]
            for codigo in orden["servicios"]:
                frecuencia[codigo] = frecuencia.get(codigo, 0) + 1
        print(f"Órdenes registradas: {len(ordenes)} | Órdenes entregadas: {entregadas}")
        print(f"Ingresos cobrados: ${ingresos:.2f}")
        veces = 0
        for codigo, cantidad in frecuencia.items():
            if cantidad > veces:
                mas_pedido = codigo
                veces = cantidad
        if veces:
            print(f"Servicio más pedido: {SERVICIOS[mas_pedido][0]} ({veces} veces)")
    elif opcion == "0":
        print("Hasta luego.")
        break
    else:
        print("Opción no válida.")
