#28 = Febrero2
#30 = Abril4  Junio6 Setiembre9 Noviembre11
#31 = Enero1 Marzo3 Mayo5 Julio7 Agosto8 Octubre10 Diciembre12


dia = int(input("Dia: "))
mes = int(input("Mes: "))
año = int(input("Año: "))
mesfebrero = 0

print(dia,"/",mes,"/",año)

n = int(input("Cuantos dias le queres sumar?: "))



while n > 0:
    n -= 1
    dia += 1
    
    if año%4 == 0 and año%100 == 0 and año%400 == 0:
        mesfebrero = 29
    elif año%4 == 0 and año%100 != 0:
        mesfebrero = 29
    else:
        mesfebrero = 28

    if dia > 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        mes += 1
        dia -= 31
    elif dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        mes += 1
        dia -= 30
    elif dia > mesfebrero and mes == 2:
        mes += 1
        dia -= mesfebrero

    if mes == 13:
        mes = 1
        año = año + 1

        
print(dia,"/",mes,"/",año)