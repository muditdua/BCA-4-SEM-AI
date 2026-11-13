graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'C': [[('J', 1)]],
    'D': [[('E', 1), ('F', 1)]],
}
h = {'A': 0, 'B': 5, 'C': 2, 'D': 4, 'E': 7, 'F': 9, 'G': 3, 'H': 6, 'J': 2}
best = {}
solved = set()
def cost(opt):
    return sum(c + h[n] for n, c in opt)
def ao(node):
    if node not in graph:
        solved.add(node)
        return
    while node not in solved:
        opt = min(graph[node], key=cost)
        best[node] = opt
        h[node] = cost(opt)
        todo = [n for n, c in opt if n not in solved]
        if not todo:
            solved.add(node)
        for n in todo:
            ao(n)
def show(node):
    if node in best:
        print(node, "->", " AND ".join(n for n, c in best[node]))
        for n, c in best[node]:
            show(n)
ao('A')
print("Cost of A:", h['A'])
print("Solution graph:")
show('A')