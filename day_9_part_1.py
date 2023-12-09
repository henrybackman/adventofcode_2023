from icecream import ic


def get_differences(nums):
    differences = []
    all_zeros = True
    for i in range(1, len(nums)):
        difference = nums[i] - nums[i-1]
        if all_zeros and difference != 0:
            all_zeros = False
        differences.append(nums[i] - nums[i-1])
    return differences, all_zeros

def main():
    ms = []
    with open('data/day9.data') as f:
        for row in f:
            m = []
            nums = [int(x) for x in row.split()]
            m.append(nums)
            cur = nums
            while True:
                differences, all_zeros = get_differences(cur)
                m.append(differences)
                if all_zeros:
                    break
                cur = differences
            ms.append(m)
    
    ans = 0
    for m in ms:
        i = len(m) - 1
        cur = m[i]
        cur.append(0)
        while i > 0:
            next = m[i-1]
            next.append(next[-1] + cur[-1])
            i -= 1
            cur = next
            
        ans += cur[-1]
    ic(ans)

if __name__ == '__main__':
    main()