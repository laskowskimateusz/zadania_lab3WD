def n_wyraz(a1, q, n):
    return a1*(q**(n-1))


def n_suma(a1, q, n):
    return a1 * ((1 - (q**n))/(1-q))


def n_iloczyn(a1, q, n):
    ciag = [a1]
    suma = 1
    for x in range(a1, n):
        ciag.append(ciag[-1] * q)
        suma *= ciag[-1]
    return suma
