from icecream import ic

def rotate_north(m):
    for x in range(len(m[0])):
        next_stop_y = 0
        for y in range(len(m)):
            val = m[y][x]
            if val == '#':
                next_stop_y = y + 1
                continue
            if val == '.':
                continue
            if val == 'O': # move up to the next stop and update
                if y <= next_stop_y: # already at the next stop
                    next_stop_y = y + 1
                    continue
                m[next_stop_y][x] = 'O'
                m[y][x] = '.'
                next_stop_y += 1
    return m


def main():
    m = []
    with open('data/day14.data') as f:
        for row in f:
            m.append([c for c in row.strip()])
    # ic(m)
    m = rotate_north(m)
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
