class Foydalanuvchilar:
    def __init__(self,ism,f_ism,email,oqish_joyi):
        self.ism = ism
        self.fism = f_ism
        self.mail = email
        self.ojoyi = oqish_joyi


    def get_ism(self):
        return self.ism.title()

    def get_fism(self):
        return self.fism

    def get_email(self):
        return self.mail

    def get_oqishjoyi(self):
        return self.ojoyi.upper()

    def get_info(self):
        return f"Ismi: {self.ism.title()}\nFoydalanuvchi ismi: {self.fism}\nEmailingiz: {self.mail}\nO'qish joyingiz: {self.ojoyi.upper()}"

user1 = Foydalanuvchilar(input("Ismingizni kirting:"),input("Foydalanuvchi ismini kiriting: "),input("Emailingizni kiriting: "),input("O'qish joyingizni kiriting: "))
print(user1.get_ism())
print(user1.get_fism())
print(user1.get_oqishjoyi())
print(user1.get_info())