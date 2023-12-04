from icecream import ic
from dataclasses import dataclass, field

@dataclass
class RowData:
    numbers: list = field(default_factory=list)
    gears: list = field(default_factory=list)

@dataclass()
class Gear:
    row: int
    index: int

@dataclass()
class Number:
    digits: list = field(default_factory=list)
    indexes: set = field(default_factory=set)
    value: int = 0

def main():
    data = {}

    with open('data/day3.data') as f:
        row_id = -1
        for row in f:
            row_id += 1
            if row_id not in data:
                data[row_id] = RowData()
            current_number = Number()
            collecting_number = False
            for i, char in enumerate(row):
                if not char.isnumeric() and collecting_number:
                    collecting_number = False
                    current_number.value = int(''.join(current_number.digits))
                    data[row_id].numbers.append(current_number)
                    current_number = Number()
                if char == '\n':
                    continue
                if char.isnumeric():
                    collecting_number = True
                    current_number.digits.append(char)
                    current_number.indexes.add(i)
                    continue 
                if char == '.':
                    continue
                if char != '*':
                    continue
                data[row_id].gears.append(Gear(row_id, i))

    sum = 0
    for row_data in data:
        for gear in data[row_data].gears:
            number_values = []
            relevant_rows = [gear.row - 1, gear.row, gear.row + 1]
            relevant_indexes = set([gear.index - 1, gear.index, gear.index + 1])
            for relevant_row in relevant_rows:
                if relevant_row not in data:
                    continue
                for number in data[relevant_row].numbers:
                    if number.indexes & relevant_indexes: # check if intersection
                        number_values.append(number.value)
            if len(number_values) == 2:
                sum += number_values[0] * number_values[1]
    ic(sum)


if __name__ == '__main__':
    main()