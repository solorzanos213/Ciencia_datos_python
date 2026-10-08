# Actividad 3.5 — Caso integrador: seguimiento académico

## Matriz de variables

| Variable | Tipo esperado | Uso posible | Riesgo o cuidado |
|---|---|---|---|
| id_aprendiz | Texto / código | Distinguir registros sin usar documento real | Proteger identidad |
| ficha | Texto / código | Agrupar registros por ficha | No comparar grupos sin contexto |
| asistencia_porcentaje | Número decimal | Reconocer posibles alertas de inasistencia | Investigar las causas |
| promedio_actividades | Número decimal | Revisar desempeño académico | No definir a una persona solo por su nota |
| evidencias_entregadas | Número entero | Ver avance de entregas | Revisar también la calidad |
| observacion | Texto | Documentar acompañamiento | Evitar juicios y lenguaje discriminatorio |

## Cinco preguntas analíticas
1. ¿Cuántos aprendices tienen asistencia menor del 80 % y promedio inferior a 3.5?
2. ¿Cuál es el porcentaje promedio de asistencia por ficha?
3. ¿Qué proporción de aprendices ha entregado menos de tres evidencias?
4. ¿Hay diferencias entre el promedio de actividades de quienes tienen alta y baja asistencia?
5. ¿Qué fichas tienen más aprendices con posibles alertas académicas?

## Pregunta prioritaria
La primera pregunta ayuda a detectar casos que merecen revisión y ofrecer apoyo a tiempo, **sin asumir que dos indicadores expliquen por completo la situación del aprendiz**.

**Privacidad:** para una actividad de práctica no se requieren datos personales reales; usar datos simulados o información autorizada.
