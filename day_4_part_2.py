from icecream import ic
from dataclasses import dataclass, field
import regex as re

@dataclass
class Card:
    win_numbers: list = field(default_factory=list)
    numbers: list = field(default_factory=list)
    matches: int = 0
    copies: int = 1

def main():
    cards = []

    with open('data/day4.data') as f:
        for row in f:
            _, card_data = row.split(': ')
            win_numbers, numbers = card_data.split(' | ')
            win_numbers = re.split(r'\s+', win_numbers)
            numbers = re.split(r'\s+', numbers)
            win_numbers = [int(x) for x in win_numbers if x]
            numbers = [int(x) for x in numbers if x]
            card = Card(win_numbers, numbers)
            cards.append(card)

    
    for i, card in enumerate(cards):
        for win_number in card.win_numbers:
            if win_number in card.numbers:
                card.matches += 1
        copy_id = i
        for _ in range(card.matches):
            copy_id += 1
            cards[copy_id].copies += card.copies

    ic(sum([card.copies for card in cards]))


if __name__ == '__main__':
    main()