def mcd(x, y):
    if y==0:  
        return x   
    else:           
        return mcd(y,x%y)  
  
a = int(input("Numero1: "))
b = int(input("Numero2: "))
  
print("Maximo Comun Divisor:",mcd(a,b))