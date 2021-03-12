def zlicz(**produkty):
    return ("Ilość produktów", len(produkty.keys())), ("Całościowa wartość produktów", sum(produkty.values()))


print(zlicz(pomidor=5, papryka=4, mąka=3, mleko=3, woda=2, chleb=3))
