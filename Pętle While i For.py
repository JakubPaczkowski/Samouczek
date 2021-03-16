#liczba = 1

#while liczba < 6:             #Wykonuje się określoną ilośc razy
#    print(liczba)
#    liczba += 1
#

#for liczba in range(0,10):
#    print(liczba)

#print("----------")

#for liczba in range(0,10,2):                       ##Piszemy zakres pętli  JEZELI PODAMY PO (1,10 2) BĘDZIE LICZYĆ PO DWA ELEMENTY KROK
#   print(liczba)
#print('---------')

#for liczba in range(0,10):
#    if liczba == 5:
#        break
#    print(liczba)                               #Breake przerywa wywołanie pętli   wtedy print dla 5 się nie wyświetli

#print("-----")

for liczba in range(0,10):
    if liczba == 5:
        continue                                #Continue przerywa aktualne wykonanie pętli i przechodzi do kolejnego wywołania
    print(liczba)

while True:         # Pętla niezkończona