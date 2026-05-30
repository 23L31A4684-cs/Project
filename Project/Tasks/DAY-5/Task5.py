# DAY-5

# Create a list filled with 5 different target package numbers (e.g., [400000, 500000, 600000, 750000, 900000]).
# Write a for loop that iterates through your list from start to finish.
# Inside the loop, print out each package amount formatted nicely with text like: "Market Salary Option: ₹[Amount]".

Target_package=[400000, 500000, 600000, 750000, 900000]
for i in range(0,5):
    print(f'Market Salary Option: $',Target_package[i])
