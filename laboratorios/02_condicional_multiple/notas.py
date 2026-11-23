# Archivo: notas.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Clasificar una nota con guardas y límites inclusivos.

nota = int(input("Nota (0–100): "))
match nota:
    case n if n < 0 or n > 100:
        print("Nota fuera de rango")
    case n if n >= 90:
        print("Excelente")
    case n if n >= 70:
        print("Aprobado")
    case _:
        print("Reprobado")
