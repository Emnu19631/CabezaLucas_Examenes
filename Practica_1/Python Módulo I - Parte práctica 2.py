matematicas = 17
ciencia = 14
historia = 15
p_matematicas = 0.40
p_ciencia = 0.30
p_historia = 0.30

nota_final = (matematicas * p_matematicas + ciencia * p_ciencia + historia * p_historia)
nota_final_r = round(nota_final, 1)

aprobado = nota_final_r >= 13.0
estado = "Aprobado" if aprobado else "Desaprobado"

print("La nota final es: {}".format(nota_final_r))
print("¿Aprobado?: {}".format("Sí" if aprobado else "No"))
print("El estudiante obtuvo una nota final de {} y su estado final es: {}".format(nota_final_r, estado))
