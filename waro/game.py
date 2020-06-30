
import dealer as d
import round as r

def play_game(config):
    """
    Play a full game, with players etc set in configuration
    """
    table = d.Dealer(config).deal(config.players)
    kitty = table.kitty
    players = table.players
    play_game_with_table(table, players, config)

def play_game_with_table(table, players, config):
    """
    Play a full game
    """
    kitty = table.kitty
    players = table.players

    for player in players:
        player.new_game()

    if config.is_verbose:
        print("TRACER: game kitty: " + str(kitty))
        for player in players:
            print("TRACER: game player: " + str(player))

    play_rounds(kitty, players, config)
    winner = find_game_winner(players)
    winner.wins_game()
    display_game_info(winner, players, config)

def display_game_info(winner, players, config):
    """
    Print game info to the console.
    """
    print("TRACER GAME WINNER: " + str(winner))

    if (config.is_verbose):
        for player in players:
            print("TRACER GAME " + str(player))
    print("")

def play_rounds(kitty, players, config):
    """
    A game is plurality of rounds.
    """
    for prize_card in kitty.hand.cards:
        round = r.Round()
        round.play_round(prize_card, players, config)

def find_game_winner(players):
    """
    The winner of the game is the player with the highest total.
    """
    return max(players, key=lambda p: p.player_stats.total)
