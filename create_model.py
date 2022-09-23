import joblib
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
x = iris.data
y = iris.target

tree = DecisionTreeClassifier()
tree.fit(x,y)
joblib.dump(tree, "./model.pkl")
