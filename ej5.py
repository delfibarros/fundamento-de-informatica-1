paginas = int(input("Paginas: "))

pagina = 3.20
basico = 500
adicional = 0

if paginas > 300 and paginas < 600:
    adicional = 200
elif paginas > 600:
    adicional = 536

print("Coste: ", pagina*paginas + adicional + basico)

    


