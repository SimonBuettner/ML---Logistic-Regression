import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Read CSV-File:
df = pd.read_csv("flat_Price.csv")

# Returns the first 5 rows:
print(df.head())

X= df[["QM"]].values
Y = df[["Price"]].values

Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, random_state = 0, test_size = 0.25)

# prints train and test data with different colors
plt.scatter(Xtrain, Ytrain)
plt.scatter(Xtest, Ytest, color = "red")
plt.title("Data Points")
plt.show()

# assigns the QM as X-Axis and Price as Y-Axis
model = LinearRegression()
model.fit(Xtrain, Ytrain)

# Prints a predicted-line on basis of the blue dots of trainings-data
predicted = model.predict(Xtest)
plt.scatter(Xtest, Ytest, color = "red")
plt.plot(Xtest, predicted, color = "red")
plt.title("Predicted")
plt.show()