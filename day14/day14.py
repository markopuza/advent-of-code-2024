import re
from math import prod
from dataclasses import dataclass
from collections import defaultdict
from tqdm import tqdm

@dataclass
class Robot:
    pos: complex
    vel: complex

robots = []
n, m = 101, 103
ticks = 100
with open('input.txt') as f:
    for l in f.readlines():
        px, py, vx, vy = map(int, re.findall(r'-?\d+', l))
        robots.append(Robot(complex(px, py), complex(vx, vy)))

quadrants_cnt = defaultdict(int)
for r in robots:
    pos = r.pos + ticks * r.vel
    pos = complex(pos.real % n, pos.imag % m)
    # don't care about robots in the middle
    if pos.real != n // 2 and pos.imag != m // 2:
        quadrants_cnt[(pos.real < n // 2, pos.imag < m // 2)] += 1

def render_picture(ticks):
    pic = [['.' for _ in range(n)] for _ in range(m)]
    for r in robots:
        pos = r.pos + ticks * r.vel
        pic[int(pos.imag) % m][int(pos.real) % n] = '#'
    return [''.join(row) for row in pic]

def adhoc_stat(pic):
    return sum(row[i] != row[i+1] for row in pic for i in range(len(row) - 1))

result1 = prod(quadrants_cnt.values())
print(f'Part 1: {result1}')

christmas_time = min(tqdm(range(10000)), key=lambda t: adhoc_stat(render_picture(t)))
for row in render_picture(christmas_time):
    print(row)
print(f'Part 2: {christmas_time}')