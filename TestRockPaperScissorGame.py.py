"""Unit test for Rock Paper Scissor game."""
import unittest
from RockPaperScissorGame import find_winner_choice


class MyTestCase(unittest.TestCase):
    """Unit test case class."""

    def test_find_winner_choice_player_win(self):
        """Do test player is the winner."""
        self.assertEqual("player", find_winner_choice("paper", "rock"))
        self.assertEqual("player", find_winner_choice("rock", "scissor"))
        self.assertEqual("player", find_winner_choice("scissor", "paper"))

    def test_find_winner_choice_computer_win(self):
        """Do test computer is the winner."""
        self.assertEqual("computer", find_winner_choice("rock", "paper"))
        self.assertEqual("computer", find_winner_choice("scissor", "rock"))
        self.assertEqual("computer", find_winner_choice("paper", "scissor"))

    def test_find_winner_choice_draw_result(self):
        """Do test function find winner choice draw result."""
        self.assertEqual("draw", find_winner_choice("rock", "rock"))
        self.assertEqual("draw", find_winner_choice("scissor", "scissor"))
        self.assertEqual("draw", find_winner_choice("paper", "paper"))

    def test_find_winner_choice_invalid_input(self):
        """Do test invalid input for find winner choice."""
        self.assertRaises(ValueError, find_winner_choice, "Nothing", "rock")
        self.assertRaises(ValueError, find_winner_choice, 1, 2)
        self.assertRaises(ValueError, find_winner_choice, "scissor", " ")
        with self.assertRaises(ValueError):
            find_winner_choice("rock1", "rock2")


# main class for unit test
if __name__ == '__main__':
    unittest.main()
