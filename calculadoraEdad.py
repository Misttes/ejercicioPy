#problema 1 
import datetime
nacimiento = int(input("ingrese año de nacimiento: "))

def edad_actual(nacimiento):
    date=datetime.datetime.now()
    year=date.year
    print(f"En {year}")
    edad=year-nacimiento
    print(f"la edad es: {edad}")
    
edad_actual(nacimiento)
