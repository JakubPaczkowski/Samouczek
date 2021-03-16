informacje_o_krajach = {}
informacje_o_krajach["Polska"] = ("Warszawa",37.97)
informacje_o_krajach["Niemcy"] = ("Berlin",82.02)
informacje_o_krajach["Słowacja"] = ("Bratysława",5.45)
informacje_o_krajach["Porugalia"] = ("Lizbona",10.00)

for kraje in informacje_o_krajach.keys():
    print(kraje)
print('--------')

kraje = input("Informacje o jakim kraju chcesz wyświetlić?")

informacje_o_krajach = informacje_o_krajach.get(kraje)
print('')
print(kraje)
print('--------')
print("Stolica:" + informacje_o_krajach[0])
print("Liczba mieszkańców (mln):" + str(informacje_o_krajach[1]))
