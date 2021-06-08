class Person:

    def __init__(self, imie, wiek):  
        self.imie = imie
        self. wiek = wiek

    def witam(self):
        print("witam jestem wesoły " + self.imie + " mam " + str(self.wiek) + " lat")
    
p1 = Person('Luki', 18)

print(p1.imie)
p1.witam()

