from icecream import ic
from dataclasses import dataclass, field
import regex as re

def main():
    data = []

    with open('data/day4.data') as f:
        for row in f:
            _, card_data = row.split(': ')
            win_numbers, card_numbers = card_data.split(' | ')
            win_numbers = re.split(r'\s+', win_numbers)
            card_numbers = re.split(r'\s+', card_numbers)
            win_numbers = [int(x) for x in win_numbers if x]
            card_numbers = [int(x) for x in card_numbers if x]
            data.append((win_numbers, card_numbers))

    sum = 0
    for card in data:
        wins = 0
        for win_number in card[0]:
            card_numbers = card[1]
            if win_number in card_numbers:
                wins += 1
        if wins:
            sum += 2 ** (wins - 1)
    ic(sum)


if __name__ == '__main__':
    main()