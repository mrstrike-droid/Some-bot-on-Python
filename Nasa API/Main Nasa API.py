from re import T
import requests
def getimagine():
    while True:
        try:
            date = input()
            r = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=Zex7CBAHQmbVfomUeIOyZXt9d8JccD4R50fNNhal&date={date}')
            parsed = r.json()
            status =  r.status_code
            print (status)
            if status == 200:
                print (parsed)
            elif status == 400:
                print ('Wrong date type input: YYYY-MM-DD')
            else:
                r.raise_for_status()    
        except requests.exceptions.HTTPError as err:
            print (err)    
print('Please specifie the date in such way: YYYY-MM-DD. Actual on current or previous days')
getimagine()
input()


