import json
import os
import random
d = {}
rand = random.randrange(0,50)
with open('C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Recepies.json','r', encoding='utf-8' ) as file:
    text = json.load(file)
    first_dict = text[rand]
    id_foto = first_dict[0]
    print(first_dict[1:])
    title = first_dict[1]
    body = first_dict[2]
    recipi = first_dict[3]
    url = first_dict[4]
    end = '\n'
    print(title+end+body+end+'Список ингридиентов: '+recipi+end+'Ссылка на рецепт: '+url)
pathimg = (f'C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Картинки\\{id_foto}.jpeg')
os.startfile(pathimg)




    