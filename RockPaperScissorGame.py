"""The mini game Rock Paper Scissor."""
import random


def find_winner_choice(player, computer):
    """Do find the winner base on a defined rule."""
    possible_choice = ["rock", "paper", "scissor"]

    if player == computer and (player in possible_choice):
        return "draw"
    elif (player == "paper" and computer == "rock") \
            or (player == "rock" and computer == "scissor") \
            or (player == "scissor" and computer == "paper"):
        return "player"
    elif (computer == "paper" and player == "rock") \
            or (computer == "rock" and player == "scissor") \
            or (computer == "scissor" and player == "paper"):
        return "computer"
    else:
        raise ValueError


def new_game():
    """Do start a new game."""
    result = ""
    match_round = 1
    player_score = 0
    computer_score = 0
    player = "rock"
    computer = "paper"
    possible_choice = ["rock", "paper", "scissor"]
    exit_game = False

    # do loop until player or computer get score = 5
    while (player_score < 5 and computer_score < 5) and not exit_game:
        print("\nRound ", match_round, " begin:")
        # validate input loop #
        while True:
            # get user input by a number associated with a choice
            player_input = input(
                "Please make your choice: 1. rock, 2. paper, 3. scissor, 4. Exit game? ")  # noqa
            # make the loop to accept only particular values defined 1,2,3
            if (player_input == "1" or player_input == "2" or player_input == "3"):  # noqa
                break
            elif player_input == "4":
                # player enter 4 to exit the game
                exit_game = True
                break
            else:
                print("Invalid input. Please try again!")

        # if user not exit game, find the winner of the entire round
        if not exit_game:
            player = possible_choice[int(player_input)-1]
            computer = random.choice(possible_choice)
            # find the winner choice between player and computer
            result = find_winner_choice(player, computer)
            if (result == "player"):
                player_score += 1
                result = "you won"
            elif (result == "computer"):
                computer_score += 1
                result = "computer won"

            # print("Round ", match_round, "result: your choice:",
            #     player, ", computer's choice:", computer, "\nResult:",
            #     result, "\tPlayer Score:",
            #     player_score, "\tComputer Score:",
            #         computer_score)  # noqa
            print(
                "You chose [{player}] vs Computer [{computer}]"
                .format(player=player, computer=computer))
            print("Round {round} result: {result}.".format(
                round=match_round, result=result), end=" ")
            print("Player Score: {player_score}".format(
                player_score=player_score), end=" ")
            print("tComputer Score: {computer_score}".format(
                computer_score=computer_score))
            # increase match round for next loop
            match_round += 1

    if player_score == computer_score:
        print("Draw match and no winner!")
    elif player_score > computer_score:
        print("Congratulations! You won ;)")
    else:
        print("Game over! You lose :(")


if __name__ == '__main__':

    # Print multiline instruction
    # performstring concatenation of string
    print("Welcome to the rock paper scissor game, "
          "the Winning Rules are as follows: \n"
          "rock vs paper->paper wins \n"
          "rock vs scissor->rock wins \n"
          "paper vs scissor->scissor wins\n")

    # start first game
    new_game()
    # do loop to ask user to restart with a new game
    while True:
        response = input(
            "\nDo you want to play again? Enter Y to restart, other key to exit... ")  # noqa
        if response.lower() == "yes" or response.lower() == "y":  # noqa
            # start game again
            new_game()
        else:
            print("Thank you! See you soon.")
            break
