from functools import cmp_to_key

with open('input.txt') as f:
    lines = f.readlines()
    rules = {tuple(map(int, l.split('|'))) for l in lines if '|' in l}
    seqs = [list(map(int, l.split(','))) for l in lines if ',' in l]

def is_correct(seq):
    return all(seq.index(m) < seq.index(n) for m, n in rules if m in seq and n in seq)

def get_mid(seq):
     return seq[len(seq)//2]

def fix(seq):
    return sorted(seq, key=cmp_to_key(lambda x, y: -1*((x, y) in rules)))

result1 = sum(get_mid(s) for s in seqs if is_correct(s))
print(f'Part 1: {result1}')

result2 = sum(get_mid(fix(s)) for s in seqs if not is_correct(s))
print(f'Part 2: {result2}')
