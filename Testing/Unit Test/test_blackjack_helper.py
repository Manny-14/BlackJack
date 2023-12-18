from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_
  # WRITE YOUR TESTS BELOW.
  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
    self.assertEqual(get_print(print_card_name, 8), "Drew an 8\n")
    self.assertEqual(get_print(print_card_name, 10), "Drew a 10\n")
    self.assertEqual(get_print(print_card_name, 11), "Drew a Jack\n")
    self.assertEqual(get_print(print_card_name, 12), "Drew a Queen\n")
    self.assertEqual(get_print(print_card_name, 13), "Drew a King\n")
  
  def test_draw_card(self):
    self.assertEqual(mock_random([1], draw_card), 11)
    self.assertEqual(mock_random([11], draw_card), 10)
    self.assertEqual(mock_random([12], draw_card), 10)
    self.assertEqual(mock_random([13], draw_card), 10)
    self.assertEqual(mock_random([8], draw_card), 8)
    
  
  def test_print_header(self):
    self.assertEqual(get_print(print_header, "YOUR TURN"), "-----------\nYOUR TURN\n-----------\n")
    self.assertEqual(get_print(print_header, 78), "-----------\n78\n-----------\n")
    self.assertEqual(get_print(print_header, ""), "-----------\n\n-----------\n")
    self.assertEqual(get_print(print_header, "GAME RESULT"), "-----------\nGAME RESULT\n-----------\n")
  
  def test_draw_starting_hand(self):
    output = mock_random([3, 5], draw_starting_hand, "DEALER")
    self.assertEqual(output, 8)
    self.assertEqual(mock_random([1, 13], draw_starting_hand, "YOUR"), 21)
    self.assertEqual(mock_random([1, 10], draw_starting_hand, "YOUR"), 21)
    self.assertEqual(mock_random([1, 5], draw_starting_hand, "DEALER"), 16)
    self.assertEqual(mock_random([12, 13], draw_starting_hand, "YOUR"), 20)
    self.assertEqual(mock_random([5, 9], draw_starting_hand, "YOUR"), 14)

  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status, 17), "Final hand: 17.\n")
    self.assertEqual(get_print(print_end_turn_status, 21), "Final hand: 21.\nBLACKJACK!\n")
    self.assertEqual(get_print(print_end_turn_status, 23), "Final hand: 23.\nBUST.\n")
    self.assertEqual(get_print(print_end_turn_status, 20), "Final hand: 20.\n")
    self.assertEqual(get_print(print_end_turn_status, 15), "Final hand: 15.\n")
  
  def test_print_end_game_status(self):
    self.assertEqual(get_print(print_end_game_status, 17, 17), "-----------\nGAME RESULT\n-----------\nPush.\n")
    self.assertEqual(get_print(print_end_game_status, 21, 18), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 17, 19), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 15, 22), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 22, 22), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 20, 21), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 21, 21), "-----------\nGAME RESULT\n-----------\nPush.\n")

if __name__ == '__main__':
    unittest.main()
