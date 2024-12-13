from math import gcd
from tqdm import tqdm
import re

class Machine():
    def __init__(self, A, B, prize, a_cost=3, b_cost=1, max_presses=100):
        self.A = A
        self.B = B
        self.prize = prize
        self.a_cost = a_cost
        self.b_cost = b_cost
        self.max_presses = max_presses

    def min_tokens_to_win(self):
        g0, g1 = gcd(self.A[0], self.B[0]), gcd(self.A[1], self.B[1])
        if self.prize[0] % g0 or self.prize[1] % g1:
            return float('inf')
        
        y = (self.A[1] * self.prize[0] - self.A[0] * self.prize[1]) / (self.A[1] * self.B[0] - self.A[0] * self.B[1])
        x = (self.prize[0] - y*self.B[0]) / self.A[0]
        if y != int(y) or x != int(x):
            return float('inf')

        if 0 <= x <= self.max_presses and 0 <= y <= self.max_presses:
            return int(self.a_cost*x + self.b_cost*y)


    def __repr__(self):
        return f'A: {self.A}, B: {self.B} (prize: {self.prize})'
    
    def __str__(self):
        return self.__repr__()

machines = []
with open('input.txt') as f:
    for m in f.read().split('\n\n'):
        ax, ay = map(int, re.search(r"X\+(\d+),\s*Y\+(\d+)", m.split('\n')[0]).groups())
        bx, by = map(int, re.search(r"X\+(\d+),\s*Y\+(\d+)", m.split('\n')[1]).groups())
        px, py = map(int, re.search(r"X\=(\d+),\s*Y\=(\d+)", m.split('\n')[2]).groups())
        machines.append(Machine((ax, ay), (bx, by), (px, py)))

result1 = sum(filter(lambda x: x is not None and x < float('inf'), [m.min_tokens_to_win() for m in tqdm(machines)]))
print(f'Part 1: {result1}')

for m in machines:
    m.prize = (m.prize[0] + 10000000000000, m.prize[1] + 10000000000000)
    m.max_presses = float('inf')
result2 = sum(filter(lambda x: x is not None and x < float('inf'), [m.min_tokens_to_win() for m in tqdm(machines)]))
print(f'Part 1: {result2}')