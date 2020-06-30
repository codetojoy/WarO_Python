
from hand import Hand
from player import Player, build_player_stats, build_bid
from strategy import NextCard

def test_wins_round_basic():
    p = Player("mozart", NextCard(), Hand([2,4,6]))
    prize_card =  10
    offer = 4
    bid = build_bid(prize_card, offer, p)

    # test
    p.wins_round(bid)

    assert p.hand.cards == [2,6]
    assert p.player_stats.total == 10
    assert p.player_stats.num_rounds_won == 1

def test_loses_round_basic():
    p = Player("mozart", NextCard(), Hand([2,4,6]))
    prize_card =  10
    offer = 4
    bid = build_bid(prize_card, offer, p)

    # test
    p.loses_round(bid)

    assert p.hand.cards == [2,6]

def test_wins_game_basic():
    p = Player("mozart", NextCard(), Hand([2,4,6]))
    p.player_stats = build_player_stats(1,1,1)

    # test
    p.wins_game()

    assert p.player_stats.num_games_won == 2
