samochod = {'Audi':'czerwony', 'Seat': 'niebieski', 'Opel':'biały'}
samochod ['Skoda'] = 'czarny'

for key in samochod:
    print(key)

print(samochod.keys())

print(samochod.get('Audi'))
print(samochod.setdefault("Mazda",'siwa'))
print(samochod.setdefault('Renaut','zielona'))

if 'Audi' in samochod:
    print('Jest')
else:
    print('Nie ma ')

print(samochod.values())

