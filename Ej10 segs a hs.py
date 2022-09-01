segundos = int(input("Ingrese periodo en segundos: "))

dias = segundos // (24*60*60)
segundos = segundos % (24*60*60)

horas = segundos // (60*60)
segundos = segundos % (60*60)

minutos = segundos // 60
segundos = segundos % 60

print("Dias: ", dias," Horas: ", horas," Minutos: ", minutos, " Segundos: ", segundos)