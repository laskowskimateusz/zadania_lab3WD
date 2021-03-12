def iloczyn_ciagu(*liczby):
    q = liczby[1]/liczby[0]
    n = len(liczby)
    return liczby[0] * ((1 - (q**n))/(1-q))


print(iloczyn_ciagu(1, 5, 25, 125, 625, 3125))
