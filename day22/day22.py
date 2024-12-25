from collections import Counter
from queue import deque
from functools import cache 

with open('input.txt') as f:
    nums = list(map(int, f.readlines()))

MOD = 16777216

@cache
def nxt(n):
    n ^= (n << 6)
    n %= MOD
    n ^= (n >> 5)
    n %= MOD
    n ^= (n << 11)
    return n % MOD

def nxt_pwr(n, p):
    for _ in range(p):
        n = nxt(n)
    return n

def get_counter(n, p):
    cnter = Counter()
    curr = n % 10
    diffs = deque([])
    for _ in range(p):
        next = nxt(n)
        nxtd = next % 10
        diffs.append(nxtd - curr)
        if len(diffs) > 4:
            diffs.popleft()
        if len(diffs) == 4:
            k = tuple(diffs)
            if k not in cnter:
                cnter[k] = nxtd
        n, curr = next, nxtd
    return cnter

result1 = sum(nxt_pwr(n, 2000) for n in nums)
print(f'Part 1: {result1}')

c = Counter()
for n in nums:
    c += get_counter(n, 2000)
result2 = max(c.values())
print(f'Part 2: {result2}')