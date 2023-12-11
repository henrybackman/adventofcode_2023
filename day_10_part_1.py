from icecream import ic
from dataclasses import dataclass, field

DIRS = ['up', 'down', 'left', 'right']
FROM = ['down', 'up', 'right', 'left']

VALID_SYMS = {
    'up': ['|', 'F', '7'],
    'down': ['|', 'J', 'L'],
    'left': ['-', 'F', 'L'],
    'right': ['-', 'J', '7']
}

VALID_DIRECTIONS_FROM = {
    '|': ['up', 'down'],
    '-': ['left', 'right'],
    'F': ['down', 'right'],
    'J': ['up', 'left'],
    'L': ['up', 'right'],
    '7': ['down', 'left']
}

VALID_DIRECTIONS_TO = {
    '|': ['up', 'down'],
    '-': ['left', 'right'],
    'F': ['up', 'left'],
    'J': ['down', 'right'],
    'L': ['down', 'left'],
    '7': ['up', 'right']
}

def get_next_coord(direction: str, from_: tuple[int, int]):
    if direction == 'up':
        return (from_[0], from_[1] - 1)
    elif direction == 'down':
        return (from_[0], from_[1] + 1)
    elif direction == 'left':
        return (from_[0] - 1, from_[1])
    elif direction == 'right':
        return (from_[0] + 1, from_[1])
    else:
        raise ValueError('Invalid direction')


@dataclass
class Path():
    length: int = 0
    coord: tuple[int, int] = field(default_factory=tuple)
    symbol: str = ''
    prev_coord: tuple[int, int] = field(default_factory=tuple)

class Map():
    def __init__(self, map):
        self.map = map

    def get(self, c: tuple[int, int]):
        try:
            return self.map[c[1]][c[0]]
        except IndexError:
            return None
    
def get_next(map_: Map, path: Path):
    next_coord = None
    symbol = None
    for direction in DIRS:
        if direction not in VALID_DIRECTIONS_FROM[path.symbol]:
            continue
        next_coord = get_next_coord(direction, path.coord)
        symbol = map_.get(next_coord)
        if not symbol:
            continue
        if direction not in VALID_DIRECTIONS_TO.get(symbol, []):
            continue
        if next_coord == path.prev_coord:
            continue
        break
    assert next_coord is not None
    assert symbol is not None
    return next_coord, symbol

def main():
    m = []
    s: tuple[int, int] = (0, 0) # x,y of start
    with open('data/day10.data') as f:
        for i, line in enumerate(f):
            parts = [char for char in line.strip()]
            try:
                s = (parts.index('S'), i)
            except ValueError:
                pass
            m.append(parts)

    map_ = Map(m)
    paths = []
    for d in DIRS:
        next_coord = get_next_coord(direction=d, from_=s)
        symbol = map_.get(next_coord)
        assert symbol is not None
        if symbol not in VALID_SYMS[d]:
            continue
        if d in VALID_DIRECTIONS_TO[symbol]:
            path = Path(length=1, coord=next_coord, prev_coord=s, symbol=symbol)
            paths.append(path)

    pass
    while True:
        for path in paths:
            next_coord, symbol = get_next(map_, path)
            path.length += 1
            path.prev_coord = path.coord
            path.symbol = symbol
            path.coord = next_coord

        if paths[0].coord == paths[1].coord:
            break
        if paths[0].prev_coord == paths[1].coord:
            break
        if paths[0].coord == paths[1].prev_coord:
            break
    ic(min([path.length for path in paths]))


if __name__ == '__main__':
    main()