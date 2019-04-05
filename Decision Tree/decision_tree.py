"""This code gives an overview how to create a decision tree """

import pandas as pd
import graphviz
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from helper import plot_classifier

# Read CSV-File:
DF = pd.read_csv("desease.csv")

# Returns the first 5 rows:
print(DF.head())

X = DF[["monthlySport", "monthlyHealthyFood"]].values
Y = DF["desease"].values

# Splitting the Set in Train and Test Data:
XTRAIN, XTEST, YTRAIN, YTEST = train_test_split(X, Y,
                                                random_state=0,
                                                test_size=0.25)
# Creates a decesion tree model with a maximum node depth of 5
# and with at least 2 numbers of samples per leaf
MODEL = DecisionTreeClassifier(criterion="gini",
                               max_depth=5,
                               min_samples_leaf=2)

MODEL = MODEL.fit(XTEST, YTEST)
print(MODEL.score(XTEST, YTEST))

# Export tree to PNG-file
TREE = export_graphviz(MODEL, None,
                       feature_names=["monthlySport", "monthlyHealthyFood"],
                       class_names=["no desase", "desease"],
                       rounded=True,
                       filled=True)

SRC = graphviz.Source(TREE, format="png")
SRC.render("./datei", view=True)

# prints the diagram
plot_classifier(MODEL, XTRAIN, YTRAIN, proba=True,
                xlabel="monthlySport",
                ylabel="monthlyHealthyFood")

plot_classifier(MODEL, XTEST, YTEST, proba=True,
                xlabel="monthlySport",
                ylabel="monthlyHealthyFood")
