# Archivo: expedicion.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 22 de noviembre de 2026
# Versión: 1.1
# Propósito: Simular el consumo de agua y alimento durante un plan de 1 a 30 jornadas y determinar cuántas se pueden completar.

from decimal import Decimal

AGUA_INICIAL = 150
ALIMENTO_INICIAL = 100
MAX_DIAS = 30

# Entrada del plan. Solo se aceptan jornadas enteras en el intervalo.
while True:
    try:
        jornadas = int(input(f"Jornadas previstas (1 a {MAX_DIAS}): "))
    except ValueError:
        jornadas = 0
    if 1 <= jornadas <= MAX_DIAS:
        break
    print(f"Duración inválida. Ingrese un entero entre 1 y {MAX_DIAS}.")

agua = float(AGUA_INICIAL)
alimento = float(ALIMENTO_INICIAL)
total_agua = 0.0
total_alimento = 0.0
completadas = 0

for dia in range(1, jornadas + 1):
    if agua == 0 or alimento == 0:
        break
    print(f"Jornada {dia} | Disponibles: {agua} L y {alimento} unid.")

    # Validar ambos consumos antes de descontar cualquier recurso.
    while True:
        try:
            uso_agua = float(input("Agua consumida (L): "))
        except ValueError:
            uso_agua = 0.0
        if 0 < uso_agua <= agua:
            break
        print(f"Agua inválida. Ingrese más de 0 y hasta {agua} L.")

    while True:
        try:
            uso_alimento = float(input("Alimento consumido (unid.): "))
        except ValueError:
            uso_alimento = 0.0
        if 0 < uso_alimento <= alimento:
            break
        print(f"Alimento inválido. Ingrese más de 0 y hasta {alimento} unid.")

    # Operar con la representación decimal evita residuos al agotar el saldo.
    agua = float(Decimal(str(agua)) - Decimal(str(uso_agua)))
    alimento = float(Decimal(str(alimento)) - Decimal(str(uso_alimento)))
    total_agua += uso_agua
    total_alimento += uso_alimento
    completadas += 1
    print(f"Saldo: {agua} L de agua | {alimento} unid. de alimento")

    if dia < jornadas and (agua == 0 or alimento == 0):
        break

# El plan siempre admite al menos una jornada con las existencias iniciales.
promedio_agua = total_agua / completadas
promedio_alimento = total_alimento / completadas
if completadas == jornadas:
    estado = "Completada"
elif agua == 0 and alimento == 0:
    estado = "Interrumpida por agotamiento de agua y alimento"
elif agua == 0:
    estado = "Interrumpida por agotamiento de agua"
else:
    estado = "Interrumpida por agotamiento de alimento"

print(f"Jornadas completadas: {completadas} de {jornadas}")
print(f"Consumo total: {total_agua:.2f} L de agua | {total_alimento:.2f} unid. de alimento")
print(f"Inventario final: {agua} L de agua | {alimento} unid. de alimento")
print(f"Promedio diario: {promedio_agua:.2f} L de agua | {promedio_alimento:.2f} unid. de alimento")
print(f"Estado: {estado}")
