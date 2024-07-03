from Construccionfuncion import Comprobacion_de_jugada_valida
from Construccionfuncion import matriz_jugada
def ubicacion_fichas(matriz_jugada,Turno):
    jug_posibles = []
    for fila in range(1,9):
        for columna in range(1,9):
            if Turno == True:
                if matriz_jugada[fila][columna] == "X":
                    #Nombredejugadas
                    jug_posibles.append(matriz_jugada[fila][columna])
            elif Turno == False:
                if matriz_jugada[fila][columna] == "O":
                    #Nombredejugadas
                    jug_posibles.append([fila,columna])
    return jug_posibles

def Computadora(ubicacion_fichas,Turno):
    jugada = ""
    lista = []
    Letra = ["A","B","C","D","E","F","G","H"]
    for ficha in ubicacion_fichas:
        if Turno == True:
            pass
        #jugadas en "X"
        elif Turno == False:
            pass
        #jugadas en "O"

    for elemento in lista:
        jugada += elemento
    if Comprobacion_de_jugada_valida(jugada) == False:
        return Computadora(matriz_jugada, Turno)
    else:
        return jugada