from tqdm import tqdm

add = lambda a, b, *rest: (a+b, *rest)
mul = lambda a, b, *rest: (a*b, *rest)
concat = lambda a, b, *rest: (int(f'{a}{b}'), *rest)

with open('input.txt') as f:
    rows = [(int(p[0]), list(map(int, p[1].split()))) for l in f.readlines() if (p := l.split(':'))]

def is_possible(res, nums, ops=[add, mul]):
    if nums[0] > res:
        return False
    if len(nums) == 1:
        return res == nums[0]
    return any(is_possible(res, op(*nums), ops) for op in ops)

result1 = sum(res for res, nums in tqdm(rows) if is_possible(res, nums))
print(f'Part 1: {result1}')

result2 = sum(res for res, nums in tqdm(rows) if is_possible(res, nums, [add, mul, concat]))
print(f'Part 2: {result2}')