from icecream import ic
import regex as re
import math

def main():
    time = 0
    target = 0
    with open('data/day6.data') as f:
        for row_no, row in enumerate(f):
            if row_no == 0:
                time = int(''.join(re.findall(r'\d+', row)))
            elif row_no == 1:
                target = int(''.join(re.findall(r'\d+', row)))
    
    min_time = (-time + math.sqrt(time**2 - 4*-1*-target))/-2
    max_time = (-time - math.sqrt(time**2 - 4*-1*-target))/-2
    margin = math.floor(max_time) - math.ceil(min_time) + 1

    ic(margin)

if __name__ == '__main__':
    main()