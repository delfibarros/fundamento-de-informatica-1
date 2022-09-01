cliente = int(input("Numero de Cliente: "))
factura = int(input("Factura Dinero: "))

print("------------------------------")

print("Si paga dentro del 1 - 10: ")
if 0.02 * factura > 200:
    print("Descuento: ", "$", factura * 0.02, " Total: ", factura - factura * 0.02)
elif 0.02 * factura < 200:
    print("Descuento: ", "$200 ", "Total: ", factura - 200)

print("Si paga dentro del 10 - 20: ")
print("Debera pagar: ", factura)

print("Si paga dentro del 20 - 30: ")
if 350 > factura * 0.10:
    print("Multa de: ", 350, " Total: ", factura + 350)
elif 350 < factura * 0.10:
    print("Multa de: ", factura * 0.10, " Total: ", factura + factura * 0.10)