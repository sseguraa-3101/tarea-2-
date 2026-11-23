# Archivo: estacionamiento.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Registrar ingresos y salidas de vehículos, facturar horas enteras y consultar la ocupación y la recaudación de la sesión.

CAPACIDAD = 20
TARIFA = 800

ocupados = 0
salidas = 0
recaudacion = 0

# El menú conserva el estado de la sesión entre operaciones.
while True:
    print("\n1. Registrar ingreso\n2. Registrar salida\n3. Consultar ocupación")
    print("4. Consultar recaudación\n5. Salir")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        if ocupados < CAPACIDAD:
            ocupados += 1
            print("Ingreso registrado.")
        else:
            print("Estacionamiento lleno. Ingreso rechazado.")
    elif opcion == "2":
        if ocupados == 0:
            print("Estacionamiento vacío. No hay salidas por registrar.")
        else:
            while True:
                try:
                    horas = int(input("Horas enteras por cobrar: "))
                except ValueError:
                    horas = 0
                if horas > 0:
                    break
                print("Horas inválidas: ingrese un entero mayor que cero.")

            # Actualizar las tres cifras solo después de validar las horas.
            pago = horas * TARIFA
            ocupados -= 1
            salidas += 1
            recaudacion += pago
            print(f"Salida registrada. Pago: ₡{pago}")
    elif opcion == "3":
        print(f"Ocupados: {ocupados} | Libres: {CAPACIDAD - ocupados}")
    elif opcion == "4":
        print(f"Recaudación: ₡{recaudacion} | Salidas: {salidas}")
    elif opcion == "5":
        print(f"Resumen final | Ocupados: {ocupados} | Salidas: {salidas} | Recaudación: ₡{recaudacion}")
        break
    else:
        print("Opción inválida. Seleccione del 1 al 5.")
