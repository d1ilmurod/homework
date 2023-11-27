"""                                Birinchi uyga vazifa """

itpark = ['backend dasturlash','frontent dasturlash','kompyuter savodxonligi','Foundation','mobi dasturlash','video mantaj','3d modellashtirish','grafik dizayn','smm','it english']


print(len(itpark))# uzunigini chiqaraadi 10 uzunligi


print(sorted(itpark)) #ro'yxatni alifbo ko'rinishida ekranga chiqaradi


print(sorted(itpark,reverse=True))# alifbo tartibi  teskari ko'rinishda chiqaradi

print(itpark)#asil ro'yxat

itpark.reverse()

print(itpark)#ro'yxatni ortidan boshlab chiqaradi 


itpark.sort() #alifbo bo'yicha tartiblaydi
print(itpark)

itpark.sort(reverse=True)#alifbo tartibi bo'yicha teskari tartiblaydi
print(itpark)


""" keyingi vazfa """

juft_sonlar = list(range(120,1200,2))#120 dan 1198 gacha bo'lgan sonlar juft sonlar

print(sum(juft_sonlar))# shu sonlarni yig'indisi

print('eng kichik juft son: ',min(juft_sonlar),'eng katta juft son: ',max(juft_sonlar)) #ro'yxatdagi eng kichik va eng katta sonlar

print(len(juft_sonlar))#ro'yxatning uzunligi yoki soni
