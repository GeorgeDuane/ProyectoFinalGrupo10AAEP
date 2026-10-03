# main.py

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from datos import camionetas, grafo

from algoritmos import (
    busqueda_fuerza_bruta,
    quicksort,
    dijkstra
)


# FUNCIONES DEL APLICATIVO

def limpiar_campos():

    entrada_placa.delete(0, tk.END)
    entrada_responsable.delete(0, tk.END)
    entrada_km.delete(0, tk.END)
    entrada_combustible.delete(0, tk.END)

    combo_estado.set("Disponible")


def registrar_camioneta():

    placa = entrada_placa.get().strip().upper()
    responsable = entrada_responsable.get().strip()
    km = entrada_km.get().strip()
    combustible = entrada_combustible.get().strip()
    estado = combo_estado.get()

    # Validar campos vacios
    if not placa or not responsable or not km or not combustible:

        messagebox.showwarning(
            "Datos incompletos",
            "Complete todos los campos."
        )

        return

    # Validar kilometraje y combustible
    try:
        km = int(km)
        combustible = int(combustible)

    except ValueError:

        messagebox.showerror(
            "Error",
            "Kilometraje y combustible deben ser numeros."
        )

        return

    # Validar porcentaje de combustible
    if combustible < 0 or combustible > 100:

        messagebox.showerror(
            "Error",
            "El combustible debe estar entre 0 y 100."
        )

        return

    # Registrar nueva camioneta
    camionetas.append({

        "placa": placa,
        "responsable": responsable,
        "kilometraje": km,
        "combustible": combustible,
        "estado": estado

    })

    messagebox.showinfo(
        "Registro",
        "Camioneta registrada correctamente."
    )

    limpiar_campos()

    mostrar_camionetas()


# MOSTRAR RESULTADOS

def escribir_resultado(texto):

    area_resultado.delete("1.0", tk.END)

    area_resultado.insert(
        tk.END,
        texto
    )


# MOSTRAR CAMIONETAS

def mostrar_camionetas():

    texto = "CAMIONETAS REGISTRADAS\n"

    texto += "-" * 75 + "\n"

    for c in camionetas:

        texto += (
            f"Placa: {c['placa']} | "
            f"Responsable: {c['responsable']} | "
            f"KM: {c['kilometraje']} | "
            f"Combustible: {c['combustible']}% | "
            f"Estado: {c['estado']}\n"
        )

    escribir_resultado(texto)


# BUSQUEDA POR FUERZA BRUTA

def buscar_camioneta():

    placa = simpledialog.askstring(
        "Buscar camioneta",
        "Ingrese la placa:"
    )

    if not placa:
        return

    resultado, operaciones = busqueda_fuerza_bruta(
        camionetas,
        placa
    )

    if resultado:

        texto = (
            "CAMIONETA ENCONTRADA\n"
            "--------------------------\n"
            f"Placa: {resultado['placa']}\n"
            f"Responsable: {resultado['responsable']}\n"
            f"Kilometraje: {resultado['kilometraje']} km\n"
            f"Combustible: {resultado['combustible']}%\n"
            f"Estado: {resultado['estado']}\n"
            f"Operaciones realizadas: {operaciones}"
        )

    else:

        texto = (
            "Camioneta no encontrada.\n"
            f"Operaciones realizadas: {operaciones}"
        )

    escribir_resultado(texto)


# ORDENAR POR KILOMETRAJE

def ordenar_por_km():

    ordenadas = quicksort(
        camionetas.copy()
    )

    texto = "CAMIONETAS ORDENADAS POR KILOMETRAJE\n"

    texto += "-" * 50 + "\n"

    for c in ordenadas:

        texto += (
            f"{c['placa']} - "
            f"{c['kilometraje']} km - "
            f"{c['responsable']} - "
            f"{c['estado']}\n"
        )

    escribir_resultado(texto)


# CALCULAR RUTA CON DIJKSTRA

