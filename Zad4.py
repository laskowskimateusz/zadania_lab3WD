def czy_trojkat_prostokatny(a, b, c):
    lista = [a, b, c]
    lista.sort()
    # print(lista)
    if lista[0]**2 + lista[1]**2 == lista[2]**2:
        return "Trójkąt ten jest prostokątny."
    return "Trójkąt ten nie jest prostokątny"


print('Podaj boki trójkąta: ')
bok1 = int(input("bok1: "))
bok2 = int(input("bok2: "))
bok3 = int(input("bok3: "))
print(czy_trojkat_prostokatny(bok1, bok2, bok3))
