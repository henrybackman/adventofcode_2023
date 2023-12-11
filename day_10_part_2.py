from icecream import ic
from dataclasses import dataclass, field
from typing import List

VALID_DIRECTIONS_FROM = {
    '|': ['up', 'down'],
    '-': ['left', 'right'],
    'F': ['down', 'right'],
    'J': ['up', 'left'],
    'L': ['up', 'right'],
    '7': ['down', 'left'],
    'S': ['up', 'down', 'left', 'right']
}

VALID_DIRECTIONS_TO = {
    '|': ['up', 'down'],
    '-': ['left', 'right'],
    'F': ['up', 'left'],
    'J': ['down', 'right'],
    'L': ['down', 'left'],
    '7': ['up', 'right'],
    'S': ['up', 'down', 'left', 'right']
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
class Node():
    coord: tuple[int, int]
    symbol: str = ''
    direction: str = ''

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return self.coord == other.coord

    def __hash__(self):
        return hash(self.coord)

@dataclass
class Path():
    nodes: List[Node] = field(default_factory=list)

class Map():
    def __init__(self, map):
        self.map = map

    def get(self, c: tuple[int, int]):
        try:
            assert c[0] >= 0
            assert c[1] >= 0
            return self.map[c[1]][c[0]]
        except (IndexError, AssertionError):
            return None
    
def get_next_node(map_: Map, node: Node, prev_node: Node | None) -> Node:
    next_coord = None
    symbol = None
    direction = None
    for d in VALID_DIRECTIONS_FROM[node.symbol]:
        direction = d
        next_coord = get_next_coord(direction, node.coord)
        symbol = map_.get(next_coord)
        if not symbol:
            continue
        if direction not in VALID_DIRECTIONS_TO.get(symbol, []):
            continue
        if prev_node and next_coord == prev_node.coord:
            continue
        break
    assert next_coord is not None
    assert symbol is not None
    assert direction is not None
    return Node(coord=next_coord, symbol=symbol, direction=direction)

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
    path = Path()
    path.nodes.append(Node(coord=s, symbol='S', direction=''))
    while True:
        node = path.nodes[-1]
        prev_node = path.nodes[-2] if len(path.nodes) > 1 else None
        next_node = get_next_node(map_, node, prev_node)
        if next_node.symbol == 'S':
            break
        path.nodes.append(next_node)
    ic(len(path.nodes) // 2)

    right_turns = 0
    left_turns = 0
    for node in path.nodes:
        if node.direction == 'left' and node.symbol == 'L':
            right_turns += 1
        elif node.direction == 'left' and node.symbol == 'F':
            left_turns += 1
        elif node.direction == 'right' and node.symbol == '7':
            right_turns += 1
        elif node.direction == 'right' and node.symbol == 'J':
            left_turns += 1
        elif node.direction == 'up' and node.symbol == 'F':
            right_turns += 1
        elif node.direction == 'up' and node.symbol == '7':
            left_turns += 1
        elif node.direction == 'down' and node.symbol == 'J':
            right_turns += 1
        elif node.direction == 'down' and node.symbol == 'L':
            left_turns += 1
    ic(right_turns)
    ic(left_turns)
    assert abs(right_turns - left_turns) == 3 # S doesn't count
    loop_turn = 'right' if right_turns > left_turns else 'left'
    inside_nodes = set()

    for node in path.nodes:
        # y_adj = 0 should be enough to find the inside nodes row by row
        x_adj = 0
        if node.direction == 'up' and node.symbol == '|':
            x_adj = 1 if loop_turn == 'right' else -1
        if node.direction == 'up' and node.symbol == '7':
            x_adj = 1 if loop_turn == 'right' else -1
        if node.direction == 'right' and node.symbol == 'J':
            x_adj = 1 if loop_turn == 'right' else -1
        inside_node = Node(coord=(node.coord[0] + x_adj, node.coord[1]))
        while inside_node not in inside_nodes and inside_node not in path.nodes and map_.get(inside_node.coord):
            inside_nodes.add(inside_node)
            inside_node = Node(coord=(inside_node.coord[0] + x_adj, inside_node.coord[1]))

    # print map with path
    for i, line in enumerate(m):
        for j, char in enumerate(line):
            symbol = ' '
            for node in path.nodes:
                if (j, i) == node.coord:
                    symbol = node.symbol
                    break
            for node in inside_nodes:
                if (j, i) == node.coord:
                    symbol = 'O'
                    break
            print(symbol, end='')
        print()
    ic(len(inside_nodes))

if __name__ == '__main__':
    main()