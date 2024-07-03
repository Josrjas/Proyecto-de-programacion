import datetime
from movimientos import Construir_funcion
from movimientos import mov
from Construccionfuncion import Comprobacion_de_jugada_valida
from Construccionfuncion import Permitido_al_jugador
from movimientos import final
from Brainiac import Computadora
from Brainiac import ubicacion_fichas
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
            termina = False
            while termina != True:
                if contador%2 == 0 or contador == 0:
                    mov(Computadora(ubicacion_fichas(matriz_jugada,Turno)))
                elif contador%2 == 1:
                    print("Introduce tu siguiente jugada")
                    jugada = input(": ")
                if final(jugada) == True:
                    termina = True

        elif Turno == "No" or "no":
            pass
