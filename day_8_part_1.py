from icecream import ic


def main():
    directions = []
    nodes = {}
    with open('data/day8.data') as f:
        for i, row in enumerate(f):
            if i == 0:
                directions = row.strip()
                continue
            if i == 1:
                continue
            node, dest = row.strip().split(' = ')
            dest = (dest[1:4], dest[6:9])
            nodes[node] = dest

    step = -1
    current_node = 'AAA'
    step_count = 0
    while True:
        step += 1
        step_count += 1   
        try:
            direction = directions[step]
        except IndexError:
            step = 0
            direction = directions[step]
        
        current_node = nodes[current_node][0] if direction == 'L' else nodes[current_node][1]
        
        if current_node == 'ZZZ':
            break
    ic(step_count)

if __name__ == '__main__':
    main()