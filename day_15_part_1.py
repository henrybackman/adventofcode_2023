from icecream import ic

def add_hash(x, c):
    x += ord(c)
    x *= 17
    x %= 256
    return x

def main():
    res = 0
    with open('data/day15.data') as f:
        for row in f:
            codes = row.strip().split(',')
            for code in codes:
                x = 0
                for c in code:
                    x = add_hash(x, c)
                res += x
    ic(res)

if __name__ == '__main__':
    main()



#     The current value starts at 0.
#     The first character is H; its ASCII code is 72.
#     The current value increases to 72.
#     The current value is multiplied by 17 to become 1224.
#     The current value becomes 200 (the remainder of 1224 divided by 256).
#     The next character is A; its ASCII code is 65.
#     The current value increases to 265.
#     The current value is multiplied by 17 to become 4505.
#     The current value becomes 153 (the remainder of 4505 divided by 256).
#     The next character is S; its ASCII code is 83.
#     The current value increases to 236.
#     The current value is multiplied by 17 to become 4012.
#     The current value becomes 172 (the remainder of 4012 divided by 256).
#     The next character is H; its ASCII code is 72.
#     The current value increases to 244.
#     The current value is multiplied by 17 to become 4148.
#     The current value becomes 52 (the remainder of 4148 divided by 256).

# So, the result of running the HASH algorithm on the string HASH is 52.