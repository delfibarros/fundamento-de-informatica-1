from operator import inv


inversionista1 = int(input("Inversion primer inversor: "))
inversionista2 = int(input("Inversion segundo inversor: "))
inversionista3 = int(input("Inversion tercer inversor: "))

inversiontotal = inversionista1 + inversionista2 + inversionista3

print("El porcentaje del inversionista 1 es de: ", inversionista1*100/inversiontotal )
print("El porcentaje del inversionista 2 es de: ", inversionista2*100/inversiontotal)
print("El porcentaje del inversionista 3 es de: ", inversionista3*100/inversiontotal) 