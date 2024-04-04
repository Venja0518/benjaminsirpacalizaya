numeroParaVerificar=int(input("ingrese el numero para verficar: "))
if numeroParaVerificar>1:
    contador=0
    for i in range(2,numeroParaVerificar):
         residuo=numeroParaVerificar%i
         if residuo==0:
            contador +=1
    if contador==0:
        print("El",numeroParaVerificar,"Es un numero primo")
    else:
        print("El",numeroParaVerificar,"No es un numero primo")
else:
     print("El",numeroParaVerificar,"No es un numero primo")