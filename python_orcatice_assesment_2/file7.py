from datetime import date, timedelta

def generate_dates():
    today = date.today()

    for i in range(7):
        yield today + timedelta(days=i)


for d in generate_dates():
    print(d)