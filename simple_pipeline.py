from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class SimpleMLPipeline:
    def __init__(self):
        #STEP 1: Initialize the components of the pipeline
        self.scaler = StandardScaler()
        self.model = LinearRegression()