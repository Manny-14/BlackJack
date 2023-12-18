# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

#User turn
user_hand = draw_starting_hand('your')
if user_hand != 21:
    response = 'y'
while user_hand < 21 and response != 'n':
    response = input('You have {}. Hit (y/n)? '.format(user_hand))
    if response != 'y' and response != 'n':
        print('Sorry, I didn\'t get that.')
    elif response == 'y':
        user_hand = user_hand + draw_card()

print_end_turn_status(user_hand)

#Dealer turn 
dealer_hand = draw_starting_hand('DEALER')
while dealer_hand < 17:
    print("Dealer has {}.".format(dealer_hand))
    dealer_hand = dealer_hand + draw_card()

print_end_turn_status(dealer_hand)
print_end_game_status(user_hand, dealer_hand)
    
