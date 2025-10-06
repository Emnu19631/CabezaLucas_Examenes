import Ejercicio_2

def probar_caso(n, indice, caso):
    print(f"\n--- CASO {caso} ---")
    lista = Ejercicio_2.generar_lista(n, indice)
    if lista:
        sin_repe = Ejercicio_2.numeros_no_repetidos(lista)
        Ejercicio_2.ordenar_lista(sin_repe)
        Ejercicio_2.mayor_par(sin_repe)

probar_caso(10, 3, 1)
probar_caso(15, 7, 2)
probar_caso(8, 12, 3)
probar_caso("10", 2, 4)
