import unittest

from oop import Shaxs


class TestShaxs(unittest.TestCase):

    def setUp(self):
        ism = "Ali"
        familiya = "Valiyev"
        passport = "AA1234567"
        tyil = 2000
        self.shaxs1 = Shaxs(ism, familiya, passport, tyil)

    def shaxsni_tekshirish(self):
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)

    def setUp(self):
        ism = 'Vali'
        familiya = 'Aliyev'
        passport = 'AC2314134'
        tyil = 2004
        idraqam = 12345678
        manzil = 'Urganch'
        self.talaba1 = Talaba(ism, familiya, passport, tyil, idraqam, manzil)

    def talabani_tekshirish(self):
        self.assertIsNotNone(self.talaba1.ism)
        self.assertIsNotNone(self.talaba1.familiya)
        self.assertIsNotNone(self.talaba1.passport)
        self.assertIsNotNone(self.talaba1.tyil)
        self.assertIsNotNone(self.talaba1.idraqam)
        self.assertIsNotNone(self.talaba1.manzil)


unittest.main()
