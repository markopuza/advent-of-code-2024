from copy import deepcopy
dirs = {'>': 1j, 'v': 1, '<': -1j, '^': -1}

with open('input.txt') as f:
    grid, moves = f.read().split('\n\n')
    grid = [l.strip() for l in grid.split('\n') if l]
    moves = ''.join(moves.replace('\n', '').strip())
grid = {complex(i, j): grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))}
orig_grid = deepcopy(grid)

ALREADY_CALLED_CACHE = set()
def make_a_move(dir, pos, grid, actually_move=True):
    global ALREADY_CALLED_CACHE
    if grid[pos] == '@':  # Restart cache
        ALREADY_CALLED_CACHE = set()
    if (dir, pos) in ALREADY_CALLED_CACHE:
        return True
    ALREADY_CALLED_CACHE.add((dir, pos))

    def swap():
        grid[pos], grid[dir + pos] = grid[dir + pos], grid[pos]

    match grid[dir + pos]:
        case '#':
            return False
        case '.':
            if actually_move:
                swap()
            return True
        case 'O':
            moved = make_a_move(dir, pos + dir, grid, actually_move)
            if actually_move and moved:
                swap()
            return moved
        case ']':
            moved = make_a_move(dir, pos + dir, grid, actually_move) and make_a_move(dir, pos + dir -1j, grid, actually_move)
            if actually_move and moved:
                swap()
            return moved
        case '[':
            moved = make_a_move(dir, pos + dir, grid, actually_move) and make_a_move(dir, pos + dir + 1j, grid, actually_move)
            if actually_move and moved:
                swap()
            return moved

def get_lanternfish(grid):
    return next(k for k, v in grid.items() if v == '@')

def gps_coor(pos):
    return int(pos.imag + 100*pos.real)

def print_grid(grid):
    for i in range(N):
        print(''.join(grid[complex(i, j)] for j in range(M)))

def expand_grid(grid):
    expanded = dict()
    subs = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}
    for k, v in grid.items():
        expanded[complex(k.real, 2*k.imag)], expanded[complex(k.real, 2*k.imag + 1)] = tuple(subs[v])
    return expanded

def make_moves(grid, moves):
    l = get_lanternfish(grid)
    for move in moves:
        if make_a_move(dirs[move], l, grid, actually_move=False):
            make_a_move(dirs[move], l, grid)
            l += dirs[move]


make_moves(grid, moves)
result1 = sum(gps_coor(k) for k, v in grid.items() if v == 'O')
print(f'Part 1: {result1}')

expanded_grid = expand_grid(orig_grid)
make_moves(expanded_grid, moves)
result2 = sum(gps_coor(k) for k, v in expanded_grid.items() if v == '[')
print(f'Part 2: {result2}')
