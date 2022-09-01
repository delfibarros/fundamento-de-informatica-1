dinero = int(input("Ingrese la cantidad de dinero: "))

mil = dinero // 1000
pesosrestantes = dinero % 1000

quinintos = pesosrestantes // 500
pesosrestantes = pesosrestantes % 500

cien = pesosrestantes // 100
restocien = pesosrestantes % 100

cincuenta = pesosrestantes // 50
pesosrestantes = pesosrestantes % 50

diez = pesosrestantes // 10
pesosrestantes = pesosrestantes % 10

uno = pesosrestantes


if uno > 0:
    print("No tenemos $", uno, "en billetes. ERROR")
elif uno == 0:
    print("Mil: ", mil, "Quinientos: ", quinintos, "Cien: ", cien, " Cincuenta: ", cincuenta, "Diez: ", diez)
    