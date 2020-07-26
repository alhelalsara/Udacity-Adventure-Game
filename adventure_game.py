import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def intro(item, option):
    print_pause("You find yourself standing in the woods. \n")
    print_pause("There are some rumors going around that a " + option + " lives somewhere close "
                ", and has been terrifying the nearby village.\n")
    print_pause("In front of you is an old house.\n")
    print_pause("To your right is an enchanted forest.\n")
    print_pause("In your hand you hold your old"
                " dagger.\n")


def forest(item, option):
    if "sword" in item:
        print_pause("\nYou walk cautiously into the forest.")
        print_pause("\nYou've been here before, and gotten all"
                    " the items. It's just an empty forst"
                    " now.")
        print_pause("\nYou walk back to the woods.\n")
    else:
        print_pause("\nYou walk cautiously into the forest.")
        print_pause("\nIt turns out the forst is indeed enchanted.")
        print_pause("\nYour eye falls on a metal behind a "
                    "tree.")
        print_pause("\nYou have found the Magical Sword!")
        print_pause("\nYou throw out your old dagger and take "
                    "the sword with you.")
        print_pause("\nYou walk back out to the woods.\n")
        item.append("sword")
    woods(item, option)


def house(item, option):
    print_pause("\nYou approach the door of the old house.")
    print_pause("\nYou are about to knock but the door "
                "opens by itself and out steps a " + option + ".")
    print_pause("\nEep! This is the " + option + "'s house!")
    print_pause("\nThe " + option + " attacks you!\n")
    if "sword" not in item:
        print_pause("You feel that you are not equipped for this, "
                    "you only have a tiny old dagger.\n")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if choice2 == "1":
            if "sword" in item:
                print_pause("\nAs the " + option + " moves to attack, "
                            "you draw your new magical sword.")
                print_pause("\nThe magical sword shines brightly in "
                            "your hand as you get prepared for the "
                            "attack.")
                print_pause("\nBut the " + option + "takes one look at "
                            "your shiny magical sword and runs away!")
                print_pause("\nYou have rid the village of the " + option +
                            ". You are victorious!\n")
            else:
                print_pause("\nYou try your best...")
                print_pause("but your old dagger is no match for the "
                            + option + ".")
                print_pause("\nYou have been defeated!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou run back into the woods. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            woods(item, option)
            break


def woods(item, option):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to walk into the enchanted forest.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            house(item, option)
            break
        elif choice1 == "2":
            forest(item, option)
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nGreat! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you again next time.\n\n\n")
    else:
        play_again()


def play_game():
    item = []
    option = random.choice(["Giant", "Black Mage", "Imp", "Dragon",
                            "Troll"])
    intro(item, option)
    woods(item, option)


play_game()
