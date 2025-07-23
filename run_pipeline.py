form simple_pipeline import simple_pipeline
X = [[1],[2],[3],[4],[5],[6]]
y = [[10,20,30,40,50,60]]


# Split the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
