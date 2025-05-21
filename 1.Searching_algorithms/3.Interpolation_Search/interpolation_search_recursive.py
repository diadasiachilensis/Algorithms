def interpolation_search_recursive(lista, elemento, left=0, right=None, pasos=0):
    if right is None:
        right = len(lista) - 1
    encontrado = False
    
    if lista[right] != lista[left] and lista[left] <= elemento <= lista[right]:
        pasos += 1
        mid = left + (elemento - lista[left]) * (right - left) // (lista[right] - lista[left])  # Use '/' instead of '//'
        
        print(f"DEBUG: 'left: {left}' | 'right: {right}' | 'medio: {mid}")
            
        if elemento == lista[mid]:
            print(f'Valor encontrado en {pasos} pasos, en la posicion {mid}')
            encontrado = True
        elif elemento < lista[mid]:
            return interpolation_search_recursive(lista, elemento, left, mid - 1, pasos)
        else:
            return interpolation_search_recursive(lista, elemento, mid + 1, right, pasos)
    
    if not encontrado:
        print(f'Valor {elemento} no encontrado')

if __name__ == '__main__':
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    elemento = 13
    interpolation_search_recursive(lista, elemento)
