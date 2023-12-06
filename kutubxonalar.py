from datetime import datetime
from datetime import datetime, timedelta
import datetime as dt

bugun = datetime.today()


for i in range(10):
    date = bugun + timedelta(weeks=i*2)
    print(date.strftime("%Y-%m-%d"))


def kalkulyator_yosh(tugulgan_sana):
    bugun = datetime.today()
    yosh = bugun - tugulgan_sana

    yil = yosh.days // 365
    oy = (yosh.days % 365) // 30
    kun = (yosh.days % 365) % 30

    return yil, oy, kun


tugulgan_sana = datetime(2004, 5, 4)
yil, oy, kun = kalkulyator_yosh(tugulgan_sana)

print(f"Siz {yil} yil, {oy} oy, va {kun} kun bo'ldi.")


