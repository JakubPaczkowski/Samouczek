countries_information={}
countries_information["Polska"] = ("Warszawa" ,37.97)

for country in countries_information.keys():
    print(country)

country=input("Info o jakim kraju chcesz zobaczyć ")

country_informaction=countries_information.get(country)
print("-")
print("country")
print('--')
print('stolica'+country_informaction[0])
print('liczba mieszkancow mln ' + str(countries_information[1]))