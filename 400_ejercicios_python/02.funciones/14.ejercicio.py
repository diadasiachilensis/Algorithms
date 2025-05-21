"""Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas;
pista: deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje utilizando el carácter =."""
def escribir_centrado(texto):
    ancho = 80
    espacios = (ancho - len(texto))//2
    texto_centrado = ' '*espacios+texto
    subrayado = '='*len(texto)
    
    print(texto_centrado)
    print(' ' * espacios + subrayado)


if __name__ == "__main__":
    escribir_centrado("Bienvenido al mundo de Python")