from prompt_toolkit import prompt


class Tool:
    """Main function"""
    def __init__(self, name):
        """Properties for tools"""
        self.name = name


class Systems:
    """Main System function"""
    def __init__(self, system, status):
        """
        Properties for the sub-systems
        """
        self.system = system
        self.status = status


def directions_four():
    """Four directions function"""
    print("You have 4 directions to go...")
    print("Please choose one of the following")
    print("left, forward, right, go-back")
    direction = input("Which way do you want to go??\n")

    return direction


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
            first_steps()


def play_check(value):
    """Checks to see if the player has enter play and it's valid"""
    try:
        if value != "play":
            raise ValueError(
                "Please type 'play' in all lowercase"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def first_steps():
    """First Steps scenario"""
    print("You have woken from stasis. However, something doesn't seem right.")
    print("After gathering your senses you stumble out the room to find lights"
          " flickering everywhere and nobody in sight.\n")
    directions_four()
    if direction == "left":
        print("left")
    elif direction == "forward":
        print("forward")
    elif direction == "right":
        print("right")
    elif direction == "go-back":
        print("go-back")


def main():
    start_game()


main()