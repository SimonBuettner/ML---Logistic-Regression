""" Giving an overview of Linear Regression """

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Read CSV-File:
DF = pd.read_csv("flat_Price.csv")

# Returns the first 5 rows:
print(DF.head())

X = DF[["QM"]].values
Y = DF[["Price"]].values

XTRAIN, XTEST, YTRAIN, YTEST = train_test_split(
    X, Y, test_size=0.25
)

# prints train and test data with different colors
plt.scatter(XTRAIN, YTRAIN)
plt.scatter(XTEST, YTEST, color="red")
plt.xlabel("QM")
plt.ylabel("Price")
plt.title("Data Points")
plt.show()

# assigns the QM as X-Axis and Price as Y-Axis
MODEL = LinearRegression()
MODEL.fit(XTRAIN, YTRAIN)

# Prints a predicted-line on basis of the blue dots of trainings-data
PREDICTED = MODEL.predict(XTEST)
plt.scatter(XTEST, YTEST, color="red")
plt.plot(XTEST, PREDICTED, color="blue")
plt.xlabel("QM")
plt.ylabel("Price")
plt.title("Predicted")
plt.show()
