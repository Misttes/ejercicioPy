import random

def confirmarEntero():
    ingreso=True
    while ingreso==True:
        ingreso=False
        
        valor=input("Ingresar valor: ")
        valorLista = list(valor)
        i=0
        longitudLista=len(valorLista)
        fin=True
        val=True
        while fin==True:
            while i < longitudLista:
                if valorLista[i] in ("0","1","2","3","4","5","6","7","8","9"):
                    i=i+1
                else:
                    print("Sólo usar Números Enteros")
                    val=False
                    break
            fin=False

        if val==True:
            valor=int(valor)
            return(valor)
        else:
            ingreso=True

print("Ingrese Saldo: ")
saldo=confirmarEntero()

saldoJugador=saldo
saldoMaquina=saldo

print("iniciando Ronda")
game=True

while game == True:
    print(f"Saldo JUGADOR: {saldoJugador}")
    print(f"Saldo MAQUINA: {saldoMaquina}")
    print("Ingrese valor a apostar: ")
    valorApuesta=confirmarEntero()
    if valorApuesta <= saldoJugador:
        if valorApuesta <= saldoMaquina:
            print("Inicia Juego")
            puntosJugador=0
            puntosMaquina=0
            print("Ingrese número de rondas")
            rondas=confirmarEntero()
            turno=1
            while rondas > 0:
                print(f"Ronda {turno}")
                turno=turno+1
                lanzar=input("Lanzar, Presione ENTER ")
                lanzamientoJugador=random.randint(1,6)
                print(f"Lanzamiento Jugador: {lanzamientoJugador}")
                lanzar=input("Lanzar, Presione ENTER ")
                lanzamientoMaquina=random.randint(1,6)
                print(f"Lanzamiento Maquina: {lanzamientoMaquina}")
                if lanzamientoJugador > lanzamientoMaquina:
                    puntosJugador=puntosJugador+1   
                    rondas=rondas-1                
                elif lanzamientoJugador < lanzamientoMaquina:
                    puntosMaquina=puntosMaquina+1
                    rondas=rondas-1
                else:
                    print("Volver a lanzar")
                    turno=turno-1
            if puntosJugador > puntosMaquina:
                saldoJugador=saldoJugador+valorApuesta
                saldoMaquina=saldoMaquina-valorApuesta
            elif puntosJugador < puntosMaquina:
                saldoMaquina=saldoMaquina+valorApuesta
                saldoJugador=saldoJugador-valorApuesta
            else:
                print("Empate")
                print(f"Su saldo es: {saldoJugador}")
                print(f"Saldo de Maquina: {saldoMaquina}")

        else:
            print("Máquina sin saldo")
            print(f"Saldo de Maquina: {saldoMaquina}")
    else:
        print("Sin saldo para apostar") 
        print(f"Su saldo es: {saldoJugador}") 
    if saldoJugador <= 0:
        print("SIN SALDO")
        print("Gana Maquina")
        print(f"Saldo MAQUINA: {saldoMaquina}")
        game = False
    elif saldoMaquina <= 0:
        print("SIN SALDO EN MAQUINA")
        print("Gana Jugador")
        print(f"Saldo JUGADOR: {saldoJugador}")
        game = False


