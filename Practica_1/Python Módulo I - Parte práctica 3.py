t_cuenta = float(input("Ingrese el total de la cuenta: "))
p_propina = float(input("Ingrese el porcentaje de propina: "))
n_personas = int(input("Ingrese el número de personas: "))

m_propina = t_cuenta * (p_propina / 100)
m_total = t_cuenta + m_propina
m_por_persona = m_total / n_personas

print("Monto total con propina: S/. {:.2f}".format(m_total))
print("Cada persona debe pagar: S/. {:.2f}".format(m_por_persona))

if m_por_persona > 100:
    print("¡Advertencia! El monto por persona supera los S/. 100")
else:
    print("El monto por persona no pasa los S/. 100.")
