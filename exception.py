def division(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print('No puedo dividir por 0')

n1 = (int(input('Dame n1: ')))
n2 = (int(input('Dame n2: ')))

print(division(n1, n2))