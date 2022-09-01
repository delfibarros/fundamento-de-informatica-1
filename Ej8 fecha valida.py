#30 = Abril Junio Septiembre Noviembre
#31 = Enero Marzo Mayo Julio Agosto Octubre Diciembre
#28 = Febrero

dia = int(input("Dia: "))
mes = int(input("Mes: "))
año = int(input("Año: "))


if año%4 == 0 and año%100 == 0 and año%400 == 0:
    diasfebrero = 29
elif año%4 == 0 and año%100 != 0:
    diasfebrero = 29
elif año%4 == 0 and año%100 != 0 and año%400 != 0:
    diasfebrero = 28
else:
    diasfebrero = 28


if mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia > 0 and dia <= 31 and año > 0:
     print("Es valido")
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dia > 0 and dia <= 31 and año > 0:
    print("Es valido")
elif mes == 2 and dia > 0 and dia <= diasfebrero and año > 0:
    print("Es Valido")
else:
    print("No es valido")