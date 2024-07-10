import random
def valorar_movimientos(ficha, matriz_jugada, turno):
    def esta_en_rango(x, y):
        return 1 <= x <= 8 and 1 <= y <= 8
    
    def puede_saltar(matriz_jugada, x, y, x2, y2):
        return (matriz_jugada[x][y] in ["O", "X"]) and (matriz_jugada[x2][y2] == "-")

    lista = {}
    x = int(ficha[0])
    y =int(ficha[1])
    
    # Se asigna un puntaje a cada movimiento y se guarda en un diccionario
    if turno: # Juega con "X"
        if esta_en_rango(x - 2, y + 2) and puede_saltar(matriz_jugada, x - 1, y + 1, x - 2, y + 2):
            lista[ficha] = 4
        elif esta_en_rango(x - 2, y - 2) and puede_saltar(matriz_jugada, x - 1, y - 1, x - 2, y - 2):
            lista[ficha] = -4
        elif esta_en_rango(x - 1, y + 1) and (matriz_jugada[x - 1][y + 1] == "-"):
            lista[ficha] = 3
        elif esta_en_rango(x - 1, y - 1) and (matriz_jugada[x - 1][y - 1] == "-"):
            lista[ficha] = -3
        elif esta_en_rango(x + 1, y + 1) and (matriz_jugada[x + 1][y + 1] == "-"):
            lista[ficha] = 2
        elif esta_en_rango(x + 1, y - 1) and (matriz_jugada[x + 1][y - 1] == "-"):
            lista[ficha] = -2
        elif esta_en_rango(x + 2, y + 2) and puede_saltar(matriz_jugada, x + 1, y + 1, x + 2, y + 2):
            lista[ficha] = 1
        elif esta_en_rango(x + 2, y - 2) and puede_saltar(matriz_jugada, x + 1, y - 1, x + 2, y - 2):
            lista[ficha] = -1
    else: # Juega con "O"
        if esta_en_rango(x + 2, y + 2) and puede_saltar(matriz_jugada, x + 1, y + 1, x + 2, y + 2):
            lista[ficha] = 4
        elif esta_en_rango(x + 2, y - 2) and puede_saltar(matriz_jugada, x + 1, y - 1, x + 2, y - 2):
            lista[ficha] = -4
        elif esta_en_rango(x + 1, y + 1) and (matriz_jugada[x + 1][y + 1] == "-"):
            lista[ficha] = 3
        elif esta_en_rango(x + 1, y - 1) and (matriz_jugada[x + 1][y - 1] == "-"):
            lista[ficha] = -3
        elif esta_en_rango(x - 1, y + 1) and (matriz_jugada[x - 1][y + 1] == "-"):
            lista[ficha] = 2
        elif esta_en_rango(x - 1, y - 1) and (matriz_jugada[x - 1][y - 1] == "-"):
            lista[ficha] = -2
        elif esta_en_rango(x - 2, y + 2) and puede_saltar(matriz_jugada, x - 1, y + 1, x - 2, y + 2):
            lista[ficha] = 1
        elif esta_en_rango(x - 2, y - 2) and puede_saltar(matriz_jugada, x - 1, y - 1, x - 2, y - 2):
            lista[ficha] = -1

    return lista

def obtener_mejor_movimiento(turno, posicion_valor):
    letras = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}
    mayor_clave = max(posicion_valor.values(), key=abs)
    maximo = [key for key, value in posicion_valor.items() if abs(value) == abs(mayor_clave)]
    jugada_posible = []

    for posicion in maximo:
        if turno:
            cpu_jugada = ""
            if posicion_valor[posicion] == 4:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) + 2]}{int(posicion[0]) - 2}"
            elif posicion_valor[posicion] == -4:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) - 2]}{int(posicion[0]) - 2}"
            elif posicion_valor[posicion] == 3:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) + 1]}{int(posicion[0]) - 1}"
            elif posicion_valor[posicion] == -3:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) - 1]}{int(posicion[0]) - 1}"
            elif posicion_valor[posicion] == 2:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) + 1]}{int(posicion[0]) + 1}"
            elif posicion_valor[posicion] == -2:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) - 1]}{int(posicion[0]) + 1}"
            elif posicion_valor[posicion] == 1:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) + 2]}{int(posicion[0]) + 2}"
            elif posicion_valor[posicion] == -1:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) - 2]}{int(posicion[0]) + 2}"
        else:
            cpu_jugada = ""
            if posicion_valor[posicion] == 4:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) + 2]}{int(posicion[0]) + 2}"
            elif posicion_valor[posicion] == -4:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) - 2]}{int(posicion[0]) + 2}"
            elif posicion_valor[posicion] == 3:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) + 1]}{int(posicion[0]) + 1}"
            elif posicion_valor[posicion] == -3:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) - 1]}{int(posicion[0]) + 1}"
            elif posicion_valor[posicion] == 2:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) + 1]}{int(posicion[0]) - 1}"
            elif posicion_valor[posicion] == -2:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) - 1]}{int(posicion[0]) - 1}"
            elif posicion_valor[posicion] == 1:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) + 2]}{int(posicion[0]) - 2}"
            elif posicion_valor[posicion] == -1:
                cpu_jugada += f"{letras[int(posicion[1])]}{int(posicion[0])}{letras[int(posicion[1]) - 2]}{int(posicion[0]) - 2}"
        jugada_posible.append(cpu_jugada)

    return random.choice(jugada_posible)

def posiciones_fichas(turno, matriz_jugada):
    posiciones = []
    for fila in range(1,9):
        for columna in range(1,9):
            if turno:
                if matriz_jugada[fila][columna] == "X":
                    posiciones.append(f"{fila}{columna}")
            else:
                if matriz_jugada[fila][columna] == "O":
                    posiciones.append(f"{fila}{columna}")
    return posiciones

def Computadora(turno, matriz_jugada):
    posiciones = posiciones_fichas(turno, matriz_jugada)

    movimientos = {}
    for ficha in posiciones:
        movimientos.update(valorar_movimientos(ficha, matriz_jugada, turno))

    return obtener_mejor_movimiento(turno, movimientos)