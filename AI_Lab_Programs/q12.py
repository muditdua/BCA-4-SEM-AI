from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
sc = StandardScaler().fit(Xtr)
Xtr, Xte = sc.transform(Xtr), sc.transform(Xte)

ann = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=42).fit(Xtr, ytr)
pred = ann.predict(Xte)
print("Accuracy:", round(accuracy_score(yte, pred) * 100, 2), "%")
print("Confusion matrix:\n", confusion_matrix(yte, pred))
print("Prediction for [5.1, 3.5, 1.4, 0.2]:", ["setosa", "versicolor", "virginica"][ann.predict(sc.transform([[5.1, 3.5, 1.4, 0.2]]))[0]])