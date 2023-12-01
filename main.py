
from voitures_proprios import voitures
from motos_yanis import motos

voiture_Abdellah = voitures("Citroen C3", "Abdellah", 2014, "éteinte")
voiture_Hamid = voitures("Citroen Berlingo", "Hamid", 2017, "éteinte")
voiture_karim = voitures("Seat Octavia", "karim", 2019, "éteinte")
voiture_Rezki = voitures("Seat Ateca", "Rezki", 2023, "éteinte")
voiture_Said = voitures("Golf 7R", "Said", 2017, "éteinte")
voiture_Smail = voitures("Renault Kangoo", "Smail", 2012, "éteinte")
voiture_Yahia = voitures("KIA K2700", "Yahia", 2013, "éteinte")
voiture_Dalila = voitures("Volkswagen Tiguan", "Dalila", 2022, "éteinte")
voiture_Djamel = voitures("Peugeot 208", "Djamel", 2014, "éteinte")

moto1 = motos("Yamaha", 2019, "éteinte")
moto2 = motos ("Honda", 2018, "éteinte")
moto3 = motos ("Kawasaki", 2017, "éteinte")
moto4 = motos ("Suzuki", 2016, "éteinte")
moto5 = motos ("Ducati", 2015, "éteinte")

proprios = [
    voiture_Abdellah,
    voiture_Hamid,
    voiture_karim,
    voiture_Rezki,
    voiture_Said,
    voiture_Smail,
    voiture_Yahia,
    voiture_Dalila,
    voiture_Djamel
]

motos_de_yanis = [
    moto1,
    moto2,
    moto3,
    moto4,
    moto5
]

for proprio in proprios:
    print(proprio)

print(voiture_Abdellah.__str__())
print(voiture_Abdellah.démarrer())
print(voiture_Abdellah.accélérer(30))
print(voiture_Abdellah.accélérer(20))
print(voiture_Abdellah.freiner(20))
print(voiture_Abdellah.freiner(20))
print(voiture_Abdellah.eteindre())
print(voiture_Abdellah.eteindre())

for moto in motos_de_yanis:
    print(moto)

print(moto1.__str__())
print(moto1.démarrer())
print(moto1.accélérer(30))
print(moto1.accélérer(20))
print(moto1.freiner(20))
print(moto1.freiner(20))
print(moto1.eteindre())
print(moto1.eteindre())




