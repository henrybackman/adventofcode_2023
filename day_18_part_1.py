from icecream import ic
import math
from copy import deepcopy
import time

def get_xy_in_direction(from_direction, x, y):
    if from_direction == 'U':
        return x, y + 1
    elif from_direction == 'D':
        return x, y - 1
    elif from_direction == 'L':
        return x - 1, y
    elif from_direction == 'R':
        return x + 1, y
    else:
        raise ValueError(f'unknown from_direction: {from_direction}')

def print_path(path):
    min_x = min([x for x, y in path])
    max_x = max([x for x, y in path])
    min_y = min([y for x, y in path])
    max_y = max([y for x, y in path])

    ic(min_x, max_x, min_y, max_y)
    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            if (x, y) in path:
                print('#', end='')
            else:
                print('.', end='')
        print()

def print_path_to_file(path, filename):
    min_x = min([x for x, y in path])
    max_x = max([x for x, y in path])
    min_y = min([y for x, y in path])
    max_y = max([y for x, y in path])

    with open(filename, 'w') as f:
        for y in range(max_y, min_y - 1, -1):
            for x in range(min_x, max_x + 1):
                if (x, y) in path:
                    f.write('#')
                else:
                    f.write('.')
            f.write('\n')

def main():
    m = []
    d = []
    with open('data/day18.data') as f:
        for row in f:
            direction, steps, color = row.strip().split(' ')
            d.append((direction, int(steps)))

    path = []
    current_step = (0, 0, 'R')
    path.append(current_step)
    for direction, step in d:
        for i in range(step):
            current_step = get_xy_in_direction(direction, *current_step)
            path.append(current_step)

    print_path_to_file(path, 'output/path.txt')
    min_x = min([x for x, y in path])
    max_x = max([x for x, y in path])
    min_y = min([y for x, y in path])
    max_y = max([y for x, y in path])

    digged_cells = set(path)
    prev_step = None
    # pending_dig = False # if path goes to left, try to dig next
    for step in path:
        if not prev_step:
            prev_step = step
            continue
        cur_x, cur_y = step
        _, prev_y = prev_step

        if cur_y == min_y or cur_y == max_y: # no need to dig first or last row
            prev_step = step
            continue
        if cur_y >= prev_y:
            prev_step = step
            continue # not going down
        # fill left side until hit path
        x = cur_x
        dug = False
        while x > min_x:
            x -= 1
            if (x, cur_y) in path and dug:
                break
            if (x, cur_y) in path:
                continue
            digged_cells.add((x, cur_y))
            dug = True
        prev_step = step

    ic(len(digged_cells))
    # print_path(digged_cells)
    print_path_to_file(digged_cells, 'output/digged.txt')

if __name__ == '__main__':
    main()
