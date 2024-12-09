from copy import deepcopy
import heapq
from itertools import chain

with open('input.txt') as f:
    disk_map = list(map(int, f.read()))
memory = list(chain.from_iterable([[None if i&1 else i//2] * n for i, n in enumerate(disk_map)]))

def compress(memory):
    memory = deepcopy(memory)
    l, r = 0, len(memory) - 1
    while r > l:
        if memory[l] is None:
            while memory[r] is None:
                r -= 1
            if r > l:
                memory[l], memory[r] = memory[r], None
        l += 1
    return memory

def _get_free_spaces(memory):
    free_spaces = [[] for _ in range(10)]
    i = 0
    while i < len(memory):
        if memory[i] is None:
            # [i, j) is a continous empty space interval
            j = next(j for j in range(i + 1, len(memory)) if memory[j] is not None)
            heapq.heappush(free_spaces[j - i], (i, j))
            i = j
        else:
            i += 1
    return free_spaces

def compress2(memory):
    memory = deepcopy(memory)
    free_spaces = _get_free_spaces(memory)

    r = len(memory) - 1
    while r > 0:
        if memory[r] is None:
            r -= 1
            continue
        # (l, r] is a continuous interval with particular memory id
        l = next(l for l in range(r, -2, -1) if l == -1 or memory[l] != memory[r])
        length = r - l

        newl, newr, gap_size = min(
                [(*free_spaces[g][0], g) for g in range(r-l, 10) if free_spaces[g]],
                default=(float('inf'), float('inf'), None)
            ) # peek
        if newl < l + 1:
            for k in range(length): # place
                memory[newl + k], memory[l + 1 + k] = memory[l + 1 + k], memory[newl + k]
            # update heap
            heapq.heappop(free_spaces[gap_size])
            if length < gap_size:
                heapq.heappush(free_spaces[gap_size - length], (newl + length, newr))
        r = l
    return memory

def checksum(memory):
    return sum(i * n for i, n in enumerate(memory) if n is not None)

result1 = checksum(compress(memory))
print(f'Part 1: {result1}')

result2 = checksum(compress2(memory))
print(f'Part 2: {result2}')