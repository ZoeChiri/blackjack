import random
import time

import random


class Card:
    def __init__(self, r, s):
        self.rank = r
        self.suit = s

    def __str__(self):
        return (self.rank + self.suit)


class Deck:
    def makeADeck(self):
        cardSuits = ["♣", "♦", "♥", "♠"]
        cardRanks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        deck = []
        for s in cardSuits:
            for r in cardRanks:
                tempCard = Card(r, s)
                deck.append(tempCard)

        random.shuffle(deck)
        return deck


class Dealer:
    cardDeck = None
    idx = -1

    values = {'K': 10, 'Q': 10, 'J': 10, '10': 10, '9': 9, '8': 8, '7': 7,
              '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'A': 1}

    def __init__(self):
        deck = Deck()
        self.cardDeck = deck.makeADeck()

    # dealing a card
    def dealCard(self):
        self.idx += 1
        card = self.cardDeck[self.idx]
        return card

    # get the total score, and change ace value
    def get_total(self, card_set):
        score = 0
        aces = 0
        for card in card_set:
            if card.rank == 'A':
                aces += 1
            score += self.values[card.rank]

        if aces > 0:
            if score + 10 <= 21:
                return score + 10
            else:
                return score

        return score

    def check_bet(self, bank, bet):
        if bet > bank:
            return False
        if bet < 0:
            return False
        return True

    # Get a valid bet
    def get_valid_bet(self, bank):
        bet = int(input('Place your bet '))
        while not self.check_bet(bank, bet):
            print('Invalid bet.  Bet again.')
            bet = int(input('Place your bet '))
        return bet


if __name__ == "__main__":
    print("here")
