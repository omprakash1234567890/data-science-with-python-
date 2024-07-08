import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Generate the dataset
n_samples = 200
age = np.random.randint(20, 60, size=n_samples)
salary = np.random.randint(30000, 120000, size=n_samples)
experience = np.random.randint(1, 40, size=n_samples)
education = np.random.choice([1, 2, 3, 4], size=n_samples)

# Create a DataFrame
df = pd.DataFrame({
    'Age': age,
    'Salary': salary,
    'Experience': experience,
    'Education': education
})

# Plot distribution of variables
plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
sns.histplot(df['Age'], kde=True, bins=20)
plt.title('Distribution of Age')

plt.subplot(3, 1, 2)
sns.histplot(df['Salary'], kde=True, bins=20)
plt.title('Distribution of Salary')

plt.subplot(3, 1, 3)
sns.histplot(df['Experience'], kde=True, bins=20)
plt.title('Distribution of Experience')

plt.tight_layout()
plt.show()

# Plot box plots for outlier detection
plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
sns.boxplot(x=df['Salary'])
plt.title('Box Plot of Salary')

plt.subplot(1, 2, 2)
sns.boxplot(x=df['Experience'])
plt.title('Box Plot of Experience')

plt.tight_layout()
plt.show()

# Calculate the correlation matrix
correlation_matrix = df[['Age', 'Salary', 'Experience']].corr()

# Plot the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()
