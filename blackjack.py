import random
import os
import sys


# TODO: Create functions for staying, hitting, busting, winning, showing hands
# TODO: Create the logic for the dealers hand on having the dealer decide by himself if he wants to hit or stay and have them
# TODO: defined as functions.


cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
# cards = cards


def value(hands):
    value = 0
    k = len(hands)
    for i in range(k):
        if hands[i] in "JQK":
            value += 10
        elif hands[i] not in "JQKA":
            value += int(hands[i])
        elif hands[i] == 'A':
            value += 1

    if value <= 11 and 'A' in hands:
        value += 10

    return value


def shuffle_cards():
    random.shuffle(cards)
    return cards


# def player_hit():
#     player_hand.append(cards.pop())
#     print('Player Hand: ', '-'.join(player_hand),
#           " Value: ", value(player_hand))


# def bust():
#     decision = input(
#         "Sorry but you busted and have lost the game. Would you like to play again? (y/n)")
#     if decision == 'y':
#         return False
#     else:
#         print("Have a great day and thanks for playing!")
#         sys.exit()


def play():
    while True:
        player_hand = []
        dealer_hand = []

        print(
            "WELCOME TO THE GAME OF BLACKJACK! TRY TO BEAT THE DEALER TO WIN HIS MONEY!")
        print("INSTRUCTIONS: GET THE CLOSEST TO 21 WITHOUT GOING OVER\n")
        print("Let's get started! Here are the starting hands!")
        shuffle_cards()
        player_hand.append(cards.pop())
        dealer_hand.append(cards.pop())
        player_hand.append(cards.pop())
        dealer_hand.append(cards.pop())
        print('Player Hand: ', '-'.join(player_hand),
              " Value: ", value(player_hand))
        print('Dealer Hand: ', '-'.join(dealer_hand),
              " Value: ", value(dealer_hand))

        print("\n It is now the players turn!\n")

        while value(player_hand) < 21:
            choice = input("Would you like to (h)it or (s)tand, player? ")

            if choice == 'h':
                player_hand.append(cards.pop())
                print("Your hand is now: ", "-".join(player_hand),
                      " Value: ", value(player_hand))

            else:
                print("The player is standing! Now it is the dealers turn1")
                break

        if value(player_hand) > 21:
            decision = input(
                "I'm sorry but you have busted, would you like to play again? (y/n)")

            if decision == 'y':
                continue

            else:
                print("Thank you for playing! I hope to see you again next time!")
                sys.exit()


play()
