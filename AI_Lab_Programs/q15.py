import numpy as np
np.random.seed(1)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])
W1, b1 = np.random.randn(2, 4), np.zeros((1, 4))
W2, b2 = np.random.randn(4, 1), np.zeros((1, 1))
sig = lambda z: 1 / (1 + np.exp(-z))
lr = 0.5

for e in range(1, 10001):
    a1 = sig(X @ W1 + b1)
    a2 = sig(a1 @ W2 + b2)
    d2 = (a2 - y) * a2 * (1 - a2)
    d1 = d2 @ W2.T * a1 * (1 - a1)
    W2 -= lr * a1.T @ d2 / 4
    b2 -= lr * d2.mean(0)
    W1 -= lr * X.T @ d1 / 4
    b1 -= lr * d1.mean(0)
    if e % 2000 == 0 or e == 1:
        print("Epoch", e, "loss =", round(float(np.mean((y - a2) ** 2)), 6))

out = sig(sig(X @ W1 + b1) @ W2 + b2)
print("\nInput  Target  Output  Predicted")
for i in range(4):
    print(X[i], "  ", y[i][0], "    ", round(float(out[i][0]), 4), "  ", int(out[i][0] > 0.5))