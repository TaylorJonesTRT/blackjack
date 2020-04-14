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
    return player_hand, dealer_hand


def player_turn():
    player_action = input("Would you like to (H)it or (S)tand?")
    if player_action == 'H' or 'h' or 'Hit' or 'hit' or 'HIT':
        player_hand.append(cards.pop())
        print("Your hand is now: ", '-'.join(player_hand),
              " Value: ", value(player_hand))

    elif player_action == 'S' or 's' or 'Sit' or 'sit' or 'SIT':
        print("Player is standing, it's now the Dealers turn!")


def dealer_turn():
    while value(dealer_hand) < 17:
        dealer_hand.append(cards.pop())
        print("The Dealers hand is now: ", "-".join(dealer_hand),
              " Value: ", value(dealer_hand))


def player_bust():
    print("Sorry but you have busted and lost, try again next time!")


def dealer_bust():
    pass


def player_win():
    pass


def dealer_win():
    pass


def main():
    wins = 0
    losses = 0
    ties = 0

    print("WELCOME TO THE GAME OF BLACKJACK")
    print("Instructions: Get as close to 21 as possible without going over")

    while True:
        print("Here are your starting hands")
        starting_hands()
        while value(player_hand) < 21:
            player_turn()
            if value(player_hand) > 21:
                player_bust()
                losses = losses + 1
                break
        else:
            print("Thank you for playing, have a great day!")
            break


main()
