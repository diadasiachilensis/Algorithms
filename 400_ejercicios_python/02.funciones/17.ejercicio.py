#Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra.
#Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

def convertir_estado(f):
    f_cambia=" ".join(f)
    print(f_cambia)

if __name__ == "__main__":
    frase=input("Ingrese frase: ")
    convertir_estado(frase)