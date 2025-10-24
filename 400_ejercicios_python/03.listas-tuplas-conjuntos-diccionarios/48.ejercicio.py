def del_duplicate(lista):
    duplicados = []
    eliminated = {}  # Diccionario que podrías usar más adelante si quieres registrar los eliminados

    print("🔍 Iniciando búsqueda de duplicados...\n")

    # Recorremos cada elemento por su índice
    for i in range(len(lista)):
        print(f"➡️ i = {i}, elemento actual: {lista[i]}")
        
        # Comparamos con los elementos que vienen después
        for j in range(i + 1, len(lista)):
            print(f"   🔸 Comparando lista[{i}] = {lista[i]} con lista[{j}] = {lista[j]}")
            
            # Si encontramos un duplicado
            if lista[i] == lista[j]:
                print(f"     ✅ Coincidencia encontrada: {lista[i]}")
                
                # Si no está en la lista de duplicados, lo agregamos
                if lista[i] not in duplicados:
                    duplicados.append(lista[i])
                    print(f"     ➕ Agregado a duplicados → {duplicados}")
                else:
                    print(f"     ⚠️ {lista[i]} ya estaba registrado como duplicado")

    print("\n✅ Búsqueda finalizada.")
    print(f"📋 Duplicados encontrados: {duplicados}")
    return duplicados


# Ejemplo de uso:
lista = [1, 2, 3, 2, 4, 1, 5, 3]
del_duplicate(lista)
