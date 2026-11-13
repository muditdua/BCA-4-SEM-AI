import random, math
random.seed(1)

def ga(new, fit, cross, mut, pop=60, gens=100):
    P = [new() for _ in range(pop)]
    for _ in range(gens):
        P.sort(key=fit, reverse=True)
        N = P[:2]
        while len(N) < pop:
            a = max(random.sample(P, 3), key=fit)
            b = max(random.sample(P, 3), key=fit)
            N += [mut(c) for c in cross(a, b)]
        P = N[:pop]
    return max(P, key=fit)

def cut(a, b):
    i = random.randint(1, len(a) - 1)
    return a[:i] + b[i:], b[:i] + a[i:]

print("1. Binary genes: maximize x^2, x in 0..1023")
val = lambda c: int("".join(map(str, c)), 2)
best = ga(lambda: [random.randint(0, 1) for _ in range(10)], lambda c: val(c) ** 2, cut,
          lambda c: [1 - g if random.random() < 0.02 else g for g in c])
print(best, "x =", val(best), "f =", val(best) ** 2)

print("\n2. Real-valued genes: minimize sum of squares")
def blend(a, b):
    r = random.random()
    return [r * x + (1 - r) * y for x, y in zip(a, b)], [(1 - r) * x + r * y for x, y in zip(a, b)]
best = ga(lambda: [random.uniform(-10, 10) for _ in range(5)], lambda c: -sum(g * g for g in c), blend,
          lambda c: [g + random.gauss(0, 0.5) if random.random() < 0.2 else g for g in c], gens=150)
print([round(g, 3) for g in best], "f =", round(sum(g * g for g in best), 5))

print("\n3. Permutation genes: shortest tour of 8 cities")
pts = [(0, 0), (2, 6), (5, 2), (6, 7), (8, 3), (3, 9), (9, 9), (1, 4)]
dist = lambda t: sum(math.dist(pts[t[i]], pts[t[(i + 1) % 8]]) for i in range(8))
def ox(a, b):
    i, j = sorted(random.sample(range(8), 2))
    mid = a[i:j]
    rest = [c for c in b if c not in mid]
    return rest[:i] + mid + rest[i:]
def swap(t):
    t = t[:]
    if random.random() < 0.2:
        i, j = random.sample(range(8), 2)
        t[i], t[j] = t[j], t[i]
    return t
best = ga(lambda: random.sample(range(8), 8), lambda t: -dist(t), lambda a, b: (ox(a, b), ox(b, a)), swap)
print(best, "length =", round(dist(best), 3))