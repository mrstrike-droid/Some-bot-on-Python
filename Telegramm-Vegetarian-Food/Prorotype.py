from thefuzz import fuzz, process
import json
with open('C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Recepies.json','r', encoding='utf-8' ) as file:
        text = json.load(file)
string2=str(input())
for i in text:
    recipi1 = i[3]            
    string1 = recipi1
    if fuzz.token_sort_ratio(string1, string2) >= 40:
        print(recipi1)
        break

            
