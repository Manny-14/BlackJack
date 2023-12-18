from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_eq_dealer_21(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand equal to 21.
        As a result, there is no winner
        '''
        output = run_test([11, 5, 6], ['y'], [1, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Jack\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 10\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_eq_21_user_above(self, input_mock, randint_mock):
        '''
        The dealer gets a blackjack, however, the player busts
        The dealer wins because the player busts
        '''
        output = run_test([2, 9, 1], ['y'], [7, 4, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 9\n" \
                   "You have 11. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 4\n" \
                   "Dealer has 11.\n" \
                   "Drew a King\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_eq_21_dealer_above(self, input_mock, randint_mock):
        '''
        The Player gets a blackjack while the dealer busts
        The player wins by getting a blackjack whilst the dealer busts
        '''
        output = run_test([12, 3, 8], ['y'], [7, 5, 11], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 3\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 5\n" \
                   "Dealer has 12.\n" \
                   "Drew a Jack\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_17_dealer_19(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand lower than 21.
        The dealer wins by having a higher hand than the user.
        '''
        output = run_test([4, 6, 7], ['y', 'n'], [4, 8, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 6\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew an 8\n" \
                   "Dealer has 12.\n" \
                   "Drew a 7\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_20_dealer_18(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The user wins by having a higher hand than the dealer.
        '''
        output = run_test([7, 4, 3, 6], ['y', 'y', 'n'], [1, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 4\n" \
                   "You have 11. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 7\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        However, the user and dealer get equal hand values and as a result, there is no winner
        '''
        output = run_test([1, 6,], ['n'], [5, 5, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 6\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 5\n" \
                   "Dealer has 10.\n" \
                   "Drew a 7\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)
   
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_19_dealer_21(self, input_mock, randint_mock):
        '''
        The dealer gets a blackjack but the user hand is less than 21
        The dealer wins by getting a blackjack.
        '''
        output = run_test([4, 9, 6], ['y', 'n'], [12, 4, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 9\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 4\n" \
                   "Dealer has 14.\n" \
                   "Drew a 7\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_21_dealer_18(self, input_mock, randint_mock):
        '''
        The User gets a blackjack while dealer gets below 21
        The User wins by having a blackjack.
        '''
        output = run_test([1, 13], [], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a King\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_22_dealer_23(self, input_mock, randint_mock):
        '''
        Both the dealer and user bust
        The dealer wins because the user also busts.
        '''
        output = run_test([11, 5, 7], ['y'], [4, 9, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Jack\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 9\n" \
                   "Dealer has 13.\n" \
                   "Drew a 10\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_20_dealer_23(self, input_mock, randint_mock):
        '''
        The dealer busts but the user stays under 21
        The player wins because the dealer busts and the player didn't.
        '''
        output = run_test([3, 12, 7], ['y', 'n'], [13, 3, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a Queen\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a 3\n" \
                   "Dealer has 13.\n" \
                   "Drew a 10\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_26_dealer_19(self, input_mock, randint_mock):
        '''
        The Player busts but the Dealer remains under 21
        The dealer wins because the player bust
        '''
        output = run_test([1, 4, 1], ['y'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 4\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "Final hand: 26.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_inputs_invalid_letter(self, input_mock, randint_mock):
        '''
        Both the dealer and the user gets a blackjack at the end of the game
        However, the user inputs an invalid letter during the course of the game
        Checking if the code still works as expected
        '''
        output = run_test([1, 2, 8], ['f', 'y'], [1, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 2\n" \
                   "You have 13. Hit (y/n)? f\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 10\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)  

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_repeated_invalid_chars(self, input_mock, randint_mock):
        '''
        Both the dealer and the user bust at the end of the game
        However, the user inputs an invalid letter or word repeatedly during the course of the game
        Checking if the code still works as expected
        '''
        output = run_test([3, 4, 6, 1], ['yes', 'y', 'g', 'no', 'yy', 'y'], [1, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 4\n" \
                   "You have 7. Hit (y/n)? yes\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 7. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 13. Hit (y/n)? g\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 13. Hit (y/n)? no\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 13. Hit (y/n)? yy\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)  
          
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_inputs_empty_string(self, input_mock, randint_mock):
        '''
        Both the dealer and the user bust at the end of the game
        However, the user accidentally presses the enter key and inputs an empty string during the game
        Checking if the code still works as expected
        '''
        output = run_test([1, 4, 8], ['', 'y'], [1, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 4\n" \
                   "You have 15. Hit (y/n)? \n" \
                   "Sorry I didn't get that.\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)  

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_inputs_invalid_letter(self, input_mock, randint_mock):
        '''
        Both the dealer and the user gets a blackjack at the end of the game
        However, it took the user a long time to get there
        Checking if the code still works as expected
        '''
        output = run_test([2, 3, 4, 2, 3, 4, 3], ['y', 'y', 'y', 'y', 'y'], [1, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 3\n" \
                   "You have 5. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "You have 9. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 11. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 10\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)  


    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()
