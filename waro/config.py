
import sys
import json
from player import Player
from strategy import build_strategy

class Config:
    def __init__(self, num_players, num_cards, num_games, is_verbose, players=[]):
        self.num_players = num_players
        self.num_cards = num_cards
        self.max_card = num_cards
        self.num_games = num_games
        self.is_verbose = is_verbose
        num_groups = num_players + 1  # include kitty
        self.num_cards_per_hand = num_cards // num_groups
        self.players = players

def build_config_from_json_file(json_file_path):
    try:
        json_file = open(json_file_path, "r")
        json_str = json_file.read()
        config = build_config_from_json(json_str)
        return config
    except:
        e = sys.exc_info()[0]
        print("illegal json: " + str(e))
        sys.exit(-1)

def build_config_from_json(json_str):
    try:
        json_dict = json.loads(json_str)

        num_cards = int(json_dict["num_cards"])
        num_games = int(json_dict["num_games"])
        is_verbose = bool(json_dict["is_verbose"])
        json_players = json_dict["players"]
        players = [ build_player(json_player) for json_player in json_players]
        num_players = len(players)

        return Config(num_players, num_cards, num_games, is_verbose, players)
    except:
        e = sys.exc_info()[0]
        print("illegal json: " + str(e))
        sys.exit(-1)

def build_player(json_player):
    name = json_player["name"]
    strategy = build_strategy(json_player["strategy"])
    return Player(name, strategy)
