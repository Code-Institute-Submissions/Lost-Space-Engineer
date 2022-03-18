# Imports
import os
import random
import sys
import time
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import prompt
# Globals
aval_tools = ["Ductape", "Spanner", "Hammer", "Screwdriver", "String",
              "Super Glue"]

PREV_POSITION = ""

# Clear function


def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Input validators


class DirectionValidator(Validator):
    """
    Direction validator to control user input
    """
    def validate(self, document):
        text = document.text
        words = ["left", "right", "forward", "backwards"]
        if text not in words:
            raise ValidationError(message="This is not a correct direction!")


class decisionValidator(Validator):
    """
    Yes or No Validation to control user input
    """
    def validate(self, document):
        text = document.text
        words = ["yes", "no"]
        if text not in words:
            raise ValidationError(message="Incorrect word try again!")


class slotValidator(Validator):
    """
    Inventory Slot Validation to control user input
    """
    def validate(self, document):
        text = document.text
        words = ["SLOT1", "SLOT2", "SLOT3", "SLOT4", "SLOT5", "SLOT6"]
        if text not in words:
            raise ValidationError(message="Incorrect slot number try again!")


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


def directions(values):
    """
    directions passed from the stage go through here
    """
    count = len(values)
    print(f"You have {count} directions to go...")
    print("Please choose one of the following")
    print(values)
    direction = prompt(
        "Which way do you want to go??\n",
        validator=DirectionValidator())

    return direction

# Classes for Inventory, Items and Subsystems


class SubSystem:
    """
    Class to store the sub system
    It stores System, Power Status and Fixed Status
    """
    def __init__(self, system, power, fixed):
        self.system = system
        self.power = power
        self.fixed = fixed

    def system_status(self):
        if self.fixed is False:
            return False
        else:
            return True

    def power_change(self, system, power):
        if power is True:
            print(f"{system} is currently online and doesn't need repairing")
        else:
            self.power = True
            print(f"{system} is coming online")

    def repair(self, fixed):
        if self.fixed is True:
            print("System is currently in working order")
        else:
            self.power = True
            self.fixed = True


NAV = SubSystem("Navigation", False, False)
POWER = SubSystem("Power", False, False)
LIGHTSPEED = SubSystem("Light Speed Drive", False, False)
LIFESUP = SubSystem("Life Support", False, False)


class Item(object):
    """
    Class for defining the Tools atributes (Slot number, Name, Durability)
    """
    def __init__(self, slot, name, durability):
        self.slot = slot
        self.name = name
        self.durability = durability


class Inventory(object):
    """
    Stores the Tools in 6 slots.
    This also has functions to add items to the inventory,
    print an inventory list
    """
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.slot] = item

    def __str__(self):
        out = '\t'.join(['slot', 'Name', 'Dur'])
        for item in self.items.values():
            out += '\n' + '\t'.join([str(x) for x in
                                    [item.slot, item.name, item.durability]])
        return out

    def tool_status(self, tool):
        for item in self.items.values():
            if item.slot == tool:
                return item.name, item.durability
            else:
                continue
            raise StopIteration

    def __iter__(self):
        return self

    def __next__(self):
        for item in self.items.values():
            if item.name == "empty":
                return item.name, item.slot
            else:
                continue
            raise StopIteration
# Functions for Tool seletion and repair of subsystem


def tools():
    """
    Function that runs when the player enters a tool room.
    """
    clear()
    print("You look around and find a box that looks hopefull")
    room_tool = random.choice(aval_tools)
    room_dura = random.randint(1, 100)
    print(f"You have found {room_tool} with the durability of {room_dura}.")
    pickup = prompt("Would you like to pick up this item? (yes or no)\n",
                    validator=decisionValidator())
    if pickup == "yes":
        for x in inventory:
            if x is not None:
                print(x[1])
                inventory.add_item(Item(x[1], room_tool, room_dura))
                break
            else:
                print("Your Inventory is full!")
                time.sleep(3)
                break
    else:
        print(f"You leave the {room_tool} where it is and exit the room")


