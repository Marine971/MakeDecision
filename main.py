import random
import requests

# create a list of animate
url = "https://api.jikan.moe/v4/anime"
response = requests.get(url).json()
anime = response['data']

titles = []
for an in anime:
    titles.append(an)

choice1 = input(" Do you want watch anime ? y : yes n : no")

# choose randomly one animate
if choice1 == "y":
    type = an['genres'][0]['name']
    # print(random.choice(titles))
    choice2 = input("What type of anime do you want to watch ? 1: Comedy 2: Action 3: Adventure 4: Sports 5: Drama ")
    match choice2:
        case "1":
            print("You choose comedy")
elif choice1 == "n":
    print("I don't have idea for you")





# functionnality 1 : Add different proprety to animate ( films, series ) and ask the user what's kind of animate

# functionnality 2 : Add Duration and ask to the user

