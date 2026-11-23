# Comprobación de los laboratorios

Resultados de las ejecuciones de consola. Cada casilla corresponde a una ejecución del archivo indicado. Las entradas se muestran en el orden en que las solicita el programa.


## menu.py

- [x] **Selección 1**. Entradas: 1 → 7 → 2. Salida comprobada: “9.0”.
- [x] **Selección 2**. Entradas: 2 → 7 → 2. Salida comprobada: “5.0”.
- [x] **Selección 3**. Entradas: 3 → 7 → 2. Salida comprobada: “14.0”.
- [x] **Selección 4**. Entradas: 4 → 10 → 4. Salida comprobada: “2.5”.
- [x] **Selección 4**. Entradas: 4 → 2 → 0. Salida comprobada: “entre cero”.
- [x] **Selección 5**. Entradas: 5. Salida comprobada: “Hasta luego”.
- [x] **Selección x**. Entradas: x. Salida comprobada: “Opción no válida”.

## reto_menu.py

- [x] **Conversor 1**. Entradas: 1 → 100. Salida comprobada: “212 °F”.
- [x] **Conversor 2**. Entradas: 2 → 32. Salida comprobada: “0 °C”.
- [x] **Conversor 3**. Entradas: 3. Salida comprobada: “Hasta luego”.
- [x] **Conversor 4**. Entradas: 4. Salida comprobada: “Opción no válida”.

## dias.py

- [x] **Día 1**. Entradas: 1. Salida comprobada: “Lunes”.
- [x] **Día 2**. Entradas: 2. Salida comprobada: “Martes”.
- [x] **Día 3**. Entradas: 3. Salida comprobada: “Miércoles”.
- [x] **Día 4**. Entradas: 4. Salida comprobada: “Jueves”.
- [x] **Día 5**. Entradas: 5. Salida comprobada: “Viernes”.
- [x] **Día 6**. Entradas: 6. Salida comprobada: “Fin de semana”.
- [x] **Día 7**. Entradas: 7. Salida comprobada: “Fin de semana”.
- [x] **Día 9**. Entradas: 9. Salida comprobada: “no válido”.

## comparacion.py

- [x] **Día 1**. Entradas: 1. Salida comprobada: “Lunes”.
- [x] **Día 2**. Entradas: 2. Salida comprobada: “Martes”.
- [x] **Día 3**. Entradas: 3. Salida comprobada: “Miércoles”.
- [x] **Día 4**. Entradas: 4. Salida comprobada: “Jueves”.
- [x] **Día 5**. Entradas: 5. Salida comprobada: “Viernes”.
- [x] **Día 6**. Entradas: 6. Salida comprobada: “Fin de semana”.
- [x] **Día 7**. Entradas: 7. Salida comprobada: “Fin de semana”.
- [x] **Día 9**. Entradas: 9. Salida comprobada: “no válido”.

## notas.py

- [x] **Nota -1**. Entradas: -1. Salida comprobada: “fuera de rango”.
- [x] **Nota 0**. Entradas: 0. Salida comprobada: “Reprobado”.
- [x] **Nota 50**. Entradas: 50. Salida comprobada: “Reprobado”.
- [x] **Nota 69**. Entradas: 69. Salida comprobada: “Reprobado”.
- [x] **Nota 70**. Entradas: 70. Salida comprobada: “Aprobado”.
- [x] **Nota 75**. Entradas: 75. Salida comprobada: “Aprobado”.
- [x] **Nota 89**. Entradas: 89. Salida comprobada: “Aprobado”.
- [x] **Nota 90**. Entradas: 90. Salida comprobada: “Excelente”.
- [x] **Nota 95**. Entradas: 95. Salida comprobada: “Excelente”.
- [x] **Nota 100**. Entradas: 100. Salida comprobada: “Excelente”.
- [x] **Nota 101**. Entradas: 101. Salida comprobada: “fuera de rango”.

## control_cafe.py

