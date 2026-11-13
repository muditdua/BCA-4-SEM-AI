A = 4
B = 3
target = 2
visited = []

def solve(a, b):
    if (a, b) in visited:
        return False
    visited.append((a, b))
    print(a, b)
    if a == target or b == target:
        print("Goal Reached")
        return True
    x = min(a, B - b)
    y = min(b, A - a)
    for na, nb in [(A, b), (a, B), (0, b), (a, 0), (a - x, b + x), (a + y, b - y)]:
        if solve(na, nb):
            return True
    return False

solve(0, 0)