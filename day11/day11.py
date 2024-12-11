from tqdm import tqdm
from collections import Counter
from copy import deepcopy

blinks = 25
with open('input.txt') as f:
    stones = Counter(map(int, f.read().split()))

def evolve(n):
    if n == 0:
        return [1]
    l = len(str(n))
    if l & 1:
        return [n*2024]
    return [int(str(n)[:l//2]), int(str(n)[l//2:])]

def apply_blinks(stones, blinks=25):
    for _ in tqdm(range(blinks)):
        for k, v in list(stones.items()):
            stones[k] -= v
            for nk in evolve(k):
                stones[nk] += v
    return stones

result1 = sum(apply_blinks(deepcopy(stones)).values())
print(f'Part 1: {result1}')

result2 = sum(apply_blinks(deepcopy(stones), blinks=75).values())
print(f'Part 2: {result2}')