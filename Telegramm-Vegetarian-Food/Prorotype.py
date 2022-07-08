string1 = 'капуста белокочанная, крупа манная, лук репчатый, майонез,постный, чеснок, соус томатный, соль, хмели-сунели'
string2=str(input())
unwanted_characters = ".,!?"
string1_words = set(string1.split())
string2_words = set(string2.split())
string1_words = {word.strip(unwanted_characters) for word in string1_words}
string2_words = {word.strip(unwanted_characters) for word in string2_words}
string2_words = {word.strip(unwanted_characters).lower() for word in string2_words}
common_words = string1_words & string2_words
if len(common_words) == 3:
    print(common_words)