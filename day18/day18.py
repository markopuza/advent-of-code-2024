with open('input.txt') as f:
    coors = [complex(*map(int, l.split(','))) for l in f.readlines()]
n = 70
bytes = 1024

def get_shortest_path(n, coors, bytes):
    obstacles = set(coors[:bytes])
    l, row = 0, {complex(0, 0)}
    visited = set()
    while row:
        visited |= row
        if complex(n, n) in row:
            return l
        row = set.union(*[{y for y in {x+1, x-1, x+1j, x-1j} if 0 <= y.real <= n and 0 <= y.imag <= n} for x in row]) - visited - obstacles
        l += 1
    return None

result1 = get_shortest_path(n, coors, bytes)
print(f'Part 1: {result1}')

l, r = 0, len(coors) - 1
while r - l > 1:
    mid = (r + l) // 2
    if get_shortest_path(n, coors, mid) is None:
        r = mid
    else:
        l = mid
result2 = f'{int(coors[l].real)},{int(coors[l].imag)}'
print(f'Part 2: {result2}')