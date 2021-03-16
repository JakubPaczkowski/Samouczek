swiatlo = input('Jakie jest światlo? (zielone,czerwone,zolte)') #Input pobiera od urzytkowkika informacje

while True:
        if str(swiatlo).startswith("c"):            #Jeżeli światło będzie czerwone wyświetl czelakaj
            print('Czekaj')

        elif str(swiatlo).startswith("zo"):           #Jeźeli nie jest czerwone sprawdzamy a może jest żółte ??
            print('Bądź gotowy')

        elif str(swiatlo).startswith('zie'):
            print('Jedź')

                                    # Jeśli nie jest ani czewone ani żółte wtedy wykunuje się instrukcja ELSE !
        else:                                #Jeśeli światło będzie zielone  wyświetli się  jedź
            print('Nie właściwa wartość ')
            continue#Zabezpieczenie przed niewłaściwą wartością


#print('jedz') if swiatlo == 'zielone'  else print('czekaj ')         #inna metoda zapisu  Jeśli jest zielone 'jedz' w przeciwnym wypadku stój



