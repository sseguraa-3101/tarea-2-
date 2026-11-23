# Archivo: reto_menu.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Convertir una temperatura entre grados Celsius y Fahrenheit.

print("CONVERSOR\n1. Celsius a Fahrenheit\n2. Fahrenheit a Celsius\n3. Salir")
match input("Elige una opción: ").strip():
    case "1":
        celsius = float(input("Temperatura (°C): "))
        print(f"Equivalencia: {celsius * 9 / 5 + 32:g} °F")
    case "2":
        fahrenheit = float(input("Temperatura (°F): "))
        print(f"Equivalencia: {(fahrenheit - 32) * 5 / 9:g} °C")
    case "3":
        print("Hasta luego.")
    case _:
        print("Opción no válida.")
