from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class SimpleMLPipeline:
    def __init__(self):
        #STEP 1: Initialize the components of the pipeline
        self.scaler = StandardScaler()
        self.model = LinearRegression()

    def train(self, X_train, y_train):
        #STEP 2: Fit the scaler and transform the training features
        X_train = self.scaler.fit_transform(X_train)

        #STEP 3: Train the regression model on th scaled data
        self.model.fit(X_scaled, y_train)
    
    def predict(self, X):
        # STEP 6: Transform input and return prediction
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)

    def model_params(self):
        return self.model.intercept_, self.model.coef_
