import networkx as nx
from tqdm import tqdm
from collections import defaultdict

graph = defaultdict(set)
with open('input.txt') as f:
    for l in f.readlines():
        a, b = l.strip().split('-')
        graph[a].add(b)
        graph[b].add(a)
    
G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)


def contains_3clique(graph, a, b, c):
    return {a, b}.issubset(graph[c]) and {a, c}.issubset(graph[b]) and {b, c}.issubset(graph[a])

result1 = 0
nodes = sorted(list(graph.keys()))
for i, a in tqdm(enumerate(nodes)):
    for j, b in enumerate(nodes[i+1:], i+1):
        for c in nodes[j+1:]:
            if 't' in (a[0] + b[0] + c[0]) and contains_3clique(graph, a, b, c):
                result1 += 1
print(f'Part 1: {result1}')

cliques = list(nx.find_cliques(G))
result2 = ','.join(sorted(max(cliques, key=len)))
print(f'Part 2: {result2}')