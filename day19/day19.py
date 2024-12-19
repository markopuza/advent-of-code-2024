from functools import cache

patterns = []
with open('input.txt') as f:
    for l in f.readlines():
        if ',' in l:
            towels = l.strip().split(', ')
        elif l.strip():
            patterns.append(l.strip())
@cache
def ways_to_make(pattern):
    if pattern == '':
        return 1
    ways = 0
    for t in towels:
        if pattern.endswith(t):
            ways += ways_to_make(pattern[:-len(t)])
    return ways

result1 = sum(ways_to_make(p) > 0 for p in patterns)
print(f'Part 1: {result1}')

result2 = sum(ways_to_make(p) for p in patterns)
print(f'Part 2: {result2}')