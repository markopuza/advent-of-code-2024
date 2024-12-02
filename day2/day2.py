with open('input.txt') as f:
    reports = [list(map(int, l.split())) for l in f.readlines()]

def safe(report):
    return any(all(x - y in diffs for x, y in zip(report, report[1:])) for diffs in ({1,2,3}, {-1,-2,-3}))

result1 = sum(safe(r) for r in reports)
print(f'Part 1: {result1}')

def safe_with_tolerance(report):
    return any(safe(report[:i] + report[i+1:]) for i in range(len(report)))

result2 = sum(safe_with_tolerance(r) for r in reports)
print(f'Part 2: {result2}')
