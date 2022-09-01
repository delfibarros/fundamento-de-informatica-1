#Hago la lista2 que es lista1 dada vuelta y despues comparo.

def capicua(lista):
    largo = len(lista)
    lista2 = []

    for i in range(largo-1,-1,-1): #Lista con 6 elementos / 0,1,2,3,4,5 / y si quiero que vaya la i desde 0 hasta 6 tengo que hacer (largo-1) asi empieza el digito 5 y que termine en -1 (Osea en 0)
        lista2.append(lista[i])
    
    print(lista)
    print(lista2)

    if lista == lista2:
        print("Es Capicua")
    else:
        print("No es Capicua")


vec = [1,2,2,3,2,2,1]
vec2 = [1,2,3,4,5,4,3]

capicua(vec)

capicua(vec2)