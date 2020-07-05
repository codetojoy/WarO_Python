
"""
This module is concerned with dealing cards to players (and the kitty).
"""

from collections import namedtuple
from random import shuffle

from hand import Hand
from hand import Kitty

class Dealer:
    """ Dealer can deal out the deck to players (and the kitty). """
    def __init__(self, config):
        self.config = config

    def deal(self, players):
        """ Deal out cards to players (and kitty). """
        deck = self._make_shuffled_deck()
        hands = self._partition(deck, self.config.num_cards_per_hand)
        kitty = Kitty(Hand(hands[0]))
        for i in range(1, len(hands)):
            players[i-1].hand = Hand(hands[i])
        Table = namedtuple('Table', 'kitty players')
        table = Table(kitty=kitty, players=players)
        return table

    def _make_shuffled_deck(self):
        """ Build a deck of cards, 1 to N, and shuffle them. """
        deck = list(range(1, self.config.num_cards + 1))
        shuffle(deck)
        return deck

    def _partition(self, deck, hand_size):
        """ Partition a set of N cards into sets of size M. """
        return [deck[i:i+hand_size] for i in range(0, len(deck), hand_size)]
