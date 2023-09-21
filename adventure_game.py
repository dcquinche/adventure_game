import time
import random


def print_pause(str):
    print(str)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")


def valid_input(prompt, opt1, opt2):
    while True:
        response = input(prompt)
        if opt1 == response:
            return response
        elif opt2 == response:
            return response


def fight(places_visited, creature, weapon):
    second_choice = valid_input("Would you like to (1) fight "
                                "or (2) run away?\n", "1", "2")
    if "1" == second_choice:
        if "cave" in places_visited:
            print_pause(f"As the {creature} moves to attack, "
                        "you unsheath your new sword.")
            print_pause(f"The sword of {weapon} shines brightly in your "
                        "hand as you brace yourself for the attack.")
            print_pause(f"But the {creature} takes one look "
                        "at your shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {creature}. "
                        "You are victorious!")
        else:
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {creature}.")
            print_pause("You have been defeated!")
        play_again = valid_input("Would you like to play again? "
                                 "(y/n)\n", "y", "n")
        if "y" == play_again:
            print_pause("Excellent! Restarting the game ...")
            play_game()
        else:
            print_pause("Thanks for playing! See you next time.")
    elif "2" == second_choice:
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.")
        field(places_visited, creature, weapon)


def house(places_visited, creature, weapon):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door "
                f"opens and out steps a {creature}.")
    print_pause(f"Eep! This is the {creature}'s house!")
    print_pause(f"The {creature} attacks you!")
    if "cave" not in places_visited:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    fight(places_visited, creature, weapon)


def cave(places_visited, creature, weapon):
    print_pause("You peer cautiously into the cave.")
    if "cave" in places_visited:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
    else:
        places_visited.append("cave")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You have found the magical sword of {weapon}!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
    print_pause("You walk back out to the field.")
    field(places_visited, creature, weapon)


def field(places_visited, creature, weapon):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    first_choice = valid_input("What would you like to do?\n"
                               "(Please enter 1 or 2).\n", "1", "2")

    if "1" == first_choice:
        house(places_visited, creature, weapon)
    elif "2" == first_choice:
        cave(places_visited, creature, weapon)


def play_game():
    places_visited = []
    creature = random.choice(["pirate", "troll", "dragon", "gorgon"])
    weapon = random.choice(["Ogoroth", "Shannara", "Gryffindor"])
    intro()
    field(places_visited, creature, weapon)


play_game()
