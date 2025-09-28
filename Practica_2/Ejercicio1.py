"""1. Escriba un programa donde tendrá los siguientes requisitos (3 ptos):
Reglas:
- Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas.
- Calcular el promedio de cada estudiante.
- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
y el valor sea otro diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor
- Mostrar en pantalla el estudiante con mayor promedio"""

def procesar_notas(estudiantes):
    resultados = {}
    max_promedio = -1
    estudiante_mejor_promedio = ""

    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / len(notas)
        promedio_redondeado = round(promedio, 1)

        if promedio >= 11:
            estado = "aprobado"
        else:
            estado = "desaprobado"

        resultados[nombre] = {
            'promedio': promedio_redondeado,
            'estado': estado
        }

        if promedio > max_promedio:
            max_promedio = promedio
            estudiante_mejor_promedio = nombre

    print("El estudiante con el mayor promedio es: {} con un promedio de {:.1f}".format(estudiante_mejor_promedio, max_promedio))

    return resultados

estudiantes_general = {'Emanuel': [18, 17, 16],  'Valeria': [13, 14, 16],'Sebastian': [9, 10, 8]}

resultados_procesados = procesar_notas(estudiantes_general)

print("\nDiccionario de resultados procesados:")
print("{}".format(resultados_procesados))