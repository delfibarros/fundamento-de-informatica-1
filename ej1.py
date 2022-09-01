def lista(x,y):

    if x > y:
        mayor = x
        menor = y
    elif y > x:
        mayor = y
        menor = x
    else:
        mayor = x
        menor = y

    vec = []

    print("Ingrese Numero entre ",menor," y ",mayor)
    numero = int(input())

    while numero != -1:

        while numero != -1 and (numero < menor or numero > mayor):
            print("Ingrese Numero valido, entre ",menor," y ",mayor)
            numero = int(input())

        if (numero >= menor and numero <= mayor) and numero != -1:
            vec.append(numero)

        if numero != -1:
            print("Ingrese Numero entre ",menor," y ",mayor)
            numero = int(input())

    return vec

def imprimirlista(v):
    largo = len(v)
    for i in range(largo):
        print(v[i],end="")
    print()



a = int(input("Numero 1: "))
b = int(input("Numero 2: "))




printLista = lista(a,b)

print(printLista)
imprimirlista(printLista)