def repair_system(system):
    """
    Function to run when repairing a subsystem.
    This calls on the subsystem class.
    """
    clear()
    if system == "Navigation":
        system = NAV
        message = "Navigation"
    elif system == "Power":
        system = POWER
        message = "Power"
    elif system == "Light Speed Drive":
        system = LIGHTSPEED
        message = "Light Speed Drive"
    elif system == "Life Support":
        system = LIFESUP
        message = "Life Support"
    print(f"You have found the {message} room.\nThe system is broken and is"
          " in need of repair")
    systemfixed = SubSystem.system_status(system)
    dura_required = random.randint(1, 100)
    while systemfixed is False:
        check_inv = prompt("Would you like to check your inventory before"
                           " attempting to fix the system?\n(yes or no)\n",
                           validator=decisionValidator())
        if check_inv == "yes":
            print(inventory)
            print("To repair the system you need to select an item from your"
                  " inventory")
            repair = prompt("Please choose an inventory slot to use\n",
                            validator=slotValidator())
            dura = inventory.tool_status(repair)
        else:
            break

        if dura[1] > dura_required:
            print(f"You have selected {dura[0]}"
                  f" with a durability of {dura[1]}.")
            print(f"The {message} system needs {dura_required} points to"
                  " complete the repair")
            confirm = prompt("Do you wish to continue using this tool?"
                             " (yes or no)\n",
                             validator=decisionValidator())
            if confirm == "yes":
                print(f"You use the {dura[0]} to repair the system")
                dura_remaining = dura[1] - dura_required
                inventory.add_item(Item(repair, dura[0], dura_remaining))
                SubSystem.repair(system, True)
                systemfixed = True
                time.sleep(2)
                print(f"The {message} System has now been fixed!")
        else:
            print(f"The {dura[0]} you have selected doesn't have"
                  " enough durability points.")
            confirm = prompt("Do you wish to continue using this tool?"
                             " (yes or no)\n",
                             validator=decisionValidator())
            if confirm == "yes":
                clear()
                dura_required = dura_required - dura[1]
                print(f"You use the {dura[0]} to repair the system")
                inventory.add_item(Item(repair, "empty", 0))
                time.sleep(2)
                print("You brake the tool but the system still has"
                      f" {dura_required} points remaining")
# Game functions


def start_game():
    """
    looks for input from player to begin the adventure and calls
    the validator for play
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


def stage_one(PREV_POSITION):
    """
    First Steps scenario
    """
    clear()
    print("You have woken from stasis. However, something doesn't seem right.")
    print("After gathering your senses you stumble out the room to find\n"
          " lights flickering everywhere and nobody in sight.\n")
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
    subsystem = "Power"
    if direction == "left":
        repair_system(subsystem)
        stage_two(PREV_POSITION)
    elif direction == "forward":
        tools()
        stage_two(PREV_POSITION)
    elif direction == "backwards":
        stage_one(PREV_POSITION)


def stage_three(PREV_POSITION):
    """
    Stage Three Scenario
    """
    clear()
    print("You travel down a corridoor.")
    print("you get to the end of the coridoor and find 3 coridoors"
          " with doors at the end.")
    ways = ["left", "forward", "right", "backwards"]
    direction = directions(ways)
    PREV_POSITION = "stage_three"
    subsystem = "Navigation"
    if direction == "left":
        repair_system(subsystem)
        stage_three(PREV_POSITION)
    elif direction == "forward":
        tools()
        stage_three(PREV_POSITION)
    elif direction == "right":
        print("Locked Airlock")
        stage_three(PREV_POSITION)
    elif direction == "backwards":
        stage_one(PREV_POSITION)


def stage_four(PREV_POSITION):
    """
    Stage four Scenario
    """
    clear()
    print("You travel down a corridoor.")
    print("you get to the end of the coridoor and find 2 coridoors"
          " with doors at the end.")
    ways = ["left", "right", "backwards"]
    direction = directions(ways)
    PREV_POSITION = "stage_four"
    subsystem = "Life Support"
    if direction == "left":
        repair_system(subsystem)
        stage_four(PREV_POSITION)
    elif direction == "right":
        stage_five(PREV_POSITION)
    elif direction == "backwards":
        stage_one(PREV_POSITION)


def stage_five(PREV_POSITION):
    """
    Stage five Scenario
    """
    clear()
    print("You travel down a corridoor.")
    print("you get to the end of the coridoor and find 4 coridoors"
          " with doors at the end.")
    ways = ["left", "forward", "right", "backwards"]
    direction = directions(ways)
    PREV_POSITION = "stage_five"
    subsystem = "Light Speed Drive"
    if direction == "left":
        tools()
        stage_five(PREV_POSITION)
    elif direction == "forward":
        stage_six(PREV_POSITION)
    elif direction == "right":
        repair_system(subsystem)
        stage_five(PREV_POSITION)
    elif direction == "backwards":
        stage_four(PREV_POSITION)


def stage_six(PREV_POSITION):
    """
    Stage six Scenario
    """
    clear()
    print("You travel down a corridoor.")
    print("you get to the end of the coridoor and find 1 short coridoor"
          " with a door at the end")
    print("There is also a door to what looks to be an elevator.")
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
        tools()
        stage_six(PREV_POSITION)
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
inventory = Inventory()
inventory.add_item(Item("SLOT1", "empty", 0))
inventory.add_item(Item("SLOT2", "empty", 0))
inventory.add_item(Item("SLOT3", "empty", 0))
inventory.add_item(Item("SLOT4", "empty", 0))
inventory.add_item(Item("SLOT5", "empty", 0))
inventory.add_item(Item("SLOT6", "empty", 0))
start_game()
