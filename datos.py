# datos.py
# Datos iniciales del aplicativo

camionetas = [
    {
        "placa": "ELM-012",
        "responsable": "Erick Lucas Marmolejo",
        "kilometraje": 52000,
        "combustible": 70,
        "estado": "Disponible"
    },
    {
        "placa": "JOQ-123",
        "responsable": "Jean Paul Ortiz",
        "kilometraje": 68000,
        "combustible": 45,
        "estado": "Asignada"
    },
    {
        "placa": "JPO-321",
        "responsable": "Jean Pier Ortiz",
        "kilometraje": 41000,
        "combustible": 85,
        "estado": "Disponible"
    }
]

# Grafo sencillo para utilizar el algoritmo de Dijkstra
grafo = {
    "Base": {"Almacen": 10, "Site A": 20},
    "Almacen": {"Base": 10, "Site B": 15},
    "Site A": {"Base": 20, "Site B": 10},
    "Site B": {"Almacen": 15, "Site A": 10}
}