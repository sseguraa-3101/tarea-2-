# Archivo: consumo_agua.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Resumir siete lecturas diarias en litros con un acumulador, un máximo y un contador de días sobre el umbral.

from math import isfinite

DIAS = 7
UMBRAL = 150

total = 0.0
mayor = 0.0
dias_sobre_umbral = 0

# El for avanza únicamente después de aceptar la lectura de la jornada.
for dia in range(1, DIAS + 1):
    while True:
        try:
            consumo = float(input(f"Día {dia} | consumo de agua (L): "))
        except ValueError:
            consumo = -1.0
        if isfinite(consumo) and consumo >= 0:
            break
        print("Consumo inválido: ingrese un número finito mayor o igual que cero.")

    # El mayor puede comenzar en cero porque todos los consumos son no negativos.
    total += consumo
    if consumo > mayor:
        mayor = consumo
    if consumo > UMBRAL:
        dias_sobre_umbral += 1

# Salida semanal. El promedio incluye también los días con consumo cero.
promedio = total / DIAS
print(f"Total semanal: {total:.2f} L")
print(f"Promedio diario: {promedio:.2f} L/día")
print(f"Mayor consumo: {mayor:.2f} L")
print(f"Días con más de {UMBRAL} L: {dias_sobre_umbral}")
