
from game import Game

def play_tourney(config):
    for i in range(0, config.num_games):
        Game().play(config)

    for player in config.players:
        player.new_game()  # clear previous game stats
        
    winner = find_tourney_winner(config.players)
    display_info(winner, config.players, config.is_verbose)

def display_info(winner, players, is_verbose):
    print("TRACER TOURNEY WINNER: " + str(winner))

    if (is_verbose):
        for player in players:
            player.new_game()  # clear previous game stats
            print("TRACER TOURNEY " + str(player))

def find_tourney_winner(players):
    return max(players, key=lambda p: p.player_stats.num_games_won)
