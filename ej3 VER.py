prod = int(input("Productos: "))
base = int(input("Precio: "))

diezPor = 0
cantBase = 0
precio = 0
total = 0

prodCopy = prod

while prod != -1:

    if prod <= 12:
        precio = prod * base
        cantBase = cantBase + prod

    elif prod > 12 and prod <= 100:
        prod = prod - 12
        precio = 12 * base + prod * base

        cantBase = cantBase + 12
        diezPor = diezPor + prod


    elif prod > 100:
        prod = prod - 100
        precio = (12 * base) + (88 * (base * 0.90)) + (prod * (base * 0.75))
       
        cantBase = cantBase + 12
        diezPor = diezPor + 88

    print("-------------------------------")
    print("Precio: ", precio)
    print("Promedio: ", precio / prodCopy) 
    print("-------------------------------")

    total = total + prodCopy    

    prod = int(input("Productos: "))
    prodCopy = prod
    if prod != -1:
        base = int(input("Precio: "))
    

print("Ventas Realizadas: ", total)
print("Cantidad de Ventas que se aplico 10%: ", diezPor)
print("Cantidad de ventas que se aplico el precio base: ", cantBase)