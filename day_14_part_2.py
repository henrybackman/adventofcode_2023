from icecream import ic
import itertools

def move_left(m):
    new_m = []
    for i in range(len(m)):
        row = m[i]
        parts = []
        o = []
        d = []
        for c in row:
            if c == 'O':
                o.append('O')
                continue
            if c == '.':
                d.append('.')
                continue
            if c == '#':
                parts.append(o + d + ['#'])
                o = []
                d = []
                continue
        parts.append(o + d)
        new_m.append(list(itertools.chain(*parts)))
    return new_m

def rotate_matrix(m):
    return [list(x) for x in list(zip(*m[::-1]))]

def main():
    m = []
    with open('data/day14.data') as f:
        for row in f:
            m.append([c for c in row.strip()])

    move_left(m)
    # ic(m)
    cycle_count = 1_000_000
    for i in range(cycle_count):
        if i % 1_000_000 == 0:
            ic(i)
        m = rotate_matrix(m)
        m = move_left(m) # upwards
        m = rotate_matrix(m)
        m = move_left(m) # leftwards
        m = rotate_matrix(m)
        m = move_left(m) # downwards
        m = rotate_matrix(m)
        m = move_left(m) # rightwards

    # ic(m)
    res = 0
    multiplier = len(m)
    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == 'O':
                res += multiplier
        multiplier -= 1
    ic(res)

if __name__ == '__main__':
    main()
