from collections import defaultdict

with open('input.txt') as f:
    grid = [l.strip() for l in f.readlines() if l]
n, m = len(grid), len(grid[0])

antennas = defaultdict(set)
for i, row in enumerate(grid):
    for j, x in enumerate(row):
        if x != '.':
            antennas[x].add(complex(i, j))

def antiantennas(depth=(1, 1)):
    def get(a, b):
        for i in range(depth[0], depth[0] + depth[1]):
            ant = a + (a - b)*i
            if 0 <= ant.real < n and 0 <= ant.imag < m:
                yield ant
            else:
                break
    return {
        k: {ant for a in antennas[k] for b in antennas[k] for ant in get(a, b) if a != b}
        for k in antennas
    }

result1 = len(set.union(*antiantennas().values()))
print(result1)

result2 = len(set.union(*antiantennas((0, m+n)).values()))
print(result2)