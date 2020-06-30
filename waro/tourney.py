
import game

def play_tourney(config):
    """ A tourney is a plurality of games. """
    for i in range(0, config.num_games):
        game.play_game(config)

    for player in config.players:
        player.new_game()  # clear last game stats

    winner = find_tourney_winner(config.players)
    display_tourney_info(winner, config.players, config.is_verbose)

def display_tourney_info(winner, players, is_verbose):
    """ Display info about the tourney results. """
    print("TRACER TOURNEY WINNER: " + str(winner))

    if is_verbose:
        for player in players:
            player.new_game()  # clear previous game stats
            print("TRACER TOURNEY " + str(player))

def find_tourney_winner(players):
    """ Tourney winner is the player who has won the most games. """
    return max(players, key=lambda p: p.player_stats.num_games_won)
