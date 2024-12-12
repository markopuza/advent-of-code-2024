with open('input.txt') as f:
    grid = [l.strip() for l in f.readlines() if l]
n, m = len(grid), len(grid[0])

def neighbours(x, y):
    for i, j in [(x-1, y), (x+1, y), (x,y-1), (x,y+1)]:
        if 0 <= i < n and 0 <= j < m:
            yield i, j

def region_metrics(x, y, grid, visited):
    if visited[x][y]:
        return 0, 0, 0
    visited[x][y] = True
    symbol = grid[x][y]
    perimeter, area, sides = 0, 0, 0
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        same_neighs = [(nx, ny) for nx, ny in neighbours(cx, cy) if grid[nx][ny] == symbol]
        area += 1
        perimeter += 4 - len(same_neighs)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (cx + dx, cy + dy) not in same_neighs:
                if (cx + dy, cy + dx) not in same_neighs:
                    sides += 1
                else:
                    sides += 0 <= cx + dy + dx < n and 0 <= cy + dx + dy < m and grid[cx + dy + dx][cy + dx + dy] == symbol

        for nx, ny in neighbours(cx, cy):
            if grid[nx][ny] == symbol and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = True
    return area, perimeter, sides

visited = [[False for _ in range(m)] for _ in range(n)]
result1, result2 = 0, 0
for x in range(n):
    for y in range(m):
        a, p, s = region_metrics(x, y, grid, visited)
        result1 += a*p
        result2 += a*s
print(f'Part 1: {result1}')
print(f'Part 2: {result2}')