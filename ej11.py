def digitocentral(numero):
    digitos = 0
    numeroaux = numero

    while numero != 0:
        numero = numero // 10 
        digitos += 1
    
    if digitos % 2 != 0:
        digitocentral = numeroaux // (10**(digitos // 2))
        digitocentral = digitocentral % 10    

        return digitocentral

    else:
        return -1

print("Digito Central: ", digitocentral(12345678989))