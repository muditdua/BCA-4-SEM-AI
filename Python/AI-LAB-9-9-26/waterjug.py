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

    # Fill A
    if solve(A, b):
        return True

    # Fill B
    if solve(a, B):
        return True

    # Empty A
    if solve(0, b):
        return True

    # Empty B
    if solve(a, 0):
        return True

    # Pour A -> B
    x = min(a, B - b)

    if solve(a - x, b + x):
        return True

    # Pour B -> A
    x = min(b, A - a)

    if solve(a + x, b - x):
        return True

    return False


solve(0, 0)