edad = 0
menores = 0
mayores = 0
sumamenores = 0
sumamayores = 0
promediomenores = 0
promediomayores = 0

while edad != -1:
    edad = int(input("Ingrese Edad: "))
    if edad > 0 and edad < 18 and edad != -1:
        menores += 1
        sumamenores = sumamenores + edad
        promediomenores = sumamenores / menores 
    elif edad >= 18 and edad < 100 and edad != -1:
        mayores += 1
        sumamayores = sumamayores + edad
        promediomayores = sumamayores / mayores
    elif edad >= 100 or edad <= 0:
        print("Edad no Validad")



print("Mayores: ", mayores, ".Y su promedio es de: ", promediomayores)
print("Menores: ", menores, ".Y su promedio es de: ", promediomenores)
