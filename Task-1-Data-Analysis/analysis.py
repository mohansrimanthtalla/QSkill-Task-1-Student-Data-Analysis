import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
data = pd.read_csv("data/students.csv")

print("===== Student Dataset =====")
print(data)

print("\n===== First 5 Rows =====")
print(data.head())

print("\n===== Last 5 Rows =====")
print(data.tail())

print("\n===== Dataset Information =====")
data.info()

print("\n===== Column Names =====")
print(data.columns)

print("\n===== Average Marks =====")
print(data[["Math", "Science", "English"]].mean())

print("\n===== Highest Marks =====")
print(data[["Math", "Science", "English"]].max())

print("\n===== Lowest Marks =====")
print(data[["Math", "Science", "English"]].min())

# Average marks
subjects = ["Math", "Science", "English"]
average_marks = data[["Math", "Science", "English"]].mean()

# Create bar chart
plt.figure(figsize=(6,4))
plt.bar(subjects, average_marks)

plt.title("Average Marks of Students")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

# Save image
plt.savefig("images/bar_chart.png")

# Show graph
plt.show()

# Create Scatter Plot
plt.figure(figsize=(6,4))

plt.scatter(data["Math"], data["Science"])

plt.title("Math vs Science Marks")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")

# Save image
plt.savefig("images/scatter_plot.png")

# Show graph
plt.show()

# Heatmap
plt.figure(figsize=(6,4))

sns.heatmap(
    data[["Math", "Science", "English", "Attendance"]].corr(),
    annot=True,
    cmap="Blues"
)

plt.title("Correlation Heatmap")

# Save image
plt.savefig("images/heatmap.png")

# Show graph
plt.show()