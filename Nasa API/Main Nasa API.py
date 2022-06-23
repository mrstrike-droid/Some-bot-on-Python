from re import T
from urllib import response
import requests
import os
def twooptionofdate():
    global r
    global date
    global startdate
    global enddate
    try:
        if twooption == 1:
            print('Please specifie the date in such way: YYYY-MM-DD. Actual on current or previous days')
            date = input()
            r = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=Zex7CBAHQmbVfomUeIOyZXt9d8JccD4R50fNNhal&date={date}')
            while True:
                parsed = r.json()
                if r.status_code == 200:
                    url = parsed['url']
                    img = requests.get (url)
                    text = parsed['explanation'] 
                    extimg = img.headers["content-type"][6:]
                    exttext = 'txt'
                    os.makedirs(f'Nasa imagine/{date} Imagine of a day')
                    pathimg = os.path.join(os.getcwd(), f'Nasa imagine/{date} Imagine of a day',f'img{date}.{extimg}')
                    pathtext = os.path.join(os.getcwd(), f'Nasa imagine/{date} Imagine of a day',f'text{date}.{exttext}')
                    with open (pathimg, 'wb') as f:
                        for chunk in img:
                            f.write(chunk) 
                    with open (pathtext, 'w') as f:
                        f.write(text)
                    print ('Done!')
                    os.startfile(pathimg) 
                    os.startfile(pathtext)
                    break                                  
        elif twooption == 2:
            print('Please specifie the date in such way: YYYY-MM-DD. First date enter, then last date.')
            startdate = input()
            enddate = input()
            r = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=Zex7CBAHQmbVfomUeIOyZXt9d8JccD4R50fNNhal&start_date={startdate}&end_date={enddate}')
            parsed = r.json()
            print('It will take some time. Please wait.')
            for x in parsed:
                url = x
                url1 = url['url']
                text1 = url['explanation']
                date1 = url['date']
                img = requests.get (url1)
                extimg = img.headers["content-type"][6:]
                exttext = 'txt'
                os.makedirs(f'Nasa imagine/{date1} Imagine of a day')
                pathimg = os.path.join(os.getcwd(), f'Nasa imagine/{date1} Imagine of a day',f'img{date1}.{extimg}')
                pathtext = os.path.join(os.getcwd(), f'Nasa imagine/{date1} Imagine of a day',f'text{date1}.{exttext}')
                with open (pathimg, 'wb') as f:
                    for chunk in img:
                        f.write(chunk) 
                with open (pathtext, 'w') as f:
                    f.write(text1)
            print ('Done!')                 
        else:
            print('Please enter: 1 or 2')
    except ValueError:
        print('Please enter: 1 or 2')
    except requests.exceptions.HTTPError as err:
        print (err)
def repeatprogramm():
    global twooption
    chooseoption = 1
    while chooseoption == 1:
        print ('If you want to find image for specific date enter: 1\nIf you want to get image for some period enter: 2')
        twooption = int(input())
        twooptionofdate()
        print ('If you want to start again press: 1\n' + 'If not, press: 2')
        chooseoption = int(input())
if __name__ == "__main__":
    print ('Chose your directory to save files:(Click on the path bar of the Windows Explorer and tap Ctrl+C and then Ctrl+V)')
    os.chdir(input())
    repeatprogramm()