"""
Travel Tracker A1
Name: Daniel Mackenzie
Date started: 30/08/20
GitHub URL: https://github.com/DGMGIT/travel-tracker-assignment-1-ichaturvedi-master
Draft 2 - part 06
worked on program. added (output_places) output current list, added quit message, added dotstrings,
made places.csv a constants
"""


from operator import itemgetter


MENU = "Menu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit\n>>> "
places_file = "places.csv"  #format. city, country, visited status V/N, priority


def main():
    places = get_places()
    print_welcome_msg(places)
    get_choices = input(MENU).upper()
    while get_choices != "Q":
        if get_choices == "L":
            print_list_places(places)
        elif get_choices == "A":
            new_place = valid_new_place()
            places.append(new_place)
            print("{} in {} (priority {}) added to Travel Tracker".format(new_place[0], new_place[1], new_place[2]))
        elif get_choices == "M": # the hardest to do
            n = places_non_visited(places)
            if n == 0:
                print("No unvisited places")
            else:
                print_list_places(places)
                mark_as_visited = valid_mark_visit(places)
                if places[mark_as_visited - 1][3] == "v":
                    print("That place is already visited")
                else:
                    places[mark_as_visited - 1][3] = "v"
        else:
            print("Invalid menu choice")
        get_choices = input(MENU).upper()
    output_places(places)
    print(f"{len(places)} places saved to places.csv\n"
          "Have a nice day :")


def get_places():
    """input a list of lists containing [city, country, visited status, priority]"""
    list_places = []
    input_file = open(places_file, 'r')
    for line in input_file:
        line = line.strip()
        place = line.split(",")
        place[2] = int(place[2])  # short fix for itemgetter to recognize as int
        list_places.append(place)
    input_file.close()
    return list_places


def print_welcome_msg(places):
    """print a welcome message"""
    print("Travel Tracker 1.0 - by Daniel Mackenzie\n"
          f"{len(places)} places loaded from places.csv")


def print_list_places(places):
    """prints a sorted list of places, total all up and amount left to visit"""
    places.sort(key=itemgetter(3, 2))
    num = -1
    num_v = 0
    length_city = 0
    length_country = 0
    for place in places: # get len of city ,country and number of visited to make it easier to print
        num += 1
        num1 = len(places[num][0])
        if num1 > length_city:
            length_city = num1
        num2 = len(places[num][1])
        if num2 > length_country:
            length_country = num2
        if places[num][3] == "v":
            num_v += 1
    num = -1
    for place in places: # prints list
        num += 1
        asterisks = " "
        if places[num][3] == "n":
            asterisks = "*"
        city = places[num][0]
        country = places[num][1]
        priority = places[num][2]
        print("{}{}. {:{}} in {:{}} priority {:3} "
              .format(asterisks, num + 1, city, length_city, country, length_country, priority))
    num_2 = len(places)
    num_3 = num_2 - num_v
    if num_3 > 0:  # prints total places, number places left to visit
        print(f"{num_2} places. You still want to visit {num_3} places.")
    elif num_3 == 0:
        print(f"{num_2} places. No places left to visit. Why not add a new place?")


def valid_new_place():
    """ask user to input a new location to visit [city, country, priority] visited status is n"""
    finished = False
    new_place = []
    city = str(input("Name: "))
    while len(city) == 0:
        print("Input can not be blank")
        city = str(input("Name"))
    new_place.append(city)
    country = str(input("Country: "))
    while len(country) == 0:
        print("Input can not be blank")
        country = str(input("Country: "))
    new_place.append(country)
    while finished is False:
        try:
            priority = int(input("Priority: "))
            while priority <= 0:
                print("Number must be > 0")
                priority = int(input("Priority: "))
            finished = True
            new_place.append(priority)
            new_place.append("n")
        except ValueError:
            print("Invalid input; enter a valid number")
    return new_place


def places_non_visited(places):
    """calculates if there are anymore places o visit"""
    places.sort(key=itemgetter(3, 2))  # will not work if not sorted after new place added ???
    n = 0
    num = 0
    for i in places:
        if "n" == places[num][3]:
            n = + 1
        num = + 1
    return n


def valid_mark_visit(places):
    """allows a user to mark a place in places as visited e.g. change n to v(places[place][2])"""
    mark_as_visited = 0
    finished = False
    while finished is False:
        try:
            mark_as_visited = int(input("Enter the number of a place to mark as visited\n>>>"))
            while mark_as_visited < 1 or mark_as_visited > len(places):
                if mark_as_visited < 1:
                    print("Number must be > 0")
                else:
                    print("Invalid place number")
                mark_as_visited = int(input("Enter the number of a place to mark as visited\n>>>"))
            finished = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return mark_as_visited


def output_places(places):
    """output current list to places.csv"""
    for i in range(len(places)):
        places[i][2] = str(places[i][2])  # doesn't work if not a str
    output_file = open(places_file, 'w')
    for i in range(len(places)):
        place = ",".join(places[i])
        print(place, file=output_file)
    output_file.close()


if __name__ == '__main__':
    main()