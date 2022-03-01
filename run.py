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
    first = input("You have 3 choices, Left, Forward or Right....\n"
                  "Please choose a direction")
    if first == "left":
        function()
    elif first == "forward":
        function()
    elif first == "right":
        function()


def main():
    start_game()


main()