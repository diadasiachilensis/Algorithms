def interpolation_search_recursive(arr, e, i=0, j=None, step=0):
    if j is None:
        j = len(arr) - 1
    encontrado = False
    
    if arr[j] != arr[i] and arr[i] <= e <= arr[j]:
        step += 1
        pos = i + ((e - arr[j]) * (j - i) // (arr[j] - arr[i]))
        print(f"DEBUG: 'low: {i}' | 'high: {j}' | 'posicion: {pos} | 'step: {step}' ")

        if e == arr[pos]:
            print(f'Valor encontrado en {step} step, en la posicion {pos}')
            encontrado = True
        elif e < arr[pos]:
            return interpolation_search_recursive(arr, e, i, pos - 1, step)
        else:
            return interpolation_search_recursive(arr, e, pos + 1, j, step)
    
    if not encontrado:
        print(f'Valor {e} no encontrado')

if __name__ == '__main__':
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
    elemento = 13
    interpolation_search_recursive(lista, elemento)
