produkty = {'czekolada': 'sztuki', 'Mąka': 'kg', 'ziemniaki': 'kg',
            'masło': 'sztuki', 'ketchup': 'sztuki', 'baton': 'sztuki'}

print(produkty)
lista = [key for key in produkty if produkty.get(key) == 'sztuki']
print(lista)
