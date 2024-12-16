from collections import defaultdict
from dataclasses import dataclass
import heapq

@dataclass(frozen=True)
class Pos():
    cost: int
    pos: complex
    dir: complex
    rots: int

    def __lt__(self, other):
        return self.cost < other.cost

with open('input.txt') as f:
    grid = {complex(i, j): x for i, row in enumerate([l.strip() for l in f.readlines() if l]) for j, x in enumerate(row)}

def get_shortest_path_cost(grid):
    start = next(x for x in grid if grid[x] == 'S')
    end = next(x for x in grid if grid[x] == 'E')
    costs = dict()
    h = [Pos(0, start, 1j, 0)]
    prev = defaultdict(list)

    def add_to_prev(nxt, curr):
        k = (nxt.pos, nxt.dir)
        if k in prev:
            desired_c = prev[(nxt.pos, nxt.dir)][0][2]
            if nxt.cost == desired_c:
                prev[k].append((curr.pos, curr.dir, nxt.cost))
            elif nxt.cost < desired_c:
                prev[k] = [(curr.pos, curr.dir, nxt.cost)]
        else:
            prev[k].append((curr.pos, curr.dir, nxt.cost))

    while h:
        curr = heapq.heappop(h)

        if (curr.pos, curr.dir) in costs and costs[(curr.pos, curr.dir)] < curr.cost:
            continue
        costs[(curr.pos, curr.dir)] = curr.cost

        if curr.pos == end:
            return curr.cost, prev, end
        if grid[curr.pos + curr.dir] in 'E.':
            forward = Pos(curr.cost + 1, curr.pos + curr.dir, curr.dir, 0)
            heapq.heappush(h, forward)
            add_to_prev(forward, curr)
        if curr.rots < 2:
            cw =  Pos(curr.cost + 1000, curr.pos, curr.dir * -1j, curr.rots + 1)
            ccw = Pos(curr.cost + 1000, curr.pos, curr.dir * 1j, curr.rots + 1)
            heapq.heappush(h, cw)
            heapq.heappush(h, ccw)
            add_to_prev(cw, curr)
            add_to_prev(ccw, curr)

result1, prev, end = get_shortest_path_cost(grid)
print(f'Part 1: {result1}')

stack = [k for k in prev if k[0] == end]
goodpos = set(stack)
while stack:
    curr = stack.pop()
    goodpos.add(curr)
    for p, d, c in prev[curr]:
        if (p, d) not in goodpos:
            stack.append((p, d))

result2 = len(set(k[0] for k in goodpos))
print(f'Part 2: {result2}')