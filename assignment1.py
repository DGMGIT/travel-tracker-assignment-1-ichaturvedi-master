"""
Travel Tracker A1
Name: Daniel Mackenzie
Date started: 30/08/20
GitHub URL: https://github.com/DGMGIT/travel-tracker-assignment-1-ichaturvedi-master
Draft 2 - part 03
worked on program. add choices L (print_list_places) prints list of places, total places, number places left to visit
add second get_choices to stop endless looping
"""


from operator import itemgetter


MENU = "Menu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit\n>>> "


def main():
    places = get_places()
    print_welcome_msg(places)
    get_choices = input(MENU).upper()
    while get_choices != "Q":
        if get_choices == "L":
            print_list_places(places)
        elif get_choices == "A":
            pass
        elif get_choices == "M":
            pass
        else:
            print("Invalid menu choice")
        get_choices = input(MENU).upper()


def get_places():
    list_places = []
    input_file = open("places.csv", 'r')
    for line in input_file:
        line = line.strip()
        place = line.split(",")
        place[2] = int(place[2])  # short fix for itemgetter to recognize as int
        list_places.append(place)
    input_file.close()
    return list_places


def print_welcome_msg(places):
    print("Travel Tracker 1.0 - by Daniel Mackenzie\n"
          f"{len(places)} places loaded from places.csv")


def print_list_places(places):
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


if __name__ == '__main__':
    main()