ingreso=True
while ingreso==True:
    ingreso=False
    peso=input("Ingresar peso en kilogramos: ")
    pesoLista = list(peso)
    i=0
    longitudLista=len(pesoLista)
    fin=True
    valor=True
    while fin==True:
        while i < longitudLista:
            if pesoLista[i] in ("0","1","2","3","4","5","6","7","8","9",".",","):
                if pesoLista[i] == ",":
                    print("No usar ',' Usar Punto '.' ")
                    valor=False
                    break
                i=i+1
            else:
                print("Valor Incorrecto")
                valor=False
                break
        fin=False

    if valor==True:
        peso=float(peso)
    else:
        ingreso=True

ingreso=True
while ingreso==True:
    ingreso=False
    altura=input("Ingresar altura en metros: ")
    alturaLista = list(altura)
    i=0
    longitudLista=len(alturaLista)
    fin=True
    valor=True
    while fin==True:
        while i < longitudLista:
            if alturaLista[i] in ("0","1","2","3","4","5","6","7","8","9",".",","):
                if alturaLista[i] == ",":
                    print("No usar ',' Usar Punto '.' ")
                    valor=False
                    break
                i=i+1
            else:
                print("Valor Incorrecto")
                valor=False
                break
        fin=False

    if valor==True:
        altura=float(altura)
    else:
        ingreso=True


imc = peso / altura
imc=round(imc,1)

if imc < (18.5) :
    print(f"IMC: {imc} Está por debajo de su peso ideal")
elif 18.5 < imc < 29.9:
    print(f"IMC: {imc} Está en rango saludable")
elif 25 < imc < 29.9:
    print(f"IMC: {imc} Tiene sobre-peso")
elif 30 < imc < 34.9:
    print(f"IMC: {imc} Tiene obesidad grado I")
elif 35 < imc < 39.9:
    print(f"IMC: {imc} Tiene obesidad grado II")
else:
    print(f"IMC: {imc} Tiene obesidad grado III") 