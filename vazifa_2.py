butun_son = int(input("Butun son kiriitng>> "))
for son in range(2,11):
    if butun_son % son == 0:
       print(f"Berilgan: {butun_son} sonimiz {son} ga qoldiqsiz bo'linadi")

