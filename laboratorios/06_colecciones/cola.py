# Archivo: cola.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: Sebastián Miguel Segura Arias
# Fecha: 21 de noviembre de 2026
# Versión: 1.0
# Propósito: Administrar el orden de atención y las llegadas de clientes.

cola = []
atendidos = 0
while True:
    print(f"\nCOLA DE ESPERA | Clientes en espera: {len(cola)}")
    print("1. Llegada\n2. Urgencia\n3. Grupo\n4. Atender\n5. Retirar\n6. Consultar posición\n7. Ver cola\n0. Cerrar")
    opcion = input("Opción: ").strip()
    if opcion == "1" or opcion == "2":
        nombre = input("Nombre: ").strip().title()
        if not nombre:
            print("Ingrese un nombre.")
            continue
        if opcion == "1":
            cola.append(nombre)
            print(f"{nombre} está en la posición {len(cola)}.")
        else:
            cola.insert(0, nombre)
            print(f"{nombre} pasa al primer lugar.")
    elif opcion == "3":
        grupo = []
        for texto in input("Nombres separados por comas: ").split(","):
            nombre = texto.strip().title()
            if nombre:
                grupo.append(nombre)
        cola.extend(grupo)
        print(f"Se agregaron {len(grupo)} clientes al final de la cola.")
    elif opcion == "4":
        if cola:
            atendidos += 1
            print(f"Pase {cola.pop(0)}, por favor.")
        else:
            print("No hay nadie esperando.")
    elif opcion == "5" or opcion == "6":
        nombre = input("Nombre del cliente: ").strip().title()
        if nombre not in cola:
            print(f"{nombre} no está en la cola.")
        elif opcion == "5":
            cola.remove(nombre)
            print(f"{nombre} salió de la cola.")
        else:
            posicion = cola.index(nombre) + 1
            print(f"Posición de {nombre}: {posicion}. Personas delante: {posicion - 1}.")
            if cola.count(nombre) > 1:
                print(f"{nombre} aparece {cola.count(nombre)} veces.")
    elif opcion == "7":
        if not cola:
            print("La cola está vacía.")
        else:
            for i in range(len(cola)):
                print(f"{i + 1}. {cola[i]}")
            print("Próximos tres:", ", ".join(cola[:3]))
            print("Lista alfabética:", ", ".join(sorted(cola)))
    elif opcion == "0":
        pendientes = cola.copy()
        cola.clear()
        print(f"Clientes atendidos hoy: {atendidos}")
        if pendientes:
            print("Quedaron sin atender:", ", ".join(pendientes))
        break
    else:
        print("Opción no válida.")
