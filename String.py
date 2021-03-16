name="   JakubPaczkowski"
name1="    JakubPaczkowski"
print(len(name))    #Sprawdza ile w zmiennej mamy liter (Sprawdza długośc zmiennej)

print(name.capitalize())    #Metoda nie przyjmuje argumentów ,Zamienia na wielką Literę

print(name.upper())         #Metoda zamienia  wszystkie Litery na DUŻE LITERY

print(name.lower())         #Metoda zmienia wszystkie litery na małe litery

print(name[5])              #Metoda wyszukuje daną literę z stringa zaczynamy liczyć od 0! !

print(name[0:5])             # Wyświetlanie od danej litery do danej litery

print(name[5:])               #Wyświetla od danej liczby do końca


pełne= "Jakub Jan Paczkowski "
print(pełne.split(" "))       # Oddzielenie od siebie wyrazów  [lista]


polaczenie = "-"

print(polaczenie.join(['Jakub', 'Jan', 'Paczkowski']))  #Dodanie do siebie wyrazów

print("- - - - - - - -")
print(name.startswith("J"))            #Metoda sprawdza czy string zaczyna się jakąś literą
print(name.startswith("j"))             #WIELKOŚĆ LITER MA ZNACZENIE


print(name.lstrip('J'))           #Usuwa tylko pierwszą literę stringa
print(name.strip('i'))             #Usuwa z lewej i prawej strony stringa

print(name.strip())             #Metoda usuwa spacje

print("- - - - - -  ")
pierwsze_imie="Jakub"
drugie_imie="Paczkowski"

print(pierwsze_imie + " " + drugie_imie)

print(polaczenie.join([pierwsze_imie ,drugie_imie]))    #Dodanie połączenia
print('-------------')


klobia_nowa = 4
print(str(klobia_nowa).zfill(2))           #Metoda uzupełnia zerami

