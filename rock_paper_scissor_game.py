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
        self.player_score = 0
        self.computer_score = 0
        self.match_round = 1
        self.max_round = 5

    def find_winner_choice(self, player, computer):
        """Do find the winner base on a defined rule."""
        player = str(player).lower()
        computer = str(computer).lower()
        if player not in self.possible_choice:
            raise ValueError
        if computer not in self.possible_choice:
            raise ValueError

        if player == computer:
            return "draw"
        elif (player == "paper" and computer == "rock") \
                or (player == "rock" and computer == "scissor") \
                or (player == "scissor" and computer == "paper"):
            return "player"
        elif (computer == "paper" and player == "rock") \
                or (computer == "rock" and player == "scissor") \
                or (computer == "scissor" and player == "paper"):
            return "computer"

    def new_game(self, max_round=5):
        """Do start a new game."""
        # reset game info
        self.reset()
        # exit game flag
        exit_game = False

        # do loop until player or computer get score = 5
        while (not self.get_game_winner()) and not exit_game:
            # print("\nRound ", self.match_round, " begin:")
            print("\nRound {round} begin:".format(round=self.match_round))
            # validate input loop #
            while True:
                # get user input by a number associated with a choice
                player_input = input(
                    "Please make your choice: 1. ROCK, 2. PAPER, 3. SCISSOR, 0. Exit game? ")  # noqa
                # make the loop to accept only particular values defined 1,2,3
                if (player_input == "1" or player_input == "2" or player_input == "3"):  # noqa
                    break
                elif player_input == "0":
                    # player enter 4 to exit the game
                    exit_game = True
                    break
                else:
                    print("Invalid input. Please try again!")

            # if user not exit game, find the winner of the entire round
            if not exit_game:
                player = self.get_choice_name(player_input)
                # computer pick a random choice
                computer = self.get_random_choice()
                # judge for who is winner for this round by the choices
                round_winner = self.find_winner_choice(player, computer)
                # set score for the winner of current round
                self.set_round_score(round_winner)
                # print round result
                self.print_round_result(player, computer, round_winner)
                # call next round
                self.next_round()

        if exit_game:
            # print message when user quit the game
            print("THE MATCH IS WIDTHRAW!")
        else:
            # get the game winner
            final_winner = self.get_game_winner()
            if final_winner == "player":
                # message for player is winner
                print("CONGRATSTULATION!!! YOU WON THE GAME.")
            elif final_winner == "computer":
                # message for player is loser
                print("SORRY MATE!!! YOU LOSE.")

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

    def set_round_score(self, winner):
        """Set round result score function."""
        winner = str(winner).lower()
        if winner == "player":
            self.player_score += 1
        elif winner == "computer":
            self.computer_score += 1
        elif winner == "draw":
            pass  # no points for both
        else:
            raise ValueError
        return True

    def next_round(self):
        """Increase the match round."""
        self.match_round += 1

    def get_game_winner(self):
        """Get game result base on current score after max_round."""
        if self.match_round < self.max_round:
            return None
        if self.computer_score < self.winner_point \
           and self.player_score < self.winner_point:
            return None
        if self.player_score == self.computer_score:
            return "draw"
        elif self.player_score < self.computer_score:
            return "computer"
        elif self.player_score > self.computer_score:
            return "player"

    def print_round_result(self, player, computer, winner):
        """Do print round result."""
        if player not in self.possible_choice or \
                computer not in self.possible_choice:
            raise ValueError
        if winner not in ["draw", "player", "computer"]:
            raise ValueError

        # print user vs computer choice
        print("You chose [{player}] vs Computer [{computer}]. "
              .format(player=player.upper(),
                      computer=computer.upper()), end="")
        # print who is winner of this round
        if winner == "draw":
            print("Round {round} is draw. ".format(
                round=self.match_round), end="")
        else:
            print("Round {round} {winner} won. ".format(
                round=self.match_round, winner=winner), end="")

        print("Player Score: {player_score}".format(
            player_score=self.player_score), end=", ")
        print("Computer Score: {computer_score}".format(
            computer_score=self.computer_score))
        return True

    def reset(self):
        """Reset game data."""
        self.match_round = 1
        self.player_score = 0
        self.computer_score = 0


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
    game.new_game()
    # do loop to ask user to restart with a new game
    while True:
        response = input(
            "\nDo you want to play again? Enter Y to restart, other key to exit... ")  # noqa
        if response.lower() == "yes" or response.lower() == "y":  # noqa
            # start game again
            game.new_game()
        else:
            print("Thank you! See you soon.")
            break
