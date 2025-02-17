def Construir_tablero(lis):
    matriz = ""
    for a in range(0, 9):
        fila = ""
        for b in range(0, 9):
            fila += f"{lis[a][b]} "
        fila += "\n"
        matriz += fila
    return matriz

def Mover_ficha(jugada,matriz_jugada):
    dic = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    j_list = []
    for caracter in jugada:
        j_list.append(caracter)
    ficha = matriz_jugada[int(j_list[1])][dic[j_list[0]]]
    matriz_jugada[int(j_list[1])][dic[j_list[0]]] = "-"
    matriz_jugada[int(j_list[3])][dic[j_list[2]]] = ficha
    return matriz_jugada

def final(matriz_jugada):
    if matriz_jugada[7] == ["7", "-", "O", "-", "O", "-", "O", "-", "O"] and matriz_jugada[8] == ["8", "O", "-", "O", "-", "O", "-", "O", "-"]:
        return "O"
    elif matriz_jugada[1] == ["1", "-", "X", "-", "X", "-", "X", "-", "X"] and matriz_jugada[2] == ["2", "X", "-", "X", "-", "X", "-", "X", "-"]:
        return "X"
