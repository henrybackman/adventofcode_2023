from icecream import ic
import math
from copy import deepcopy
import time

# doesn't take into account cases where getting to specific cell is
# not the cheapest way but allows avoiding the 3 straight rule and overall
# is cheaper
# need different approach to this, probably depth first search instead of
# breadth first search


class Path():
    def __init__(self, m, direction, x=0, y=0, step_history=[], straight_count=0, heat_loss=0):
        self.m = m
        self.direction = direction
        self.straight_count = straight_count
        self.x = x
        self.y = y
        self.heat_loss = heat_loss
        self.step_history = step_history if step_history else [(x, y, direction)]
        self.valid = True

    def add_step(self, new_direction):   
        if new_direction == self.direction:
            self.straight_count += 1
        else:
            self.straight_count = 1

        self.direction = new_direction

        if self.direction == 'up':
            self.y -= 1
        elif self.direction == 'down':
            self.y += 1
        elif self.direction == 'left':
            self.x -= 1
        elif self.direction == 'right':
            self.x += 1
        else:
            raise Exception('Invalid direction')

        if (self.straight_count >= 3 
            or self.x < 0 
            or self.y < 0 
            or self.x >= len(self.m[0]) 
            or self.y >= len(self.m)):
            self.valid = False

        # check if already in step history
        if (self.x, self.y, self.direction) in self.step_history:
            self.valid = False

        if self.valid:    
            self.step_history.append((self.x, self.y, self.direction))
            self.heat_loss += self.m[self.y][self.x]


def is_opposite(d1, d2):
    if d1 == 'up' and d2 == 'down':
        return True
    if d1 == 'down' and d2 == 'up':
        return True
    if d1 == 'left' and d2 == 'right':
        return True
    if d1 == 'right' and d2 == 'left':
        return True
    return False

def print_map(height, width, paths):
    print('-' * width)
    out = []
    for y in range(height):
        out.append([])
        for x in range(width):
            out[y].append('.')
    for path in paths:
        for x, y, _ in path.step_history:
            out[y][x] = '#'
    print('\n'.join([''.join(row) for row in out]))
    # time.sleep(0.1)

def print_path(height, width, path):
    print('-' * width)
    out = []
    for y in range(height):
        out.append([])
        for x in range(width):
            out[y].append('.')
    for x, y, _ in path.step_history:
        out[y][x] = '#'
    print('\n'.join([''.join(row) for row in out]))
    # time.sleep(0.1)

def main():
    m = []
    with open('data/day17.data') as f:
        for row in f:
            m.append([int(x) for x in list(row.strip())])

    paths = set()
    target_xy = (len(m[0]) - 1, len(m) - 1)
    min_heat_losses = {}
    
    paths.add(Path(m, 'down'))
    # paths.add(Path(m, 'right'))
    while paths:
        path = paths.pop()
        if not path.valid:
            continue
        cell_xy = (path.x, path.y)
        # ic('handling:')
        # ic(path.x, path.y, path.direction, path.step_history)
        current_min_heat_loss = min_heat_losses.get(cell_xy, math.inf)
        # if path.heat_loss >= current_min_heat_loss:
        #     continue # another path has less heat loss

        min_heat_losses[cell_xy] = path.heat_loss
        print_path(len(path.m), len(path.m[0]), path)
        
        if cell_xy == target_xy:
            continue # at the end

        # otherwise continue paths in all directions
        for direction in ['up', 'down', 'left', 'right']:
            if is_opposite(direction, path.direction):
                continue # no need to check opposite direction

            new_path = deepcopy(path)
            new_path.add_step(direction)
            if not new_path.valid:
                continue
            
            # ic('adding:')
            # ic(new_path.x, new_path.y, new_path.direction, new_path.step_history, path.straight_count, path.step_history)
            paths.add(new_path)
        # print_map(len(path.m), len(path.m[0]), paths)

    ic(min_heat_losses[target_xy])
if __name__ == '__main__':
    main()
