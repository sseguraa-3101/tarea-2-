# Archivo: menu.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Resolver una operación de la calculadora elegida en el menú.

print("CALCULADORA\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
opcion = input("Elige una opción: ").strip()
match opcion:
    case "1" | "2" | "3" | "4":
        primero = float(input("Primer número: "))
        segundo = float(input("Segundo número: "))
        match opcion:
            case "1":
                print(f"Resultado: {primero + segundo}")
            case "2":
                print(f"Resultado: {primero - segundo}")
            case "3":
                print(f"Resultado: {primero * segundo}")
            case "4":
                if segundo == 0:
                    print("No se puede dividir entre cero.")
                else:
                    print(f"Resultado: {primero / segundo}")
    case "5":
        print("Hasta luego.")
    case _:
        print("Opción no válida.")
