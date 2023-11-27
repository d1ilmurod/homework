class Avto:
    def __init__(self,model,rang,karobka,narh,yil):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.yil = yil
        self.kilometr = 0
    
    def get_info(self):
        return f"Model: {self.model.title()}\nRangi: {self.rang}\nKarobka: {self.karobka}\nNarxi: {self.narh} - dollar$\nYili: {self.yil}\n{self.kilometr} kilometr yurgan "
    
    def update_km(self):
        self.kilometr += 100
        
    def set_km(self,km):
        self.kilometr = km


avto1 = Avto('supra','qora','mexanik',50_000,2023)

avto2 = Avto('cobalt','qora','mexanik',15_000,2023)
avto2.update_km()

print(avto1.get_info(),'\n')
print(avto2.get_info(),'\n')


avto3 = Avto('Malibu','qora','mexanik',20_000,2023)
avto3.set_km(101)
print(avto3.get_info(),'\n')