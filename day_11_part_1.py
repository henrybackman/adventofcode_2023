from icecream import ic
from dataclasses import dataclass, field

class Map():
    def __init__(self) -> None:
        self.m = []
        self.galaxies = []
        self.x_galaxy_counts = {}
        self.y_galaxy_counts = {}
        self.x_expansions = set()
        self.y_expansions = set()
    
    def add_row(self, row):
        self.m.append(row)
        for i, c in enumerate(row):
            x = i
            y = len(self.m) - 1
            if c == '#':
                self.galaxies.append((x, y))
                self.x_galaxy_counts[x] = self.x_galaxy_counts.get(x, 0) + 1
                self.y_galaxy_counts[y] = self.y_galaxy_counts.get(y, 0) + 1
    
    def find_expansions(self):
        for x in range(len(self.m[0])):
            if x not in self.x_galaxy_counts:
                self.x_expansions.add(x)
        for y in range(len(self.m)):
            if y not in self.y_galaxy_counts:
                self.y_expansions.add(y)

def main():
    m = Map()
    with open('data/day11.data') as f:
        for i, line in enumerate(f):
            m.add_row([c for c in line.strip()])

    m.find_expansions()
    galaxy_pairs = set()
    for galaxy in m.galaxies:
        for other in m.galaxies:
            if galaxy == other:
                continue
            galaxy_pairs.add(tuple(sorted([galaxy, other])))
    
    # calculate distances
    total_distance = 0
    for pair in galaxy_pairs:
        x1, y1 = pair[0]
        x2, y2 = pair[1]
        x_first, x_last = sorted([x1, x2])
        y_first, y_last = sorted([y1, y2])
        x_diff = x_last - x_first
        y_diff = y_last - y_first
        for x in range(x_first + 1, x_last):
            if x in m.x_expansions:
                x_diff += 1
        for y in range(y_first + 1, y_last):
            if y in m.y_expansions:
                y_diff += 1
        distance = x_diff + y_diff
        total_distance += distance
    ic(total_distance)

if __name__ == '__main__':
    main()