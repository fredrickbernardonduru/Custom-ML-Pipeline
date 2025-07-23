form simple_pipeline import simple_pipeline
X = [[1],[2],[3],[4],[5],[6]]
y = [[10,20,30,40,50,60]]


# Split the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#Create and run the pipeline
pipeline = simple_pipeline()
pipeline.train(X_train, y_train)

#Evaluate performance
print("Train R² Score:", pipeline.evaluate(X_train, y_train))
print("Train R² Score:", pipeline.evaluate(X_test, y_test))

#Predict on new data
predictions = pipeline.predict(X_test)
print("Predictions on test set:", predictions)


# Print model parameters
intercept, coef = pipeline.model_params()
print("Model Intercept:", intercept)
print("Model Coefficients:", coef)
