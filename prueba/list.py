myList = list(('a','hola','b','j','adios','otro'))

# print(len(myList))

# print(myList)

# print(myList[-1])

# print(5 in myList)

myList.append('pepito')

myList.extend(('dos','mas'))

myList.insert(0, '78')

print(myList)

# Pop al ultimo elemento
myList.pop()

# Pop a un indice
myList.pop(4)

# Eliminamos el elemento
myList.remove('b')

myList.sort()

print(myList)

myList.clear()

print(myList)

numList = [7,44,2,223,5,7]
print(numList)
numList.sort()

print(numList)

numList.sort(reverse=True)

numList[0] = 6969

print(numList)

print(numList.index(7))

del numList