- [x] **Acceso inmediato y centinela**. Entradas: CAFE2026 → 0. Salida comprobada: “Acceso concedido” · “Bolsas revisadas: 0”.
- [x] **Segundo intento**. Entradas: hola → CAFE2026 → 0. Salida comprobada: “restantes: 2” · “Acceso concedido”.
- [x] **Bloqueo por tres intentos**. Entradas: a → b → c. Salida comprobada: “restantes: 2” · “restantes: 1” · “restantes: 0” · “Acceso bloqueado”.
- [x] **El código distingue mayúsculas**. Entradas: cafe2026 → CAFE2026 → 0. Salida comprobada: “incorrecto” · “Acceso concedido”.
- [x] **Centinela tras tres datos**. Entradas: CAFE2026 → 500 → 495 → 505 → 0. Salida comprobada: “Peso de la bolsa 4” · “Bolsas revisadas: 3”.
- [x] **Dos pesos negativos consecutivos**. Entradas: CAFE2026 → -3 → -1 → 500 → 0. Salida comprobada: “Bolsas revisadas: 1”.
- [x] **Reintento en segunda bolsa**. Entradas: CAFE2026 → 500 → -2 → 498 → 0. Salida comprobada: “Bolsas revisadas: 2”.
- [x] **Límites incluidos**. Entradas: CAFE2026 → 490 → 510 → 0. Salida comprobada: “Aceptadas:        2” · “Peso mínimo: 490 g | Peso máximo: 510 g”.
- [x] **Fuera de ambos límites**. Entradas: CAFE2026 → 489 → 511 → 0. Salida comprobada: “Defectuosas:      2”.
- [x] **Una buena y una defectuosa**. Entradas: CAFE2026 → 500 → 520 → 0. Salida comprobada: “Aceptadas:        1” · “Defectuosas:      1”.
- [x] **Alarma y reporte del ejemplo**. Entradas: CAFE2026 → 500 → 520 → 480 → 530. Salida comprobada: “Bolsas revisadas: 4” · “75.0 %” · “507.5 g” · “ALERTA”.
- [x] **Una buena reinicia la racha**. Entradas: CAFE2026 → 520 → 480 → 500 → 530 → 0. Salida comprobada: “Bolsas revisadas: 4”.
- [x] **Tres defectuosas desde el inicio**. Entradas: CAFE2026 → 520 → 480 → 530. Salida comprobada: “Bolsas revisadas: 3” · “ALERTA”.
- [x] **Porcentaje y promedio**. Entradas: CAFE2026 → 500 → 495 → 520 → 0. Salida comprobada: “Bolsas revisadas: 3” · “Aceptadas:        2” · “Defectuosas:      1” · “33.3 %” · “505.0 g”.

## ahorro_cooperativa.py

- [x] **Plazo, tasa y bono anual**. Entradas: 100 → 0 → -2 → 12 → 6 → 1300. Salida comprobada: “0.50” · “100.50” · “12.40” · “1252.12”.
- [x] **Ejemplo, meta y cinco tasas**. Entradas: 100 → 14 → 6 → 1300. Salida comprobada: “303.01” · “1,400.00” · “53.78” · “12.40” · “1,466.18” · “mes 13.” · “4 % anual -> saldo final $1,447.86” · “6 % anual -> saldo final $1,466.18” · “8 % anual -> saldo final $1,484.76” · “10 % anual -> saldo final $1,503.62” · “12 % anual -> saldo final $1,522.76”.
- [x] **Meta del mes diez**. Entradas: 100 → 14 → 6 → 1000. Salida comprobada: “mes 10.”.
- [x] **Meta del primer mes**. Entradas: 100 → 14 → 6 → 100. Salida comprobada: “mes 1.”.
- [x] **Meta pendiente**. Entradas: 50 → 3 → 12 → 500. Salida comprobada: “faltan $346.98”.
- [x] **Reto, meta adelantada**. Entradas: 100 → 30 → 0 → 2480. Salida comprobada: “mes 25.” · “mes 24.” · “1 mes(es) antes”.

## recepcion.py

- [x] **Registro, nombre vacío, cotización y confirmación**. Entradas: 1 → Ana → 1 → (vacío) → 3 → 95 → 3 → abc → 0 → n → 2 → 0 → s. Salida comprobada: “Bicicleta #1 recibida a nombre de Ana.” · “nombre no puede quedar vacío” · “1 h 35 min. Mano de obra: $19.00” · “números enteros” · “Lunes a viernes” · “Bicicletas recibidas hoy: 1.”.

## turnos.py

- [x] **Agenda 8/12/45**. Entradas: 8 → 12 → 45. Salida comprobada: “11:00 a 11:45” · “Turnos disponibles: 5”.
- [x] **Agenda 8/12/60**. Entradas: 8 → 12 → 60. Salida comprobada: “11:00 a 12:00” · “Turnos disponibles: 4”.
- [x] **Agenda 13/9/17/60**. Entradas: 13 → 9 → 17 → 60. Salida comprobada: “16:00 a 17:00” · “Turnos disponibles: 4”.

