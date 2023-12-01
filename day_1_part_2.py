from icecream import ic
import regex

def get_data():
    data = []
    with open('data/day1.data') as f:
        for row in f:
            data.append(row.strip())
            
    return data

def main():
    data = get_data()

    num_to_str = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5:'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    str_to_num = dict((v,k) for k,v in num_to_str.items())

    num_search = '|'.join(['\d'] + [num_to_str for num_to_str in num_to_str.values()])

    total = 0
    for row in data:
        # regex to get first digit of the string, ignoring the rest
        numbers = regex.findall(fr'{num_search}', row, overlapped=True)
        first_num_str = numbers[0]
        last_num_str = numbers[-1]
        try:
            first_num = int(first_num_str)
        except ValueError:
            first_num = str_to_num[first_num_str]
        try:
            last_num = int(last_num_str)
        except ValueError:
            last_num = str_to_num[last_num_str]
        num = int(str(first_num) + str(last_num))
        total += num
    ic(total)

if __name__ == '__main__':
    main()