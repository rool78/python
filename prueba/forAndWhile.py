lista = [3, 54, 1, 34, 55, 655, 12]

# Tenemos break y continue...
for n in lista:
    print(n)

for n in range(1, 8):
    print(n)

msg = "burbuja"

for n in msg:
    print(n)

cont = 0

while True:
    if cont > 5:
        break

    print("hola while " + str(cont))

    cont += 1

cont = 0

while cont < 5:
    print("while mejor... :) " + str(cont))
    cont += 1



