import datetime

date = datetime.date(2024, 12, 25)
toady = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2040, 1, 1, 12, 20, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("target date has passed")
else:
    print("target date has not passed")
