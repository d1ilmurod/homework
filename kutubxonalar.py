from datetime import datetime, timedelta

bugun = datetime.today()


for i in range(10):
    date = bugun + timedelta(weeks=i*2)
    print(date.strftime("%Y-%m-%d"))
