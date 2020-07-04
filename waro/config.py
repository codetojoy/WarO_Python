
"""
The config module is concerned with configuration of the game.
"""

import sys
import json
import collections

from player import Player
from strategy import build_selector

"""
A 'Config' captures info from the JSON file (num_cards, players) and
holds some derived, computed values as well.
"""
Config = collections.namedtuple("Config", "num_players num_cards max_card num_games is_verbose num_groups num_cards_per_hand players")

def build_config(num_players, num_cards, num_games, is_verbose, players=[]):
    """ Build a config "named tuple". """
    num_groups = num_players + 1  # include kitty
    num_cards_per_hand = num_cards // num_groups
    config = Config(num_players=num_players, num_cards=num_cards, max_card=num_cards,
                    is_verbose=is_verbose, num_groups=num_groups, num_games=num_games,
                    num_cards_per_hand=num_cards_per_hand, players=players)
    return config

def build_config_from_json_file(json_file_path):
    """
    Build a configuration from a JSON file.
    If we can't use the file, that is a non-recoverable error so we exit.
    """
    try:
        json_file = open(json_file_path, "r")
        json_str = json_file.read()
        config = build_config_from_json(json_str)
        return config
    except (PermissionError, FileNotFoundError) as e:
        e = sys.exc_info()[0]
        print("illegal json: " + str(e))
        sys.exit(-1)

def build_config_from_json(json_str):
    """
    Build a configuration from a JSON string.
    If we can't parse the string (e.g. if num_cards is not an integer), that 
    is a non-recoverable error and we exit.
    """
    try:
        json_dict = json.loads(json_str)

        num_cards = int(json_dict["num_cards"])
        num_games = int(json_dict["num_games"])
        is_verbose = bool(json_dict["is_verbose"])
        json_players = json_dict["players"]
        players = [ build_player(json_player) for json_player in json_players]
        num_players = len(players)

        return build_config(num_players, num_cards, num_games, is_verbose, players)
    except:
        e = sys.exc_info()[0]
        print("illegal json: " + str(e))
        sys.exit(-1)

def build_player(json_player):
    """
    Build a Player from a JSON fragment.
    e.g. {"name": "mozart", "strategy": "max_card"}
    """
    name = json_player["name"]
    strategy = build_selector(json_player["strategy"])
    return Player(name, strategy)
