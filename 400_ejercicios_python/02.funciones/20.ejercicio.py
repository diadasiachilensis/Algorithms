def login(user,password):
    if user == "usuario1" and password == "asdasd":
        return True
    else:
        return False

if __name__=="__main__":
    i =0
    while i<3:
        user=input("Introduce tu usuario: ")
        password=input("Introduce tu contraseña: ")
        if login(user,password) == True:
            print("Bienvenido")
            break
        elif i<3:
            print("Usuario o contraseña incorrectos")
            i+=1
        elif i==3:
            print("Has superado el numero de intentos")
            break

        