"""
Travel Tracker A1
Name: Daniel Mackenzie
Date started: 30/08/20
GitHub URL: https://github.com/DGMGIT/travel-tracker-assignment-1-ichaturvedi-master
Draft 2 - part 02
worked on program. made welcome message into function, added function to retrieve places file, added choice to menu
"""


MENU = "Menu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit\n>>> "


def main():
    places = get_places()
    print_welcome_msg(places)
    get_choices = input(MENU).upper()
    while get_choices != "Q":
        if get_choices == "L":
            pass
        elif get_choices == "A":
            pass
        elif get_choices == "M":
            pass
        else:
            pass


def get_places():
    list_places = []
    input_file = open("places.csv", 'r')
    for line in input_file:
        line = line.strip()
        place = line.split(",")
        list_places.append(place)
    input_file.close()
    return list_places


def print_welcome_msg(places):
    print("Travel Tracker 1.0 - by Daniel Mackenzie\n"
          f"{len(places)} places loaded from places.csv")


if __name__ == '__main__':
    main()