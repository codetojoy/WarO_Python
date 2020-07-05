
import abc

class HandOwner(abc.ABC):
    """ Anything that 'owns' a set of cards (e.g. player, kitty). """
    def __init__(self, name, hand=None):
        self.name = name
        self.hand = hand

    def __str__(self):
        result = self.name
        if (self.hand is not None):
            result += str(self.hand)
        return result

class Hand:
    """ A "Hand" is a set of cards (integers). """
    def __init__(self, cards=[]):
        self.cards = cards

    def __str__(self):
        return f"cards: {self.cards}" if self.cards else ""

    def select(self, card):
        """ Selecting a card for a "play" (and removal from hand). """
        self.cards.remove(card)

class Kitty(HandOwner):
    """ The kitty is a set of cards and effectively a "hand". """
    def __init__(self, hand=None):
        HandOwner.__init__(self, "Kitty", hand)
