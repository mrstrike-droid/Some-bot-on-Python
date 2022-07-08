import json
import os
import random
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
def random_recipe():
    global recipi, title, body, url, end
    rand = random.randrange(0,50)
    with open('C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Recepies.json','r', encoding='utf-8' ) as file:
        text = json.load(file)
        first_dict = text[rand]
        id_foto = first_dict[0]
        title = first_dict[1]
        body = first_dict[2]
        recipi = first_dict[3]
        url = first_dict[4]
        end = '\n'
        print(title+end+body+end+'Список ингридиентов: '+recipi+end+'Ссылка на рецепт: '+url)
    #pathimg = (f'C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Картинки\\{id_foto}.jpeg')
    #os.startfile(pathimg)    
def search_recipe():
    random_recipe()
    while True:
        string1 = recipi
        print('Введите ингредиенты: ')
        string2=str(input())
        unwanted_characters = ".,!?"
        string1_words = set(string1.split())
        string2_words = set(string2.split())
        string1_words = {word.strip(unwanted_characters) for word in string1_words}
        string2_words = {word.strip(unwanted_characters) for word in string2_words}
        string2_words = {word.strip(unwanted_characters).lower() for word in string2_words}
        common_words = string1_words & string2_words
        if len(common_words) >= 3:
            print(title+end+body+end+'Список ингридиентов: '+recipi+end+'Ссылка на рецепт: '+url)
            break
        else:
            random_recipe()
search_recipe()



    