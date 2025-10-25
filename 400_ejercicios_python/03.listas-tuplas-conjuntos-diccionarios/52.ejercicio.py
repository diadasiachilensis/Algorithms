"""
52)Calcular Histograma: Crea un histograma de letras a partir de una cadena de texto.
"""
texto = "La programación en Python es poderosa y divertida"

def histogram_dic(texto):
    list_word=texto.lower()
    letra={}
    for char in list_word:
        if char.isalpha():
            if char not in letra:
                letra[char] = 1
                print(f"Nueva letra -> {char}")
            else: 
                letra[char] += 1
                print(f"letra {char} incrementada en {letra[char]}")
        else:
            print(f"Caracter ignorado: {char} no es una letra")
    print("Histograma final")
    for k,v in letra.items():
        print(f"{k} : {"*"*v} {v}")

histogram_dic(texto)