nombre = "Emanuel"
salario = 1200
edad = "32"
compania = "IBM"

edad_int = int(edad)

if edad_int > 30:
    mensaje = "Usted tiene un bono de 10% en el mes de diciembre"
    bono = salario * 0.10
else:
    mensaje = "Usted tiene un bono del 5% en el mes de diciembre"
    bono = salario * 0.05

bono_final = (salario ** 2) + bono

print("Nombre: {}\n Salario: {}\n Edad (string): {}\n Edad (int): {}\n Compañía: {}\n {}\n El bono final es: {}"
      .format(nombre,salario,edad,edad_int,compania,mensaje,bono_final))