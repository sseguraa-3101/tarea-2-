# Archivo: ahorro_cooperativa.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Proyectar un ahorro mensual con bonos, metas y comparación de tasas.

MESES_POR_ANO = 12
BONO_FIDELIDAD = 0.01
AUMENTO_DEPOSITO = 0.05

deposito = float(input("Depósito mensual ($): "))
meses = int(input("Plazo (meses): "))
while meses <= 0:
    meses = int(input("El plazo debe ser positivo. Plazo (meses): "))
tasa_anual = float(input("Tasa de interés anual (%): "))
meta = float(input("Meta de ahorro ($): "))
tasa_mensual = tasa_anual / 100 / MESES_POR_ANO

# El primer recorrido usa un depósito fijo. El segundo aplica el reto anual.
mes_meta_fijo = 0
for modo in range(2):
    saldo = 0.0
    total_depositado = 0.0
    intereses = 0.0
    bonos = 0.0
    mes_meta = 0
    aporte = deposito
    print("\nDepósito fijo" if modo == 0 else "\nDepósito creciente")
    print(f"{'Mes':>4} {'Depósito':>10} {'Interés':>9} {'Bono':>9} {'Saldo':>12}")
    for mes in range(1, meses + 1):
        if modo == 1 and mes > 1 and (mes - 1) % MESES_POR_ANO == 0:
            aporte *= 1 + AUMENTO_DEPOSITO
        saldo += aporte
        total_depositado += aporte
        interes = saldo * tasa_mensual
        saldo += interes
        intereses += interes
        bono = 0.0
        if mes % MESES_POR_ANO == 0:
            bono = saldo * BONO_FIDELIDAD
            bonos += bono
            saldo += bono
        if mes_meta == 0 and saldo >= meta:
            mes_meta = mes
        print(f"{mes:4} {aporte:10.2f} {interes:9.2f} {bono:9.2f} {saldo:12.2f}")
    print(f"Total depositado: ${total_depositado:,.2f}")
    print(f"Intereses ganados: ${intereses:,.2f}")
    print(f"Bonos recibidos: ${bonos:,.2f}")
    print(f"Saldo final: ${saldo:,.2f}")
    if mes_meta:
        print(f"La meta de ${meta:,.2f} se alcanza en el mes {mes_meta}.")
    else:
        print(f"Para alcanzar la meta faltan ${meta - saldo:,.2f}.")
    if modo == 0:
        mes_meta_fijo = mes_meta

if mes_meta_fijo and mes_meta:
    print(f"El depósito creciente alcanza la meta {mes_meta_fijo - mes_meta} mes(es) antes.")
elif mes_meta:
    print("Solo el depósito creciente alcanza la meta en el plazo indicado.")
else:
    print("Ningún plan alcanza la meta dentro del plazo.")

print("\nComparación de tasas para el mismo plan de depósito fijo:")
for tasa in range(4, 13, 2):
    saldo = 0.0
    for mes in range(1, meses + 1):
        saldo += deposito
        saldo += saldo * tasa / 100 / MESES_POR_ANO
        if mes % MESES_POR_ANO == 0:
            saldo += saldo * BONO_FIDELIDAD
    print(f"{tasa:2} % anual -> saldo final ${saldo:,.2f}")
