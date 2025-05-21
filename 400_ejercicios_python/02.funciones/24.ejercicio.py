d=0
m=0
a=0
total=0
bisiesto=False
# Diccionarios de días por mes
mes_bisiesto = {
    1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
    8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
mes_no_bisiesto = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
    8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

def menu():
    print("Detector de día juliano \nIntroduzca la fecha\n")
    
    # Leer la fecha correctamente
    d, m, a = leer_fecha()
    
    # Determinar si el año es bisiesto
    bisiesto = es_bisiesto(a)
    
    # Calcular el total de días hasta el mes anterior
    total = calcular_total_meses(m, bisiesto)
    
    # Sumar los días del mes actual
    total = calcular_juliano(d, total)

    # Imprimir el resultado final
    print(f"El día juliano para la fecha {d}-{m}-{a} es {total}")

def leer_fecha():
    while True:
        try: 
            d=int(input("introduzca el día: "))
            m=int(input("introduzca el mes (numero): "))
            a=int(input("introduzca el año: "))
            if not (1<=d<=31):
                print("debe ingresar un dia entre el 1 al 31: ")
                continue
            if not (1<=m<=12):
                print("debe ingresar un mes entre el 1 al 12: ")
                continue
            if a <= 0:
                print("debe ser un numero entero positivo: ")
                continue
            return d,m,a
        except ValueError:
            raise ValueError("Debe cumplir con lo solicitado")

# Función para determinar si es bisiesto
def es_bisiesto(a):
    return (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)

def calcular_total_meses(m, bisiesto):
    # Elegimos el diccionario correcto según si el año es bisiesto o no
    if bisiesto:
        diccionario_meses = mes_bisiesto
    else:
        diccionario_meses = mes_no_bisiesto

    # Inicializamos el total de días en 0
    total_dias = 0

    # Sumamos los días de los meses anteriores al mes dado
    for i in range(1, m):  # Recorremos desde el mes 1 hasta el mes anterior a 'm'
        total_dias += diccionario_meses.get(i, 0)  # Obtenemos los días del mes y los sumamos

    return total_dias  # Devolvemos la suma total
    
# Función para calcular el día juliano
def calcular_juliano(d, total):
    return total + d  # Suma el día del mes actual

if __name__ == "__main__":
    menu()