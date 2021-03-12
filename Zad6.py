def suma_ciagu(a=1, b=4, ile=10):
    return a * ((1 - (b**ile))/(1-b))


def iloczyn_ciagu(a=1, b=4, ile=10):
    ciag = [a]
    suma = 1
    for x in range(a, ile):
        ciag.append(ciag[-1] * b)
        suma *= ciag[-1]
    return suma


print("Suma elementów ciągu: ", int(suma_ciagu()))
print("Iloczyn elementów ciągu: ", iloczyn_ciagu())
