# DAY-16

# Advanced Structuring : Lists of Dictonaries

# Task-1
# Create a list named company_roster containing two dictionaries. Each dictionary should have two keys: "name" and "department". Fill them with dummy data.
company_roster = [
    {"name":"Chinna","Department":"ACSE"},
    {"name":"Chinni","Department":"ACSE"}
]

# Task-2
# Write a for loop that steps through your company_roster list, looks inside each dictionary, and prints out only the "name" of each employee.
for i in company_roster:
    emp_name=i["name"]
    print(f"The employee name is {emp_name}")

# Task-3
# Access the very first dictionary in your list using index [0]. Add a brand new key called "status" and assign it the value "Active". Print the updated list to verify the change.
company_roster[0]["Status"]="Active"
print(company_roster)