## serie.py

- [x] **Serie WTU12345678**. Entradas: WTU12345678. Salida comprobada: “fabricante: WTU”.
- [x] **Serie wtu12345678**. Entradas: wtu12345678. Salida comprobada: “fabricante: WTU”.
- [x] **Serie WT912345678**. Entradas: WT912345678. Salida comprobada: “carácter 3 debe ser letra”.
- [x] **Serie wtu 1234-567**. Entradas: wtu 1234-567. Salida comprobada: “Otros símbolos: 2” · “tiene 12”.
- [x] **Serie AB1**. Entradas: AB1. Salida comprobada: “tiene 3”.

## ficha.py

- [x] **Consulta sábado**. Entradas: sábado. Salida comprobada: “día 6” · “5 estrellas | ###### 6” · “4 estrellas | ###    3” · “3 estrellas | #      1” · “2 estrellas | #      1” · “1 estrellas | #      1” · “Promedio: 4.0” · “50 %” · “reseña número 11”.
- [x] **Consulta LUNES**. Entradas: LUNES. Salida comprobada: “día 1” · “5 estrellas | ###### 6” · “4 estrellas | ###    3” · “3 estrellas | #      1” · “2 estrellas | #      1” · “1 estrellas | #      1” · “Promedio: 4.0” · “50 %” · “reseña número 11”.
- [x] **Consulta domingo**. Entradas: domingo. Salida comprobada: “domingo no atendemos” · “5 estrellas | ###### 6” · “4 estrellas | ###    3” · “3 estrellas | #      1” · “2 estrellas | #      1” · “1 estrellas | #      1” · “Promedio: 4.0” · “50 %” · “reseña número 11”.

## cola.py

- [x] **Orden de llegada, urgencia, grupo, consulta y cierre**. Entradas: 4 → 1 → ana → 1 → Luis → 2 → marta → 3 → pedro, luis , ,sofía → 6 → luis → 7 → 5 → Juan → 4 → 5 → Luis → 0. Salida comprobada: “No hay nadie esperando.” · “3 clientes” · “Posición de Luis: 3” · “Luis aparece 2 veces” · “1. Marta” · “2. Ana” · “3. Luis” · “Próximos tres: Marta, Ana, Luis” · “Lista alfabética: Ana, Luis, Luis, Marta, Pedro, Sofía” · “Juan no está en la cola.” · “Pase Marta” · “Luis salió de la cola” · “atendidos hoy: 1” · “sin atender: Ana, Pedro, Luis, Sofía”.

## bodega.py

- [x] **Stock, consumo, pedido, baja y actualización de precios**. Entradas: 1 → 2 → Cadena → 3 → cadena → 5 → 3 → cadena → 2 → 8 → 4 → cadena → 3 → camara → 2 → cadena → 1 → cable → 4 → FIN → 2 → cadena → 2 → camara → 2 → cable → 6 → parche → 6 → parche → 7 → 2 → camara → 0. Salida comprobada: “cadena: 2 <- pedir más” · “Repuestos distintos: 4” · “2 unidades a $15.00” · “Solo hay 2 unidades” · “Quedan 0 unidades” · “Valor de la bodega: $51.50” · “cadena: 4 unidades” · “camara: 5 unidades” · “cable: 4 unidades” · “parche eliminado” · “Ese repuesto no existe” · “camara: 5 unidades a $8.00”.

## taller.py

- [x] **Órdenes, faltante, entrega y reporte**. Entradas: 1 → 2 → Ana → ca → PA → XX → fin → 2 → Luis → CA → CA → FR → FIN → 5 → 4 → 1 → 4 → 1 → 3 → 6 → 0. Salida comprobada: “Cambio de cadena” · “Código no existe” · “Orden #1 registrada. Total: $20.00” · “Sin cadena” · “Orden #2 registrada. Total: $23.00” · “pastillas: 3” · “cadena: 0 <- reabastecer” · “parche: 9” · “Orden #1 entregada a Ana” · “ya fue entregada” · “#2 Luis | CA, FR” · “Órdenes registradas: 2 | Órdenes entregadas: 1” · “Ingresos cobrados: $20.00” · “Cambio de cadena (2 veces)”.
