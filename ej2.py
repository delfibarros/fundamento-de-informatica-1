legajo = int(input("Legajo: "))

if legajo != -1:
    nota = int(input("Nota: "))
    while nota < 1 or nota > 10:
        nota = int(input("Nota: "))

aprobados = 0
desaprobados = 0
aplazados = 0

while legajo != -1:
    
    if nota >= 4:
        aprobados += 1
        print("Aprobado")
    elif nota < 4 and nota != 1:
        desaprobados += 1
        print("Desaprobado")
    elif nota == 1:
        aplazados += 1
        print("Aplazado")

    legajo = int(input("Legajo: "))
    
    if legajo != -1:
        nota = int(input("Nota: "))

    while nota < 1 or nota > 10:
        nota = int(input("Nota: "))

print("============================")
print("Aprobados:",aprobados)
print("Desaprobados:",desaprobados)
print("Aplazados:",aplazados)
print("============================")