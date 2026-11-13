import math

def tsp(d):
    n = len(d)
    memo = {}

    def go(mask, cur):
        if mask == (1 << n) - 1:
            return d[cur][0], [0]
        if (mask, cur) in memo:
            return memo[(mask, cur)]
        best = (math.inf, [])
        for nxt in range(n):
            if not mask & (1 << nxt):
                c, p = go(mask | (1 << nxt), nxt)
                c += d[cur][nxt]
                if c < best[0]:
                    best = (c, [nxt] + p)
        memo[(mask, cur)] = best
        return best

    c, p = go(1, 0)
    return c, [0] + p

dist = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
cost, path = tsp(dist)
print("Optimal Cost:", cost)
print("Optimal Path:", " -> ".join(map(str, path)))