def contar_elementos(list_bulleye,p):
    dictionary= {}
    n=0
    for i in list_bulleye:
        if i == p:
            n += 1
            dictionary[i] = n
    print(dictionary)
    return dictionary
    

elements = ["apple", "banana", "apple", "orange", "banana", "apple", "kiwi", "orange", "kiwi", "kiwi"]
a="banana"
contar_elementos(elements,a)