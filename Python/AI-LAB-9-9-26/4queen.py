N = 4

def safe(b, r, c):
    for i in range(r):
        if b[i] == c or abs(b[i] - c) == r - i:
            return False
    return True

def solve(b, r):
    if r == N:
        for x in b:
            print(" ".join("Q" if x == c else "." for c in range(N)))
        print()
        return
    for c in range(N):
        if safe(b, r, c):
            b[r] = c
            solve(b, r + 1)

solve([-1] * N, 0)