import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from helper import plot_classifier


df = pd.read_csv("test.csv")

print(df.head())

X = df[["monthlySport", "monthlyHealthyFood"]].values
y = df["desease"].values

XTrain, XTest, yTrain, yTest = train_test_split(X, y, random_state = 66, test_size = 0.25)

#scaler = StandardScaler()
#monthlyHealthyFood")scaler.fit(XTrain)

#XTrain = scaler.transform(XTrain)
#XTest = scaler.transform(XTest)

plt.scatter(XTrain[:, 0], XTrain[:, 1], c=yTrain)
plt.xlabel("monthlySport")
plt.ylabel("monthlyHealtyFood")
plt.show()

model = LogisticRegression()
model.fit(XTrain, yTrain)
print("Die Vorhersagegenauigkeit entspricht: ")
print(model.score(XTest, yTest))
print(model.predict(XTest))

plot_classifier(model, XTrain, yTrain, proba = True, xlabel = "monthlySport", ylabel = "monthlyHealthyFood")
plot_classifier(model, XTest, yTest, proba = True, xlabel = "monthlySport", ylabel = "monthlyHealthyFood")
