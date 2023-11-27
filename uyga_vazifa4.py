def sonlar_kopaytma(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma
print(sonlar_kopaytma(1,2,3,4,5,6,7,8,9))