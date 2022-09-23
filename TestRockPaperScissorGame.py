"""Unit test for Rock Paper Scissor game."""
import unittest
from RockPaperScissorGame import find_winner_choice


class MyTestCase(unittest.TestCase):
    """Unit test case class."""

    def test_find_winner_choice_player_win(self):
        """Do test player is the winner."""
        player, computer = "paper", "rock"
        winner = "player"
        self.assertEqual(winner, find_winner_choice(player, computer))
        player, computer = "rock", "scissor"
        self.assertEqual(winner, find_winner_choice(player, computer))
        player, computer = "scissor", "paper"
        self.assertEqual(winner, find_winner_choice(player, computer))

    def test_find_winner_choice_computer_win(self):
        """Do test computer is the winner."""
        computer, player = "paper", "rock"
        winner = "computer"
        self.assertEqual(winner, find_winner_choice(player, computer))
        computer, player = "rock", "scissor"
        self.assertEqual(winner, find_winner_choice(player, computer))
        computer, player = "scissor", "paper"
        self.assertEqual(winner, find_winner_choice(player, computer))

    def test_find_winner_choice_draw_result(self):
        """Do test function find winner choice draw result."""
        winner = "draw"
        player, computer = "rock", "rock"
        self.assertEqual(winner, find_winner_choice(player, computer))
        player, computer = "scissor", "scissor"
        self.assertEqual(winner, find_winner_choice(player, computer))
        player, computer = "paper", "paper"
        self.assertEqual(winner, find_winner_choice(player, computer))

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
