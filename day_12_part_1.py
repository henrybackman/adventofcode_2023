from icecream import ic
from dataclasses import dataclass, field
import regex as re

def get_perms(permutations, springs, counts):
    # ic(permutations, springs, counts)
    if len(springs) == 0 and len(counts) > 0:
        # ic('no springs left, but counts left')
        # ic(permutations, springs, counts)
        return permutations

    if len(counts) == 0 and len(springs) > 0:
        # if there's any fixed positions left, return 0
        for spring in springs:
            if '#' in spring:
                # ic('no counts left, but # still in springs')
                # ic(permutations, springs, counts)
                return permutations
        # otherwise this is valid, probably?
        permutations += 1
        # ic('probably valid?')
        # ic(permutations, springs, counts)
        return permutations
   
    # this is the valid end state
    if len(counts) == 0 and len(springs) == 0:
        # ic('valid end state')
        # ic(permutations, springs, counts)
        permutations += 1
        return permutations
    
    rest_springs = springs[1:] if len(springs) > 1 else []
    rest_counts = counts[1:] if len(counts) > 1 else []

    # if the spring is shorter than the count, try the next spring for the count
    if len(springs[0]) < counts[0]:
        return get_perms(permutations, rest_springs, counts)
    
    # if the spring starts with a fixed position, remove count, add empty if needed and then continue
    if springs[0].startswith('#'):
        # reduce count by one and remove fixed position
        fixed_springs = [springs[0][counts[0]:]] + rest_springs
        if fixed_springs[0].startswith('#'):
            # ic('cannot have # where empty should go')
            # ic(permutations, springs, counts)
            return permutations # cannot have empty here
        if len(fixed_springs[0]) > 0:
            fixed_springs[0] = fixed_springs[0][1:] # adding the empty space
        if len(fixed_springs[0]) == 0:
            fixed_springs = rest_springs # remove the spring if empty 
        counts = counts[1:]
        return get_perms(permutations, fixed_springs, rest_counts)
    
    # if the spring is a wild card, it can either be a fixed position or empty
    # empty
    empty_springs = [springs[0][1:]] + rest_springs # take the first character off
    empty_counts = counts[0:] # counts are not modified
    permutations = get_perms(permutations, empty_springs, empty_counts)

    # fixed position, just replace the character with a #
    fixed_springs = ['#' + springs[0][1:]] + rest_springs
    permutations = get_perms(permutations, fixed_springs, counts)
    return permutations
 

def main():
    permutations = 0
    with open('data/day12.data') as f:
        for row in f:
            springs, counts = row.split(' ')
            counts = [int(counts) for counts in counts.split(',')]
            # remove empty spaces
            springs = re.split(r'\.+', springs)
            springs = [spring for spring in springs if spring != '']
            perms = get_perms(0, springs, counts)
            # ic('_______________________________')
            # ic(springs, counts, perms)
            # ic('_______________________________')
            permutations += perms
            
    ic(permutations)

if __name__ == '__main__':
    main()

# 7273 too high