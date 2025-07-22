from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
import pickle 

iris = load_iris()

X = iris.data #* 150 mau, moi mau co 4 dac trung

y = iris.target #* 0 = Setosa, 1 = Versicolor, 2 = Virginica

print("Tên các đặc trưng:", iris.feature_names)
print("Tên các lớp:", iris.target_names)
print("Dữ liệu đầu vào (X):")
print(X[:10])  # Hiển thị 5 dòng đầu tiên
print("\nNhãn đầu ra (y):")
print(y[:10])

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state= 0, test_size=0.2)

clf = DecisionTreeClassifier(max_depth=3, random_state=0)
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

filename = "Iris_classification.pkl"

with open(filename, "wb") as file:
    pickle.dump(clf, file)


