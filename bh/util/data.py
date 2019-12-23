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
        cardRanks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J",
                     "Q", "K"]
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


class Game:
    bank = 20
    dealer = None
    player_cards = []
    dealer_cards = []
    bet = 0

    def __init__(self):
        self.dealer = Dealer()

    def play(self):
        print('Bank = ' + str(self.bank))
        print('Play?  Enter \'no\' to quit, enter anything else to play')
        if input() == 'no':
            return False
        return True

    def place_bet(self):
        self.bet = self.dealer.get_valid_bet(self.bank)
        self.bank -= self.bet
        return self.bet

    def get_bank(self):
        return self.bank

    def deal_player(self):
        card = self.dealer.dealCard()
        self.player_cards.append(card)

    def deal_dealer(self):
        card = self.dealer.dealCard()
        self.dealer_cards.append(card)

    def hit_or_stand(self):
        choice = input('hit or stand?').lower()
        if choice == 'stand':
            return False
        return True

    def score_player(self):
        return self.dealer.get_total(self.player_cards)

    def score_dealer(self):
        return self.dealer.get_total(self.dealer_cards)

    def player_status(self):
        print("Score: ", self.score_player())
        for card in self.player_cards:
            print(card.rank, card.suit)

    def dealer_status(self):
        print("Score: ", self.score_dealer())
        for card in self.dealer_cards:
            print(card.rank, card.suit)

    def player_bet_win(self):
        self.bank += 2 * self.bet

    def remove_cards(self):
        self.player_cards = []
        self.dealer_cards = []


def GamePlay(game):
    if game.play():
        print("Valid bet:", game.place_bet())
        print("Bank: ", game.get_bank())
        game.deal_player()
        game.deal_player()
        game.player_status()
        while game.hit_or_stand():
            game.deal_player()
            game.player_status()
            if game.score_player() > 21:
                print("Lost")
                return
        # Dealer Play
        game.deal_dealer()
        game.deal_dealer()
        while game.score_dealer() <= 16:
            game.deal_dealer()
        if game.score_dealer() > 21:
            print("dealer lost")
            game.dealer_status()
            game.player_bet_win()
            return
        if game.score_dealer() >= game.score_player():
            print("dealer wins")
            game.dealer_status()
        return


if __name__ == "__main__":
    game = Game()
    while game.get_bank() > 0:
        GamePlay(game)
        game.remove_cards()
