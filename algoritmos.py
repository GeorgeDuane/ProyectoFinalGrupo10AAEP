# algoritmos.py

import heapq


#BUSQUEDA POR FUERZA BRUTA

def busqueda_fuerza_bruta(camionetas, placa):
    operaciones = 0

    for camioneta in camionetas:
        operaciones += 1

        if camioneta["placa"].upper() == placa.upper():
            return camioneta, operaciones

    return None, operaciones


#QUICKSORT - ORDENAR POR KILOMETRAJE

def quicksort(camionetas):

    if len(camionetas) <= 1:
        return camionetas

    pivote = camionetas[len(camionetas) // 2]["kilometraje"]

    menores = [
        c for c in camionetas
        if c["kilometraje"] < pivote
    ]

    iguales = [
        c for c in camionetas
        if c["kilometraje"] == pivote
    ]

    mayores = [
        c for c in camionetas
        if c["kilometraje"] > pivote
    ]

    return quicksort(menores) + iguales + quicksort(mayores)


# DIJKSTRA - RUTAS MINIMAS

def dijkstra(grafo, inicio):

    distancias = {
        nodo: float("inf")
        for nodo in grafo
    }

    distancias[inicio] = 0

    cola = [(0, inicio)]

    while cola:

        distancia_actual, nodo_actual = heapq.heappop(cola)

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafo[nodo_actual].items():

            nueva_distancia = distancia_actual + peso

            if nueva_distancia < distancias[vecino]:

                distancias[vecino] = nueva_distancia

                heapq.heappush(
                    cola,
                    (nueva_distancia, vecino)
                )

    return distancias