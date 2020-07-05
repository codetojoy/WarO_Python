
from config import build_config
from dealer import Dealer
from hand import Kitty
from player import Player
from strategy import build_selector

def test_make_shuffled_deck_length():
    num_cards = 20
    config = build_config(0, num_cards, 0, False)

    # test
    deck = Dealer(config)._make_shuffled_deck()

    assert len(deck) == 20

def test_make_shuffled_deck_shuffled():
    num_cards = 20
    config = build_config(0, num_cards, 0, False)

    # test
    deck = Dealer(config)._make_shuffled_deck()

    count = sum(deck)
    assert count == (num_cards * (num_cards + 1)) / 2

def test_partition_basic():
    num_players = 3
    num_cards = 12
    config = build_config(num_players, num_cards, 0, False)
    deck = list(range(1, num_cards + 1))

    # test
    result = Dealer(config)._partition(deck, config.num_cards_per_hand)

    assert len(result) == 4
    for hand in result:
        assert len(hand) == 3

def test_deal_basic():
    p1 = Player("mozart", build_selector("next_card"))
    p2 = Player("beethoven", build_selector("next_card"))
    p3 = Player("chopin", build_selector("next_card"))
    players = [p1, p2, p3]
    num_players = len(players)
    num_cards = 12
    config = build_config(num_players, num_cards, 0, False)

    # test
    result = Dealer(config).deal(players)

    kitty = result.kitty
    players = result.players
    assert len(kitty.hand.cards) == 3
    for player in players:
        assert len(player.hand.cards) == 3
