def welcome():
    print("What type of animal are you: ")
    animal = input()
    print("Pride Rock welcomes you {}.".format(animal))
    print("Come and celebrate with us!")


welcome()

def visit(place):
    if (place == "The Elephant Graveyard"):
        print("Oh no! There are hyenas here!")
    else:
        print("This place is interesting.")

visit("The Elephant Graveyard")
visit("The Jungle")

def roar(num_roars):
    for roar in range(num_roars):
        print("roar!")
    print("ROAR!!!")
    
roar(3)
