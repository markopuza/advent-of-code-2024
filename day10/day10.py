with open('input.txt') as f:
    grid = [list(map(int, l.strip())) for l in f.readlines() if l]
n, m = len(grid), len(grid[0])

scores = [[int(grid[i][j] == 9) for j in range(m)] for i in range(n)]
nines = [[{(i, j)} if grid[i][j] == 9 else set() for j in range(m)] for i in range(n)]
for k in range(8, -1, -1):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == k:
                for ni, nj in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                    if 0 <= ni < n  and 0 <= nj < m and grid[ni][nj] == k + 1:
                        scores[i][j] += scores[ni][nj]
                        nines[i][j] |= nines[ni][nj]

result1 = sum(len(nines[i][j]) for i in range(n) for j in range(m) if grid[i][j] == 0)
print(f'Part 1: {result1}')

result2 = sum(scores[i][j] for i in range(n) for j in range(m) if grid[i][j] == 0)
print(f'Part 2: {result2}')