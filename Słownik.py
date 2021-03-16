#Słownik struktura danych klucz-wartość

kraje_i_stolice = {'Polska':'Warszawa','Niemcy':'Berlin'}
print(kraje_i_stolice)
#podajemy klucz pod którym chcemy przechować wartość

kraje_i_stolice['Czechy'] = 'praga'
print(kraje_i_stolice)

#Sprawdzenie kluczy

print('')

for kraje in kraje_i_stolice.keys():
    print(kraje)
print('')

#Sprawdzenie wartości

for stolice in kraje_i_stolice.values():
    print(stolice)

print()
#Sprawdzenie kluczy i wartości

for stolice,kraje in kraje_i_stolice.items():
    print(kraje + '-' + stolice)

print('')

#Wyświetlenie wartości z danego klucza II Sposoby

print(kraje_i_stolice["Polska"])
print(kraje_i_stolice.get("Polska"))

#Wartość .setdefault pobiera wartość danego klucza jeśli tego klucza nie ma wtedy wstawia ten klucz wraz z tą wartością któą się poda
print("")
print(kraje_i_stolice.setdefault("Polska", "Waszynkton DC"))
print(kraje_i_stolice)

#Jesli podana była by warszawa to zostanie wyświetlona i nic nie zostanie dodane do słownika