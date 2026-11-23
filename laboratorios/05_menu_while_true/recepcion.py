# Archivo: recepcion.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Recibir bicicletas y cotizar mano de obra en un menú repetitivo.

TARIFA_HORA = 12.0
recibidas = 0
while True:
    print("\nRECEPCIÓN · RUEDA LIBRE")
    print("1. Recibir bicicleta\n2. Ver horario\n3. Cotizar mano de obra\n0. Cerrar recepción")
    opcion = input("Opción: ").strip()
    if opcion == "1":
        cliente = input("Nombre del cliente: ").strip()
        if not cliente:
            print("El nombre no puede quedar vacío.")
            continue
        recibidas += 1
        print(f"Bicicleta #{recibidas} recibida a nombre de {cliente}.")
    elif opcion == "2":
        print("Lunes a viernes de 8:00 a 17:00. Sábado de 8:00 a 12:00.")
    elif opcion == "3":
        texto = input("Minutos de trabajo estimados: ").strip()
        if not texto.isdecimal():
            print("Escriba los minutos con números enteros.")
            continue
        minutos = int(texto)
        costo = minutos * TARIFA_HORA / 60
        print(f"Trabajo de {minutos // 60} h {minutos % 60} min. Mano de obra: ${costo:.2f}")
    elif opcion == "0":
        if input("¿Cerrar la recepción? (s/n): ").strip().lower() == "s":
            print(f"Recepción cerrada. Bicicletas recibidas hoy: {recibidas}.")
            break
    else:
        print("Opción no válida.")
