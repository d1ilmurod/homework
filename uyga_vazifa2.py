navoiy = {
    't_ism':'alisher navoiy',
    't_sanasi':1441,
    'kasbi':'shoir'
}

xorazimiy = {
    't_ism':'al xorazimiy',
    't_sanasi':783,
    'kasbi':'matematik'
}

temur = {
    't_ism':'amir temur',
    't_sanasi':1336,
    'kasbi':'sarkarda'
}

ulugbek = {
    't_ism':"mirzo ulug'bek",
    't_sanasi':1394,
    'kasbi':'astranom'
}

information = [navoiy,xorazimiy,temur,ulugbek]

for info in information:
    print(f"\n{info['t_ism'].title()}\n{info['t_sanasi']}-yilda tug'ulgan \nKasbi: {info['kasbi'].title()}")