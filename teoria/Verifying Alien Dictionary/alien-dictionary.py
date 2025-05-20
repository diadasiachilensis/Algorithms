order= ["hlabcdfgijkmnopqrstuvwxyz"]

def alien_sorted(words,order):
    #1. Hacemos un diccionario que le dice cada letra que posicion tiene
    #Por ejemplo, si order = "bac...", entonces 'b' → 0, 'a' → 1, 'c' → 2, ...
    for i in range(len(order)):
        letter=order[i]
        letter_order[letter]=i

    #2. Funcion para comprara dos palabras segun nuestro diccionario alienigena 
    def compare(w1,w2):
        #Miramos letra por letra hasta que una sea distinta
        n=min(len(w1),len(w2))
        for j in range(n):
            # si la letra de w1 va antes en el diccionario, w1 < w2 → OK
            if letter_order[w1[j]] < letter_order[w2[j]]:
                print(f"{w1} < {w2} → ✅")
                return True
            #si va despues, ya sabemos que no esta ordenado
            