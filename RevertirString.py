#letra = input("ingresa una letra que quieras invertir ")
palabra = "hola"
palabra_invertida = ""
def recorrer(a):
    global palabra_invertida
    if len(a) == 0:
        return 0
    palabra_invertida += a[-1]
    return recorrer(a[:-1]) 
print(recorrer(palabra))
print(palabra_invertida)