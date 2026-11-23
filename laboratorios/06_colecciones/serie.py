# Archivo: serie.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Validar la estructura del número de serie de una bicicleta.

LARGO = 11
serie = input("Número de serie del cuadro: ").strip().upper()
letras = 0
digitos = 0
otros = 0
for caracter in serie:
    if caracter.isalpha():
        letras += 1
    elif caracter.isdigit():
        digitos += 1
    else:
        otros += 1
print(f"Letras: {letras} | Dígitos: {digitos} | Otros símbolos: {otros}")

valido = len(serie) == LARGO
if not valido:
    print(f"Error: debe tener {LARGO} caracteres y tiene {len(serie)}.")
else:
    for posicion in range(LARGO):
        caracter = serie[posicion]
        if posicion < 3 and not caracter.isalpha():
            print(f"Error: el carácter {posicion + 1} debe ser letra.")
            valido = False
        elif posicion >= 3 and not caracter.isdigit():
            print(f"Error: el carácter {posicion + 1} debe ser dígito.")
            valido = False
if valido:
    print(f"Número de serie válido. Código de fabricante: {serie[:3]}")
else:
    print("Número de serie inválido.")
