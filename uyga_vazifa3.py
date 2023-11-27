#1 juft sonn funksiya
def juft_tok(son):
    """Bu funksiya sonni juft yoki toqligini aniqlovchi funksiya"""
    if son % 2 == 0:
        print(f'{son} juft son')
    else:
        print(f'{son} toq son')

juft_tok(int(input('Son kiriting: '))) 

#2solishtirish funksiya

def katta_kichik(son1,son2):
    """Bu funksiya ikkita sonni katta yoki kichikligini topadi"""
    if son1 > son2:
        print(f"Birinchi son katta {son1}")

    elif son1 < son2:
        print(f"Ikkinchi son katta {son2}")
    else:
        print(f'Ular teng {son1} = {son2}')
        
katta_kichik(int(input('Birinchi sonni kiritng: ')),int(input('Ikkinchi sonni kiritng: '))) 
    
#3daraja funksiyasi

def daraja(son,son2):
    """Sonni darajaga ko'taruvchi funksiya"""
    print(f"{son} ning darajasi ga: {son ** son2} teng")

daraja(int(input('Son kiriting: ')),int(input('Darajani kiriting: ')))