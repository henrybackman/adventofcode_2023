from icecream import ic
import regex

def get_data():
    data = []
    with open('data/day2.data') as f:
        for row in f:
            data.append(row.strip())
            
    return data

def main():
    data = get_data()

    limits = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    sum_of_valid_game_ids = 0
    for game_data in data:
        is_valid_game = True
        parts = game_data.split(': ')
        picks = parts[1].split('; ')
        color_counts = []
        for pick in picks:
            cube_counts = pick.split(', ')
            for cube_count in cube_counts:
                count = int(cube_count.split(' ')[0])
                color = cube_count.split(' ')[1]
                if limits[color] and count > limits[color]:
                    is_valid_game = False
                    break
            
            if not is_valid_game:
                break

        if is_valid_game:
            id = int(regex.search(r'(?<=^Game )\d*', parts[0]).group())
            sum_of_valid_game_ids += id
    ic(sum_of_valid_game_ids)

if __name__ == '__main__':
    main()