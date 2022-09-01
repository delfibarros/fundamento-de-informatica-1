def invalido(min, max):
    numero = int(input("Numero: "))
    while numero < min or numero > max:
        numero = int(input("Ingrese Numero Valido. Numero:"))
    return numero

def buscarMayor(vec):
    mayor = vec[0]
    for i in range(12):
        if vec[i] > mayor:
            mayor = vec[i]
            posicion = i
    
    return posicion

meses = [0,0,0,0,0,0,0,0,0,0,0,0] #12 
mesesTexto = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

legajo = int(input("Legajo: "))

while legajo != -1:
    print("Dia de Nacimiento:")
    dia = invalido(0,31)

    print("Mes de Nacimiento:")
    mes = invalido(1,12)

    print("Año de Nacimiento:")
    año = invalido(0,5000)

    mes = mes - 1 #Para la Lista

    meses[mes] += 1

    legajo = int(input("Legajo: "))



for i in range(12):
    print(mesesTexto[i],":",meses[i])

mayor = buscarMayor(meses)
print("Mayor Mes es",mesesTexto[mayor],"con",meses[mayor])

