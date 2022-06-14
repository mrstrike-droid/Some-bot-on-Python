import requests
def getimagine():
    try:
        date = input()
        r = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=Zex7CBAHQmbVfomUeIOyZXt9d8JccD4R50fNNhal&date={date}')
        r1 = r.json()
        print (r1)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print ("Looks like someone entered the wrong date format:",err)
print('Please specifie the date in such way: YYYY-MM-DD')
getimagine()
input()


