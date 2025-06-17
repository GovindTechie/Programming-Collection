import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a Blank DataFrame and Add Multiple Columns and Values
df = pd.DataFrame()

# Adding columns and values
df['Name'] = ['Alice', 'Bob', 'Charlie']
df['Age'] = [25, 30, 35]
df['City'] = ['New York', 'Los Angeles', 'Chicago']

print("DataFrame with added columns and values:\n", df)

# Step 2: Export DataFrame into CSV and Excel
# Export to CSV
df.to_csv('data.csv', index=False)
print("DataFrame exported to 'data.csv'")

# Export to Excel
df.to_excel('data.xlsx', index=False)
print("DataFrame exported to 'data.xlsx'")

# Step 3: Create Charts/Graphs
# Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['Age'], color='blue')
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age of Individuals')
plt.show()

# Line Graph
plt.figure(figsize=(10, 6))
plt.plot(df['Name'], df['Age'], marker='o')
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age of Individuals Over Names')
plt.show()