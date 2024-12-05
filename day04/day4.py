DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
WORD = 'XMAS'

with open('input.txt') as f:
    grid = [l.strip() for l in f.readlines()]
n, m = len(grid), len(grid[0])

result1 = 0
for i in range(n):
    for j in range(m):
        for dx, dy in DIRS:
            coors = [(i + k*dx, j + k*dy) for k in range(len(WORD))]
            if all(0 <= cx < n and 0 <= cy < m for cx, cy in coors):
                result1 += ''.join(grid[cx][cy] for cx, cy in coors) == WORD

print(f'Part 1: {result1}')

result2 = 0
for i in range(1, n-1):
    for j in range(1, n-1):
        if grid[i][j] == 'A':
            if ''.join([grid[i-1][j-1], grid[i+1][j+1]]) in ['MS', 'SM']:
                result2 += ''.join([grid[i-1][j+1], grid[i+1][j-1]]) in ['MS', 'SM']
        
print(f'Part 2: {result2}')