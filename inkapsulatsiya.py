class Shaxs:
    __odamlar_soni = 0

    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        Shaxs.__odamlar_soni += 1

    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    @classmethod
    def get_odamlar_soni(cls):
        return cls.__odamlar_soni


class Talaba(Shaxs):
    __talabalar_soni = 0

    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        Talaba.__talabalar_soni += 1

    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni


shaxs1 = Shaxs('Ali', 'Valiyev', 'AA1231231', 2000)
shaxs2 = Shaxs('Ali', 'Valiyev', 'AA1231231', 2000)
shaxs3 = Shaxs('Ali', 'Valiyev', 'AA1231231', 2000)
shaxs4 = Shaxs('Ali', 'Valiyev', 'AA1231231', 2000)


print(shaxs3.get_odamlar_soni())

talaba1 = Talaba("Toshmat", "Eshmatov", 'AA1234567',
                 2004, '12123123123', 'idontknow')
talaba2 = Talaba("Toshmat", "Eshmatov", 'AA1234567',
                 2004, '12123123123', 'idontknow')
talaba3 = Talaba("Toshmat", "Eshmatov", 'AA1234567',
                 2004, '12123123123', 'idontknow')
talaba4 = Talaba("Toshmat", "Eshmatov", 'AA1234567',
                 2004, '12123123123', 'idontknow')
talaba5 = Talaba("Toshmat", "Eshmatov", 'AA1234567',
                 2004, '12123123123', 'idontknow')


print(talaba1.get_talabalar_soni())
