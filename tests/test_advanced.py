# -*- coding: utf-8 -*-


from .context import bh
from bh.util.data import Dealer
from bh.util.data import Card
from bh.util.data import Deck
from bh.util.data import Game
from bh.util.data import GamePlay

from unittest import TestCase

import io
import sys


class DealerTestSuite(TestCase):
    """Dealer  test cases."""

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


class GameTestSuite(TestCase):

    def test_hit_or_stand(self):
        captured_input = io.StringIO('stand')
        sys.stdin = captured_input
        game = Game()
        self.assertFalse(game.hit_or_stand())

        captured_input = io.StringIO('hit')
        sys.stdin = captured_input
        self.assertTrue(game.hit_or_stand())
