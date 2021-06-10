import datetime as dt
class Person:
    def __init__(self, imie, rok_urodzenia):  
        self.imie = imie
        self.rok_urodzenia = rok_urodzenia
        self.wiek = 0

    def witam(self):
        print("witam jestem wesoły " + self.imie + " mam " + str(self.wiek) + " lat")
    
    def wieak(self):
        rok = dt.datetime.now()
        self.wiek = rok.year - self.rok_urodzenia
        return self.wiek


p1 = Person('Luki', 2002)

print(p1.imie)
p1.witam()

print(p1.wieak())