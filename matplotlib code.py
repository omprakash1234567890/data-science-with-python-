import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [23, 45, 56, 78, 213],
    'Line': [1, 4, 9, 16, 25]
}

df = pd.DataFrame(data)

# Bar chart
plt.figure(figsize=(10, 5))
plt.bar(df['Category'], df['Values'], color='skyblue')
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Bar Chart of Values by Category')
plt.show()

# Line chart
plt.figure(figsize=(10, 5))
plt.plot(df['Category'], df['Line'], marker='o', linestyle='-', color='green', label='Line')
plt.xlabel('Category')
plt.ylabel('Line')
plt.title('Line Chart of Line by Category')
plt.legend()
plt.show()

# Combined chart
fig, ax1 = plt.subplots(figsize=(10, 5))

bars = ax1.bar(df['Category'], df['Values'], color='skyblue', label='Values')
ax1.set_xlabel('Category')
ax1.set_ylabel('Values', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

ax2 = ax1.twinx()
line = ax2.plot(df['Category'], df['Line'], marker='o', linestyle='-', color='green', label='Line')
ax2.set_ylabel('Line', color='green')
ax2.tick_params(axis='y', labelcolor='green')

fig.suptitle('Combined Bar and Line Chart')

# Combine labels from both plots
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left', bbox_to_anchor=(0.1, 0.9))

plt.show()
