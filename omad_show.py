from random import *

print("Omad shou o'yniga xush kelibsiz")
print("Siz 10 ta raqam kiritishingiz kerak")
nomerlar = []
n = 0
while True:
    kiritish = input(f"{n+1}-Raqamni kiriting: ")
    nomerlar.append(kiritish)
    javob = input("Yana kiritasizmi (yes,no): ")
    if javob.lower() != 'no':
        print("Yana raqam kiriting")
        n += 1
    else:
        break

print("Raqamlar kiritildi\n")
print("Tasdifiy raqamlarni tanlash uchun 'start' buyrug'ini yuboring\n")
while True:
    buyruq = input("Buyruq yuborish: ")
    if buyruq.lower() != 'start':
        print("Bunday buyruq yo'q, Qaytadan 'start' buyrug'ini kiriting")
    else:
        raqam = choice(nomerlar)
        print(f"Keyingi o'yinimzi qatnashchisi {raqam} manashu raqam egasi, olqishllaringiz👏👏 sizni keyingi o'ying taklif qilamiz")
        break

