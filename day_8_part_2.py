from icecream import ic


def find_repeating_cycle(nodes, directions, node):
    visited_node_steps = dict()
    step = -1
    current_node = node
    step_count = 0
    visited_node_steps[(current_node, len(directions) - 1)] = None # if starting node is in the loop, then it would be the last step of directions
    while True:
        step += 1
        step_count += 1   
        try:
            direction = directions[step]
        except IndexError:
            step = 0
            direction = directions[step]
        
        current_node = nodes[current_node][0] if direction == 'L' else nodes[current_node][1]
        visited_node_step = (current_node, step)
        if visited_node_step in visited_node_steps: # loop started
            break
        visited_node_steps[visited_node_step] = None # only the key matters
    loop_start = 0
    for i, visited_node_step in enumerate(visited_node_steps):
        visited_node, visited_step = visited_node_step
        if visited_node == current_node and visited_step == step:
            loop_start = i
            break
    repeating_cycle = list(visited_node_steps)[loop_start:]
    return repeating_cycle, loop_start    

def find_dividers(n):
    dividers = []
    for i in range(1, n + 1):
        if n % i == 0:
            dividers.append(i)
    return sorted(dividers, reverse=True)

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

    starting_nodes = []
    for node in nodes:
        if node[-1] == 'A':
            starting_nodes.append(node)
    
    cycles = []
    for starting_node in starting_nodes:
        cycle, start = find_repeating_cycle(nodes, directions, starting_node)
        stops = []
        for i, node_step in enumerate(cycle):
            node, step = node_step
            if node[-1] == 'Z':
                stops.append(i)
        cycles.append((start, stops, len(cycle)))
        ic(starting_node, start, stops, len(cycle))

    ic(cycles)
    # assume that each cycle has only one exit node, and that the exit node is at the end of the cycle
    cycle_lengths = []
    for _, _, cycle_length in cycles:
        cycle_lengths.append((cycle_length, find_dividers(cycle_length)))

    # find the least common multiple of the cycle lengths usin greatest common divisors
    lcm = None
    previous_dividers = None
    for cycle_length, dividers in cycle_lengths:
        ic(cycle_length, dividers)
        if not lcm:
            lcm = cycle_length
            previous_dividers = dividers
            continue
        # find the greatest common divisor of the previous cycle length and the current cycle length
        # and use it to update lcm
        for divider in dividers:
            if divider in previous_dividers:
                lcm = (lcm * cycle_length) // divider
                break
    
    ic(lcm) # 10668805667831

if __name__ == '__main__':
    main()
