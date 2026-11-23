# Archivo: ficha.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Consultar la ficha de la bicicleta, el horario y las reseñas del taller.

DIAS_ATENCION = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado")
RESENAS_MES = (5, 4, 5, 3, 5, 4, 5, 2, 5, 4, 1, 5)
bicicleta = ("Trek", "Marlin 5", 29, "Rojo")
marca, modelo, rodado, color = bicicleta
print(f"Ficha de ingreso: {marca} {modelo} | Rodado: {rodado} pulgadas | Color: {color}")
print(f"Atendemos {len(DIAS_ATENCION)} días: de {DIAS_ATENCION[0]} a {DIAS_ATENCION[-1]}.")
print("Horario completo:", ", ".join(DIAS_ATENCION[:5]))
print("Medio día:", DIAS_ATENCION[-1])
dia = input("¿Qué día traerá su bicicleta? ").strip().capitalize()
if dia in DIAS_ATENCION:
    print(f"{dia} es el día {DIAS_ATENCION.index(dia) + 1} de atención de la semana.")
else:
    print(f"El {dia.lower()} no atendemos.")

for estrellas in range(5, 0, -1):
    cantidad = RESENAS_MES.count(estrellas)
    print(f"{estrellas} estrellas | {'#' * cantidad:<6} {cantidad}")
total = len(RESENAS_MES)
print(f"Reseñas: {total} | Promedio: {sum(RESENAS_MES) / total:.1f}")
print(f"Peor: {min(RESENAS_MES)} | Mejor: {max(RESENAS_MES)}")
print(f"Clientes muy satisfechos: {100 * RESENAS_MES.count(5) / total:.0f} %")
if 1 in RESENAS_MES:
    print(f"Revisar la reseña número {RESENAS_MES.index(1) + 1}: primera de 1 estrella.")
