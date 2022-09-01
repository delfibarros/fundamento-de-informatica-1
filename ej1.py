def multi(a,b):
   contador = 0
   total = 0
   while contador < b:
      total += a
      contador += 1
   return total

num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero:"))
print(num1,"*",num2,"=",multi(num1,num2))

