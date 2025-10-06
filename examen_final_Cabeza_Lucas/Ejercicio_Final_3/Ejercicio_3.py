"""3. (2 ptos) Crear un decorador conteo.
Reglas:
- El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente al usuario.
- Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada exitosamente.
- La función que vas a crear va a capturar, la edad, nombre de un alumno, la
hora y el minuto en que fue registrado (usar la librería correspondiente de
tiempo)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”
- La función que será decorada también estará pasando 4 notas que calculará
la media del estudiante."""

import datetime

def conteo(funcion):
    def interno(*args, **kwargs):
        total_parametros = len(args) + len(kwargs)

        if total_parametros <= 1:
            print("Debe ingresar más de un parámetro para procesar.")
            return None
        resultado = funcion(*args, **kwargs)

        print("La función fue ejecutada exitosamente.")
        return resultado
    return interno

@conteo
def registrar_alumno(nombre, edad, *notas):

    ahora = datetime.datetime.now()
    h, m = ahora.hour, ahora.minute

    print("{} de {} años ha sido registrado a las {} horas con {} minutos.".format(nombre, edad, h, m))

    if notas:
        media = sum(notas) / len(notas)
        print("La media del estudiante es: {:.2f}".format(media))
    else:
        print("No se ingresaron notas.")

if __name__ == "__main__":
    print("\n--- Ejemplo 1 ---")
    registrar_alumno("Pedro", 30, 15, 18, 20, 17)

    print("\n--- Ejemplo 2 ---")
    registrar_alumno("Ana", 22, 10, 12, 14, 16)

    print("\n--- Ejemplo 3 ---")
    registrar_alumno("Luis" )
