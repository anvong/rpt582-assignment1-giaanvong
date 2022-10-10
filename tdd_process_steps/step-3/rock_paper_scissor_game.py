"""The mini game Rock Paper Scissor."""
import random


class RockPaperScissor():
    """The game object of Rock Paper Scissor."""

    possible_choice = ["rock", "paper", "scissor"]
    player_score = 0
    computer_score = 0
    match_round = 1
    max_round = 5
    winner_point = 5

    def __init__(self):
        """Class constructer."""
        pass

    def get_random_choice(self):
        """Get a random choice."""
        return random.choice(self.possible_choice)

    def get_choice_name(self, enter_key):
        """Get choice name from an input key."""
        enter_key = str(enter_key)
        if (enter_key == "1" or enter_key == "2" or enter_key == "3"):
            return self.possible_choice[int(enter_key)-1]
        else:
            raise ValueError


if __name__ == '__main__':

    # Print multiline instruction
    # performstring concatenation of string
    print("Welcome to the rock paper scissor game, "
          "the Winning Rules are as follows: \n"
          "rock vs paper->paper wins \n"
          "rock vs scissor->rock wins \n"
          "paper vs scissor->scissor wins\n")

    # start first game
    game = RockPaperScissor()
