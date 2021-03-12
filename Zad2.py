import random

lista1 = [random.randint(1, 100) for x in range(10)]
print(lista1)
nowa_lista1 = [x for x in lista1 if x % 2 == 0]
print(nowa_lista1)
