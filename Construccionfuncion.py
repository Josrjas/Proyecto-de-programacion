matriz_inicial = [[" ","A","B","C","D","E","F","G","H"],
                  ["1","-","O","-","O","-","O","-","O"],
                  ["2","O","-","O","-","O","-","O","-"],
                  ["3","-","-","-","-","-","-","-","-"],
                  ["4","-","-","-","-","-","-","-","-"],
                  ["5","-","-","-","-","-","-","-","-"],
                  ["6","-","-","-","-","-","-","-","-"],
                  ["7","-","X","-","X","-","X","-","X"],
                  ["8","X","-","X","-","X","-","X","-"]]

matriz_jugada = matriz_inicial
def Comprobacion_de_jugada_valida(jugada):
    if len(jugada) == 4:
        caracter_de_variable = list(jugada)
        dic = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
        Letra = ["A", "B", "C", "D", "E", "F", "G", "H"]

        # Verificar que los caracteres de las letras están en Letra y los números están en el rango correcto
        if caracter_de_variable[0] in Letra and caracter_de_variable[2] in Letra and int(caracter_de_variable[1]) in range(1, 9) and int(caracter_de_variable[3]) in range(1, 9):

            pos_fila_inicio = int(caracter_de_variable[1])
            pos_col_inicio = dic[caracter_de_variable[0]]
            pos_fila_fin = int(caracter_de_variable[3])
            pos_col_fin = dic[caracter_de_variable[2]]

            # Verificar que las posiciones de inicio y fin están dentro de los límites de la matriz
            if (1 <= pos_fila_inicio < len(matriz_jugada) and
                    1 <= pos_col_inicio < len(matriz_jugada[0]) and
                    1 <= pos_fila_fin < len(matriz_jugada) and
                    1 <= pos_col_fin < len(matriz_jugada[0])):
                ficha_fin = matriz_jugada[pos_fila_fin][pos_col_fin]

                # Verificar si la casilla de inicio contiene una ficha válida (O o X)
                ficha_inicio = matriz_jugada[pos_fila_inicio][pos_col_inicio]
                if ficha_inicio in ["O", "X"] and ficha_fin not in ["O","X"]:

                    # Verificar que la casilla de destino está vacía o contiene una ficha oponente
                    ficha_fin = matriz_jugada[pos_fila_fin][pos_col_fin]
                    if ficha_fin == "-" or ficha_fin in ["X", "O"]:

                        # Calcular las distancias entre las posiciones
                        dif_filas = abs(pos_fila_fin - pos_fila_inicio)
                        dif_cols = abs(pos_col_fin - pos_col_inicio)

                        # Verificar los movimientos válidos
                        if dif_filas == 2 and dif_cols == 2:
                                if matriz_jugada[(pos_fila_inicio + pos_fila_fin)//2][(pos_col_inicio + pos_col_fin)//2] != "-":
                                    return True
                                else:
                                    return False
                        elif dif_filas == 1 and dif_cols == 1:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
def Permitido_al_jugador(jugada,contador):
    caracter_de_variable = []
    dic = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    for caracter in jugada:
        caracter_de_variable.append(caracter)
    if contador%2 == 0 and (matriz_jugada[int(caracter_de_variable[1])][dic[caracter_de_variable[0]]]) == "O":
        return True
    elif contador%2 == 1 and (matriz_jugada[int(caracter_de_variable[1])][dic[caracter_de_variable[0]]]) == "X":
        return True
    else:
        return False
