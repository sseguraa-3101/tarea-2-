# Archivo: turnos.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Calcular los turnos que caben completos entre la apertura y el cierre.

print("AGENDA DE TURNOS")
apertura = int(input("Hora de apertura (0 a 23): "))
while not 0 <= apertura < 23:
    apertura = int(input("Ingrese una hora de apertura entre 0 y 22: "))
cierre = int(input("Hora de cierre (0 a 23): "))
while not apertura < cierre <= 23:
    cierre = int(input("El cierre debe ser posterior a la apertura y hasta las 23: "))
duracion = int(input("Minutos por turno: "))
while duracion <= 0:
    duracion = int(input("Duración positiva en minutos: "))

turnos = 0
for inicio in range(apertura * 60, cierre * 60 - duracion + 1, duracion):
    fin = inicio + duracion
    turnos += 1
    print(f"Turno {turnos:2}: {inicio // 60:02d}:{inicio % 60:02d} a {fin // 60:02d}:{fin % 60:02d}")
print(f"Turnos disponibles: {turnos}")
