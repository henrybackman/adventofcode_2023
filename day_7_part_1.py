from icecream import ic
from dataclasses import dataclass, field
from collections import OrderedDict
import regex as re
import math

class Hand():

    card_map = {
        'A': 'A',
        'K': 'B',
        'Q': 'C',
        'J': 'D',
        'T': 'E',
        '9': 'F',
        '8': 'G',
        '7': 'H',
        '6': 'I',
        '5': 'J',
        '4': 'K',
        '3': 'L',
        '2': 'M'
    }

    def __init__(self, hand: str, bid: int):
        self.original_hand = hand
        self.hand = ''.join([self.card_map[card] for card in hand])
        self.rank = self.get_rank()
        self.bid = bid

    def __lt__(self, other):
        if self.rank > other.rank:
            return True
        elif self.rank == other.rank:
            return self.hand > other.hand
        else:
            return False
    
    def get_rank(self):
        card_values = {}
        for card in self.hand:
            card_values[card] = card_values.get(card, 0) + 1
        card_values = OrderedDict(sorted(card_values.items(), key=lambda item: item[1], reverse=True))
        distinct_cards = len(card_values)
        _, highest_count = card_values.popitem(last=False)
        try:
            _, second_highest_count = card_values.popitem(last=False)
        except KeyError:
            second_highest_count = 0
        if distinct_cards == 1:
            return 1
        elif distinct_cards == 2 and highest_count == 4: # four of a kind
            return 2
        elif distinct_cards == 2 and highest_count == 3 and second_highest_count == 2: # full house
            return 3
        elif distinct_cards == 3 and highest_count == 3: # three of a kind
            return 4
        elif highest_count == 2 and second_highest_count == 2: # two pairs
            return 5
        elif distinct_cards == 4: # one pair
            return 6
        else: # high card
            return 7
        

def main():
    hands: list[Hand] = []
    with open('data/day7.data') as f:

        for row in f:
            hands.append(Hand(row.split(' ')[0], int(row.split(' ')[1])))
    
    hands.sort()
    total = 0
    for i in range(len(hands)):
        rank = i + 1
        winnings = rank * hands[i].bid
        total += winnings
    ic(total)

if __name__ == '__main__':
    main()