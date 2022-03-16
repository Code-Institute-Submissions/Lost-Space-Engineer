import os
import random
import sys
import time
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import prompt

aval_tools = ["Ductape", "Spanner", "Hammer", "Screwdriver", "String",
              "Super Glue"]

PREV_POSITION = ""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class DirectionValidator(Validator):
    """
    Direction validator
    """
    def validate(self, document):
        text = document.text
        words = ["left", "right", "forward", "backwards"]
        if text not in words:
            raise ValidationError(message="This is not a correct direction!")


class decisionValidator(Validator):
    """
    Yes or No Validation
    """
    def validate(self, document):
        text = document.text
        words = ["yes", "no"]
        if text not in words:
            raise ValidationError(message="Incorrect word try again!")


class SubSystem:
    """
    Sub Systems
    """
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


NAV = SubSystem("Navigation", False, False)
POWER = SubSystem("Power", False, False)
LIGHTSPEED = SubSystem("Light Speed Drive", False, False)
LIFESUP = SubSystem("Life Support", False, False)


class Inventory:
    """
    Class for storing Inventory
    """
    def __init__(self, slot, durability):
        self.slot = slot
        self.tools = {}
        self.durability = durability

    def add_item(self, tool):
        self.tools[tool.name] = tool

    def __str__(self):
        out = '\t'.join(['slot', 'Name', 'Dur'])
        for tool in self.tools.values():
            out += '\t'.join([str(x) for x in
                             [tool.slot, tool.name, tool.durability]])


def directions(values):
    """
    directions function
    """
    count = len(values)
    print(f"You have {count} directions to go...")
    print("Please choose one of the following")
    print(values)
    direction = prompt(
        "Which way do you want to go??\n",
        validator=DirectionValidator())

    return direction


def tools():
    """
    Function to collect a random tool
    """
    print("Congratulations you have found a room containing a tool")
    print("You look around and find a box that looks hopefull")
    room_tool = random.choice(aval_tools)
    room_dura = random.randint(1, 100)
    gettool = prompt("")


def repair_system(system):
    """
    Function to run when repairing a subsystem.
    This calls on the subsystem class.
    """
    print(f"You have found the {system} room. The system is borken and is"
          " in need of repair")
    check_inv = prompt("Would you like to check you inventory before"
                       " attempting to fix the system?\n",
                       validator=decisionValidator())

    if check_inv == "yes":
        print(Inventory)
    print("To repair the system you need to select an item from your"
          " inventory")
    repair = prompt("Please choose an inventory slot to use\n")


def start_game():
    """
    looks for input from player to begin the adventure
    """
    print("Welcome to the text adventure game Lost Space Engineer\n")
    print("The aim of the game is to explore the ship and "
          "fix any broken sub-systems")
    print("While exploring the ship you may find tools "
          "to help fix any broken systems\n")
    while True:
        play = input("Are you ready? if so type 'play'\n")

        if play_check(play):
            print("Good Luck and have fun!!")
            PREV_POSITION = "Start Game"
            stage_one(PREV_POSITION)


def play_check(value):
    """
    Checks to see if the player has enter play and it's valid
    """
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


def stage_one(PREV_POSITION):
    """
    First Steps scenario
    """
    clear()
    print("You have woken from stasis. However, something doesn't seem right.")
    print("After gathering your senses you stumble out the room to find lights"
          " flickering everywhere and nobody in sight.\n")
    ways = ["left", "forward", "right", "backwards"]
    direction = directions(ways)
    PREV_POSITION = "stage_one"
    if direction == "left":
        stage_two(PREV_POSITION)
    elif direction == "forward":
        stage_three(PREV_POSITION)
    elif direction == "right":
        stage_four(PREV_POSITION)
    elif direction == "backwards":
        print("As you left the room the door slams shut behind you and you're "
              "unable to get back in")
        time.sleep(5)
        stage_one(PREV_POSITION)


def stage_two(PREV_POSITION):
    """
    Stage Two Scenario
    """
    clear()
    if POWER.power is False:
        print("You travel down a coridoor,"
              " the lights are flickering on and off.")
    else:
        print("You travel down a coridoor, the lights are blinking red")
        print("you get to the end of the coridoor and find 2 short coridoors"
              " with doors at the end.")
    ways = ["left", "forward", "backwards"]
    direction = directions(ways)
    PREV_POSITION = "stage_two"
    if direction == "left":
        print("Power Sub system")
    elif direction == "forward":
        tools()
    elif direction == "backwards":
        stage_one(PREV_POSITION)


def stage_three(PREV_POSITION):
    """
    Stage Three Scenario
    """
    clear()
    print("")
    print("")
    ways = ["left", "forward", "right", "backwards"]
    direction = directions(ways)
    PREV_POSITION = "stage_three"
    subsystem = "Navigation"
    if direction == "left":
        repair_system(subsystem)
    elif direction == "forward":
        print("Tool")
    elif direction == "right":
        print("Locked Airlock")
    elif direction == "backwards":
        stage_one(PREV_POSITION)


def stage_four(PREV_POSITION):
    """
    Stage four Scenario
    """
    clear()
    print("")
    print("")
    ways = ["left", "right", "backwards"]
    direction = directions(ways)
    PREV_POSITION = "stage_four"
    if direction == "left":
        print("Sub system Life Support")
    elif direction == "right":
        stage_five(PREV_POSITION)
    elif direction == "backwards":
        stage_one(PREV_POSITION)


def stage_five(PREV_POSITION):
    """
    Stage five Scenario
    """
    clear()
    print("")
    print("")
    ways = ["left", "forward", "right", "backwards"]
    direction = directions(ways)
    PREV_POSITION = "stage_five"
    if direction == "left":
        print("Tool")
    elif direction == "forward":
        stage_six(PREV_POSITION)
    elif direction == "right":
        print("Sub System LSD")
    elif direction == "backwards":
        stage_four(PREV_POSITION)


def stage_six(PREV_POSITION):
    """
    Stage six Scenario
    """
    clear()
    print("")
    print("")
    ways = ["forward", "right", "backwards"]
    direction = directions(ways)
    PREV_POSITION = "stage_six"
    if direction == "forward":
        if POWER.fixed and NAV.fixed and LIFESUP.fixed and LIGHTSPEED.fixed:
            finish()
        else:
            print("The door is locked, not all Sub-Systems have been repaired")
            time.sleep(5)
            stage_six(PREV_POSITION)
    elif direction == "right":
        print("Tool")
    elif direction == "backwards":
        stage_five(PREV_POSITION)


def finish():
    """
    The Finish - Game Over
    """
    clear()
    print("Congratulations, you have completed the text based adventure game"
          " Lost Space engineer")
    print("If you want to play again, please refresh your browser!\n")
    print("Thanks for playing!!")
    sys.exit()


clear()
start_game()
