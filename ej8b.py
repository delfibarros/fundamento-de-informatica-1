cantEmpleados = int(input("Ingrese la cantidad de empleados: "))

if cantEmpleados > 0:
    print("------------------------------------------------------")
    legajo = int(input("Legajo: ")) 
    categoria = int(input("Categoria: "))
    while categoria < 1 or categoria > 3:
        categoria = int(input("Categoria: "))
    salario = int(input("Salario: "))
else: 
    salario = 0


importe_total = 0
mas200000 = 0
menos50000 = 0
masgana = 0
sueldomasbajo = salario
c1 = 0 
c2 = 0
c3 = 0
salario1 = 0
salario2 = 0
salario3 = 0
legajomasgana = 0
totalsalarios = 0


while cantEmpleados != 0:

    totalsalarios += 1

    importe_total = importe_total + salario
    if salario > 200000:
        mas200000 += 1
    if salario < 50000 and categoria == 3:
        menos50000 += 1
    if salario > masgana:
        masgana = salario
        legajomasgana = legajo
    if salario < sueldomasbajo:
        sueldomasbajo = salario
    if categoria == 1:
        salario1 = salario1 + salario
    if categoria == 2:
        salario2 = salario2 + salario
    if categoria == 3:
        salario3 = salario3 + salario
    
    cantEmpleados -= 1

    if cantEmpleados != 0:
        print("------------------------------------------------------")
        legajo = int(input("Legajo: ")) 
        categoria = int(input("Categoria: "))
        while categoria < 1 or categoria > 3:
            categoria = int(input("Categoria: "))
        salario = int(input("Salario: "))
        
if totalsalarios == 0:
    totalsalarios = 1

print("------------------------------------------------------")
print("======================================================")
print("Importe Total: ",importe_total)
print("Ganan mas de $200000: ",mas200000)
print("Ganan menos de $50000 y son categoria 3: ",menos50000)
print("Legajo del que mas Gana: ",legajomasgana )
print("Sueldo mas Bajo: ",sueldomasbajo)
print("C1: ",salario1,"C2: ",salario2,"C3: ",salario3)
print("Salario Promedio: ",importe_total / totalsalarios)
print("======================================================")