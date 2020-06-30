
import sys

def hybrid(prize_card, hand, max_card):
    """ Hybrid strategy pivots, based on the value of the prize. """
    selector = None
    if prize_card > (max_card // 2):
        selector = build_selector("max_card")
    else:
        selector = build_selector("min_card")
    return selector(prize_card, hand, max_card)

def max_card(prize_card, hand, max_card):
    """ Max-card strategy always picks the highest card in the hand. """
    return max(hand.cards)

def min_card(prize_card, hand, max_card):
    """ Min-card strategy always picks the lowest card in the hand. """
    return min(hand.cards)

def nearest_card(prize_card, hand, max_card):
    """ Nearest-card strategy picks the card closest to the prize card. """
    return min(hand.cards, key= lambda card: abs(prize_card - card))

def next_card(prize_card, hand, max_card):
    """ Next-card strategy just picks the next card in the hand (effectively random). """
    return hand.cards[0]

def console(prize_card, hand, max_card):
    """ Console strategy gets input from the user. """
    result = None
    done = False

    while not done:
        print("")
        print("prize: " + str(prize_card) + " hand: " + str(hand.cards))
        print("enter your pick:")
        answer = parse_input(input())
        if (answer in hand.cards):
            print("OK")
            done = True
            result = answer
        else:
            print("illegal pick ... try again")

    return result

def parse_input(value):
    """ Get intput from the user. No error-checking. """
    result = None
    try:
        result = int(value)
    except:
        pass

    return result

def build_selector(strategy_str):
    """
    Returns selector function based on the name provided.
    e.g. "max_card", "nearest_card", etc.
    """
    current_module = sys.modules[__name__]
    return getattr(current_module, strategy_str)
