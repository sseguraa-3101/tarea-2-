# Archivo: comparacion.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Comparar el clasificador de días con su versión if/elif/else.

# Versión del clasificador con la condicional múltiple de la rúbrica.
dia = int(input("Número del día (1–7): "))
if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6 or dia == 7:
    print("Fin de semana")
else:
    print("Número de día no válido")
