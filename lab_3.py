import pandas as pd

# Create a dictionary containing employee data
data = {
    "Employee": ["John", "Anna", "Peter", "Linda", "Tom"],
    "Age": [28, 24, 35, 32, 40],
    "Salary": [50000, 60000, 70000, 55000, 65000]
}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print("Employee Table:")
print(df)

# Calculate total salary of employees
total_salary = df['Salary'].sum()
print("\nTotal Salary of Employees: $", total_salary)

# Calculate max salary of employees
max_salary = df['Salary'].max()
print("Maximum Salary of Employees: $", max_salary)

# Calculate min salary of employees
min_salary = df['Salary'].min()
print("Minimum Salary of Employees: $", min_salary)
# Find the employee with the max salary
max_salary_employee = df.loc[df['Salary'].idxmax()]['Employee']
print("Employee with Maximum Salary: ", max_salary_employee)

# List the employee names whose salary is greater than $50,000
employees_greater_than_50000 = df[df['Salary'] > 50000]['Employee'].tolist()
print("\nEmployees with Salary greater than $50,000: ", employees_greater_than_50000)