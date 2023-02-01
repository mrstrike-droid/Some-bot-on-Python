from datetime import datetime
from datetime import timedelta
import datetime
def compare_time(): 
    z = datetime.datetime(year=2023,month=1,day=31,hour=20,minute=50).strftime("%Y-%m-%d %H:%M")
    while True:        
        x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        if x == z:
            z = datetime.datetime.strptime(z, '%Y-%m-%d %H:%M')
            z = z+timedelta(days = 1)
            z= datetime.datetime.strftime(z, "%Y-%m-%d %H:%M")
            print(z)
compare_time()

