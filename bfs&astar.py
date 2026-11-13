import heapq
graph = {'S': [('A', 1), ('B', 4)], 'A': [('B', 2), ('C', 5), ('D', 12)], 'B': [('C', 2)], 'C': [('D', 3), ('G', 7)], 'D': [('G', 2)], 'G': []}
h = {'S': 7, 'A': 6, 'B': 4, 'C': 3, 'D': 2, 'G': 0}
def best_first(start, goal):
    q = [(h[start], start, [start], 0)]
    seen = set()
    while q:
        _, n, path, cost = heapq.heappop(q)
        if n in seen:
            continue
        seen.add(n)
        if n == goal:
            return path, cost
        for m, c in graph[n]:
            if m not in seen:
                heapq.heappush(q, (h[m], m, path + [m], cost + c))
    return None, 0
def astar(start, goal):
    q = [(h[start], 0, start, [start])]
    best = {start: 0}
    while q:
        f, g, n, path = heapq.heappop(q)
        if n == goal:
            return path, g
        for m, c in graph[n]:
            ng = g + c
            if ng < best.get(m, 999):
                best[m] = ng
                heapq.heappush(q, (ng + h[m], ng, m, path + [m]))
    return None, 0
p, c = best_first('S', 'G')
print("Best First Search:", p, c)
p, c = astar('S', 'G')
print("A* Search:", p, c)