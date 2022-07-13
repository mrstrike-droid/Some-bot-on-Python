import json
import os
import random
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
def random_recipe():
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
    with open('C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Recepies.json','r', encoding='utf-8' ) as file:
        text = json.load(file)
        print('Введите ингредиенты: ')
        string2=str(input())
        print('Searching...')
        for i in text:
            id_foto = i[0]
            title = i[1]
            body = i[2]
            url = i[4]
            end = '\n'
            recipi1 = i[3]            
            string1 = recipi1
            unwanted_characters = ".,!?"
            string1_words = set(string1.split())
            string2_words = set(string2.split())
            string1_words = {word.strip(unwanted_characters) for word in string1_words}
            string2_words = {word.strip(unwanted_characters) for word in string2_words}
            string2_words = {word.strip(unwanted_characters).lower() for word in string2_words}
            common_words = string1_words & string2_words
            if len(common_words) >= 3:
                print(title+end+body+end+'Список ингридиентов: '+recipi1+end+'Ссылка на рецепт: '+url)
                break
def search_recipe_by_title():
    with open('C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Recepies.json','r', encoding='utf-8' ) as file:
        text = json.load(file)
        print('Поиск блюда по названию: ')
        string2=str(input())
        print('Какое количество блюд вы хотите увидеть: ')
        recipe_shown = int(input())
        recipe_count = 0
        for i in text:
            id_foto = i[0]
            body = i[2]
            recipi1 = i[3]
            url = i[4]
            end = '\n'
            title = i[1]           
            string1 = title
            unwanted_characters = ".,!?"
            string1_words = set(string1.split())
            string2_words = set(string2.split())
            string1_words = {word.strip(unwanted_characters) for word in string1_words}
            string2_words = {word.strip(unwanted_characters) for word in string2_words}
            string2_words = {word.strip(unwanted_characters).lower() for word in string2_words}
            common_words = string1_words & string2_words
            if len(common_words) >= 1:
                recipe_count +=1
                print(title+end+body+end+'Список ингридиентов: '+recipi1+end+'Ссылка на рецепт: '+url)
                if recipe_shown == recipe_count:
                    break
search_recipe_by_title()



    