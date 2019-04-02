import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from helper import plot_classifier

# Read CSV-File:
df = pd.read_csv("heartRisk.csv")

# Returns the first 5 rows:

df = df.drop(['cp', 'trestbps', 'chol', 'fbs', 'restecg', 'exang', 'oldpeak', 'slope', 'ca', 'thal'], axis=1)

print(df.head())

X = df[["age", "sex", "thalach"]].values
y = df["attack"].values

# Splitting the Set in Train and Test Data:
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.25)

model = DecisionTreeClassifier(criterion="entropy")
model.fit(XTrain, yTrain)
print(model.score(XTest, yTest))
