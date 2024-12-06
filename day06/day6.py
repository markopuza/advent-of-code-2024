from tqdm import tqdm

NXT = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
DIR = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

with open('input.txt') as f:
    maze = [list(l.strip()) for l in f.readlines()]
    n, m = len(maze), len(maze[0])

STUCK_CACHE = set()
def get_guards_path(maze):
    """Returns all visited positions, and a boolean indicator if the guard got stuck."""
    guard = '^'
    gx, gy = [(x, y) for x in range(n) for y in range(m) if maze[x][y] == guard][0]
    visited = {(gx, gy, guard)}

    while 0 <= gx < n and 0 <= gy < m:
        if (gx, gy, guard) in STUCK_CACHE:
            return None, True
        dx, dy = DIR[guard]
        if 0 <= gx + dx < n and 0 <= gy + dy < m and maze[gx + dx][gy + dy] == '#':
            guard = NXT[guard]
        else:
            gx += dx
            gy += dy
            if (gx, gy, guard) in visited:
                for gx, gy, guard in visited:
                    STUCK_CACHE.add((gx, gy, guard))
                return visited, True
            visited.add((gx, gy, guard))

    return visited, False

original_path = {(x, y) for x, y, _ in get_guards_path(maze)[0] if 0 <= x < n and 0 <= y < m}
result1 = len(original_path)
print(f'Part 1: {result1}')

result2 = 0
for i, j in tqdm(original_path, 'Guard walking'):
    if 0 <= i < n and 0 <= j < m and maze[i][j] == '.':
        maze[i][j] = '#'
        result2 += get_guards_path(maze)[1]
        maze[i][j] = '.'
print(f'Part 2: {result2}')