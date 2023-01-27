import datetime


def change_date():
    x = datetime.datetime.now()
    while True:
        if x.month == 12 and x.day == 31:
            x = x.replace(year=x.year+1, month=1,day=1)
        elif x.month == 1 or x.month==3 or x.month==5 or x.month==7 or x.month==8 or x.month==10 or x.month==12:
            if x.day == 31: 
                x = x.replace(month=x.month+1,day=1)
        elif x.month==2:
            if x.day == 28: 
                x = x.replace(month=x.month+1,day=1)
        elif x.month==4 or x.month==6 or x.month==9 or x.month==11:
            if x.day == 30: 
                x = x.replace(month=x.month+1,day=1)
        if x.day == 1:
            print(x)
        x = x.replace(day = x.day + 1) 
        print(x)
y = datetime.datetime(year = 2023, month=1, day=27, hour=17, minute=10).strftime("%Y-%m-%d %H:%M")
while True:
    z = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(y)
    print(z)
    if y == z:
        print('hello')
        break

#change_date()