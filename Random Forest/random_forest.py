""" This code provides an overview how to create a random forest """

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
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

# creates a random forest with a maximum node-depth of 4
# and a minumum number of 3 examples per leaf
MODEL = RandomForestClassifier(criterion="gini",
                               max_depth=4,
                               min_samples_leaf=3)

MODEL = MODEL.fit(XTEST, YTEST)
print(MODEL.score(XTEST, YTEST))

plot_classifier(MODEL, XTRAIN, YTRAIN, proba=True,
                xlabel="monthlySport",
                ylabel="monthlyHealthyFood")

plot_classifier(MODEL, XTEST, YTEST, proba=True,
                xlabel="monthlySport",
                ylabel="monthlyHealthyFood")
