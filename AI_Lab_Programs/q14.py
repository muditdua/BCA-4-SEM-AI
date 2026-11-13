import random
from sklearn.neural_network import MLPClassifier
random.seed(1)

pS = {1: 0.01, 0: 0.4}
pW = {(1, 1): 0.99, (1, 0): 0.9, (0, 1): 0.8, (0, 0): 0.0}

def sample():
    r = int(random.random() < 0.2)
    s = int(random.random() < pS[r])
    w = int(random.random() < pW[(s, r)])
    return r, s, w

def exact(s, w):
    p = {}
    for r in (0, 1):
        pr = 0.2 if r else 0.8
        ps = pS[r] if s else 1 - pS[r]
        pw = pW[(s, r)] if w else 1 - pW[(s, r)]
        p[r] = pr * ps * pw
    return p[1] / (p[0] + p[1])

data = [sample() for _ in range(20000)]
X = [[s, w] for r, s, w in data]
y = [r for r, s, w in data]
ann = MLPClassifier(hidden_layer_sizes=(8,), max_iter=2000, random_state=1).fit(X, y)

print("P(Rain=1 | Sprinkler, WetGrass)")
print("Sprinkler WetGrass   Exact   ANN")
for s in (0, 1):
    for w in (0, 1):
        print(f"    {s}         {w}       {exact(s, w):.3f}   {ann.predict_proba([[s, w]])[0][1]:.3f}")