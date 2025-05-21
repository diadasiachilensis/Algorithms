import io
import sys

def procedimiento(list1):
    for i in list1:
        d=i*"*"
        print(d)

def capturar_salida(func, *args):
    """ Captura la salida de print para poder hacer pruebas con assert """
    salida_capturada = io.StringIO()
    sys.stdout = salida_capturada  # Redirigir la salida estándar a la variable
    func(*args)  # Llamar la función
    sys.stdout = sys.__stdout__  # Restaurar salida estándar
    return salida_capturada.getvalue().strip()  # Retornar la salida capturada sin espacios extra

if __name__ == "__main__":
    # 🔹 Pruebas con assert para procedimiento()
    assert capturar_salida(procedimiento, [4, 9, 7]) == "****\n*********\n*******"
    assert capturar_salida(procedimiento, [1, 2, 3]) == "*\n**\n***"
    assert capturar_salida(procedimiento, [5, 5, 5]) == "*****\n*****\n*****"
    assert capturar_salida(procedimiento, []) == ""  # Caso con lista vacía
    assert capturar_salida(procedimiento, [10]) == "**********"  # Caso con un solo número
    assert capturar_salida(procedimiento, [2, 4, 6, 8]) == "**\n****\n******\n********"  # Secuencia ascendente

    print("✅ Todas las pruebas pasaron correctamente.")
