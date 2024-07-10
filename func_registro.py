import json

def guardar_matrices_en_json(matrices, nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        json.dump(matrices, archivo)

def leer_matrices_desde_json(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        matrices = json.load(archivo)
    return matrices

def imprimir_juegos(matrices):
    guardar_matrices_en_json(matrices, "juegos_guardados.json")

    # Leer múltiples matrices desde un archivo JSON
    matrices_leidas = leer_matrices_desde_json("juegos_guardados.json")

    # Imprimir las matrices leídas
    for i, matriz in enumerate(matrices_leidas):
        print(f"Partida {i + 1}:")
        tablero = ""
        for a in range(0, 9):
            fila = ""
            for b in range(0, 9):
                fila += f"{matriz[a][b]} "
            fila += "\n"
            tablero += fila
        print(tablero)