
from config import Config
from dealer import Dealer
from hand import Kitty, Hand
from player import Player, build_bid
from round import Round
from strategy import build_selector

def test_get_bids_basic():
    players = [ Player("mozart", build_selector("next_card"), Hand([1,2,3])),
                Player("beethoven", build_selector("next_card"), Hand([4,5,6])),
                Player("chopin", build_selector("next_card"), Hand([7,8,9])) ]
    num_players = len(players)
    num_cards = 12
    config = Config(num_players, num_cards, 0, False)

    prize_card =  10

    # test
    bids = Round().get_bids(prize_card, players, config.max_card)

    assert len(bids) == 3
    assert bids[0].bidder.name == "mozart"
    assert bids[0].offer == 1
    assert bids[0].prize_card == prize_card

def test_find_winning_bid_basic():
    p1 = Player("mozart", build_selector("next_card"))
    p2 = Player("beethoven", build_selector("next_card"))
    p3 = Player("chopin", build_selector("next_card"))
    prize_card =  10
    b1 = build_bid(prize_card, 7, p1)
    b2 = build_bid(prize_card, 9, p2)
    b3 = build_bid(prize_card, 8, p3)
    bids = [b1, b2, b3]

    # test
    result = Round().find_winning_bid(bids)

    assert result.bidder.name == "beethoven"
