from icecream import ic

def follow_beam(m, x, y, direction):
    new_beams = set()
    next_value = None
    current_x = x
    current_y = y
    if direction == 'up':
        current_y -= 1
    elif direction == 'down':
        current_y += 1
    elif direction == 'left':
        current_x -= 1
    elif direction == 'right':
        current_x += 1
    
    if current_x < 0 or current_y < 0:
        return None
    try:
        next_value = m[current_y][current_x]
    except IndexError:
        return None
    
    if next_value == '.':
        new_beams.add((current_x, current_y, direction))
    elif direction == 'up' or direction == 'down':
        if next_value == '|':
            new_beams.add((current_x, current_y, direction))
        if next_value == '-':
            new_beams.add((current_x, current_y, 'left'))
            new_beams.add((current_x, current_y, 'right'))
        if direction == 'up':
            if next_value == '/':
                new_beams.add((current_x, current_y, 'right'))
            if next_value == '\\':
                new_beams.add((current_x, current_y, 'left'))
        if direction == 'down':
            if next_value == '/':
                new_beams.add((current_x, current_y, 'left'))
            if next_value == '\\':
                new_beams.add((current_x, current_y, 'right'))
    elif direction == 'left' or direction == 'right':
        if next_value == '-':
            new_beams.add((current_x, current_y, direction))
        if next_value == '|':
            new_beams.add((current_x, current_y, 'up'))
            new_beams.add((current_x, current_y, 'down'))
        if direction == 'left':
            if next_value == '/':
                new_beams.add((current_x, current_y, 'down'))
            if next_value == '\\':
                new_beams.add((current_x, current_y, 'up'))
        if direction == 'right':
            if next_value == '/':
                new_beams.add((current_x, current_y, 'up'))
            if next_value == '\\':
                new_beams.add((current_x, current_y, 'down'))
    
    return new_beams

def get_energy(m, x, y, direction):
    beams = set()
    beams.add((x, y, direction))

    energized_nodes = set()
    resolved_beams = set()
    while beams:
        x, y, direction = beams.pop()
        if (x, y, direction) in resolved_beams:
            continue
        resolved_beams.add((x, y, direction))
        energized_nodes.add((x, y))
        new_beams = follow_beam(
            m, x, y, direction)
        if new_beams:
            beams.update(new_beams)

    return len(energized_nodes) - 1 # -1 because we start at (-1, 0) which is not valid

def main():
    m = []
    with open('data/day16.data') as f:
        for row in f:
            m.append(list(row.strip()))

    max_energy = 0
    starting_beams = set()
    # from left to right
    for sy in range(len(m)):
        starting_beams.add((-1, sy, 'right'))
    # from top to bottom
    for sx in range(len(m[0])):
        starting_beams.add((sx, -1, 'down'))
    # from right to left
    for sy in range(len(m)):
        starting_beams.add((len(m[0]), sy, 'left'))
    # from bottom to top
    for sx in range(len(m[0])):
        starting_beams.add((sx, len(m), 'up'))
    
    for starting_beam in starting_beams:
        x, y, direction = starting_beam
        energy = get_energy(m, x, y, direction)
        if energy > max_energy:
            max_energy = energy

    ic(max_energy)

if __name__ == '__main__':
    main()
