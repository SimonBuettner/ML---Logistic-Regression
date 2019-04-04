import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from helper import plot_classifier

# Read CSV-File:
df = pd.read_csv("test.csv")

# Returns the first 5 rows:
print(df.head())

# Defines incoming data monthlySport and monthlyHealthyFood
# Variable y defines the color, NOT the axis
X = df[["monthlySport", "monthlyHealthyFood"]].values
y = df["desease"].values

# Splitting the Set in Test and Train Data:
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size = 0.25)


# Would change the scale between x- and y-axis. But not really necessary,
# since the scale is actually the same
#scaler = StandardScaler()
#monthlyHealthyFood")scaler.fit(XTrain)
#XTrain = scaler.transform(XTrain)
#XTest = scaler.transform(XTest)


# XTrain[:, 0]: gets all data of the first column (monthlySport) for the X-Axis
# XTrain[:, 1]: gets all data of the second column (monthlyHealthyFood) for the Y-Axis
# c=yTrain: Defines the color
plt.scatter(XTrain[:, 0], XTrain[:, 1], c=yTrain)
plt.xlabel("Number of Sport activities per month")
plt.ylabel("Number of eating healthy per month")
plt.title("TRAINING DATA")
plt.show()

# Defines Logistic Regression Model:
model = LogisticRegression()

# Trains the model 
model.fit(XTrain, yTrain)
yPredicted = model.predict(XTest)

print("Die Vorhersagegenauigkeit entspricht: ")
print(100 * model.score(XTest, yTest), "%")

# Prints diagram of the real test Data:
plt.scatter(XTest[:, 0], XTest[:, 1], c=yTest)
plt.xlabel("Number of Sport activities per month")
plt.ylabel("Number of eating healthy per month")
plt.title("REAL TEST DATA")
plt.show()

# Prints diagram of the Prediction:
plt.scatter(XTest[:, 0], XTest[:, 1], c=yPredicted)
plt.xlabel("Number of Sport activities per month")
plt.ylabel("Number of eating healthy per month")
plt.title("PREDICTED DATA")
plt.show()

# Prints diagramm of the real test Data with seperator
plot_classifier(model, XTest, yTest, proba = True, xlabel = "Number of Sport activities per month", ylabel = "Number of eating healthy per month")