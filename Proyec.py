import random
import datetime
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
def Construir_funcion(lis):
    matriz = ""
    for a in range(0, 9):
        fila = ""
        for b in range(0, 9):
            fila += f"{lis[a][b]} "
        fila += "\n"
        matriz += fila
    return matriz

def mov (jugada):
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

def Computadora(ubicacion_fichas,Turno):
    m_jud = ""
    jugada = ""
    lista = {}
    j_posibles = []
    Letras = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}
    #Limitar el rango para que no salga de limites
    for ficha in ubicacion_fichas:
        if Turno == True:
            print(ficha[0], ficha[1])
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
        #print(lista)
        if Turno == False:
            pass


    if Turno == True:
        mayor_clave = max(lista.values(), key=abs)
        maximo = [key for key, value in lista.items() if abs(value) == abs(mayor_clave)]

        print(f"{maximo} max")
        #print(lista)
        #print(Construir_funcion(matriz_jugada))
        for item in maximo:

            j_list = item
            cpu_jugada = ""
            print(item)
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
        print(j_posibles)
        print(jug)
    return jug

Apagar = False
while Apagar == False:
    matriz_inicial = [[" ", "A", "B", "C", "D", "E", "F", "G", "H"],
                      ["1", "-", "O", "-", "O", "-", "O", "-", "O"],
                      ["2", "O", "-", "O", "-", "O", "-", "O", "-"],
                      ["3", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["4", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["5", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["6", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ["7", "-", "X", "-", "X", "-", "X", "-", "X"],
                      ["8", "X", "-", "X", "-", "X", "-", "X", "-"]]

    matriz_jugada = matriz_inicial
    # Menu principal
    print("                                            ")
    print("JUEGO de Damas Chinas")
    print("1 Comezar Juego")
    print("2 Juegos realizados")
    print("3 Jugar contra computadora")
    opcion = input("Opcion: ")
    open("registro", 'a')
    while opcion not in "1" and opcion not in "2" and opcion not in "3":
        opcion = input("Opcion: ")

    # opciones
    if int(opcion) == 1:
        hora_actual = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}"
        fecha = datetime.date.today()
        print("COMENZAR JUEGO")
        J_1 = str(input("Nombre de jugador 1: "))
        J_2 = str(input("Nombre de jugador 2: "))
        print("-------- ------------------Escriba Esc para cancelar la partida--------------------------------")
        print(f"{J_1} VS {J_2} {fecha} {hora_actual}")
        print("Introduce tu siguiente movimiento. Ejem:(Posición Inicial)(Posión Final) ---> A2B3")
        print(Construir_funcion(matriz_inicial))
        # El tablero del juego
        termina = False
        contador = 0
        ganador = ""
        print(f"Turno de {J_1}")
        while termina != True:
            jugada = input(": ")
            if Comprobacion_de_jugada_valida(jugada) == True and Permitido_al_jugador(jugada, contador):
                contador += 1
                matriz_jugada = mov(jugada)
                print(Construir_funcion(matriz_jugada))
                ganador = final(matriz_jugada)
                if contador % 2 == 0:
                    print(f"Turno de {J_1}")
                elif contador % 2 == 1:
                    print(f"Turno de {J_2}")
                if ganador:
                    termina = True
                    if ganador == "O":
                        print(f"¡Ha ganado {J_1}!")
                        print(f"¡Ha perdido {J_2}!")
                        ganador = J_1
                    elif ganador == "X":
                        print(f"¡Ha ganado {J_2}!")
                        print(f"¡Ha perdido {J_1}!")
                        ganador = J_2
            elif jugada == "Esc":
                print("Partida Cancelada")
                ganador = "Cancelada"
                termina = True
            elif Comprobacion_de_jugada_valida(jugada) == False or Permitido_al_jugador(jugada, contador):
                print("Error en jugada")
        with open("registro", 'r') as archivo:
            a = len(archivo.readlines())
        with open("registro", 'a') as archivo:
            archivo.write(f"{a + 1} {J_1} VS {J_2}   {fecha} {hora_actual}   {ganador}\n")
            archivo.close()

    # registro de jugadas
    elif int(opcion) == 2:
        print("JUEGOS REALIZADOS: ")
        # registro del juego
        print("  Jugadores      FechaHora       Ganador")
        imputFile = open("registro", 'r')
        for linea in imputFile:
            print(linea.strip())

    elif int(opcion) == 3:
        contador = 0
        print("Introduce tu nombre")
        J_1 = input(":")
        print("¿Jugaras primero? (Si o No)")
        Turno = input(": ")
        while Turno != "Si" and Turno != "No" and Turno != "si" and Turno != "no":
            Turno = input(": ")
        if Turno == "Si" or "si":
            Turno = True
            termina = False
            print(Construir_funcion(matriz_inicial))
            while termina != True:
                if contador%2 == 1:
                    jugada_CPU = Computadora(ubicacion_fichas(matriz_jugada,Turno),Turno)
                    matriz_jugada = mov(jugada_CPU)
                    print(f"CPU juega: {jugada_CPU}")
                    print(Construir_funcion(matriz_jugada))
                    contador += 1
                elif contador % 2 == 0 or contador == 0:
                    print("Introduce tu siguiente jugada")
                    jugada = input(": ")
                    if Comprobacion_de_jugada_valida(jugada) == False:
                        print("Error en jugada")
                    else:
                        print(Construir_funcion(mov(jugada)))
                        contador += 1
                if final(matriz_jugada) == True:
                    termina = True

        elif Turno == "No" or "no":
            Turno = False
            termina = False
            print(Construir_funcion(matriz_inicial))
            while termina != True:
                if contador % 2 == 0 or contador == 0:
                    jugada_CPU = Computadora(ubicacion_fichas(matriz_jugada, Turno), Turno)
                    matriz_jugada = mov(jugada_CPU)
                    print(f"CPU juega: {jugada_CPU}")
                    print(Construir_funcion(matriz_jugada))
                    contador += 1
                elif contador % 2 == 1:
                    print("Introduce tu siguiente jugada")
                    jugada = input(": ")
                    if Comprobacion_de_jugada_valida(jugada) == False:
                        print("Error en jugada")
                    else:
                        print(Construir_funcion(mov(jugada)))
                        contador += 1
                if final(matriz_jugada) == True:
                    termina = True