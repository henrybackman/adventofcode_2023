from icecream import ic
from collections import OrderedDict
import math

def main():
    seeds = []
    maps = []
    with open('data/day5.data') as f:
        collecting_map = False
        map_name = None
        maps = OrderedDict()
        for row in f:
            if not seeds:
                seeds = row.strip().split(': ')[1].split(' ')
                continue
            if not row.strip():
                collecting_map = False
                continue
            if not collecting_map:
                collecting_map = True
                map_name = row.strip().split(' ')[0]
                maps[map_name] = []
                continue
            to_, from_, range_ = [int(x) for x in row.split(' ')]
            maps[map_name].append((to_, from_, range_))

    min_location = math.inf
    for seed in seeds:
        location = int(seed)
        for map in maps.values():
            for to_, from_, range_ in map:
                if from_ <= location <= from_ + range_:
                    shift = int(to_) - int(from_)
                    location += shift
                    break
        if location < min_location:
            min_location = location
    
    ic(min_location)

if __name__ == '__main__':
    main()