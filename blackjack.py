import random
import sys


# TODO: Create functions for staying, hitting, busting, winning, showing hands, dealer decisions
# TODO: Add a betting function that lets the player keep playing until they run out of chips
# TODO: Maybe think of a better way to determine the value of an Ace card
# TODO: Add in a mechanism to count wins, losses, and ties.


# Determining the value of the cards in the deck.
# If you have an Ace in your hands it's value (1 or 11) will be automatically determined depnding on the value of your hand
# if the card was not there. So if your hand value is greater than 11 then an Ace will be a value of 1 otherwise it will be 11.
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


def play():
    while True:
        cards = ['2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        player_hand = []
        dealer_hand = []

        # Shuffle the deck of cards so that it's always random
        random.shuffle(cards)

        print(
            "WELCOME TO THE GAME OF BLACKJACK! TRY TO BEAT THE DEALER TO WIN HIS MONEY!")
        print("INSTRUCTIONS: GET THE CLOSEST TO 21 WITHOUT GOING OVER\n")
        print("Let's get started! Here are the starting hands!")
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
                print("The player is standing! Now it is the dealers turn!\n")
                break

        if value(player_hand) > 21:
            decision = input(
                "I'm sorry but you have busted, would you like to play again? (y/n)")

            if decision == 'y':
                continue

            else:
                print("Thank you for playing! I hope to see you again next time!")
                sys.exit()

        while value(dealer_hand) < 21:
            if value(dealer_hand) <= 17:
                print("The Dealer is wishing to hit! Here is his hand now!")
                dealer_hand.append(cards.pop())
                print('Dealer Hand: ', '-'.join(dealer_hand),
                      " Value: ", value(dealer_hand), "\n")

            elif value(dealer_hand) > 17:
                print(
                    "The Dealer is wishing to stand now! Here is his hand and value as it is!")
                print('Dealer Hand: ', '-'.join(dealer_hand),
                      " Value: ", value(dealer_hand), "\n")
                break

        if value(dealer_hand) > 21:
            decision2 = input(
                "The Dealer has busted and you have won! Would you like to play again? (y/n)")

            if decision2 == 'y':
                continue

            else:
                print("Thank you for playing! I hope to see you again next time!")
                sys.exit()

        while value(player_hand) <= 21 and value(dealer_hand) <= 21:
            if value(player_hand) > value(dealer_hand):
                print("You beat the dealer! Congrats")
                new_game = input("Would you like to play again? (y/n)")
                if new_game == 'y':
                    break
                else:
                    print("Thanks for playing! See you next time!")
                    sys.exit()

            elif value(player_hand) < value(dealer_hand):
                print("The dealer has beaten you :(. Better luck next time!")
                new_game2 = input("Would you like to play again? (y/n)")
                if new_game2 == 'y':
                    break
                else:
                    print("Thanks for playing! See you next time!")
                    sys.exit()

            elif value(player_hand) == value(dealer_hand):
                print("You have tied with the dealer!")
                new_game3 = input("Would you like to play again? (y/n)")
                if new_game3 == 'y':
                    break
                else:
                    print("Thanks for playing! See you next time!")
                    sys.exit()

        continue


play()
