
import sys

def hybrid(prize_card, hand, max_card):
    selector = None
    if (prize_card > (max_card // 2)):
        selector = build_selector("max_card")
    else:
        selector = build_selector("min_card")
    return selector(prize_card, hand, max_card)

def max_card(prize_card, hand, max_card):
    return max(hand.cards)

def min_card(prize_card, hand, max_card):
    return min(hand.cards)

def nearest_card(prize_card, hand, max_card):
    return min(hand.cards, key= lambda card: abs(prize_card - card))

def next_card(prize_card, hand, max_card):
    return hand.cards[0]

def console(prize_card, hand, max_card):
    result = None
    done = False

    while (not done):
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
    result = None
    try:
        result = int(value)
    except:
        pass

    return result

def build_selector(strategy_str):
    current_module = sys.modules[__name__]
    return getattr(current_module, strategy_str)
