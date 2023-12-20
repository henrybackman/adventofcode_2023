from icecream import ic

def solve(m):
    # search col 
    cand = 1
    width = len(m[0])
    height = len(m)
    while cand < width:
        is_mirror_col = True
        distance_from_end = width - cand
        min_x = max(0, width - 2 * distance_from_end)
        max_x = min(width, cand)
        for y in range(len(m)):
            for x in range(min_x, max_x):
                left_val = m[y][x]
                right_x = cand + (cand - x) - 1
                right_val = m[y][right_x]
                # ic(cand, x, right_x, left_val, right_val)
                if left_val != right_val:
                    # ic('not mirror')
                    is_mirror_col = False
                    break
            if not is_mirror_col:
                break
        if is_mirror_col:
            # ic('found')
            return cand   
        cand += 1

    # search row if col not found
    cand = 1
    while cand < height:
        is_mirror = True
        distance_from_end = height - cand
        min_y = max(0, height - 2 * distance_from_end)
        max_y = min(height, cand)
        for y in range(min_y, max_y):
            for x in range(width):
                up_val = m[y][x]
                down_y = cand + (cand - y) - 1
                down_val = m[down_y][x]
                # ic(cand, x, down_y, up_val, down_val)
                if up_val != down_val:
                    # ic('not mirror')
                    is_mirror = False
                    break
            if not is_mirror:
                break
        if is_mirror:
            # ic('found')
            return cand * 100 
        cand += 1

    assert False # should not reach here


def main():
    l = []
    cur = []
    with open('data/day13.data') as f:
        for row in f:
            if len(row.strip()) == 0:
                l.append(cur)
                cur = []
                continue
            
            cur.append([c for c in row.strip()])
        l.append(cur)
    res = 0
    for pattern in l:
        # ic(pattern)
        res += solve(pattern)
    ic(res)

if __name__ == '__main__':
    main()
