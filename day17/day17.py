from random import randint
from math import gcd

class Computer:
    def a(self, val=None):
        if val is None:
            return self.registers[0]
        self.registers[0] = val

    def b(self, val=None):
        if val is None:
            return self.registers[1]
        self.registers[1] = val

    def c(self, val=None):
        if val is None:
            return self.registers[2]
        self.registers[2] = val

    def __init__(self, a, b, c):
        self.registers = [a, b, c]
        self.ptr = 0

    def combo(self, val):
        match val:
            case _ if 0 <= val <= 3:
                return val
            case 4:
                return self.a()
            case 5:
                return self.b()
            case 6:
                return self.c()

    def run_program(self, program):
        self.ptr = 0
        while self.ptr < len(program):
            operand = program[self.ptr + 1]
            match program[self.ptr]:
                case 0: # adv
                    self.a(self.a() // (1 << self.combo(operand)))
                case 1: # bxl
                    self.b(self.b() ^ operand)
                case 2: # bst
                    self.b(self.combo(operand) % 8)
                case 3: # jnz
                    if self.a():
                        self.ptr = operand
                        continue
                case 4: # bxc
                    self.b(self.b() ^ self.c())
                case 5: # out
                    yield self.combo(operand) % 8
                case 6: # bdv
                    self.b(self.a() // (1 << self.combo(operand)))
                case 7: # cdv
                    self.c(self.a() // (1 << self.combo(operand)))
            self.ptr += 2


with open('input.txt') as f:
    a, b, c, program = 0, 0, 0, []
    for l in f.readlines():
        if 'A: ' in l:
            a = int(l.split(': ')[-1])
        if 'B: ' in l:
            b = int(l.split(': ')[-1])
        if 'C: ' in l:
            c = int(l.split(': ')[-1])
        if 'Program: ' in l:
            program = list(map(int, l.split(': ')[-1].split(',')))

comp = Computer(a, b, c)
result1 = ','.join(map(str, comp.run_program(program)))
print(f'Part 1: {result1}')

valid = [0]
for l in range(len(program)):
    valid = [
        nw
        for n in valid 
        for i in range(8) # only the last three bits matter for the next computer output
        if list(Computer((nw := 8*n + i), 0, 0).run_program(program))[-l-1:] == program[-l-1:]
    ]
result2 = min(valid)
print(f'Part 2: {result2}')