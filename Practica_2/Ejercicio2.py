"""2. Usando el concepto de funciones (3 ptos):
Reglas:
- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso en el input de
datos)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original"""


def normalizar_nombres(nombres):
    nombres_normalizados = []
    vistos = []

    for nombre in nombres:
        nombre = nombre.strip()
        partes = nombre.split()
        for parte in partes:
            parte_titulo = parte.title()
            if parte_titulo not in vistos:
                vistos.append(parte_titulo)
                nombres_normalizados.append(parte_titulo)
    return nombres_normalizados

lista_nombres = [ " emanuel  ",  "MARIA",  "fabio luis", "ana",  "fabio", " maria   cristina ",  "EMANUEL"]
lista_normalizada = normalizar_nombres(lista_nombres)

print("Lista original:{}".format(lista_nombres))
print("Lista normalizada: {}".format( lista_normalizada))
