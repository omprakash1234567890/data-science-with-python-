import pandas as pd

# Sample data creation
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, None, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', None],
    'Salary': [70000, 80000, None, 60000, 75000]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
file_path = 'pandas_library_codes.csv'
df.to_csv(file_path, index=False)

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Filter rows where 'Age' is greater than 25
filtered_df = df[df['Age'] > 25]

# Fill missing values in 'Age' with the mean age
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

# Drop rows with missing 'City'
df = df.dropna(subset=['City'])

# Calculate summary statistics for 'Salary'
salary_mean = df['Salary'].mean()
salary_median = df['Salary'].median()

# Print results
print("Filtered DataFrame where 'Age' is greater than 25:")
print(filtered_df)
print("\nDataFrame after handling missing values:")
print(df)
print("\nSummary statistics for 'Salary':")
print(f"Mean Salary: {salary_mean}")
print(f"Median Salary: {salary_median}")
