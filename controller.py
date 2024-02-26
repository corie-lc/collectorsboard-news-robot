import crawler

def control_panel():
    print("Welcome to CollectorsBoard Robot Menu")
    print("-------------------")

    print("This application is secured by ENV VAR and will fail upon an incorrectly setup env!")

    print("1) PokemonTCG ")

    name = input('Which Robot Would You Like To Use?: ')

    if name == "1":
        print("-- LOADING PokemonTCG Robot Please Wait..")
        crawler.pokemon_news_robot()
        print("FINISHED")
        print("------------------------")
        control_panel()
    else:
        print("Invalid Input")


control_panel()