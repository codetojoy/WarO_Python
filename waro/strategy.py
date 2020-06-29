
from abc import ABC

class Strategy(ABC):
    def select_card(self, prize_card, hand, max_card):
        pass

class HybridCard(Strategy):
    def select_card(self, prize_card, hand, max_card):
        result = None
        if (prize_card > (max_card // 2)):
            result = MaxCard().select_card(prize_card, hand, max_card)
        else:
            result = MinCard().select_card(prize_card, hand, max_card)
        return result

class MaxCard(Strategy):
    def select_card(self, prize_card, hand, max_card):
        return max(hand.cards)

class MinCard(Strategy):
    def select_card(self, prize_card, hand, max_card):
        return min(hand.cards)

class NearestCard(Strategy):
    def select_card(self, prize_card, hand, max_card):
        return min(hand.cards, key= lambda card: abs(prize_card - card))

class NextCard(Strategy):
    def select_card(self, prize_card, hand, max_card):
        return hand.cards[0]

class ConsoleCard(Strategy):
    def select_card(self, prize_card, hand, max_card):
        result = None
        done = False

        while (not done):
            print("")
            print("prize: " + str(prize_card) + " hand: " + str(hand.cards))
            print("enter your pick:")
            answer = self.parse_input(input())
            if (answer in hand.cards):
                print("OK")
                done = True
                result = answer
            else:
                print("illegal pick ... try again")

        return result

    def parse_input(self, value):
        result = None
        try:
            result = int(value)
        except:
            pass

        return result

def build_strategy(strategy_str):
    strategy = None

    if (strategy_str == "hybrid_card"):
        strategy = HybridCard()
    elif (strategy_str == "max_card"):
        strategy = MaxCard()
    elif (strategy_str == "min_card"):
        strategy = MinCard()
    elif (strategy_str == "nearest_card"):
        strategy = NearestCard()
    elif (strategy_str == "next_card"):
        strategy = NextCard()
    elif (strategy_str == "console_card"):
        strategy = ConsoleCard()
    else:
        raise ValueError("unknown strategy: " + strategy_str)

    return strategy
