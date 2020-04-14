import random
import os
import sys


# TODO: Create functions for staying, hitting, busting, winning, showing hands
# TODO: Create the logic for the dealers hand on having the dealer decide by himself if he wants to hit or stay and have them
# TODO: defined as functions.


cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
# deck = cards

player_hand = []
dealer_hand = []


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


def shuffle_deck():
    random.shuffle(cards)


def starting_hands():
    shuffle_deck()
    player_hand.append(cards.pop())
    dealer_hand.append(cards.pop())
    player_hand.append(cards.pop())
    dealer_hand.append(cards.pop())
    print('Player Hand: ', '-'.join(player_hand),
          " Value: ", value(player_hand))
    print('Dealer Hand: ', '-'.join(dealer_hand),
          " Value: ", value(dealer_hand))


def player_turn():
    while value(player_hand) < 21:
        action = input("Would you like to (H)it or (S)tand?")
        if action == 'H':
            player_hand.append(cards.pop())
            print("Your hand is now: ", '-'.join(player_hand),
                  " Value: ", value(player_hand))
        elif action == 'S':
            break


def dealer_turn():
    pass


def player_bust():
    while value(player_hand) > 21:
        print("Sorry but you have busted and lost, try again next time!")
        continue


def dealer_bust():
    pass


# starting_hands()
first_time = True

while True:
    print("Welcome to the game of Blackjack! If you wish you can play a game against the dealer")
    print("Would you like to play? (y)es or (n)o")

    choice = input()

    if choice == 'y' and first_time is True:
        first_time = False
        starting_hands()
        print(first_time)
        player_turn()

    elif first_time is False:
        break

    elif choice == 'n':
        print("See you next time!")
        sys.exit()
