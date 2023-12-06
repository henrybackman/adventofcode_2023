from icecream import ic
import regex as re
import math

def main():
    times = []
    targets = []
    data = None
    with open('data/day6.data') as f:
        for row_no, row in enumerate(f):
            if row_no == 0:
                times = [int(x) for x in re.findall(r'\d+', row)]
            elif row_no == 1:
                targets = [int(x) for x in re.findall(r'\d+', row)]
        data = zip(times, targets)
    
    res = 1
    for time, target in data:
        min_time = (-time + math.sqrt(time**2 - 4*-1*-target))/-2
        max_time = (-time - math.sqrt(time**2 - 4*-1*-target))/-2
        margin = math.floor(max_time) - math.ceil(min_time) + 1
        res *= margin
    
    ic(res)

if __name__ == '__main__':
    main()