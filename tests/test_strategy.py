
from hand import Hand
from strategy import *

def test_hybrid_card_high():
    prize_card = 16 
    hand = Hand([15,2,18,6])
    max_card = 20

    # test
    result = HybridCard().select_card(prize_card, hand, max_card)

    assert result == 18

def test_hybrid_card_low():
    prize_card = 8
    hand = Hand([15,2,18,6])
    max_card = 20

    # test
    result = HybridCard().select_card(prize_card, hand, max_card)

    assert result == 2

def test_max_card_basic():
    prize_card = 10
    hand = Hand([1,3,4,2])
    max_card = 20

    # test
    result = MaxCard().select_card(prize_card, hand, max_card)

    assert result == 4

def test_nearest_card_basic():
    prize_card = 10
    hand = Hand([1,11,14,5])
    max_card = 20

    # test
    result = NearestCard().select_card(prize_card, hand, max_card)

    assert result == 11

def test_min_card_basic():
    prize_card = 10
    hand = Hand([1,3,4,2])
    max_card = 20

    # test
    result = MinCard().select_card(prize_card, hand, max_card)

    assert result == 1

def test_next_card_basic():
    prize_card = 10
    hand = Hand([1,3,4,2])
    max_card = 20

    # test
    result = NextCard().select_card(prize_card, hand, max_card)

    assert result == 1
