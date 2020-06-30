
"""
The player module contains players, bids, player stats.
"""

from hand import Hand
from hand import HandOwner
from collections import namedtuple

class Player(HandOwner):
    def __init__(self, name, selector, hand=Hand()):
        HandOwner.__init__(self, name, hand)
        self.selector = selector
        self.player_stats = new_player_stats()

    def play_card(self, prize_card, hand, max_card):
        return self.selector(prize_card, hand, max_card)

    def wins_round(self, bid):
        self.hand.select(bid.offer)
        self.player_stats = win_round_player_stats(self.player_stats, bid.prize_card)

    def loses_round(self, bid):
        self.hand.select(bid.offer)

    def wins_game(self):
        self.player_stats = win_game_player_stats(self.player_stats)

    def new_game(self):
        self.player_stats = new_game_player_stats(self.player_stats)

    def __str__(self):
        total = self.player_stats.total
        num_games_won = self.player_stats.num_games_won
        num_rounds_won = self.player_stats.num_rounds_won
        result = HandOwner.__str__(self) + " total: " + str(total) + " num_rounds: " + str(num_rounds_won) + " num_games: " + str(num_games_won)
        return result

# player_stats is named tuple:

def build_player_stats(total, num_games_won, num_rounds_won):
    PlayerStats = namedtuple("PlayerStats", "total num_games_won num_rounds_won")
    player_stats = PlayerStats(total=total, num_games_won=num_games_won, num_rounds_won=num_rounds_won)
    return player_stats

def new_player_stats():
    return build_player_stats(0, 0, 0)

def win_round_player_stats(player_stats, prize_card):
    new_total = player_stats.total + prize_card
    num_games_won = player_stats.num_games_won
    new_num_rounds_won = player_stats.num_rounds_won + 1
    return build_player_stats(new_total, num_games_won, new_num_rounds_won)

def win_game_player_stats(player_stats):
    new_total = player_stats.total
    num_games_won = player_stats.num_games_won + 1
    new_num_rounds_won = player_stats.num_rounds_won
    return build_player_stats(new_total, num_games_won, new_num_rounds_won)

def new_game_player_stats(player_stats):
    new_total = 0
    num_games_won = player_stats.num_games_won
    new_num_rounds_won = 0
    return build_player_stats(new_total, num_games_won, new_num_rounds_won)

# bid is a namedtuple

def build_bid(prize_card, offer, bidder):
    Bid = namedtuple("Bid", "prize_card offer bidder")
    bid = Bid(prize_card=prize_card, offer=offer, bidder=bidder)
    return bid
