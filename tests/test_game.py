
from bid import build_bid
from config import Config
from dealer import Dealer
from game import Game
from hand import Kitty, Hand
from player import Player, build_player_stats
from round import Round
from strategy import NextCard

from collections import namedtuple

def test_find_game_winner_basic():
    p1 = Player("mozart", NextCard())
    p2 = Player("beethoven", NextCard())
    p3 = Player("chopin", NextCard())
    p1.player_stats = build_player_stats(30, 0, 0)
    p2.player_stats = build_player_stats(20, 1, 0)
    p3.player_stats = build_player_stats(10, 0, 0)
    players = [p1, p2, p3]

    num_players = len(players)
    num_cards = 12
    config = Config(num_players, num_cards, 0, False)

    # test
    winner = Game().find_game_winner(players)

    assert winner.name == "mozart"

def test_play_with_table_basic():
    p1 = Player("mozart", NextCard(), Hand([1,6,7]))
    p2 = Player("beethoven", NextCard(), Hand([2,5,9]))
    p3 = Player("chopin", NextCard(), Hand([3,4,8]))
    players = [p1, p2, p3]
    num_players = len(players)
    num_cards = 12
    config = Config(num_players, num_cards, 0, False)

    kitty = Kitty(Hand([10,11,12]))
    Table = namedtuple('Table', 'kitty players')
    table = Table(kitty=kitty, players=players)

    # test
    Game().play_with_table(table, players, config)

    assert len(players) == 3
    assert p1.player_stats.total == 11
    assert p2.player_stats.total == 12
    assert p3.player_stats.total == 10
    assert p1.player_stats.num_rounds_won == 1
    assert p2.player_stats.num_rounds_won == 1
    assert p3.player_stats.num_rounds_won == 1
    assert p1.player_stats.num_games_won == 0
    assert p2.player_stats.num_games_won == 1
    assert p3.player_stats.num_games_won == 0
