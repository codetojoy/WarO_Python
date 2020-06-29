
from dealer import Dealer
from round import Round

class Game:
    def play(self, config):
        """
        Play a full game, with players etc set in configuration
        """
        table = Dealer(config).deal(config.players)
        kitty = table.kitty
        players = table.players
        self.play_with_table(table, players, config)

    def play_with_table(self, table, players, config):
        """
        Play a full game
        """
        kitty = table.kitty
        players = table.players

        for player in players:
            player.new_game()

        if (config.is_verbose):
            print("TRACER: game kitty: " + str(kitty))
            for player in players:
                print("TRACER: game player: " + str(player))

        self.play_rounds(kitty, players, config)
        winner = self.find_game_winner(players)
        winner.wins_game()
        self.display_info(winner, players, config)

    def display_info(self, winner, players, config):
        """
        Print game info to the console.
        """
        print("TRACER GAME WINNER: " + str(winner))

        if (config.is_verbose):
            for player in players:
                print("TRACER GAME " + str(player))
        print("")

    def play_rounds(self, kitty, players, config):
        """
        A game is plurality of rounds.
        """
        for prize_card in kitty.hand.cards:
            round = Round()
            round.play_round(prize_card, players, config)

    def find_game_winner(self, players):
        """
        The winner of the game is the player with the highest total.
        """
        return max(players, key=lambda p: p.player_stats.total)
