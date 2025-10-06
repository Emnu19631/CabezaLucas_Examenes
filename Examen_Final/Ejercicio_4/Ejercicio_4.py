"""4. (2 ptos) Crear un programa usando decoradores para mostrar solo la hora
y el minuto del momento que se usa el decorador
Reglas:
- Al ejecutar el decorador mostrará un mensaje: “El decorador está siendo
ejecutado a las H con m minutos y S segundos”
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: usando 6 números e indicar el mayor de
todos ellos (o x números) para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**kwards) para usar más de 6 valores en la función (value_7 = 10,
value_8 = 22, value_9=45) y visualizar los resultados usando el decorador
implementado con un mínimo tres ejemplos."""

import datetime

def deco_ej4(funcion):
    def interior(*args, **kwargs):
        ahora = datetime.datetime.now()
        h, m, s = ahora.hour, ahora.minute, ahora.second

        print("\nEl decorador está siendo ejecutado a las {} con {} minutos y {} segundos".format(h, m, s))
        valores = funcion(*args, **kwargs)

        suma = sum(valores)

        print("Suma de elementos: {}".format(suma))

        return valores

    return interior

@deco_ej4
def mayor_valor(*args, **kwargs):
    valores = list(args) + list(kwargs.values())
    mayor = max(valores)
    print("El mayor valor es: {}" .format(mayor))
    return valores

if __name__ == "__main__":
    print("--- Ejemplo 1 ---")
    mayor_valor(1, 2, 3, 4, 5, 6)

    print("\n--- Ejemplo 2 ---")
    mayor_valor(10, 20, 30, value_7=40, value_8=5)

    print("\n--- Ejemplo 3 ---")
    mayor_valor(100, 200, 50, value_7=10, value_8=22, value_9=45)
