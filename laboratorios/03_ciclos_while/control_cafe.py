# Archivo: control_cafe.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Revisar las bolsas de café, vigilar rachas defectuosas y resumir el turno.

CODIGO_SUPERVISOR = "CAFE2026"
MAX_INTENTOS = 3
PESO_OBJETIVO = 500
TOLERANCIA = 10
MAX_CONSECUTIVAS = 3

intentos = 0
acceso_concedido = False
while intentos < MAX_INTENTOS and not acceso_concedido:
    intentos += 1
    acceso_concedido = input("Código de supervisor: ") == CODIGO_SUPERVISOR
    if not acceso_concedido:
        print(f"Código incorrecto. Intentos restantes: {MAX_INTENTOS - intentos}")

if not acceso_concedido:
    print("Acceso bloqueado. Avise al jefe de planta.")
else:
    print("Acceso concedido. Inicie el registro (0 para terminar).")
    revisadas = 0
    aceptadas = 0
    defectuosas = 0
    consecutivas = 0
    peso_acumulado = 0.0
    terminar = False
    linea_detenida = False
    while not terminar and not linea_detenida:
        peso = float(input(f"Peso de la bolsa {revisadas + 1} (g): "))
        while peso < 0:
            print("El peso no puede ser negativo.")
            peso = float(input(f"Peso de la bolsa {revisadas + 1} (g): "))
        if peso == 0:
            terminar = True
        else:
            revisadas += 1
            peso_acumulado += peso
            if revisadas == 1 or peso < peso_minimo:
                peso_minimo = peso
            if revisadas == 1 or peso > peso_maximo:
                peso_maximo = peso
            diferencia = peso - PESO_OBJETIVO
            if diferencia < 0:
                diferencia = -diferencia
            if diferencia <= TOLERANCIA:
                aceptadas += 1
                consecutivas = 0
                print("  OK")
            else:
                defectuosas += 1
                consecutivas += 1
                linea_detenida = consecutivas == MAX_CONSECUTIVAS
                print(f"  DEFECTUOSA ({consecutivas} seguidas)")

    print("\n===== REPORTE DEL TURNO =====")
    print(f"Bolsas revisadas: {revisadas}")
    print(f"Aceptadas:        {aceptadas}")
    print(f"Defectuosas:      {defectuosas}")
    if revisadas > 0:
        print(f"% defectuosas:    {100 * defectuosas / revisadas:.1f} %")
        print(f"Peso promedio:    {peso_acumulado / revisadas:.1f} g")
        print(f"Peso mínimo: {peso_minimo:g} g | Peso máximo: {peso_maximo:g} g")
    if linea_detenida:
        print(f"ALERTA: línea detenida por {MAX_CONSECUTIVAS} bolsas defectuosas seguidas.")
        print("Revise la dosificadora.")
