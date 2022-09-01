def restoMes(dia, mes, año):

    if año%4 == 0 and año%100 == 0 and año%400 == 0:
        diasfebrero = 29
    elif año%4 == 0 and año%100 != 0:
        diasfebrero = 29
    elif año%4 == 0 and año%100 != 0 and año%400 != 0:
        diasfebrero = 28
    else:
        diasfebrero = 28

    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias = 30
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias = 31
    elif mes == 2: 
        dias = diasfebrero

    diasRestantes = dias - dia

    return diasRestantes


def restoDiasAño(dia, mes, año):

    if año%4 == 0 and año%100 == 0 and año%400 == 0:
        diasfebrero = 29
    elif año%4 == 0 and año%100 != 0:
        diasfebrero = 29
    elif año%4 == 0 and año%100 != 0 and año%400 != 0:
        diasfebrero = 28
    else:
        diasfebrero = 28

    if diasfebrero == 29:
        diasAñoRestantes = 366
    else: 
        diasAñoRestantes = 365
    
    diasTranscurridos = dia
    mes -= 1

    while mes != 0:
        if mes == 4 or mes == 6 or mes == 9 or mes == 11: #30 Dias
            dias = 30
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: #31 Dias
            dias = 31
        elif mes == 2: 
            dias = diasfebrero
        
        diasTranscurridos = diasTranscurridos + dias
        mes -= 1
    
    return (diasAñoRestantes - diasTranscurridos)

def diasTranscurridosAño(dia, mes, año):

    if año%4 == 0 and año%100 == 0 and año%400 == 0:
        diasfebrero = 29
    elif año%4 == 0 and año%100 != 0:
        diasfebrero = 29
    elif año%4 == 0 and año%100 != 0 and año%400 != 0:
        diasfebrero = 28
    else:
        diasfebrero = 28
    
    diasTranscurridos = dia
    mes -= 1

    while mes != 0:
        if mes == 4 or mes == 6 or mes == 9 or mes == 11: #30 Dias
            dias = 30
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: #31 Dias
            dias = 31
        elif mes == 2: 
            dias = diasfebrero
        
        diasTranscurridos = diasTranscurridos + dias
        mes -= 1
    
    return (diasTranscurridos)

def tiempoTranscurrido(dia1, mes1, año1, dia2, mes2, año2):
#años
    años = 0
    while año1 != año2:
        if año1 > año2:
            año1 -= 1
        elif año2 > año1:
            año2 -= 1
        años += 1 
#meses
    meses = 0
    while mes1 != mes2:
        if mes1 > mes2:
            mes1 -= 1
        elif mes2 > mes1:
            mes2 -= 1

        meses += 1

#dias
    dias = 0
    while dia1 != dia2:
        if dia1 > dia2:
            dia1 -= 1
        elif dia2 > dia1:
            dia2 -= 1
        dias += 1

    tiempo = str(dias) + " Dias " + str(meses) + " Meses " + str(años) + " Años "

    return tiempo

print("Dias para fin de mes: ", restoMes(16,1,2003))   #Poner Fecha
print("Dias para fin de año: ", restoDiasAño(16,1,2003)) #Poner Fecha
print("Dias transucrridos: ", diasTranscurridosAño(16,1,2003)) #Poner Fecha
print("Tiempo transcurrido: ", tiempoTranscurrido(20, 1, 2010, 16, 4, 2003)) #Poner Fecha