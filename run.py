import os
import random
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import prompt

aval_tools = ["Ductape", "Spanner", "Hammer", "Screwdriver", "String",
              "Super Glue"]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class DirectionValidator(Validator):
    """Direction validator"""
    def validate(self, document):
        text = document.text
        words = ["left", "right", "forward", "backwards"]
        if text not in words:
            raise ValidationError(message="This is not a correct direction!")


class SubSystem:
    """Sub Systems"""
    def __init__(self, system, power, fixed):
        self.system = system
        self.power = power
        self.fixed = fixed

    def power_change(self, system, power):
        if power is True:
            print(f"{system} is currently online and doesn't need repairing")
        else:
            self.power = True
            print(f"{system} is coming online")

    def repair(self, fixed):
        if fixed is True:
            print(f"{system} is currently in working order")
        else:
            self.fixed = False
            print(f"{system} is now repaired! Well done!")


NAVIGATION = SubSystem("navigation", False, False)
POWER = SubSystem("power", False, False)
LIGHTSPEEDDRIVE = SubSystem("Light Speed Drive", False, False)
LIFESUPPORT = SubSystem("Life Support", False, False)


class Tools:
    """Class for tools"""
    def __init__(self, name, durability):
        self.name = name
        self.durability = durability


class Inventory:
    """Class for storing Inventory"""
    def __init__(self):
        self.tools = {}

    def add_item(self, tool):
        self.tools[tool.name] = tool

    def print_inv(self):
        print('\t'.join(['Name', 'Dur']))
        for tool in self.tools.values():
            print('\t'.join([str(x) for x in [tool.name, tool.durability]]))


def directions(values):
    """directions function"""
    count = len(values)
    print(f"You have {count} directions to go...")
    print("Please choose one of the following")
    print(values)
    direction = prompt(
        "Which way do you want to go??\n",
        validator=DirectionValidator())

    return direction


def tools():
    """Function to collect a random tool"""
    print("Congratulations you have found a room containing tools")
    print("You look around and find a box that looks hopefull")


def start_game():
    """looks for input from player to begin the adventure"""
    print("Welcome to the text adventure game Lost Space Engineer\n")
    print("The aim of the game is to explore the ship and "
          "fix any broken sub-systems")
    print("While exploring the ship you may find tools "
          "to help fix any broken systems\n")
    while True:
        play = input("Are you ready? if so type 'play'\n")

        if play_check(play):
            print("Good Luck and have fun!!")

            stage_one()


def play_check(value):
    """Checks to see if the player has enter play and it's valid"""
    try:
        if value != "play":
            raise ValueError(
                "Please type 'play' in all lowercase"
            )
    except ValueError as e:
        clear()
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def stage_one():
    """First Steps scenario"""
    print("You have woken from stasis. However, something doesn't seem right.")
    print("After gathering your senses you stumble out the room to find lights"
          " flickering everywhere and nobody in sight.\n")
    ways = ["left", "forward", "right", "backwards"]
    direction = directions(ways)
    if direction == "left":
        stage_two()
    elif direction == "forward":
        stage_three()
    elif direction == "right":
        stage_four()
    elif direction == "backwards":
        print("As you left the room the door slams shut behind you and you're "
              "unable to get back in")


def stage_two():
    """Stage Two Scenario"""
    clear()
    if POWER.power is False:
        print("You travel down a coridoor,"
              " the lights are flickering on and off.")
    else:
        print("You travel down a coridoor, the lights are blinking red")
    print("you get to the end of the coridoor and find 2 short coridoors"
          " with doors at the end.")
    ways = ["left", "forward"]
    direction = directions(ways)
    if direction == "left":
        print("left")
    elif direction == "forward":
        print("forward")


def stage_three():
    """Stage Three Scenario"""
    clear()
    print("")
    print("")
    ways = ["left", "forward", "right", "backwards"]
    direction = directions(ways)
    if direction == "left":
        print("left")
    elif direction == "forward":
        print("forward")
    elif direction == "right":
        print("right")
    elif direction == "backwards":
        print("backwards")


def stage_four():
    """Stage four Scenario"""
    clear()
    print("")
    print("")
    ways = ["left", "right", "backwards"]
    direction = directions(ways)
    if direction == "left":
        print("left")
    elif direction == "right":
        print("right")
    elif direction == "backwards":
        print("backwards")


def stage_five():
    """Stage five Scenario"""
    clear()
    print("")
    print("")
    ways = ["left", "forward", "right", "backwards"]
    direction = directions(ways)
    if direction == "left":
        print("left")
    elif direction == "forward":
        print("forward")
    elif direction == "right":
        print("right")
    elif direction == "backwards":
        print("backwards")


def stage_six():
    """Stage six Scenario"""
    clear()
    print("")
    print("")
    ways = ["forward", "right", "backwards"]
    direction = directions(ways)
    if direction == "forward":
        print("forward")
    elif direction == "right":
        print("right")
    elif direction == "backwards":
        print("backwards")


def finish():
    """The Finish - Game Over"""
    clear()
    print("")
    print("")


clear()
start_game()
