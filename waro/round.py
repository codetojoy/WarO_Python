
from bid import build_bid

class Round:
    def play_round(self, prize_card, players, config):
        bids = self.get_bids(prize_card, players, config)

        winning_bid = self.find_winning_bid(bids)
        for bid in bids:
            player = bid.bidder
            if (player.name == winning_bid.bidder.name):
                player.wins_round(bid)
            else:
                player.loses_round(bid)

        self.display_info(players, winning_bid.bidder.name, prize_card, bids, config)

    def display_info(self, players, winner_name, prize_card, bids, config):
        print("TRACER ROUND p: " + winner_name + " wins " + str(prize_card))

        if (config.is_verbose):
            for player in players:
                bid = next(filter(lambda b: b.bidder.name == player.name, bids))
                print("TRACER ROUND bid: " + str(bid.offer) + " " + str(player))
        print("")

    def get_bids(self, prize_card, players, config):
        bids = [self.get_bid(prize_card, p, config) for p in players]
        return bids

    def get_bid(self, prize_card, player, config):
        offer = player.strategy.select_card(prize_card, player.hand, config.max_card)
        bid = build_bid(prize_card, offer, player)
        return bid

    def find_winning_bid(self, bids):
        result = max(bids, key=lambda bid: bid.offer)
        return result
