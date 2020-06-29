
from hand import Hand

def test_select_basic():
    hand = Hand([4,3,2,1])

    # test
    hand.select(3)

    assert hand.cards == [4,2,1]
