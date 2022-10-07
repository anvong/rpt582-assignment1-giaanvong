"""Unit test for Rock Paper Scissor game."""
import unittest
from RockPaperScissorGame import RockPaperScissor


class MyTestCase(unittest.TestCase):
    """Unit test case class."""

    def test_find_winner_choice_player_win(self):
        """Do test player is the winner."""
        game_object = RockPaperScissor()
        # winner is player
        winner = "player"
        # player paper win
        player, computer = "paper", "rock"
        self.assertEqual(
            winner, game_object.find_winner_choice(player, computer))
        # player rock win
        player, computer = "rock", "scissor"
        self.assertEqual(
            winner, game_object.find_winner_choice(player, computer))
        # player scissor win -
        player, computer = "scissor", "paper"
        self.assertEqual(
            winner, game_object.find_winner_choice(player, computer))

    def test_find_winner_choice_computer_win(self):
        """Do test computer is the winner."""
        # start game class
        game_object = RockPaperScissor()
        # define winner
        winner = "computer"
        # computer is winner with paper
        computer, player = "paper", "rock"
        self.assertEqual(
            winner, game_object.find_winner_choice(player, computer))
        # computer is winner with rock
        computer, player = "rock", "scissor"
        self.assertEqual(
            winner, game_object.find_winner_choice(player, computer))
        # computer is winner with scissor
        computer, player = "scissor", "paper"
        self.assertEqual(
            winner, game_object.find_winner_choice(player, computer))

    def test_find_winner_choice_draw_result(self):
        """Do test function find winner choice draw result."""
        # start game class
        game_object = RockPaperScissor()
        winner = "draw"
        player, computer = "rock", "rock"
        self.assertEqual(
            winner, game_object.find_winner_choice(player, computer))
        player, computer = "scissor", "scissor"
        self.assertEqual(
            winner, game_object.find_winner_choice(player, computer))
        player, computer = "paper", "paper"
        self.assertEqual(
            winner, game_object.find_winner_choice(player, computer))

    def test_find_winner_choice_invalid_input(self):
        """Do test invalid input for find winner choice."""
        # start game class
        game_object = RockPaperScissor()
        # assert the error
        self.assertRaises(
            ValueError, game_object.find_winner_choice, "Nothing", "rock")
        self.assertRaises(ValueError, game_object.find_winner_choice, 1, 2)
        self.assertRaises(
            ValueError, game_object.find_winner_choice, "scissor", " ")
        with self.assertRaises(ValueError):
            game_object.find_winner_choice("rock1", "rock2")

    def test_get_random_choice_ok(self):
        """Test random choice OK case."""
        # possible choices
        possible_choice = ["rock", "paper", "scissor", ]
        # start game class
        game_object = RockPaperScissor()
        # test randomize choice given by game class
        pc = game_object.get_random_choice()
        self.assertIn(pc, possible_choice)
        pc = game_object.get_random_choice()
        self.assertIn(pc, possible_choice)

    def test_get_choice_name(self):
        """Test the function returning correct choice from a key."""
        # possible_choice = ["rock", "paper", "scissor", ]
        # start game class
        game_object = RockPaperScissor()
        # get rock with key 1
        self.assertEqual(
            "rock", game_object.get_choice_name("1"))
        # get paper with key 2
        self.assertEqual(
            "paper", game_object.get_choice_name("2"))
        # get scissor with key 3
        self.assertEqual(
            "scissor", game_object.get_choice_name("3"))

    def test_get_choice_name_invalid_key(self):
        """Test the error will be raise by input invalid ley."""
        # possible_choice = ["rock", "paper", "scissor", ]
        # start game class
        game_object = RockPaperScissor()
        # choice key with invalid input will raise error
        self.assertRaises(ValueError, game_object.get_choice_name, 0)
        self.assertRaises(ValueError, game_object.get_choice_name, "Something")
        self.assertRaises(ValueError, game_object.get_choice_name, None)
        self.assertRaises(ValueError, game_object.get_choice_name, " ")
        self.assertRaises(ValueError, game_object.get_choice_name, "0")
        self.assertRaises(ValueError, game_object.get_choice_name, "99")

    def test_set_round_score(self):
        """Test the function set the round score."""
        # start game class
        game_object = RockPaperScissor()
        # test set score by winner with
        self.assertTrue(game_object.set_round_score("player"))
        self.assertTrue(game_object.set_round_score("draw"))
        self.assertTrue(game_object.set_round_score("computer"))

    def test_set_round_score_raise_error(self):
        """Test the function set_round_score raise Error."""
        # start game class
        game_object = RockPaperScissor()
        # test set score by winner invalid string
        self.assertRaises(ValueError, game_object.set_round_score, "Stranger")
        self.assertRaises(ValueError, game_object.set_round_score, "player ")
        self.assertRaises(
            ValueError, game_object.set_round_score, " computer ")
        self.assertRaises(ValueError, game_object.set_round_score, " draw ")
        self.assertRaises(ValueError, game_object.set_round_score, " ")
        # try with None value
        self.assertRaises(ValueError, game_object.set_round_score, None)
        # try with number value
        self.assertRaises(ValueError, game_object.set_round_score, 1)
        # try with boolean
        self.assertRaises(ValueError, game_object.set_round_score, True)
        self.assertRaises(ValueError, game_object.set_round_score, False)

    def test_get_game_winner(self):
        """Test get game winner."""
        # start game class
        game_object = RockPaperScissor()
        # Test case 1: player win
        game_object.set_round_score("player")
        game_object.next_round()
        game_object.set_round_score("player")
        game_object.next_round()
        game_object.set_round_score("player")
        game_object.next_round()
        game_object.set_round_score("player")
        game_object.next_round()
        game_object.set_round_score("computer")
        game_object.next_round()
        game_object.set_round_score("player")
        # assert the
        self.assertEqual(
            "player", game_object.get_game_winner())

        # Test case 2: computer win
        game_object.reset()
        game_object.set_round_score("player")
        game_object.next_round()
        game_object.set_round_score("draw")
        game_object.next_round()
        game_object.set_round_score("draw")
        game_object.next_round()
        game_object.set_round_score("computer")
        game_object.next_round()
        game_object.set_round_score("computer")
        game_object.next_round()
        game_object.set_round_score("draw")
        game_object.next_round()
        game_object.set_round_score("draw")
        game_object.next_round()
        game_object.set_round_score("player")
        game_object.next_round()
        game_object.set_round_score("computer")
        game_object.next_round()
        game_object.set_round_score("computer")
        game_object.next_round()
        game_object.set_round_score("computer")
        # assert the
        self.assertEqual(
            "computer", game_object.get_game_winner())

    def test_print_round_result(self):
        """Test print match round result."""
        game_object = RockPaperScissor()

        # Test case 1 print player win message
        player, computer = "paper", "rock"
        winner = "player"
        game_object.set_round_score("player")
        self.assertTrue(game_object.print_round_result(
            player, computer, winner))
        game_object.next_round()

        player, computer = "scissor", "paper"
        winner = "player"
        game_object.set_round_score("player")
        self.assertTrue(game_object.print_round_result(
            player, computer, winner))
        game_object.next_round()

        player, computer = "rock", "scissor"
        winner = "player"
        game_object.set_round_score("player")
        self.assertTrue(game_object.print_round_result(
            player, computer, winner))
        game_object.next_round()

        # Test case 2 print draw message
        player, computer = "scissor", "scissor"
        winner = "draw"
        game_object.set_round_score("draw")
        self.assertTrue(game_object.print_round_result(
            player, computer, winner))
        game_object.next_round()

        player, computer = "rock", "rock"
        winner = "draw"
        game_object.set_round_score("draw")
        self.assertTrue(game_object.print_round_result(
            player, computer, winner))
        game_object.next_round()

        player, computer = "paper", "paper"
        winner = "draw"
        game_object.set_round_score("draw")
        self.assertTrue(game_object.print_round_result(
            player, computer, winner))
        game_object.next_round()

        # Test case 3 computer win message
        player, computer = "rock", "paper"
        winner = "computer"
        game_object.set_round_score("computer")
        self.assertTrue(game_object.print_round_result(
            player, computer, winner))

        player, computer = "scissor", "rock"
        winner = "computer"
        game_object.set_round_score("computer")
        self.assertTrue(game_object.print_round_result(
            player, computer, winner))

        player, computer = "paper", "scissor"
        winner = "computer"
        game_object.set_round_score("computer")
        self.assertTrue(game_object.print_round_result(
            player, computer, winner))


# main class for unit test
if __name__ == '__main__':
    unittest.main()
