def n_wyraz(a1, r, n):
    return a1+(n-1)*r


def n_suma(a1, An, n):
    return ((a1 + An)/2)*n


def n_iloczyn(a1, r, n):
    ciag = [a1]
    suma = 1
    for x in range(a1, n):
        ciag.append(ciag[-1] + r)
        suma *= ciag[-1]
    return suma
