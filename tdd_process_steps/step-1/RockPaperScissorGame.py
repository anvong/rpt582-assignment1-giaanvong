"""The mini game Rock Paper Scissor."""


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

    def get_random_choice(self):
        """Get a random choice."""

    def get_choice_name(self, enter_key):
        """Get choice name from an input key."""


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
