import datetime
ingreso=input("Iniciar programa : Presione Enter ")
print("Ingreso OK")
date=datetime.datetime.now()
tiempo=date.hour
print(f"Hora Actual: {tiempo}")

if tiempo < 12:
    print("Buenos Dias, Bienvenido")
elif 12 <= tiempo <= 18:
    print("Buenas Tardes, Bienvenido")
else:
    print("Buenas Noches, Bienvenido")





