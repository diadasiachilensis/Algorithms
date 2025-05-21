#Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
#Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media.
#El programa pedirá el número de días que se van a introducir.




def medianTemperature(a,b):
    temp=(a+b)//2
    print(f"La mediana de la temperatura deurate un dia fue de {temp} °C")



if __name__ == "__main__":
    numDays=int(input("¿Cuántos días se van a introducir? "))
    for i in range(numDays):
        maxTemp=float(input(f"Introduzca la temperatura máxima del día {i+1}: "))
        minTemp=float(input(f"Introduzca la temperatura mínima del día {i+1}: "))
        medianTemperature(maxTemp,minTemp)