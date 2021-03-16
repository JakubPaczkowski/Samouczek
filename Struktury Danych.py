#lista_imion = []              #Lista listy elementów tego samego typu

#lista_imion.append('Kuba')
#lista_imion.append('Tomek')                       #.append dodaje do listy elementy
#lista_imion.append('Ania')

#print(lista_imion)


lista_imion = ['Kuba' ,'Tomerk' ,'Ania']             #Inny sposób zapisu listy
print(lista_imion)
 #Jeśli chcemy wyświetlić poszczególne elementy listy powinliśmy

for imiona in lista_imion:
    print(imiona)                         #Imiona zmienna któą będziemy wyświetlać  ,lista imion nazwa listy kluczowe jest słowo  in
                                         #Dla każdego imienia w liście |lista_imion| wykonaj daną rzecz
print('           ')

#Odwrócenie Listy

lista_imion = ['Kuba', 'Tomek','Ania']

lista_imion.reverse()
for imiona in lista_imion:
    print(imiona)

print('         ')
#Sortowanie listy

lista_imion =['Kuba','Tomek','Ania']
lista_imion.sort()
for imiona in lista_imion:
    print(imiona)

print("        ")
#Wyswietlanie poszczególnego elementu listy

lista_imion =['Kuba',"Tomek" ,"Ania "]
print(lista_imion[0])

#Metoda aby policzyć ile razy dany duplikat element występuje na liście
lista_imion =["Kuba", "Kuba" , "Ania", "Tomek "]
print(lista_imion.count('Kuba'))

#Sprawdza jaka długa jest lista ile występuje imion
print (len(lista_imion))

lista_imion =["Kuba", "Kuba" , "Ania", "Tomek "]
print(lista_imion)

#.remove usuwa element z listy
lista_imion.remove('Kuba')
print(lista_imion)

#.clear usuwa wszystko z listy
lista_imion =["Kuba", "Kuba" , "Ania", "Tomek "]
print(lista_imion)

#lista_imion.clear()                                      # !!!!Jeśli nie jest zakleione kasuje listę!!!
print(lista_imion)

#Dodanie listy do listy połączenie

lista_imion2 = ['Dominik']
lista_imion3 = lista_imion + lista_imion2
#Sortowanie

print(lista_imion3)
#Sortowanie od tyłu
lista_imion3.sort(reverse=True)
print(lista_imion3)


#Krotka !!!! Struktura która jest nie zmienna
#W krotce nie możemy nic zmienic ani rozmiaru ani dodać anu usuwać elementu |Dotyczy ona pewnego konceptu
osoba = ("Jakub" , "Paczkowski" , 19)
print(osoba)


#metoda set W secie nie możemy mieć zduplikowanych danych
imiona_set = {'Kuba','Kuba','Ania'}
print(imiona_set)


#Dodanie pustego seta i metody dodania
miona_set = set()
miona_set.add('Kuba')
miona_set.add('Ania')

#Usuwanie z setu
imiona_set.remove('Kuba')                        #A tutaj wyskoczy błąd pacz dół >
imiona_set.discard('Kuba')                        #Różnią się tym,że jeżeli poda się wartość któa nie istnieje np"adam"
print(imiona_set)


#Dodanie do siebie setu

imiona_set = set()
imiona_set.add('Kuba')
imiona_set.add('Tomek')

imiona_set2 = {'Ania','Kasia'}

imiona_set3 = imiona_set.union(imiona_set2)
print(imiona_set3)
print()
#Sety to po polsku zbiory a zbiory w matematyce możemy porównywać




