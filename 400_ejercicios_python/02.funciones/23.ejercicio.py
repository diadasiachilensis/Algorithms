def convert_s(h,m,s):
    resultado= h*3600+m*60+s
    print(f"El tiempo en segundos es: {resultado}")

def convert_hms(h,m,s):
    if s<60:
        print(f"El tiempo es: {h} horas, {m} minutos, {s} segundos")
    elif s>=3600:
        return convert_hms(h+1,m,s-3600)
    else:
        return convert_hms(h,m+1,s-60)

def menu():
    while True:
        print("elija su opcion:")
        print("1.- convertir horas a segundos")
        print("2.- convertir segundos a horas")
        print("3.- salir")
        opcion = int(input("Introduce tu opcion: "))
        if opcion == 1:
            hours=int(input("Introduce las horas: "))
            minutes=int(input("Introduce los minutos: "))
            seconds=int(input("Introduce los segundos: "))
            convert_s(hours,minutes,seconds)
            break
        elif opcion == 2:
            seconds=int(input("Introduce los segundos: "))
            convert_hms(0,0,seconds)
            break
        elif opcion == 3:
            print("Hasta luego")
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    menu()