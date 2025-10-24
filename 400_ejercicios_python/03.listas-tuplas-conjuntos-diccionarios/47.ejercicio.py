def search_word(A, B):
    print(f"🔎 Comparando las letras de '{A}' con las letras de '{B}'...\n")
    # Bucle externo: recorre cada letra de A
    for i in A:
        print(f"\n➡️ Nueva letra de A: '{i}'")
        # Bucle interno: recorre cada letra de B
        for j in B:
            print(f"   - Comparando '{i}' con '{j}'...")
            if i == j:
                print(f"     🎯 Coincidencia encontrada -> '{i}' está en B")
                break  # salimos del bucle interno y pasamos a la siguiente letra de A
            else:
                print(f"     ❌ No coincide, seguir buscando en B...")
        print(f"   🔁 Fin de recorrido de B para la letra '{i}'")
    print("\n✅ Fin de comparación entre cadenas.")

A = "sol"
B = "abscsolwxyz"
search_word(A, B)