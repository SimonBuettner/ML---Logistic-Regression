import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Read CSV-File:
df = pd.read_csv("flat_Price.csv")

# Returns the first 5 rows:
print(df.head())

plt.scatter(df["QM"], df["Price"])
plt.title("Data Points")
plt.show()

# assigns the QM as X-Axis and Price as Y-Axis
model = LinearRegression()
model.fit(df[["QM"]], df[["Price"]])

print("The prediction of the sales price of a flat with 42 sqm is: ")
print(model.predict([[42]]))

x_min = min(df["QM"])
x_max = max(df["QM"])

plt.scatter(df["QM"], df["Price"])

predicted = model.predict([[x_min], [x_max]])
plt.plot([x_min,x_max], predicted, color = "red")
plt.title("Line Graph")
plt.show()