def suma_ciagu(*liczby):
    q = liczby[1]/liczby[0]
    n = len(liczby)
    return liczby[0] * ((1 - (q**n))/(1-q))


def iloczyn_ciagu(*liczby):
    ciag = [liczby[0]]
    q = liczby[1]/liczby[0]
    suma = 1
    for x in range(len(liczby)):
        ciag.append(ciag[-1] * q)
        suma *= ciag[-1]
    return suma


print("Suma elementów ciągu: ", suma_ciagu(1, 5, 25, 125, 625, 3125))
print("Iloczyn elementów ciągu: ", iloczyn_ciagu(1, 5, 25, 125, 625, 3125))
