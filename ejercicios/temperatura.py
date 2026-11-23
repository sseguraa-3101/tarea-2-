# Archivo: temperatura.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Determinar cuántos aumentos fijos hacen falta para alcanzar una temperatura mínima y mostrar cada lectura.

from decimal import Decimal
from math import isfinite

# Entrada y validación. Una configuración inválida termina la sesión.
try:
    temperatura_inicial = float(input("Temperatura inicial (°C): "))
    objetivo = float(input("Temperatura objetivo (°C): "))
    incremento = float(input("Incremento por ciclo (°C): "))
except ValueError:
    print("Error: ingrese temperaturas y un incremento numéricos finitos.")
else:
    if not (isfinite(temperatura_inicial) and isfinite(objetivo) and isfinite(incremento)):
        print("Error: ingrese temperaturas y un incremento numéricos finitos.")
    elif objetivo <= temperatura_inicial:
        print("Error: el objetivo debe ser mayor que la temperatura inicial.")
    elif incremento <= 0:
        print("Error: el incremento debe ser mayor que cero.")
    else:
        temperatura_actual = temperatura_inicial
        ciclos = 0

        # La suma decimal evita agregar un ciclo de más al trabajar con décimas.
        while temperatura_actual < objetivo:
            siguiente = float(Decimal(str(temperatura_actual)) + Decimal(str(incremento)))
            if not isfinite(siguiente) or siguiente <= temperatura_actual:
                print("Error: el incremento excede la precisión numérica disponible.")
                break
            temperatura_actual = siguiente
            ciclos += 1
            print(f"Ciclo {ciclos}: {temperatura_actual} °C")
        else:
            # Solo se informa éxito cuando la temperatura alcanzó el objetivo.
            print(f"Temperatura alcanzada: {temperatura_actual} °C")
            print(f"Ciclos totales: {ciclos}")
