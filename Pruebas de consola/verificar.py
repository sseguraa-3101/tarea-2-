"""Ejecuta los casos documentados con el mismo intérprete que inicia este archivo."""
import json
from pathlib import Path
import subprocess
import sys

CARPETA = Path(__file__).resolve().parent
EJERCICIOS = CARPETA.parent / "ejercicios"
fallos = 0

for ficha in sorted(CARPETA.glob("casos_*.json")):
    ejercicio = ficha.stem.removeprefix("casos_")
    casos = json.loads(ficha.read_text(encoding="utf-8"))
    registro = []
    for caso in casos:
        entrada = "\n".join(caso["entrada"]) + "\n"
        ejecucion = subprocess.run(
            [sys.executable, "-X", "utf8", str(EJERCICIOS / (ejercicio + ".py"))],
            input=entrada, capture_output=True, encoding="utf-8", timeout=10,
        )
        salida = ejecucion.stdout
        errores = []
        if ejecucion.returncode != 0:
            errores.append(ejecucion.stderr)
        posicion = 0
        for fragmento in caso["verificar"]:
            indice = salida.find(fragmento, posicion)
            if indice == -1:
                errores.append("No apareció en el orden esperado: " + fragmento)
            else:
                posicion = indice + len(fragmento)
        for fragmento in caso.get("ausentes", []):
            if fragmento in salida:
                errores.append("Apareció un texto inesperado: " + fragmento)
        for fragmento, cantidad in caso.get("conteos", {}).items():
            if salida.count(fragmento) != cantidad:
                errores.append(f"Cantidad incorrecta para {fragmento!r}")
        estado = "FALLA" if errores else "CUMPLE"
        if errores:
            fallos += 1
        print(f'{caso["id"]} | {estado} | {caso["escenario"]}')
        registro.extend([
            f'=== {caso["id"]} | {estado} | {caso["escenario"]} ===',
            "ENTRADAS EN ORDEN: " + ", ".join(caso["entrada"]),
            f"CÓDIGO DE SALIDA: {ejecucion.returncode}", "SALIDA DE CONSOLA:",
            salida.rstrip(), *errores, "",
        ])
    (CARPETA / f"ejecucion_{ejercicio}.txt").write_text("\n".join(registro), encoding="utf-8")

sys.exit(1 if fallos else 0)
