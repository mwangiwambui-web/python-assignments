
# Iris Dataset Analysis in Python Script Format

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the dataset with error handling
try:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Display the first few rows
print("\nFirst 5 rows:")
print(df.head())

# Check data types
print("\nData types:")
print(df.dtypes)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Basic statistics
print("\nSummary statistics:")
print(df.describe())

# Grouping and mean calculations
print("\nMean of features by species:")
print(df.groupby("species").mean())

# Plotting
plt.figure(figsize=(12, 8))

# Line Chart
plt.subplot(2, 2, 1)
plt.plot(df.index, df["petal length (cm)"], color='green')
plt.title("Petal Length Over Index")
plt.xlabel("Index")
plt.ylabel("Petal Length (cm)")

# Bar Chart
plt.subplot(2, 2, 2)
avg_petal_length = df.groupby('species')["petal length (cm)"].mean()
avg_petal_length.plot(kind='bar', color='skyblue')
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Avg Petal Length (cm)")

# Histogram
plt.subplot(2, 2, 3)
plt.hist(df["sepal width (cm)"], bins=10, color='orange', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")

# Scatter Plot
plt.subplot(2, 2, 4)
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species", palette="deep")
plt.title("Sepal Length vs Petal Length")

plt.tight_layout()
plt.show()
