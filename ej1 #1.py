def promedio(v):
    largo = len(v)
    suma = 0
    for i in range(largo):
        suma = suma + v[i]
    
    promedio = suma / largo

    return promedio

def notasQueSuperanPromedio(v,promedio):
    contador = 0
    largo = len(v)
    for i in range(largo):
        if v[i] > promedio:
            contador += 1
    
    return contador

def ordenar(v,v2):
    largo = len(v)
    for i in range(largo-1):
        for j in range(i+1,largo):
            if v[i] > v[j]:
                aux1 = v[i]
                v[i] = v[j]
                v[j] = aux1
                aux2 = v2[i]
                v2[i] = v2[j]
                v2[j] = aux2
    
    return v,v2

def legajosQueSuperanPromedio(legajos,promedio,notas):
    largo = len(legajos)
    vec = []
    for i in range(largo):
        if notas[i] > promedio:
            vec.append(legajos[i])
    
    return vec

def busquedaSecuencial(v,valor):
    i = 0
    largo = len(v)
    while i < largo and v[i] != valor:
        i += 1
    if i < largo:
        return i
    else:
        return -1

notaMayorCuatro = 0
desaprobados = 0
promedioNotas = 0
legajos = []
notas = []

legajo= int(input("Legajo: "))
while legajo != -1:
    legajos.append(legajo)
    nota= int(input("Nota: "))
    while (nota < 1 or nota > 10):
        nota = int(input("Error. Nota: "))
    notas.append(nota)
    if nota >= 4:
        notaMayorCuatro += 1
    if nota <= 4:
        desaprobados += 1
    legajo = int(input("Legajo: "))
    while busquedaSecuencial(legajos, legajo) != -1:
        legajo = int(input("Error. Legajo: "))




print("Legajos:",legajos)
print("Notas:",notas)

if len(legajos) > 0: 
    promedioNotas = promedio(notas) 
    print("Promedio Notas:",promedioNotas)

notasMasPromedio = notasQueSuperanPromedio(notas, promedioNotas)
print("Cantidad de notas que superan el promedio:",notasMasPromedio)

legajosQueSuperanProm = legajosQueSuperanPromedio(legajos,promedioNotas,notas)
print("Legajos que superan Promedio:",legajosQueSuperanProm)

print("===================================")
ordenado1,ordenado2 = ordenar(legajos,notas)
print("Legajos:", ordenado1)
print("Notas:", ordenado2)
