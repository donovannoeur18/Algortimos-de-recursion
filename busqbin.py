def busqueda_binaria_recursiva(lista_ordenada, objetivo, bajo, alto):
    if alto < bajo:
        return -1

    medio = (alto + bajo) // 2

    if lista_ordenada[medio] == objetivo:
        return medio
    elif objetivo < lista_ordenada[medio]:
        return busqueda_binaria_recursiva(lista_ordenada, objetivo, bajo, medio - 1)
    else:
        return busqueda_binaria_recursiva(lista_ordenada, objetivo, medio + 1, alto)

mi_lista = [1, 5, 7, 10, 12, 15, 20]
elemento_a_buscar = 12
indice = busqueda_binaria_recursiva(mi_lista, elemento_a_buscar, 0, len(mi_lista) - 1)

if indice != -1:
    print(f"El elemento está en el índice: {indice}")
else:
    print("El elemento no se encontró en la lista.")