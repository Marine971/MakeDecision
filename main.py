import random
import requests

# create a list of animate
url = "https://api.jikan.moe/v4/anime"
response = requests.get(url).json()
anime = response['data']

def ChoiceAnime(title):
    titles = []
    for an in anime:
        titles.append(an)
        type = an['genres'][0]['name']
        name = an['title']
        if ( type == title): print(name)


choice1 = input(" Do you want watch anime ? y : yes n : no")
if choice1 == "y":
# functionnality 1 : Add different proprety to animate ( films, series ) and ask the user what's kind of animate


    choice2 = input("What type of anime do you want to watch ? 1: Comedy 2: Action 3: Adventure 4: Sports 5: Drama ")
    ChoiceAnime(choice2)


elif choice1 == "n":
    print("I don't have idea for you")







# functionnality 2 : Add Duration and ask to the user

