from collections import Counter

with open('input.txt') as f:
    nums = [int(n) for n in f.read().split()]
    left, right = nums[::2], nums[1::2]

result1 = sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))
print(f'Part 1: {result1}')

cleft, cright = Counter(left), Counter(right)
result2 = sum(cleft[k] * k * cright[k] for k in cleft)
print(f'Part 2: {result2}')