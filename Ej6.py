km = int(input("Ingrese los km que desea realizar: "))
minimo = 150

if km > 0 and km < 10:
    porkm = 20
elif km >= 10:
    porkm = 15
    
print("Coste: ", minimo + km * porkm)