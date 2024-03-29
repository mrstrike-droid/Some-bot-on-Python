from matplotlib import path
import requests
import os
from PIL import Image, ImageFont, ImageDraw 
def getimage():
    global camera, nameofcamera, sol1, end, earth_date
    global roveridentificator, rovername, launch_date, landing_date, status, pathimg
    try:
        while True:
            print('Please enter the date from 0 sol to 1000, or maybe more')
            sol = input()
            os.makedirs(f'Nasa imagine of the mars/Imagine of a sol {sol}')
            r = requests.get (f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key=Zex7CBAHQmbVfomUeIOyZXt9d8JccD4R50fNNhal')
            parsed = r.json()
            if r.status_code == 200:
                Parsed_dict = parsed['photos']
                print('It will take a while')
                for i in Parsed_dict:
                    url1 = i['img_src']
                    identificator = i['id']
                    img = requests.get (url1)
                    extimg = img.headers["content-type"][6:]
                    pathimg = os.path.join(os.getcwd(), f'Nasa imagine of the mars/Imagine of a sol {sol}',f'img{sol}{identificator}.{extimg}')
                    with open (pathimg, 'wb') as f:
                        for chunk in img:
                                f.write(chunk) 
                    camera = i['camera']
                    nameofcamera = camera['name']
                    sol1 = i['sol']
                    earth_date = i['earth_date']
                    rover = i['rover']
                    roveridentificator = rover['id']
                    rovername = rover ['name']
                    landing_date = rover['landing_date']
                    launch_date = rover['launch_date']
                    status = rover['status']
                    end = '\n'
                    add_text_to_img ()
                break
            elif r.status_code == 400:
                print ('Wrong date format')  
    except ValueError:
        print('Please enter: from 0 to curent sol of mission')
    except requests.exceptions.HTTPError as err:
        print (err)
def add_text_to_img ():
    my_image = Image.open(pathimg)
    title_text = 'sol: ' + str(sol1)+ end + 'Earth date: ' + str(earth_date)+ end + 'Id of rover: '+ str(roveridentificator) + end + 'Name of rover: '+ str(rovername) + end + 'Lauching date: ' + str(launch_date) + end + 'Landing date: '+ str(landing_date) + end + 'Mission status: '+ str(status) + end + 'Name of camera: ' + str(nameofcamera)
    width, height = my_image.size
    if width >= 1024 & height >= 1024:
        font = ImageFont.load_default()
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((20,20), title_text, fill = 'yellow', font=font)
        my_image.save(pathimg)
    elif width <= 1024 & height <= 1024:
        os.remove(pathimg)
def repeatprogramm():
    repeatprogramm = 1
    while repeatprogramm == 1:
        getimage()
        print('Done')
        print ('If you want to start again press: 1\n' + 'If not, press: 2')
        repeatprogramm = int(input())
if __name__ == "__main__":
    print ('Chose your directory to save files:(Click on the path bar of the Windows Explorer and tap Ctrl+C and then Ctrl+V)')
    os.chdir(input())
    repeatprogramm()

