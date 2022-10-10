"""Unit test for Rock Paper Scissor game."""
import unittest
from RockPaperScissorGame import RockPaperScissor


class MyTestCase(unittest.TestCase):
    """Unit test case class."""

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


# main class for unit test
if __name__ == '__main__':
    unittest.main()
