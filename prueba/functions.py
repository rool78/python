import random

def darNumero():
    num = input("Dame un numero: ")
    num = int(num)

    if num > 10:
        print("The number is greater than 10")
        if num == 13 or num == 12:
            print("Es 13 o 12")
    else:
        print("The number is 10 or less than 10")

    if num != 5:
        print("Your number is not 5")
    else:
        print("Your number is 5")

def adivinaElNumero(numero):
    numeroSecreto = random.randrange(1, 6)
    return numeroSecreto == int(numero)


print('Bienvenido a adivinar el numero del 1 al 5')

correcto = False

while not correcto:
    num = input('Por favor, di un número del 1 al 5: ')

    check = lambda numero: int(numero) == random.randrange(1,6)

    if check(num):
        print('Enhorabuena, el numero es correcto') 
        correcto = True


