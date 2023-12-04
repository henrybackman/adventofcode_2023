from icecream import ic
from dataclasses import dataclass, field

@dataclass
class RowData:
    numbers: list = field(default_factory=list)
    relevant_indexes: set = field(default_factory=set)

@dataclass()
class Number:
    digits: list = field(default_factory=list)
    indexes: list = field(default_factory=list)
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
                    current_number.indexes.append(i)
                    continue 
                if char == '.':
                    continue
                relevant_rows = [row_id - 1, row_id, row_id + 1]
                for relevant_row in relevant_rows:
                    if relevant_row < 0:
                        continue
                    if relevant_row not in data:
                        data[relevant_row] = RowData()
                    relevant_index = [i - 1, i, i + 1]
                    for ri in relevant_index:
                        data[relevant_row].relevant_indexes.add(ri)

    ic(data)
    sum = 0
    for row_data in data:
        for number in data[row_data].numbers:
            for i in number.indexes:
                if i in data[row_data].relevant_indexes:
                    sum += number.value
                    break
    ic(sum)


if __name__ == '__main__':
    main()