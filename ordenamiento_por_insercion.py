import random

def ordenamiento_por_insercion(lista):

    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion_actual = i
        print(posicion_actual)
        print(valor_actual)
        print(i)

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
        print(lista)

    return lista



if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista?'))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)