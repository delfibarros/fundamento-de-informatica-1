def extraerDigito(numero, cifra):
    
    numeroaux2 = numero

    if numero < 0:
        numero = numero * -1
    
    numeroaux1 = numero
    digitos = 0

    while numero != 0:
        numero = numero // 10 
        digitos += 1

    if cifra > digitos:
        return -1
        
    else:
        numeroaux1 = numeroaux1 // (10 ** (cifra))
        numeroaux1 = numeroaux1 % 10

    if numeroaux2 < 0:
        numeroaux1 = numeroaux1 * -1

    return numeroaux1


numero = int(input("Numero: "))
digito = int(input("Digito: "))

print(extraerDigito(numero, digito))