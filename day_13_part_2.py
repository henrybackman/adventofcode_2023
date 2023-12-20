from icecream import ic

def solve(m, col_filter=None, row_filter=None):
    # search col 
    cand = 1
    width = len(m[0])
    height = len(m)
    while cand < width:
        if cand == col_filter:
            cand += 1
            continue
        is_mirror_col = True
        distance_from_end = width - cand
        min_x = max(0, width - 2 * distance_from_end)
        max_x = min(width, cand)
        for y in range(len(m)):
            for x in range(min_x, max_x):
                left_val = m[y][x]
                right_x = cand + (cand - x) - 1
                right_val = m[y][right_x]
                if left_val != right_val:
                    is_mirror_col = False
                    break
            if not is_mirror_col:
                break
        if is_mirror_col:
            return cand, cand, None
        cand += 1

    # search row if col not found
    cand = 1
    while cand < height:
        if cand == row_filter:
            cand += 1
            continue
        is_mirror = True
        distance_from_end = height - cand
        min_y = max(0, height - 2 * distance_from_end)
        max_y = min(height, cand)
        for y in range(min_y, max_y):
            for x in range(width):
                up_val = m[y][x]
                down_y = cand + (cand - y) - 1
                down_val = m[down_y][x]
                if up_val != down_val:
                    is_mirror = False
                    break
            if not is_mirror:
                break
        if is_mirror:
            return cand * 100, None, cand
        cand += 1

    return 0, None, None


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
        original_res, col_filter, row_filter = solve(pattern)
        new_res = 0
        found = False
        # try changing each value until new res is found
        for y in range(len(pattern)):
            for x in range(len(pattern[0])):
                orig_val = pattern[y][x]
                new_val = '#' if orig_val == '.' else '.'
                pattern[y][x] = new_val
                new_res, _, _ = solve(pattern, col_filter, row_filter)
                if new_res > 0 and new_res != original_res:
                    found = True
                    break
                pattern[y][x] = orig_val
            if found:
                break
        assert found
        res += new_res
    ic(res)

if __name__ == '__main__':
    main()
