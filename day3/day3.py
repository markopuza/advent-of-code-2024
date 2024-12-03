import re

MUL = r'mul\((\d{1,3}),(\d{1,3})\)'
DODONT = r"don't\(\).*?do\(\)"

with open('input.txt') as f:
    inp = f.read()

result1 = sum(int(x)*int(y) for x, y in re.findall(MUL, inp))
print(f'Part 1: {result1}')

inp = re.sub(DODONT, '', inp + 'do()', flags=re.DOTALL)
result2 = sum(int(x)*int(y) for x, y in re.findall(MUL, inp))
print(f'Part 2: {result2}')