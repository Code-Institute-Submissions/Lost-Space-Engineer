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
                  break



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
            print(f"Invalid data: {e}, please try again.\n")
            return False

      return True


def main():
      start_game()

main()