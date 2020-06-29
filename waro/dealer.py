
"""
This module is concerned with deal cards to players.
"""

from collections import namedtuple
from random import shuffle

from hand import Hand
from hand import Kitty

class Dealer:
    def __init__(self, config):
        self.config = config

    def deal(self, players):
        """
        Deal out cards to players (and kitty)
        """
        deck = self.make_shuffled_deck()
        hands = self.partition(deck, self.config.num_cards_per_hand)
        kitty = Kitty(Hand(hands[0]))
        for i in range(1, len(hands)):
            players[i-1].hand = Hand(hands[i])
        Table = namedtuple('Table', 'kitty players')
        table = Table(kitty=kitty, players=players)
        return table

    def make_shuffled_deck(self):
        """
        Build a deck of cards, 1 to N, and shuffle them.
        """
        deck = list(range(1, self.config.num_cards + 1))
        shuffle(deck)
        return deck

    def partition(self, deck, num_cards_per_hand):
        """
        Partition a set of N cards into sets of size M.
        """
        return list(self.partition_generator(deck, num_cards_per_hand))

    def partition_generator(self, list, n):
        """
        Build a generator for partitioning.
        """
        for i in range(0, len(list), n):
            yield list[i:i + n]
