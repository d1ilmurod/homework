class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        return yil - self.tyil

    def add_shaxs(self, shaxs):
        if isinstance(shaxs, Shaxs):
            self.shaxslar.append(shaxs)
        else:
            print('Shaxs haqida malumot kiriting')

    def __lt__(self, boshqa_shaxs):
        return self.tyil < boshqa_shaxs.tyil

    def __eq__(self, boshqa_shaxs):
        return self.tyil == boshqa_shaxs.tyil

    def __repr__(self):
        return "Shaxslar haqida ma'lumot kiritish classi"


class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, idraqam, bosqich, manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = bosqich
        self.manzil = manzil

    def get_id(self):
        return self.idraqam

    def get_bosqich(self):
        return self.bosqich

    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

    def __lt__(self, boshqa_talaba):
        return self.bosqich < boshqa_talaba.bosqich

    def __eq__(self, boshqa_talaba):
        return self.tyil == boshqa_talaba.tyil

    def __repr__(self):
        return "Talaba klassi"


print(Shaxs())  # shaxs class haiqda malumot beradi
print(Talaba())  # talaba class haqida malumot beradi
shaxs1 = Shaxs('Ali', 'Valiyev', 'AA1234456', 2000)
shaxs2 = Shaxs('Ali', 'Valiyev', 'AB1234456', 2001)
shaxs3 = Shaxs('Ali', 'Valiyev', 'AC1234456', 2000)


print(shaxs1 > shaxs2)  # False
print(shaxs1 == shaxs3)  # True

talaba1 = Talaba('Hasan', 'Husanov', 'AA1231232',
                 2003, 12123123124124124, 3, 'yerda')
talaba2 = Talaba('Hasan', 'Husanov', 'AA1231232',
                 2004, 12123123124124124, 2, 'yerda')
talaba3 = Talaba('Hasan', 'Husanov', 'AA1231232',
                 2004, 12123123124124124, 3, 'yerda')


print(talaba1 > talaba2)  # True
print(talaba2 == talaba3)  # True
