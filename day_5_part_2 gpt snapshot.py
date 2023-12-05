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
                seeds = [(int(seeds[i]), int(seeds[i+1])) for i in range(0, len(seeds), 2)]
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

    maps = OrderedDict(reversed(list(maps.items())))
    min_location = 0
    stop = False
    while True:
        cur = min_location
        for map_name, map_ in maps.items():
            for from_, to_, range_ in map_: # reversing mapping, so from_ is to_ here
                if from_ <= cur <= from_ + range_:
                    shift = to_ - from_
                    cur += shift
                    break
        # search candidate in the seeds
        for seed_start, seed_count in seeds:
            if seed_start <= cur < seed_start + seed_count:
                stop = True
                break
        if stop:
            break
        min_location += 1
        if min_location % 1_000_000 == 0:
            ic(min_location)

    ic(min_location)

if __name__ == '__main__':
    main()