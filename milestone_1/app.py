
movie_list = []

def addmovies():
        add_movie = input("Would you like to add a movie to your collection?")
        while (add_movie == "y"):
            name = input("Enter the movie name")
            year = int(input("Enter the year it was made in"))
            actor = input("Enter the main actor's name")
            movie_list.append(
            {
            "name" : name,
            "year" : year,
            "actor" : actor

            })
            add_movie = input("Would you like to add a movie to your collection?")

        menu()
def listmovies():
    for movie in movie_list:
        printmovie(movie)
    menu()

def quitmenu():
    quit

def findmovie():
    movie_name = input("Enter a movie name")
    for movie in movie_list:
      if movie["name"] == movie_name:
        #print(f"{movie_name} is in the watch list.")1

        printmovie(movie)
    else:
        print("no movie found")
        #print(f"{movie_name} is not in the watch list")


    menu()

def menu():
    main_menu = int(input("Enter a number between 1-5 to select an option from the following"
            "\n\t\t1. Add a movie "
             "\n\t\t2. Find a movie "
             "\n\t\t4. List all movies"
             "\n\t\t5. Exit (quit) "))
    while(main_menu != 5):
        if main_menu == 1:
            addmovies()
        elif main_menu == 2:
            findmovie()
        elif main_menu == 3:
            pass
        elif main_menu == 4:
            listmovies()
        elif main_menu == 5:
            quitmenu()
        else:
            print("Unknown command... please try again")
            main_menu = int(input("Enter a number between 1-5 to select an option from the following"))

'''
useroptions = {
    1: addmovies,
    2: findmovie,
    4: listmovies,
    5: quitmenu
}

def menu1():
    selection = int(input("Enter an option"))
    while selection != 5:
        if selection in useroptions:
            option = useroptions[selection]
            option()
        else:
            print("Unknown command")
    selection = int(input("Enter an option"))
'''
def printmovie(movie):
    print(f"MOVIE NAME: {movie['name']}")
    print(f"YEAR: {movie['year']}")
    print(f"ACTOR: {movie['actor']}")



menu()

