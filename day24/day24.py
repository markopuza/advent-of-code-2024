from itertools import permutations
from random import randint
fs = dict()

with open('input.txt') as f:
    for l in f.readlines():
        if ':' in l:
            name, val = l.strip().split(': ')
            fs[name] = eval(f'lambda: {val}')
        elif '->' in l:
            a, op, b, _, res = l.strip().split()
            O = {'AND': '&', 'OR': '|', 'XOR': '^'}[op]
            fs[res] = eval(f'lambda: fs["{a}"]() {O} fs["{b}"]()')

def execute_adder(fs):
    zs = sorted([k for k in fs.keys() if k.startswith('z')])
    return sum((1 << i)*fs[k]() for i, k in enumerate(zs))

def evaluate_adder(fs, max_bit=45, tests=3):
    """Returns true if the adder is probably correct"""
    for _ in range(tests):
        x, y = 0, 0
        for i in range(max_bit):
            xbit, ybit = randint(0, 1), randint(0, 1)
            x += i << xbit
            y += i << ybit
            fs['x' + str(i).zfill(2)] = lambda: xbit
            fs['y' + str(i).zfill(2)] = lambda: ybit
        if execute_adder(fs) != x + y:
            return False
    return True

result1 = execute_adder(fs)
print(f'Part 1: {result1}')
