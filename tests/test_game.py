
import config as c
import game as g
import hand as h
import player as p
import strategy as s

from collections import namedtuple

def test_find_game_winner_basic():
    p1 = p.Player("mozart", s.build_selector("next_card"))
    p2 = p.Player("beethoven", s.build_selector("next_card"))
    p3 = p.Player("chopin", s.build_selector("next_card"))
    p1.player_stats = p.build_player_stats(30, 0, 0)
    p2.player_stats = p.build_player_stats(20, 1, 0)
    p3.player_stats = p.build_player_stats(10, 0, 0)
    players = [p1, p2, p3]

    num_players = len(players)
    num_cards = 12
    config = c.build_config(num_players, num_cards, 0, False)

    # test
    winner = g.find_game_winner(players)

    assert winner.name == "mozart"

def test_play_with_table_basic():
    p1 = p.Player("mozart", s.build_selector("next_card"), h.Hand([1,6,7]))
    p2 = p.Player("beethoven", s.build_selector("next_card"), h.Hand([2,5,9]))
    p3 = p.Player("chopin", s.build_selector("next_card"), h.Hand([3,4,8]))
    players = [p1, p2, p3]
    num_players = len(players)
    num_cards = 12
    config = c.build_config(num_players, num_cards, 0, False)

    kitty = h.Kitty(h.Hand([10,11,12]))
    Table = namedtuple('Table', 'kitty players')
    table = Table(kitty=kitty, players=players)

    # test
    g.play_game_with_table(table, players, config)

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
