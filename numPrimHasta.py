numero=int(input("Ingrese hasta qué número se mostrarán los números primos: "))
for numero in range (1,numero):
    if numero>1:
        contador=0
        i=2
        while i<numero and contador==0:   
            residuo=numero%i
            if residuo==0:
                contador+=1
            i+=1
        if contador==0:
            print (numero)