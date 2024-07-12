import json
import datetime
from movimientos import Construir_tablero
from movimientos import Mover_ficha
from validacionDeMovimientos import Comprobacion_de_jugada_valida
from validacionDeMovimientos import Permitido_al_jugador
from movimientos import final
from Brainiac import Computadora 
#Estadisticas
try:    
    with open('estadisticas.json', 'r') as file:
        estadisticas = json.load(file)
except FileNotFoundError:
    estadisticas = {}

estadistica = {}

# Todos las partidas
try:
    with open("juegos_guardados.json", 'r') as file:
        partidas = json.load(file)
except FileNotFoundError:
    partidas = []

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
    print("4 Salir del Juego")
    opcion = input("Opcion: ")
    open("registro", 'a')
    while opcion not in ("1","2","3","4"):
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
        print(Construir_tablero(matriz_inicial))

        # Guardar Datos para el registro
        #Todos los jugadores
        for j in (J_1, J_2):
            if j not in estadistica:
                estadistica[j] = [1,0]
            else:
                estadistica[j][0] += 1

        #Jugadores por parida
        Datos =[]
        Datos.append([J_1, J_2])

        # El tablero del juego
        termina = False
        contador = 0
        alguienGano = ""
        print(f"Turno de {J_1}")
        while termina != True:
            jugada = input(": ")
            if Comprobacion_de_jugada_valida(jugada,matriz_jugada) == True and Permitido_al_jugador(jugada, contador,matriz_jugada):
                contador += 1
                matriz_jugada = Mover_ficha(jugada,matriz_jugada)
                print(Construir_tablero(matriz_jugada))
                alguienGano = final(matriz_jugada)
                if contador % 2 == 0:
                    print(f"Turno de {J_1}")
                elif contador % 2 == 1:
                    print(f"Turno de {J_2}")
                if alguienGano:
                    partidas.append(matriz_jugada)
                    termina = True
                    if alguienGano == "O":
                        print(f"¡Ha ganado {J_1}!")
                        print(f"¡Ha perdido {J_2}!")
                        ganador = J_1

                        estadistica[J_1][1] += 1 
                    elif alguienGano == "X":
                        print(f"¡Ha ganado {J_2}!")
                        print(f"¡Ha perdido {J_1}!")
                        ganador = J_2
                        
                        estadistica[J_2][1] += 1 

            elif jugada == "Esc":
                partidas.append(matriz_jugada)
                
                print("Partida Cancelada")
                ganador = "Cancelada"
                termina = True
            elif Comprobacion_de_jugada_valida(jugada,matriz_jugada) == False or Permitido_al_jugador(jugada, contador, matriz_jugada):
                print("Error en jugada")
        
        with open("registro", 'r') as archivo:
            a = len(archivo.readlines())
        with open("registro", 'a') as archivo:
            archivo.write(f"{a + 1} {J_1} VS {J_2}   {fecha} {hora_actual}   {ganador}\n")
            archivo.close()

    # registro de jugadas
    elif int(opcion) == 2:
        # Juegos Realizados
        print("JUEGOS REALIZADOS: ")
        print("  Jugadores      FechaHora       Ganador")
        imputFile = open("registro", 'r')
        for linea in imputFile:
            print(linea.strip())
        # Estadisticas
        print("Estadisticas: ")
        print("Jugador   Cant.Juegos   Ganadas")
        for jugador in estadistica:
            print(f"{jugador}   {estadistica[jugador][0]}   {estadistica[jugador][1]}")

        # Opciones
        print( "0. Regresar Menu Principal")
        print( "1. Ver Juego")

        opciones = input("Opcion: ")
        while opciones not in ("0", "1"):
            opciones = input("Opcion: ")

        if opciones == "0":
            None
        #Ver juegos
        elif opciones == "1":
            for i in range(len(partidas)):
                print(f"Partida {i+1}")
                print(Construir_tablero(partidas[i]))
                print()


    elif int(opcion) == 3:
        open("registro", 'a')
        ganador = ""

        contador = 0
        print("Introduce tu nombre")
        J_1 = input(":")

        hora_actual = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}"
        fecha = datetime.date.today()
        
        for j in (J_1, "Computadora"):
            if j not in estadistica:
                estadistica[j] = [1,0]
            else:
                estadistica[j][0] += 1

        
        print("¿Jugaras primero? (Si o No)")
        Turno = input(": ").lower()
        while Turno != "si" and Turno != "no":
            Turno = input(": ")
        termina = False
        if Turno == "si":
            Turno = True
            print(Construir_tablero(matriz_inicial))
            
            while termina != True:
                if contador%2 == 1:
                    jugada_CPU = Computadora(Turno,matriz_jugada)
                    matriz_jugada = Mover_ficha(jugada_CPU,matriz_jugada)
                    print(f"CPU juega: {jugada_CPU}")
                    print(Construir_tablero(matriz_jugada))
                    contador += 1
                else:
                    print("Introduce tu siguiente jugada")
                    jugada = input(": ")
                    if jugada == "Esc":
                        partidas.append(matriz_jugada)

                        print("Partida Cancelada")
                        termina = True
                        ganador = "Cancelada"
                    else:
                        if Comprobacion_de_jugada_valida(jugada, matriz_jugada) == False:
                            print("Error en jugada")
                        elif Permitido_al_jugador(jugada, contador, matriz_jugada) == False:
                            print("No puedes mover esa ficha")
                        else:
                            print(Construir_tablero(Mover_ficha(jugada, matriz_jugada)))
                            contador += 1
                if final(matriz_jugada) == True:
                    partidas.append(matriz_jugada)

                    termina = True
                    if contador % 2 == 1:
                        ganador = J_1
                    else:
                        ganador = "Computadora"
        else:
            Turno = False
            print(Construir_tablero(matriz_inicial))
           
            while termina != True:
                if contador % 2 == 0:
                    jugada_CPU = Computadora(Turno,matriz_jugada)
                    matriz_jugada = Mover_ficha(jugada_CPU,matriz_jugada)
                    print(f"CPU juega: {jugada_CPU}")
                    print(Construir_tablero(matriz_jugada))
                    contador += 1
                else:
                    print("Introduce tu siguiente jugada")
                    jugada = input(": ")
                    if jugada == "Esc":
                        partidas.append(matriz_jugada)

                        print("Partida Cancelada")
                        termina = True
                        ganador = "Cancelada"  
                    else:
                        if Comprobacion_de_jugada_valida(jugada, matriz_jugada) == False:
                            print("Error en jugada")
                        elif Permitido_al_jugador(jugada, contador, matriz_jugada) == False:
                            print("No puedes mover esa ficha")
                        else:
                            print(Construir_tablero(Mover_ficha(jugada, matriz_jugada)))
                            contador += 1

                if final(matriz_jugada) == True:
                    partidas.append(matriz_jugada)

                    termina = True
                    if contador % 2 == 1:
                        ganador = J_1
                        estadistica[ganador][1] += 1 
                    else:
                        ganador = "Computadora"
                        estadistica[ganador][1] += 1

        with open("registro", 'r') as archivo:
            a = len(archivo.readlines())
        with open("registro", 'a') as archivo:
            archivo.write(f"{a + 1} {J_1} VS Computadora   {fecha} {hora_actual}   {ganador}\n")
            archivo.close()

    elif int(opcion) == 4:
        Apagar = True

    estadisticas.update(estadistica)
    
    #Añadiendo las estadisticas al Json
    for clave, valor in estadistica.items():
        if clave in estadisticas:
            estadisticas[clave] += valor
        else:
            estadisticas[clave] = valor
            
    with open("estadisticas.json", 'w') as file:
        json.dump(estadisticas, file, indent=4)

    #Añadiendo las partidas al Json
    with open("juegos_guardados.json", 'w') as file:
        json.dump(partidas, file, indent=4)



