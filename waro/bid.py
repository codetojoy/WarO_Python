
from collections import namedtuple

def build_bid(prize_card, offer, bidder):
    Bid = namedtuple("Bid", "prize_card offer bidder")
    bid = Bid(prize_card=prize_card, offer=offer, bidder=bidder)
    return bid
