
import player as p

def play_round(prize_card, players, max_card, is_verbose):
    """ Play round for this prize-card from the kitty. """
    bids = get_bids(prize_card, players, max_card)

    winning_bid = find_winning_bid(bids)
    for bid in bids:
        player = bid.bidder
        if player.name == winning_bid.bidder.name:
            player.wins_round(bid)
        else:
            player.loses_round(bid)

    display_round_info(players, winning_bid.bidder.name, prize_card, bids, is_verbose)

def display_round_info(players, winner_name, prize_card, bids, is_verbose):
    """ Display info about this round. """
    print("TRACER ROUND p: " + winner_name + " wins " + str(prize_card))

    if is_verbose:
        for player in players:
            bid = next(filter(lambda b: b.bidder.name == player.name, bids))
            print("TRACER ROUND bid: " + str(bid.offer) + " " + str(player))
    print("")

def get_bids(prize_card, players, max_card):
    """ Collect bids from all the players, for this round. """
    bids = [get_bid(prize_card, p, max_card) for p in players]
    return bids

def get_bid(prize_card, player, max_card):
    """ Collect bid from the player, for this round. """
    offer = player.play_card(prize_card, player.hand, max_card)
    bid = p.build_bid(prize_card, offer, player)
    return bid

def find_winning_bid(bids):
    """ Winning bid is the highest offer. """
    result = max(bids, key=lambda bid: bid.offer)
    return result
