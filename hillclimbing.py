def f(x):
    return -x * x + 20 * x + 5

def neighbours(x):
    return [x + 1, x - 1, x + 2, x - 2, x + 3, x - 3]

def hill_climbing(x):
    steps = 0
    while True:
        moved = False
        for n in neighbours(x):
            if f(n) > f(x):
                x = n
                moved = True
                steps += 1
                print("  moved to", x, "f =", f(x))
                break
        if not moved:
            return x, steps

def steepest_ascent(x):
    steps = 0
    while True:
        best = max(neighbours(x), key=f)
        if f(best) <= f(x):
            return x, steps
        x = best
        steps += 1
        print("  moved to", x, "f =", f(x))

start = -7
print("Simple Hill Climbing, start =", start)
x, s = hill_climbing(start)
print("Best x =", x, "f(x) =", f(x), "steps =", s)

print("\nSteepest Ascent Hill Climbing, start =", start)
x, s = steepest_ascent(start)
print("Best x =", x, "f(x) =", f(x), "steps =", s)