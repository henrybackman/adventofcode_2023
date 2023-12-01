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
    ic(data)
    total = 0
    for row in data:
        # regex to get first digit of the string, ignoring the rest
        first_digit = regex.search(r'(?<=^\D*)\d', row).group()
        last_digit = regex.search(r'\d(?=\D*$)', row).group()
        num = int(str(first_digit) + str(last_digit))
        total += num
    ic(total)

if __name__ == '__main__':
    main()