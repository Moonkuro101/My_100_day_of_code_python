from prettytable import PrettyTable

# Create a PrettyTable instance
table = PrettyTable()

# Add data to the table
table.field_names = ["Name", "Age", "City"]
table.add_row(["John", 30, "New York"])
table.add_row(["Alice", 25, "Los Angeles"])
table.add_row(["Bob", 35, "Chicago"])

# Print the table
print(table)
