#Ej 9

sueldo = int(input("Ingrese el sueldo basico: ")) #Sueldo
antiguedad = int(input("Ingrese la antiguedad: ")) #Antiguedad
ecivil = int(input("Ingrese el estado civil: ")) #Estado civil 1 == Soltero, 2 == Casado

if ecivil == 1: #Si el estado civil es 1 osea soltero 

    sueldo2 = sueldo + (sueldo*0.05*antiguedad) #Variable Del sueldo base + 5% del sueldo base por la cantidad de años
    ecivil = "Soltero" #Defino ecivil como "Soltero" porque puso 1
    edadben = 0.05 #Beneficio por año que trabaja 

elif ecivil == 2: #Si el estado civil es 2 osea casado 

    sueldo2 = sueldo + (sueldo*0.07*antiguedad) #Variable Del sueldo base + 7% del sueldo base por la cantidad de años
    ecivil = "Casado" #Defino ecivil como "Casado" porque puso 2
    edadben = 0.07 #Beneficio por año que trabaja

print("Estado Civil: ", ecivil)
print("")
print("Sueldo basico    Antiguedad   Descuentos   Importe")
print("$",sueldo,"           ",antiguedad,"años""                 +",sueldo*edadben*antiguedad,)                     
print("                   Jubilacion  -",sueldo2*0.11)
print("                   Obra social -",sueldo2*0.03)
print("                   Sindicato   -",sueldo2*0.03)
print("                                         ..........")
print("                   Sueldo neto:            ",sueldo2 * 0.83)

