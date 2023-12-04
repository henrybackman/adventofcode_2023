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

    sum_of_game_powers = 0
    for game_data in data:
        limits = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        parts = game_data.split(': ')
        picks = parts[1].split('; ')
        for pick in picks:
            cube_counts = pick.split(', ')
            for cube_count in cube_counts:
                count = int(cube_count.split(' ')[0])
                color = cube_count.split(' ')[1]
                if color in limits:
                    limits[color] = max(limits[color], count)
        game_power = limits['red'] * limits['green'] * limits['blue']
        sum_of_game_powers += game_power
    ic(sum_of_game_powers)

if __name__ == '__main__':
    main()