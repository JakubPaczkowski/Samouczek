miejsce_zamieszkania = {'Jan Kowalski':10,'Marcin Paczkowski':20}    #Mieszka pod 10 i 20
miejsce_zamieszkania['Jakub Paczkowski'] = "30"                  #Dodanie elementu do krotki

print(miejsce_zamieszkania)

print('')

for key in miejsce_zamieszkania.items():               #Wyświetla wszystkie klucze które mamy czyli 10 , 20, 30
    print(key)                                        #Wyświetla nasze klucze  pamiętaj o wyciąciu !

print('')

print(miejsce_zamieszkania.get("Marcin Paczkowski"))               #Pokazuje tylko dane klucze
print(miejsce_zamieszkania.values())                                #Pokazuje tylko dane wartość

print(miejsce_zamieszkania.setdefault("Marzena Paczkowska", "40"))    #Metoda która dodaje gdy nie ma klucza i wstawia z wartością do krotki ^
(miejsce_zamieszkania)["Jan Kowalski"] = "11"                  #Gdy nadpiszemy wartość  zostanie ona dopisana do klucza
print(miejsce_zamieszkania)

print('')

print(miejsce_zamieszkania.pop("Marzena Paczkowska","40"))                 #.Pop usuwa watrość i pokazuje z printem co usuneła
print(miejsce_zamieszkania.popitem())                                      # .popitem usuwa ostatnią dodaną watrość w tym przypadku Jakuba z 30 |nie przyjmuje wartości w ()

if "Jan Kowalski" in miejsce_zamieszkania:                      #Sprawdza czy dany element jest w liście krotce
    print("Znaleziono")
else:
    print("Nie znaleziono")