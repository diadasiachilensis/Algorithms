def longitud(iterable):
    count=0
    for _ in iterable:
        count+=1
    return count

if __name__ == "__main__":
    print(longitud("Hola mundo"))
    print(longitud([1,2,3,4,5,6,7,8,9,10]))
    print(longitud((1,2,3,4,5,6,7,8,9,10)))
    print(longitud({1,2,3,4,5,6,7,8,9,10}))
    print(longitud({1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10}))