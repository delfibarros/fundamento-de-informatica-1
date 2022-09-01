nota1 = int(input("Ingrese primer nota: ")) #Primero Ingreso las 2 Notas
nota2 = int(input("Ingrese segunda nota: "))

if nota1 < 0 or nota2 < 0 or nota1 > 10 or nota2 > 10: #Miro que las notas ingresadas sean entre 0 y 10
    print("ERROR")
elif nota1 >= 7 and nota2 >= 7: #Si las 2 notas son mayores o iguales a 7 promociona
    print("El alumno se encuentra promocionado")
elif nota1 >= 4 and nota2 >= 4: #Si las 2 notas son mayores  o iguales que 4 aprueba
    print("El alumno esta aprobado")
elif nota1 < 4 or nota2 < 4: #Si las 2 notas son menores a 4 debe recuperar
    print("El alunmno debe recuperar")