def ejecutar_dijkstra():

    inicio = simpledialog.askstring(
        "Calcular ruta",
        "Ingrese punto de inicio:\n\n"
        "Base\n"
        "Almacen\n"
        "Site A\n"
        "Site B"
    )

    if not inicio:
        return

    equivalencias = {

        "base": "Base",
        "almacen": "Almacen",
        "site a": "Site A",
        "site b": "Site B"

    }

    nodo = equivalencias.get(
        inicio.strip().lower()
    )

    if nodo not in grafo:

        messagebox.showerror(
            "Error",
            "Punto de inicio no valido."
        )

        return

    distancias = dijkstra(
        grafo,
        nodo
    )

    texto = f"RUTAS DESDE: {nodo}\n"

    texto += "-" * 35 + "\n"

    for destino, distancia in distancias.items():

        texto += (
            f"{nodo} -> {destino}: "
            f"{distancia} km\n"
        )

    escribir_resultado(texto)


# INTERFAZ GRAFICA

ventana = tk.Tk()

ventana.title(
    "Control Basico de Flota"
)

ventana.geometry(
    "900x600"
)

ventana.resizable(
    False,
    False
)


# TITULO

titulo = tk.Label(

    ventana,

    text="CONTROL BASICO DE FLOTA DE CAMIONETAS",

    font=("Arial", 16, "bold")

)

titulo.pack(
    pady=10
)


# REGISTRO DE CAMIONETAS

marco_datos = tk.LabelFrame(

    ventana,

    text="Registro de camioneta",

    padx=10,

    pady=10

)

marco_datos.pack(
    fill="x",
    padx=20
)


# Placa

tk.Label(
    marco_datos,
    text="Placa:"
).grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)

entrada_placa = tk.Entry(
    marco_datos,
    width=20
)

entrada_placa.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)


# Responsable

tk.Label(
    marco_datos,
    text="Responsable:"
).grid(
    row=0,
    column=2,
    padx=5,
    pady=5
)

entrada_responsable = tk.Entry(
    marco_datos,
    width=25
)

entrada_responsable.grid(
    row=0,
    column=3,
    padx=5,
    pady=5
)


# Kilometraje

tk.Label(
    marco_datos,
    text="Kilometraje:"
).grid(
    row=1,
    column=0,
    padx=5,
    pady=5
)

entrada_km = tk.Entry(
    marco_datos,
    width=20
)

entrada_km.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)


# Combustible

tk.Label(
    marco_datos,
    text="Combustible (%):"
).grid(
    row=1,
    column=2,
    padx=5,
    pady=5
)

entrada_combustible = tk.Entry(
    marco_datos,
    width=25
)

entrada_combustible.grid(
    row=1,
    column=3,
    padx=5,
    pady=5
)


# Estado

tk.Label(
    marco_datos,
    text="Estado:"
).grid(
    row=2,
    column=0,
    padx=5,
    pady=5
)

combo_estado = ttk.Combobox(

    marco_datos,

    values=[
        "Disponible",
        "Asignada",
        "Mantenimiento"
    ],

    state="readonly",

    width=18

)

combo_estado.grid(
    row=2,
    column=1,
    padx=5,
    pady=5
)

combo_estado.set(
    "Disponible"
)


# Boton registrar

tk.Button(

    marco_datos,

    text="Registrar camioneta",

    command=registrar_camioneta,

    width=20

).grid(

    row=2,

    column=3,

    padx=5,

    pady=5
)


# FUNCIONES DE FLOTA

marco_botones = tk.LabelFrame(

    ventana,

    text="Funciones del control de flota",

    padx=10,

    pady=10
)

marco_botones.pack(
    fill="x",
    padx=20,
    pady=10
)


botones = [

    (
        "Mostrar camionetas",
        mostrar_camionetas
    ),

    (
        "Buscar camioneta",
        buscar_camioneta
    ),

    (
        "Ordenar por kilometraje",
        ordenar_por_km
    ),

    (
        "Calcular rutas",
        ejecutar_dijkstra
    )

]


for i, (texto, funcion) in enumerate(botones):

    tk.Button(

        marco_botones,

        text=texto,

        command=funcion,

        width=22

    ).grid(

        row=0,

        column=i,

        padx=5,

        pady=5
    )


# RESULTADOS

marco_resultado = tk.LabelFrame(

    ventana,

    text="Resultados",

    padx=10,

    pady=10
)

marco_resultado.pack(

    fill="both",

    expand=True,

    padx=20,

    pady=5
)


area_resultado = tk.Text(

    marco_resultado,

    width=100,

    height=18
)

area_resultado.pack(

    fill="both",

    expand=True
)


# Mostrar datos al iniciar
mostrar_camionetas()


# Iniciar interfaz
ventana.mainloop()