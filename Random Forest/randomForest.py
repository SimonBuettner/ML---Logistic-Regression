import pandas as pd
import graphviz
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
from helper import plot_classifier

# Read CSV-File:
df = pd.read_csv("desease.csv")

# Returns the first 5 rows:

print(df.head())

X = df[["monthlySport", "monthlyHealthyFood", "overweight"]].values
y = df["desease"].values

# Splitting the Set in Train and Test Data:
XTrain, XTest, yTrain, yTest = train_test_split(X, y, random_state=0, test_size=0.25)

model = DecisionTreeClassifier(criterion="gini", max_depth=5, min_samples_leaf=2)
model = model.fit(XTest, yTest)
print(model.score(XTest, yTest))

# os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
tree = export_graphviz(model, None, 
            feature_names=["monthlySport", "monthlyHealthyFood", "overweight"],
            class_names=["no desase", "desease"], 
            rounded=True, 
            filled=True)
src = graphviz.Source(tree, format="png")
src.render("./datei", view=True)

#plot_classifier(model, XTrain, yTrain, proba=True, xlabel="monthlySport", ylabel="monthlyHealthyFood")
#plot_classifier(model, XTest, yTest, proba=True, xlabel="monthlySport", ylabel="monthlyHealthyFood")
