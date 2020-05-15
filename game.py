import random

def jugar(usuario, maquina):
    if usuario == maquina:
        print('Empate!!!')
        return
    elif usuario == 1 and maquina == 3:
        print('Esta vez... Tu ganas')
        return
    elif usuario == 2 and maquina == 1:
        print('Esta vez... Tu ganas')
        return
    elif usuario == 3 and maquina == 2:
        print('Esta vez... Tu ganas')
        return
    else:
        print('Has perdido... Que facil!')
        return

opciones = {
    1: "Piedra",
    2: "Papel",
    3: "Tijera"
}

print("Bienvenido al juego de Piedra, papel y tijera")

acierto = False
fin = False

while not acierto and not fin:
    print("1. Piedra, 2. Papel, 3. Tijera")
    eleccion = input("Elije su opción: ")
    eleccion = int(eleccion)

    if eleccion > 0 and eleccion < 4:
        print("Has elegido... " + opciones.get(eleccion))
    
        print('Tu maquina esta eligiendo... Sera mas rapido que tu! Mucho mas!')
        machineNumber = random.randrange(1, 4)
        print('Tu maquina a seleccionado...' + opciones.get(machineNumber).capitalize() + '!!!')
        jugar(eleccion, machineNumber)
        terminar = input("Desea seguir jugando? (Y/n): ")
    else:
        print('Que es eso??')
        terminar = input("Desea seguir jugando? (Y/n): ")

    if terminar.lower() == 'n':
        print('Gracias por jugar!')
        fin = True
