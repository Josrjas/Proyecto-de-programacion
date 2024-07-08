import random
def ubicacion_fichas(matriz_jugada,Turno):
    jug_posibles = []
    for fila in range(1,9):
        for columna in range(1,9):
            if Turno == True:
                if matriz_jugada[fila][columna] == "X":
                    #Nombredejugadas
                    jug_posibles.append(f"{fila}{columna}")
            elif Turno == False:
                if matriz_jugada[fila][columna] == "O":
                    #Nombredejugadas
                    jug_posibles.append(f"{fila}{columna}")
    return jug_posibles

def Computadora(ubicacion_fichas,Turno,matriz_jugada):
    m_jud = ""
    jugada = ""
    lista = {}
    j_posibles = []
    Letras = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}
    #Limitar el rango para que no salga de limites
    for ficha in ubicacion_fichas:
        if Turno == True:
            #En esta parte se puntuara a cada movimiento posible y luego se guardara en un diccionario
            #Caso en donde se prioriza un salto de 2 casillas
            #Adelante derecha
            if ((int(ficha[1]) + 2) <= 8) and ((int(ficha[0]) - 2) >= 1)and (matriz_jugada[int(ficha[0])-1][int(ficha[1])+1] == "O" or matriz_jugada[int(ficha[0])-1][int(ficha[1])+1] == "X" and matriz_jugada[int(ficha[0])-2][int(ficha[1])+2] == "-"):
                lista[ficha] = 4
            #Adelante izquierda
            elif ((int(ficha[1]) + 2) >= 1) and ((int(ficha[0]) - 2) >= 1) and (matriz_jugada[int(ficha[0])-1][int(ficha[1])-1] == "O" or matriz_jugada[int(ficha[0])-1][int(ficha[1])-1] == "X" and matriz_jugada[int(ficha[0])-2][int(ficha[1])-2] == "-"):
                lista[ficha] = -4
            else:
                # Caso en donde solo se mueve una ficha
                #Adelante derecha
                if ((int(ficha[1]) + 1) <= 8) and ((int(ficha[0]) - 1) >= 1) and (matriz_jugada[int(ficha[0])-1][int(ficha[1])+1] == "-"):
                    lista[ficha] = 3
                #adelante izquierda
                elif ((int(ficha[1]) - 1) >= 1) and ((int(ficha[0]) - 1) >= 1)and (matriz_jugada[int(ficha[0])-1][int(ficha[1])-1] == "-"):
                    lista[ficha] = -3
                else:
                    #Caso movimiento hacia atras una casilla
                    if ((int(ficha[0]) + 1) <= 8) and ((int(ficha[0]) + 1) <= 8) and (matriz_jugada[int(ficha[0])+1][int(ficha[1])+1] == "-"):
                        lista[ficha] = 2
                    elif ((int(ficha[0]) - 1) >= 1) and ((int(ficha[0]) + 1) <= 8) and (matriz_jugada[int(ficha[0])+1][int(ficha[1])-1] == "-"):
                        lista[ficha] = -2
                    else:
                        #Caso movimiento hacia atra 2 casillas
                        if ((int(ficha[1]) + 2) <= 8) and ((int(ficha[0]) + 2) <= 8) and (matriz_jugada[int(ficha[0]) + 1 ][int(ficha[1]) + 1] == "O" or matriz_jugada[int(ficha[0]) + 1][int(ficha[1]) + 1] == "X" and matriz_jugada[int(ficha[0]) + 2][int(ficha[1]) + 2] == "-"):
                            lista[ficha] = 1
                        elif ((int(ficha[1]) - 2) >= 1) and ((int(ficha[0]) + 2) <= 8) and (matriz_jugada[int(ficha[0]) + 1][int(ficha[1]) - 1] == "O" or matriz_jugada[int(ficha[0]) + 1][int(ficha[1]) - 1] == "X" and matriz_jugada[int(ficha[0]) + 2][int(ficha[1]) - 2] == "-"):
                            lista[ficha] = -1
                        else:
                            #no movimientos posibles
                            lista[ficha] = 0
        elif Turno == False:
            if ((int(ficha[1]) +  2) <= 8) and ((int(ficha[0]) + 2) <= 8)and (matriz_jugada[int(ficha[0])+1][int(ficha[1])+1] == "O" or matriz_jugada[int(ficha[0])+1][int(ficha[1])+1] == "X" and matriz_jugada[int(ficha[0])+2][int(ficha[1])+2] == "-"):
                lista[ficha] = 4
            #Adelante izquierda
            elif ((int(ficha[1]) - 2) >= 1) and ((int(ficha[0]) + 2) <= 8) and (matriz_jugada[int(ficha[0])+1][int(ficha[1])-1] == "O" or matriz_jugada[int(ficha[0])+1][int(ficha[1])-1] == "X" and matriz_jugada[int(ficha[0])+2][int(ficha[1])-2] == "-"):
                lista[ficha] = -4
            else:
                # Caso en donde solo se mueve una ficha
                #Adelante derecha
                if ((int(ficha[1]) + 1) <= 8) and ((int(ficha[0]) + 1) <= 8) and (matriz_jugada[int(ficha[0])+1][int(ficha[1])+1] == "-"):
                    lista[ficha] = 3
                #adelante izquierda
                elif ((int(ficha[1]) - 1) >= 1) and ((int(ficha[0]) + 1) >= 1)and (matriz_jugada[int(ficha[0])+1][int(ficha[1])-1] == "-"):
                    lista[ficha] = -3
                else:
                    #Caso movimiento hacia atras una casilla
                    if ((int(ficha[0]) - 1) >= 1) and ((int(ficha[1]) + 1) <= 8) and (matriz_jugada[int(ficha[0])-1][int(ficha[1])+1] == "-"):
                        lista[ficha] = 2
                    elif ((int(ficha[0]) - 1) >= 1) and ((int(ficha[1]) - 1) >= 1) and (matriz_jugada[int(ficha[0])-1][int(ficha[1])-1] == "-"):
                        lista[ficha] = -2
                    else:
                        #Caso movimiento hacia atra 2 casillas
                        if ((int(ficha[1]) + 2) <= 8) and ((int(ficha[0]) - 2) <= 8) and (matriz_jugada[int(ficha[0]) - 1 ][int(ficha[1]) + 1] == "O" or matriz_jugada[int(ficha[0]) - 1][int(ficha[1]) + 1] == "X" and matriz_jugada[int(ficha[0]) - 2][int(ficha[1]) + 2] == "-"):
                            lista[ficha] = 1
                        elif ((int(ficha[1]) - 2) >= 1) and ((int(ficha[0]) - 2) <= 8) and (matriz_jugada[int(ficha[0]) - 1][int(ficha[1]) - 1] == "O" or matriz_jugada[int(ficha[0]) - 1][int(ficha[1]) - 1] == "X" and matriz_jugada[int(ficha[0]) - 2][int(ficha[1]) - 2] == "-"):
                            lista[ficha] = -1
                        else:
                            #no movimientos posibles
                            lista[ficha] = 0
    if Turno == True:
        mayor_clave = max(lista.values(), key=abs)
        maximo = [key for key, value in lista.items() if abs(value) == abs(mayor_clave)]
        for item in maximo:

            j_list = item
            cpu_jugada = ""
            a = 1
            b = 0
            if lista[item] == 4:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) + 2]}{int(j_list[b]) - 2}"
            elif lista[item] == -4:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) - 2]}{int(j_list[b]) - 2}"
            elif lista[item] == 3:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) + 1]}{int(j_list[b]) - 1}"
            elif lista[item] == -3:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) - 1]}{int(j_list[b]) - 1}"
            elif lista[item] == 2:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) + 1]}{int(j_list[b]) + 1}"
            elif lista[item] == -2:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) - 1]}{int(j_list[b]) + 1}"
            elif lista[item] == 1:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) + 2]}{int(j_list[b]) + 2}"
            elif lista[item] == -1:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) - 2]}{int(j_list[b]) + 2}"
            j_posibles.append(cpu_jugada)
        jug = random.choice(j_posibles)
    elif Turno == False:
        mayor_clave = max(lista.values(), key=abs)
        maximo = [key for key, value in lista.items() if abs(value) == abs(mayor_clave)]
        for item in maximo:
            j_list = item
            cpu_jugada = ""
            a = 1
            b = 0
            if lista[item] == -4:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) - 2]}{int(j_list[b]) + 2}"
            elif lista[item] == 4:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) + 2]}{int(j_list[b]) + 2}"
            elif lista[item] == -3:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) - 1]}{int(j_list[b]) + 1}"
            elif lista[item] == 3:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) + 1]}{int(j_list[b]) + 1}"
            elif lista[item] == -2:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) - 1]}{int(j_list[b]) - 1}"
            elif lista[item] == 2:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) + 1]}{int(j_list[b]) - 1}"
            elif lista[item] == -1:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) - 2]}{int(j_list[b]) - 2}"
            elif lista[item] == 1:
                cpu_jugada += f"{Letras[int(j_list[a])]}{int(j_list[b])}{Letras[(int(j_list[a])) + 2]}{int(j_list[b]) - 2}"
            j_posibles.append(cpu_jugada)
        jug = random.choice(j_posibles)


    return jug
