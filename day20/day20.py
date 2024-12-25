from tqdm import tqdm
import heapq
from collections import defaultdict

class Complex(complex):
    def __lt__(self, other):
        return abs(self) < abs(other)
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

with open('input.txt') as f:
    grid = {Complex(i, j): ch for i, row in enumerate(f.readlines()) for j, ch in enumerate(row)}

start = next(k for k in grid if grid[k] == 'S')
end = next(k for k in grid if grid[k] == 'E')

def get_costs(grid, start, end):
    costs = {start: 0}
    h = [(0, start)]
    while h:
        cost, pos = heapq.heappop(h)
        costs[pos] = cost
        if pos == end:
            return costs
        for ne in (pos + Complex(1, 0), pos + Complex(-1, 0), pos + Complex(0,1), pos + Complex(0,-1)):
            if ne in grid and ne not in costs and grid[ne] in '.SE':
                heapq.heappush(h, (cost + 1, ne))

def count_shortcuts(grid, start, end, max_shortcut, min_saving):
    shortcuts = 0
    costs = get_costs(grid, start, end)
    for k in tqdm(costs):
        for kk in costs:
            d = abs(k.imag - kk.imag) + abs(k.real - kk.real)
            if d <= max_shortcut:
                shortcuts += abs(costs[k] - costs[kk]) - d >= min_saving
    return shortcuts // 2

result1 = count_shortcuts(grid, start, end, 2, 100)
print(f'Part 1: {result1}')
result2 = count_shortcuts(grid, start, end, 20, 100)
print(f'Part 2: {result2}')