from re import T
import requests
import os
def getimagine():
    while True:
        try:
            date = input()
            r = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=Zex7CBAHQmbVfomUeIOyZXt9d8JccD4R50fNNhal&date={date}')
            parsed = r.json()
            if r.status_code == 200:
                print (parsed)
                url = parsed['hdurl']
                img = requests.get (url)
                text = parsed['explanation'] 
                ext = img.headers["content-type"][6:]
                exttext = 'txt'
                print ('Chose your directory to save:(Click on the path bar of the Windows Explorer and tap Ctrl+C and then Ctrl+V)')
                os.chdir(input())
                os.makedirs(f'Nasa imagine/{date} Imagine of a day')
                pathimg = os.path.join(os.getcwd(), f'Nasa imagine/{date} Imagine of a day',f'img{date}.{ext}')
                pathtext = os.path.join(os.getcwd(), f'Nasa imagine/{date} Imagine of a day',f'text{date}.{exttext}')
                with open (pathimg, 'wb') as f:
                    for chunk in img:
                        f.write(chunk) 
                with open (pathtext, 'w') as f:
                    f.write(text)
                print ('Done!')
                os.startfile(pathimg) 
                os.startfile(pathtext)        
            elif r.status_code == 400:
                print ('Wrong date type input: YYYY-MM-DD')
            else:
                r.raise_for_status()    
        except requests.exceptions.HTTPError as err:
            print (err)
print('Please specifie the date in such way: YYYY-MM-DD. Actual on current or previous days')
getimagine()



