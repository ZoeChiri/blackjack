# -*- coding: utf-8 -*-

from .context import bh
from bh.util.data import Dealer
from bh.util.data import Card
from bh.util.data import Deck

from unittest import TestCase


class DealerTestSuite(TestCase):
    """Advanced test cases."""

    def test_deck(self):
        deck = Deck()
        cardDeck = deck.makeADeck()
        counter = 0
        for card in cardDeck:
            counter += 1
            print(card)
        self.assertEqual(52, counter)

    def test_deal(self):
        dealer = Dealer()
        print(dealer.dealCard())
        print(dealer.dealCard())

    def test_get_total(self):
        dealer = Dealer()
        card_set = []
        card_set.append(dealer.dealCard())
        card_set.append(dealer.dealCard())
        print(dealer.get_total(card_set))
